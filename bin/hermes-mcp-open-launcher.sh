#!/bin/bash
# Deterministic launcher for the Hermes MCP open (unauthenticated) bridge.
# Runs mcp-proxy v6.7.11 (pinned local dep) bound to loopback only, bridging
# stdio `hermes mcp serve` to Streamable HTTP on 127.0.0.1:8080.
set -euo pipefail

MCP_PROXY="/home/hms/hermesmcp/deps/node_modules/.bin/mcp-proxy"
HERMES="/home/hms/.hermes/hermes-agent/venv/bin/hermes"

exec node "${MCP_PROXY}" \
  --host 127.0.0.1 \
  --port 8080 \
  --endpoint /mcp \
  --server stream \
  -- "${HERMES}" mcp serve
