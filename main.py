from fastapi import FastAPI
from mcp_endpoint.server import mcp

# Create FastAPI application
app = FastAPI(
    title="MCP Endpoint Caller",
    description="A Model Context Protocol (MCP) server that calls external HTTP endpoints",
    version="0.1.0"
)

# Mount the FastMCP server at /mcp
app.mount("/mcp", mcp.streamable_http_app())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)