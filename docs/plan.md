# Implementation Plan

## Completed transport milestones

### Step 1 — Verify Hermes MCP locally on the VPS — COMPLETE
- Hermes Agent v0.20.4 verified.
- Native `hermes mcp serve` verified over stdio.
- `tools/list` and read-only `conversations_list` passed.

**Status: PASS.**

### Step 2 — stdio → Streamable HTTP bridge — COMPLETE
- `mcp-proxy` v6.7.11 bridges stdio to `http://127.0.0.1:8080/mcp`.
- Runs under `hermes-mcp-open.service` as user `hms`.
- Port 8080 remains loopback-only.

**Status: PASS.**

### Step 3 — Local HTTP validation — COMPLETE
- HTTP `initialize` passed.
- HTTP `tools/list` matched the native Hermes MCP surface.
- HTTP `conversations_list` passed with `isError: false`.

**Status: PASS.**

### Step 4 — Public HTTPS exposure — COMPLETE
- nginx exposes `https://christian.taranti.pserver.space/mcpgpt/mcp`.
- Existing Lark `/mcp` endpoint remains untouched.
- Public `tools/list` and `conversations_list` passed over valid HTTPS.

**Status: PASS.**

### Step 5 — ChatGPT draft integration — COMPLETE
- ChatGPT Enterprise draft app connected successfully.
- ChatGPT discovered all 10 native Hermes MCP actions.
- Read-only `conversations_list` passed from ChatGPT.
- Read-only `messages_read` passed from ChatGPT.

**Status: PASS.**

## Agent delegation correction

### Problem discovered
The native Hermes MCP `messages_send` action sends a message outward as the Hermes bot. It does **not** submit a user instruction to the Hermes agent.

Observed failure mode:

```text
ChatGPT -> messages_send("do X") -> platform conversation
```

The resulting message is stored as an assistant/bot-authored message, so Hermes does not execute it as a new user task.

### Step 6 — Add explicit `agent_run` delegation — IMPLEMENTED, VPS TEST PENDING

The repository now provides `hermes_mcp_extended.py`.

It imports Hermes's native `mcp_serve.create_mcp_server`, preserving all native Hermes MCP tools, and adds:

```text
agent_run(prompt, timeout_seconds=600)
```

Behavior:
- starts a real Hermes agent task using `hermes chat --quiet --source tool -q <prompt>`;
- uses the installed Hermes profile/configuration, tools, skills, MCP servers, and model settings;
- runs in a new non-interactive Hermes agent session;
- returns the Hermes agent response directly to the MCP caller;
- does not send a Telegram/WhatsApp/Feishu/Slack message merely to create the task.

`agent_run` must be considered write-capable because the delegated Hermes task may invoke tools with side effects.

The launcher now starts the extended server behind the existing `mcp-proxy` instead of launching `hermes mcp serve` directly.

### Required VPS verification for Step 6
After pulling the repository on the VPS:

1. Restart `hermes-mcp-open.service`.
2. Confirm the service starts cleanly.
3. Run local `tools/list` and verify the original 10 tools plus `agent_run` (11 total).
4. Run public HTTPS `tools/list` and verify `agent_run` is present.
5. Invoke a harmless agent task, e.g. `agent_run("Reply exactly: AGENT_RUN_OK")`.
6. Confirm the returned result contains `ok: true` and the Hermes response.
7. Refresh the ChatGPT draft app actions list.
8. Verify ChatGPT sees `agent_run` as the new action.
9. Test a harmless delegated task from ChatGPT before attempting any side-effecting task.

**Status: IMPLEMENTED IN GIT; NOT YET VERIFIED ON VPS.**

## Access control — OPEN
The public MCP endpoint is currently unauthenticated. This is independent of the agent-delegation change and remains an open security item.

## Current architecture

```text
ChatGPT Enterprise
        |
        | MCP Streamable HTTP over HTTPS
        v
https://christian.taranti.pserver.space/mcpgpt/mcp
        |
        v
nginx
        |
        v
mcp-proxy (127.0.0.1:8080)
        |
        | MCP stdio
        v
hermes_mcp_extended.py
        |
        +-- Hermes native MCP tools
        |
        +-- agent_run
                |
                v
        hermes chat -q
                |
                v
           Hermes agent
```
