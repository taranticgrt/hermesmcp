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
- Local `http://127.0.0.1:8080/mcp` `initialize` → 200, returns Hermes server capabilities (`protocolVersion 2024-11-05`, `tools/prompts/resources`).
- Public `https://christian.taranti.pserver.space/mcpgpt/mcp` `initialize` → 200, same Hermes capabilities.
- `tools/list` through both endpoints returns the Hermes tool surface, matching the stdio baseline (incl. `conversations_list`).
- Read-only `conversations_list` call succeeds with `isError: false`.
- Missing/invalid session ID returns a structured MCP error (correct error propagation).

**Files/configs changed (this repo):**
- `docs/plan.md` — marked stdio baseline, local HTTP bridge, and public HTTPS bridge as PASS; recorded public URL, nginx/port 8080 loopback-only, `hermes-mcp-open.service`, `mcp-proxy` v6.7.11; authentication set as the next open step.
- `history.md` — this entry.
- `bin/hermes-mcp-open-launcher.sh` (new).
- `deps/package.json`, `deps/package-lock.json` (new; `mcp-proxy` ^6.7.11).
- `deps/node_modules/` present on disk but **not** committed (dependency cache).

Out-of-repo (not committed here): Hermes MCP bridge systemd unit, nginx `portx-ssl` config (`/etc/nginx/sites-enabled/portx-ssl`).

**Status:**
- Local HTTP bridge: PASS.
- Public HTTPS bridge: PASS.
- Endpoint currently **unauthenticated** — authentication is the next open step before production write use.
- **Lark `/mcp` was NOT touched** — the bridge uses the distinct path `/mcpgpt/mcp`; the Lark deployment on `/mcp` (`lark-ai-mcp.service`, port 8999) was left untouched.
