# Hermes MCP Bridge

## Goal

Expose Hermes to ChatGPT through a secure, standards-compliant remote MCP endpoint while preserving Hermes as the authority for its native MCP tools.

Hermes already provides its conversation/messaging MCP interface through:

```bash
hermes mcp serve
```

This project bridges that stdio MCP transport to remote Streamable HTTP and adds one explicit delegation capability that the native Hermes MCP does not provide: `agent_run`.

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
mcp-proxy
        |
        | MCP over stdio
        v
hermes_mcp_extended.py
        |
        +-- native Hermes MCP tools from mcp_serve
        |
        +-- agent_run(prompt)
                |
                v
        hermes chat -q <prompt>
                |
                v
             Hermes agent
```

## Why `agent_run` exists

The native `messages_send` tool sends a message **outward as Hermes** to Telegram, WhatsApp, Feishu, Slack, or another configured platform. It does not submit a user instruction to the Hermes agent.

`agent_run` is intentionally separate. It starts a real non-interactive Hermes agent task and returns the final response to the MCP caller.

This prevents a request such as "ask Hermes to do X" from accidentally becoming a bot-authored platform message containing the text "do X".

## Primary objectives

- Preserve Hermes as the authoritative provider for its native MCP tools.
- Bridge MCP stdio to MCP Streamable HTTP.
- Preserve native tool discovery, schemas, and errors.
- Add `agent_run` without changing or overloading `messages_send`.
- Keep the bridge small, auditable, and independent from Hermes source modifications.
- Run Hermes agent delegation using the installed Hermes profile, tools, skills, MCP servers, and model configuration.

## Native Hermes tools preserved

The extended server imports Hermes's own `mcp_serve.create_mcp_server`, so the existing tools remain native to Hermes, including:

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

The project adds:

- `agent_run` — execute a real Hermes agent task and return its response directly.

## Safety note

`agent_run` may cause Hermes to invoke tools with side effects depending on the prompt and Hermes configuration. It must be treated as a write-capable action even though its return path is synchronous and does not itself send a platform message.

## Documentation

- [`docs/plan.md`](docs/plan.md) — implementation and verification plan.
- [`history.md`](history.md) — project change history.
