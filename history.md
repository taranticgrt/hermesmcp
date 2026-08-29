# History

This file records material changes to the Hermes MCP Bridge project.

## 2026-08-28

### Initial project definition

- Created the project README.
- Defined the objective: expose Hermes's existing stdio MCP server to ChatGPT through a secure HTTPS Streamable HTTP MCP endpoint.
- Explicitly excluded reimplementation of Hermes tools and REST-per-tool translation.
- Established initial success criteria covering local MCP operation, HTTP bridging, external verification, ChatGPT discovery, and authentication.

Commit: `e89dc21fb7098075b9c9ccdb221da66e1f43ae45`

### Project history initialized

- Created `history.md` to maintain a trace of material repository changes.

Commit: `8ed459cc399115c9b6e11d493bf05b5eef4a7ee5`

### Implementation plan added

- Created `docs/plan.md`.
- Added phased verification of the installed Hermes MCP server before bridge implementation.
- Added bridge selection, protocol transparency testing, security, VPS deployment, external MCP validation, ChatGPT Enterprise integration, hardening, and definition-of-done criteria.

Commit: `1f784c263f309d2848812f12a06a7fa73b65f79c`

## 2026-08-29 (05:28 UTC)

### Hermes MCP bridge deployed (stdio → Streamable HTTP over HTTPS)

Deployed the MCP bridge end-to-end on the VPS, from Hermes stdio to a public HTTPS MCP endpoint.

**Public endpoint:** `https://christian.taranti.pserver.space/mcpgpt/mcp`

**What was deployed:**
- `mcp-proxy` v6.7.11 (pinned local dep under `deps/`, no `npx` at boot) bridging stdio `hermes mcp serve` → Streamable HTTP.
- Bridge binds loopback only: `127.0.0.1:8080/mcp`.
- systemd unit `hermes-mcp-open.service` runs as user `hms`; `KillMode=mixed`, `TimeoutStopSec=15`, SIGTERM, restart on failure.
- Deterministic launcher `bin/hermes-mcp-open-launcher.sh`.
- nginx `location = /mcpgpt/mcp` → `http://127.0.0.1:8080/mcp`, `proxy_buffering off`, 3600s timeouts, HTTP/1.1, `Connection ""`.

**Exact test results (2026-08-29):**
- Local `http://127.0.0.1:8080/mcp` `initialize` → 200, returns Hermes server capabilities.
- Public `https://christian.taranti.pserver.space/mcpgpt/mcp` `initialize` → 200.
- `tools/list` through both endpoints returns the Hermes tool surface.
- Read-only `conversations_list` succeeds with `isError: false`.

**Status:**
- Local HTTP bridge: PASS.
- Public HTTPS bridge: PASS.
- Endpoint currently unauthenticated.
- Lark `/mcp` was not touched.

Deployment commit: `b038f9985c6134f7fa5ba30bd88ea4ec190faf1f`
Ignore local dependency cache: `e279f2ded53fc547b32a6950a4eb7006fecdb605`

## 2026-08-29 — Agent delegation correction

### Root cause identified

ChatGPT successfully connected to the Hermes MCP and could read conversations, but using `messages_send` to "ask Hermes to do something" did not execute an agent task.

Inspection of the Hermes conversation showed the delegated text stored with `role: assistant`, proving that `messages_send` sends an outward platform message as Hermes rather than creating a new user instruction for the Hermes agent.

### Implementation

Added an explicit extended MCP server that preserves Hermes's native MCP tools and adds `agent_run(prompt, timeout_seconds)`.

`agent_run` launches a real non-interactive Hermes task via:

```text
hermes chat --quiet --source tool -q <prompt>
```

The delegated task uses the installed Hermes configuration, normal tool/skill/MCP surface, and returns its result directly to the MCP caller. It does not overload or change `messages_send` semantics.

Changes:
- Added `hermes_mcp_extended.py`.
- Updated `bin/hermes-mcp-open-launcher.sh` to launch the extended stdio MCP server behind mcp-proxy.
- Updated `README.md` with the distinction between outward platform messaging and agent delegation.
- Updated `docs/plan.md` with the new architecture and VPS verification gate.

Commits:
- `4a703369cf2de79060d32faf6862a5a05ddcdf56` — add `agent_run` extended MCP server.
- `997b66848ba2b257ad73225590a32b2237b4663e` — launch the extended server.
- `6a4488bdce9163b4a692f7c258443311bc9e085d` — document agent-delegation semantics.
- `ff55776a31d1fc2bb321b81987451680de03c11e` — add deployment/test plan for `agent_run`.

**Status:** implemented in GitHub; VPS pull/restart/tests still required before considering the feature complete.
