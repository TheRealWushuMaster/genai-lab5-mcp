from fastmcp.server.server import FastMCP
from typing import Any

mcp: FastMCP[Any] = FastMCP[Any](name="HelloServer") # pyright: ignore[reportExplicitAny]

@mcp.tool
def say_hello(name: str) -> str:
    """Returns a hello message."""
    return f"Howdy, {name}?"

if __name__ == "__main__":
    mcp.run()
