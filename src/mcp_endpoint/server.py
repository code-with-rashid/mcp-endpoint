from mcp.server.fastmcp import FastMCP
import httpx

# Initialize FastMCP server with Streamable HTTP transport for production
mcp = FastMCP(name="EndpointCaller", stateless_http=True)


@mcp.tool()
async def call_endpoint(url: str) -> str:
    """Call an external HTTP endpoint and return its response as text.

    Args:
        url: The URL of the endpoint to call (e.g., https://api.example.com/data).

    Returns:
        The response text from the endpoint or an error message if the request fails.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            response.raise_for_status()
            return response.text
        except httpx.HTTPStatusError as e:
            return f"HTTP Error: {e.response.status_code} - {e.response.text}"
        except httpx.RequestError as e:
            return f"Request Error: {str(e)}"
