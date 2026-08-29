#!/bin/bash
# Deterministic launcher for the Hermes MCP open (unauthenticated) bridge.
# Runs mcp-proxy v6.7.11 (pinned local dep) bound to loopback only, bridging
# the extended Hermes stdio MCP server to Streamable HTTP on 127.0.0.1:8080.
set -euo pipefail

MCP_PROXY="/home/hms/hermesmcp/deps/node_modules/.bin/mcp-proxy"
HERMES_ROOT="/home/hms/.hermes/hermes-agent"
HERMES_PYTHON="${HERMES_ROOT}/venv/bin/python3"
EXTENDED_SERVER="/home/hms/hermesmcp/hermes_mcp_extended.py"

export HERMES_ROOT
export HERMES_BIN="${HERMES_ROOT}/venv/bin/hermes"

exec node "${MCP_PROXY}" \
  --host 127.0.0.1 \
  --port 8080 \
  --endpoint /mcp \
  --server stream \
  -- "${HERMES_PYTHON}" "${EXTENDED_SERVER}"
