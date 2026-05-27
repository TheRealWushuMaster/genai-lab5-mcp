
from mcp.types import Prompt, Resource, Tool
from fastmcp.client.client import CallToolResult
import asyncio
from fastmcp import Client

async def main() -> None:
    client = Client("hello_server.py")
    async with client:
        _ = await client.ping()
        tools: list[Tool] = await client.list_tools()
        resources: list[Resource] = await client.list_resources()
        prompts: list[Prompt] = await client.list_prompts()
        result: CallToolResult = await client.call_tool("say_hello",
                                                        {"name": "Mr. Feynman"})
        print(result)

asyncio.run(main=main())
