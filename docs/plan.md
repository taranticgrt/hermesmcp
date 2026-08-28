# Implementation Plan

## Immediate implementation plan

The first milestone is to prove that the Hermes stdio MCP can be exposed correctly through an HTTP MCP bridge **on the VPS itself**. We will not attempt ChatGPT integration until this works reliably.

### Step 1 — Verify Hermes MCP locally on the VPS
- Record the installed Hermes version.
- Run `hermes mcp serve`.
- Confirm it uses stdio.
- Execute MCP `initialize` and `tools/list` directly against Hermes.
- Save the returned tool inventory as the baseline.

### Step 2 — Implement the stdio → Streamable HTTP bridge
- Prefer an existing maintained MCP SDK/proxy if it correctly supports both transports.
- Otherwise implement the smallest possible bridge.
- The bridge must forward MCP protocol messages, not recreate individual Hermes tools.
- Expose a local endpoint such as `http://127.0.0.1:<port>/mcp`.

### Step 3 — Test the HTTP connector on the VPS first
Before TLS, DNS, or ChatGPT are involved, test the HTTP MCP endpoint locally on the VPS.

Required tests:
1. `initialize` succeeds through HTTP.
2. `tools/list` matches the direct Hermes stdio baseline.
3. A harmless read-only Hermes tool can be invoked through HTTP.
4. Hermes/MCP errors propagate correctly.
5. Restarting the bridge or Hermes does not leave orphan processes or broken sessions.

**Gate:** do not continue to public HTTPS until these local VPS HTTP tests pass.

### Step 4 — Expose the tested bridge through HTTPS
- Keep the bridge bound to localhost.
- Use the VPS's existing reverse proxy and valid TLS certificate.
- Expose only `https://<host>/mcp` publicly.
- Verify TLS and MCP behavior from an external MCP client.

### Step 5 — Add access control
- Treat the endpoint as privileged because Hermes exposes write-capable tools.
- Confirm the authentication mechanisms supported by the target ChatGPT Enterprise workspace.
- Add authentication before enabling production write operations.

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
