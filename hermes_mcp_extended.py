#!/usr/bin/env python3
"""Extended Hermes MCP server.

This module preserves the native Hermes MCP tool surface and adds one explicit
agent-delegation tool: ``agent_run``.

``messages_send`` sends a message *outward* as the Hermes bot. ``agent_run``
starts a real Hermes agent task and returns the agent's response to the MCP
caller. Keeping the two operations separate prevents the semantic confusion
that motivated this extension.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import time
from pathlib import Path

HERMES_ROOT = Path(
    os.environ.get("HERMES_ROOT", "/home/hms/.hermes/hermes-agent")
).resolve()
HERMES_BIN = os.environ.get(
    "HERMES_BIN", str(HERMES_ROOT / "venv" / "bin" / "hermes")
)

# Hermes is installed from git on the VPS. Make the source checkout explicit so
# importing its top-level mcp_serve module does not depend on the service cwd.
if str(HERMES_ROOT) not in sys.path:
    sys.path.insert(0, str(HERMES_ROOT))

from mcp_serve import EventBridge, create_mcp_server  # noqa: E402

MAX_PROMPT_CHARS = 200_000
DEFAULT_TIMEOUT_SECONDS = 600
MAX_TIMEOUT_SECONDS = 3600
MAX_ERROR_CHARS = 4000


def _json(payload: dict) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2)


def _bounded_timeout(value: int) -> int:
    try:
        timeout = int(value)
    except (TypeError, ValueError):
        timeout = DEFAULT_TIMEOUT_SECONDS
    return max(10, min(timeout, MAX_TIMEOUT_SECONDS))


async def _terminate_process(process: asyncio.subprocess.Process) -> None:
    if process.returncode is not None:
        return
    process.terminate()
    try:
        await asyncio.wait_for(process.wait(), timeout=5)
    except asyncio.TimeoutError:
        process.kill()
        await process.wait()


def create_extended_mcp(event_bridge: EventBridge):
    """Create Hermes's native MCP server and add explicit agent delegation."""
    mcp = create_mcp_server(event_bridge=event_bridge)

    @mcp.tool()
    async def agent_run(
        prompt: str,
        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
    ) -> str:
        """Run a real Hermes agent task and return its final response.

        This is agent delegation, not platform messaging. Hermes executes the
        prompt in a new non-interactive agent session using its normal profile,
        configured tools, skills, MCP servers, and model settings. The result is
        returned directly to the MCP caller; this tool does not send a Telegram,
        WhatsApp, Feishu, Slack, or other platform message.

        The task MAY invoke Hermes tools that have side effects, depending on the
        prompt and Hermes configuration. Treat this as a write-capable action.

        Args:
            prompt: Instruction for the Hermes agent to execute.
            timeout_seconds: Maximum runtime, 10..3600 seconds (default 600).
        """
        if not isinstance(prompt, str) or not prompt.strip():
            return _json({"ok": False, "error": "prompt must be non-empty"})
        if len(prompt) > MAX_PROMPT_CHARS:
            return _json(
                {
                    "ok": False,
                    "error": f"prompt exceeds {MAX_PROMPT_CHARS} characters",
                }
            )

        timeout = _bounded_timeout(timeout_seconds)
        started = time.monotonic()
        env = os.environ.copy()
        env.setdefault("HOME", "/home/hms")
        env.setdefault("NO_COLOR", "1")

        argv = [
            HERMES_BIN,
            "chat",
            "--quiet",
            "--source",
            "tool",
            "-q",
            prompt,
        ]

        try:
            process = await asyncio.create_subprocess_exec(
                *argv,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
                cwd=str(HERMES_ROOT),
            )
        except Exception as exc:
            return _json(
                {
                    "ok": False,
                    "error": "failed to start Hermes agent",
                    "detail": str(exc)[:MAX_ERROR_CHARS],
                }
            )

        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(), timeout=timeout
            )
        except asyncio.TimeoutError:
            await _terminate_process(process)
            return _json(
                {
                    "ok": False,
                    "error": "Hermes agent timed out",
                    "timeout_seconds": timeout,
                    "duration_seconds": round(time.monotonic() - started, 3),
                }
            )

        response = stdout.decode("utf-8", errors="replace").strip()
        error_text = stderr.decode("utf-8", errors="replace").strip()
        duration = round(time.monotonic() - started, 3)

        if process.returncode != 0:
            return _json(
                {
                    "ok": False,
                    "error": "Hermes agent exited with an error",
                    "exit_code": process.returncode,
                    "stderr": error_text[-MAX_ERROR_CHARS:],
                    "stdout": response[-MAX_ERROR_CHARS:],
                    "duration_seconds": duration,
                }
            )

        return _json(
            {
                "ok": True,
                "response": response,
                "duration_seconds": duration,
            }
        )

    return mcp


async def _run() -> None:
    bridge = EventBridge()
    bridge.start()
    server = create_extended_mcp(bridge)
    try:
        await server.run_stdio_async()
    finally:
        bridge.stop()


def main() -> None:
    try:
        asyncio.run(_run())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
