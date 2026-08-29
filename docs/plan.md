# Implementation Plan

## Immediate implementation plan

The first milestone is to prove that the Hermes stdio MCP can be exposed correctly through an HTTP MCP bridge **on the VPS itself**. We will not attempt ChatGPT integration until this works reliably.

### Step 1 — Verify Hermes MCP locally on the VPS — COMPLETE
Verified on 2026-08-28 with Hermes Agent v0.20.4 (2026.8.18), Python 3.11.15.

Completed checks:
- `hermes mcp serve` exists and runs.
- The command exposes no HTTP/SSE/port options and operates as the Hermes stdio MCP server.
- MCP Inspector successfully initialized the server and executed `tools/list`.
- The discovered baseline tool surface includes:
  - `conversations_list`
  - `conversation_get`
  - `messages_read`
  - `attachments_fetch`
  - `events_poll`
  - `events_wait`
  - `messages_send`
  - `channels_list`
  - `permissions_list_open`
  - `permissions_respond`
- A real read-only `tools/call` of `conversations_list` with `{"limit":5}` succeeded with `isError: false` and returned five conversations.
- Hermes may attempt OAuth initialization for configured upstream MCP clients such as Lark at startup; this can be skipped interactively for the baseline test. Non-interactive startup handling must be addressed before service deployment.

**Baseline status: PASS** (verified 2026-08-28).

### Step 2 — Implement the stdio → Streamable HTTP bridge — COMPLETE
- Used the maintained `mcp-proxy` (v6.7.11) to bridge stdio → Streamable HTTP.
- The bridge forwards MCP protocol messages; it does not recreate individual Hermes tools.
- Local endpoint exposed at `http://127.0.0.1:8080/mcp`.
- `mcp-proxy` v6.7.11 pinned locally under `deps/` (committed) for deterministic operation (no `npx` at boot).
- Launcher: `bin/hermes-mcp-open-launcher.sh`.
- Runs as user `hms` under systemd service `hermes-mcp-open.service`.

**Local HTTP bridge status: PASS** (verified 2026-08-28/29).

### Step 3 — Test the HTTP connector on the VPS first — COMPLETE
Verified against `http://127.0.0.1:8080/mcp`:
1. `initialize` succeeds through HTTP and returns the Hermes MCP server capabilities.
2. `tools/list` returns the Hermes tool surface (matches the direct stdio baseline).
3. `conversations_list` invocations succeed with `isError: false`.
4. Protocol errors propagate correctly (e.g. missing/invalid session ID returns a structured MCP error).
5. Service restart is clean — `hermes mcp serve` is the service's own child; `KillMode=mixed`, `TimeoutStopSec=15` prevents orphan processes.

**Local VPS HTTP tests: PASS.**

### Step 4 — Expose the tested bridge through HTTPS — COMPLETE
- Bridge stays bound to loopback only (`127.0.0.1:8080`).
- Existing nginx reverse proxy + valid TLS certificate terminate HTTPS.
- Public URL: **`https://christian.taranti.pserver.space/mcpgpt/mcp`**
- `location = /mcpgpt/mcp` → `http://127.0.0.1:8080/mcp`, with `proxy_buffering off`, 3600s timeouts, HTTP/1.1, `Connection ""` (streaming-safe).
- Note: the path is `/mcpgpt/mcp`, not `/mcp`, because `/mcp` at this host is owned by the separate Lark /mcp deployment (untouched).
- Verified from an external MCP client over HTTPS: `initialize` succeeds and `tools/list`/`conversations_list` pass.

**Public HTTPS bridge status: PASS.**

### Step 5 — Add access control — NEXT (open)
- The endpoint is currently **unauthenticated** and Hermes exposes write-capable tools; treat it as privileged.
- Confirm the authentication mechanisms supported by the target ChatGPT Enterprise workspace.
- Add authentication before enabling production write operations.
- This is the next open step in the plan.

### Step 6 — Connect ChatGPT
Only after the HTTPS endpoint passes independent MCP testing:
- register the MCP endpoint in ChatGPT Enterprise;
- run tool discovery;
- compare discovered tools with the Hermes baseline;
- test one read-only call first;
- test write-capable tools only after authorization is confirmed.

## Architecture

```text
ChatGPT Enterprise
        |
        | MCP Streamable HTTP over HTTPS
        v
https://<host>/mcp
        |
        v
HTTPS reverse proxy
        |
        v
Hermes MCP bridge (localhost HTTP)
        |
        | MCP over stdio
        v
hermes mcp serve
        |
        v
      Hermes
```

## Key implementation rule

Hermes remains the authoritative MCP server. The bridge must perform transport adaptation only. It must not reimplement `messages_send`, `conversation_get`, or any other Hermes tool as custom REST endpoints.

## Definition of the first milestone

The first milestone is complete when, entirely on the VPS:

- `hermes mcp serve` works directly over stdio;
- the local HTTP MCP bridge starts successfully;
- MCP `initialize` works over HTTP;
- HTTP `tools/list` is semantically equivalent to direct stdio `tools/list`;
- one read-only Hermes tool works through the HTTP bridge;
- bridge/Hermes restart behavior is clean.

Only then do we expose the bridge through HTTPS and proceed toward ChatGPT Enterprise integration.
