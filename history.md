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
