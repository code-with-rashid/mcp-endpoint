from fastapi import FastAPI
from mcp_endpoint.server import mcp

if __name__ == "__main__":
    mcp.run(transport="sse")