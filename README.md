# Hermes MCP Bridge

## Goal

Expose the MCP server already provided by Hermes to ChatGPT through a secure, standards-compliant remote MCP endpoint.

Hermes already provides its MCP interface through:

```bash
hermes mcp serve
```

The project therefore should **not reimplement Hermes tools or business logic**. Its purpose is to bridge the existing Hermes MCP stdio transport to the remote transport required by ChatGPT.

## Target architecture

```text
ChatGPT Enterprise
        |
        | MCP over HTTPS
        | Streamable HTTP
        v
https://<host>/mcp
        |
        v
Hermes MCP Bridge
        |
        | MCP over stdio
        v
hermes mcp serve
        |
        v
      Hermes
```

## Primary objectives

- Preserve Hermes as the authoritative MCP server and tool provider.
- Bridge MCP stdio to MCP Streamable HTTP without translating individual Hermes tools.
- Expose a stable `/mcp` endpoint over HTTPS from the VPS where Hermes is running.
- Preserve MCP protocol semantics, schemas, errors, discovery, and future Hermes tools.
- Allow ChatGPT to discover Hermes tools through normal MCP `initialize` and `tools/list` operations.
- Add authentication and access control suitable for exposing Hermes remotely.
- Keep the bridge small, auditable, and independent from Hermes internals.
- Support reliable operation as a VPS service, including lifecycle management, logging, and health checks.

## Non-goals

- Reimplementing Hermes conversation or messaging APIs.
- Creating HTTP REST endpoints for each Hermes MCP tool.
- Forking Hermes unless a confirmed Hermes defect makes that necessary.
- Exposing the Hermes stdio process directly to the network.

## Initial success criteria

1. `hermes mcp serve` runs successfully on the VPS.
2. A local bridge can initialize an MCP session against the Hermes stdio server.
3. `tools/list` through the bridge returns the tools exposed by Hermes.
4. The bridge exposes a standards-compliant Streamable HTTP MCP endpoint.
5. The endpoint is reachable through valid HTTPS.
6. An external MCP client can initialize, discover tools, and execute a read-only Hermes tool.
7. ChatGPT can connect to the endpoint and discover the Hermes tool set.
8. Authentication is added before production exposure of write-capable Hermes tools.

## Documentation

- [`docs/plan.md`](docs/plan.md) — implementation and verification plan.
- [`history.md`](history.md) — project change history.
