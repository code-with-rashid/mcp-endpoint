MCP Endpoint Caller
A Model Context Protocol (MCP) server that exposes a tool to call external HTTP endpoints and return their responses. Built with the MCP Python SDK and FastAPI, this project is designed to be hosted for consumption by MCP-compliant clients or LLMs (e.g., Claude Desktop).
Features

Exposes a call_endpoint tool that makes HTTP GET requests to user-provided URLs.
Uses Streamable HTTP transport for production-ready deployment.
Handles errors gracefully with descriptive messages.
Configured with uv for dependency management.

Requirements

Python >= 3.10
uv for dependency management

Installation

Clone the repository (replace with your repository URL):
git clone https://github.com/yourusername/mcp-endpoint.git
cd mcp-endpoint


Install dependencies using uv:
uv sync



Running Locally

Start the server:
uv run python main.py

The server will be available at http://localhost:8000/mcp.

Test with MCP Inspector (for development):
uv run mcp dev src/mcp_endpoint/server.py

This opens the MCP Inspector to interact with the call_endpoint tool.

Integrate with Claude Desktop (optional):
uv run mcp install src/mcp_endpoint/server.py --name "Endpoint Caller"



Usage

Tool: call_endpoint

Parameters: url (string, e.g., https://api.example.com/data)

Example Request (via MCP client or LLM):
{
    "tool": "call_endpoint",
    "arguments": {
        "url": "https://jsonplaceholder.typicode.com/todos/1"
    }
}


Example Response:
"{\"id\": 1, \"title\": \"delectus aut autem\", ...}"

or, on error:
"HTTP Error: 404 - Not Found"


Health Check: Verify the server at http://localhost:8000/mcp/health.


Deployment
To host the server for others to consume:

Deploy to a cloud platform (e.g., Render, Heroku, or AWS):
Use a WSGI/ASGI server like uvicorn or gunicorn.
Example with gunicorn:uv run gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000


Ensure the server is accessible publicly (e.g., https://your-domain.com/mcp).


Set environment variables (if needed, e.g., for API keys):export API_KEY=your_key

or use a .env file with python-dotenv.
Share the endpoint: Provide clients with the server URL (/mcp) and instructions to use the call_endpoint tool.

Development

Add dependencies:uv add package-name


Run tests (if added):uv run pytest



License
MIT License. See LICENSE for details.