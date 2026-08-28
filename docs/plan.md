# Implementation Plan

## 1. Confirm the Hermes MCP baseline

### 1.1 Verify installed Hermes version
- Record the exact Hermes version running on the VPS.
- Record the output of `hermes mcp serve --help`.
- Confirm the command uses stdio transport in the installed version.

### 1.2 Inventory the MCP surface
- Start `hermes mcp serve` locally.
- Perform MCP `initialize`.
- Call `tools/list`.
- Record the exact tool names, descriptions, input schemas, and capabilities exposed by the installed Hermes version.
- Identify which tools are read-only and which can mutate state or send messages.

### 1.3 Establish a baseline test
- Execute at least one harmless read-only tool through stdio.
- Save the request/response shape as a protocol fixture for later bridge tests.

## 2. Select the bridge implementation

### 2.1 Requirements
The bridge must:
- accept MCP Streamable HTTP connections;
- communicate with Hermes using MCP over stdio;
- preserve JSON-RPC/MCP semantics rather than translating individual tools;
- preserve tool discovery dynamically;
- handle process startup, shutdown, errors, and stderr safely;
- support concurrent or sequential client sessions according to MCP requirements;
- avoid leaking secrets or Hermes stderr into protocol responses.

### 2.2 Evaluate implementation options
Evaluate maintained MCP SDK/proxy approaches before writing custom protocol code.

Selection criteria:
- current MCP Streamable HTTP support;
- stdio client support;
- small dependency surface;
- active maintenance;
- clear session/lifecycle semantics;
- compatibility with the installed Hermes MCP implementation;
- easy systemd/container deployment.

### 2.3 Decision record
Document the selected bridge technology and why alternatives were rejected.

## 3. Build the local bridge

### 3.1 Process lifecycle
- Launch `hermes mcp serve` as a child process or connect through a clearly defined local supervisor model.
- Keep stdin/stdout exclusively for MCP protocol traffic.
- Route diagnostic output separately.
- Detect child-process failure and expose a clear service failure rather than corrupt MCP responses.

### 3.2 Streamable HTTP endpoint
- Expose `/mcp` on localhost only during development.
- Implement the MCP Streamable HTTP requirements expected by current clients.
- Do not create REST endpoints corresponding to Hermes tool names.

### 3.3 Protocol transparency tests
Verify through the HTTP bridge:
- `initialize`;
- capability negotiation;
- `tools/list`;
- at least one read-only `tools/call`;
- error propagation;
- malformed request handling;
- Hermes subprocess restart/failure behavior.

Compare the observed HTTP-bridge tool definitions with the direct stdio baseline. They must remain semantically equivalent.

## 4. Security design

### 4.1 Threat model
Treat the MCP endpoint as privileged because Hermes may expose message-sending and other mutating tools.

Consider at minimum:
- unauthenticated internet access;
- stolen credentials;
- replay attempts;
- unauthorized tool invocation;
- prompt-driven misuse of write tools;
- excessive request rates;
- denial of service against the Hermes subprocess;
- accidental secret logging.

### 4.2 Authentication
- Confirm which authentication methods the target ChatGPT Enterprise custom-app flow supports in the user's workspace.
- Select a supported mechanism before production use.
- Prefer per-user identity/authorization where practical rather than a globally shared permanent secret.
- Keep authentication termination at the HTTPS/bridge layer; do not modify Hermes solely for transport authentication.

### 4.3 Authorization
- Determine whether all authenticated users may use all Hermes tools.
- If not, define policy enforcement without modifying Hermes tool semantics.
- Consider initially allowing only read-only tools until the full path is verified.

## 5. VPS deployment

### 5.1 Service layout
Target deployment:

```text
Internet / ChatGPT
       |
       v
HTTPS reverse proxy :443
       |
       v
Hermes MCP bridge (localhost)
       |
       v
hermes mcp serve (stdio)
```

### 5.2 Reverse proxy
- Use the VPS's existing TLS-capable reverse proxy.
- Publish only the HTTPS endpoint.
- Keep the bridge's internal port bound to loopback unless there is a documented reason not to.
- Configure timeouts compatible with MCP Streamable HTTP behavior.

### 5.3 Service supervision
- Run the bridge under systemd or an equivalent supervisor.
- Define restart policy.
- Ensure child Hermes processes cannot accumulate after crashes/restarts.
- Add log rotation.

### 5.4 Health and observability
Add minimal operational visibility:
- process health;
- Hermes child-process state;
- MCP request failures;
- authentication failures;
- startup/version information.

Do not log confidential message bodies or credentials by default.

## 6. External MCP verification

Before involving ChatGPT, verify the public endpoint with an independent MCP client/inspector.

Tests:
1. TLS certificate validation.
2. MCP initialization.
3. `tools/list`.
4. Read-only tool invocation.
5. Session behavior.
6. Authentication rejection for unauthorized requests.
7. Recovery after bridge restart.

## 7. ChatGPT Enterprise integration

### 7.1 Workspace capability check
- Verify that the target Enterprise workspace exposes the custom MCP/custom app creation controls.
- Record the actual UI path observed in the tenant rather than relying on assumed documentation paths.

### 7.2 Register endpoint
Configure the HTTPS MCP endpoint in ChatGPT using the supported authentication method.

### 7.3 Discovery verification
- Run tool discovery/scan.
- Compare discovered tools with the baseline Hermes `tools/list` inventory.
- Investigate any missing, altered, or rejected tool schemas before proceeding.

### 7.4 Safe execution test
Start with a read-only Hermes tool.

Only after read-only operation is stable should a write-capable tool such as message sending be tested.

## 8. Hardening

After end-to-end functionality is proven:
- finalize authentication and authorization;
- add rate limiting where appropriate;
- constrain network exposure;
- define backups/configuration management;
- pin dependency versions;
- add automated protocol regression tests;
- document upgrade procedure for Hermes and the MCP bridge;
- verify behavior whenever Hermes changes its MCP tool surface or MCP protocol version.

## 9. Definition of done

The first production-ready milestone is complete when:

- Hermes remains unmodified and authoritative for its MCP tools.
- The bridge exposes standards-compliant MCP Streamable HTTP over valid HTTPS.
- The public bridge port is protected by authentication.
- Direct stdio and bridged `tools/list` results are consistent.
- An external MCP client passes initialization, discovery, and read-only invocation tests.
- ChatGPT Enterprise discovers the Hermes tools.
- ChatGPT successfully invokes a read-only Hermes operation.
- Write-capable operations are explicitly authorized and tested safely.
- The bridge runs as a supervised VPS service with restart behavior and usable diagnostics.
- Deployment and recovery procedures are documented.
