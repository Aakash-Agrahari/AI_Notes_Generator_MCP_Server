from mcp.server.fastmcp import FastMCP

# here we will initialize mcp server
mcp = FastMCP("MyExampleServer")

# defining a tool
@mcp.tool()
def greet(name: str) -> str:
    print('1')
    """Greets the user by name."""
    return f"Hello, {name}!"

# defining a tool
@mcp.tool()
def add(a: int, b: int) -> int:
  print('2')
  """Adds two numbers."""
  return a + b

# defining a resource
@mcp.resource("info://description")
def description() -> str:
    print('3')
    """Provides a description of the server."""
    return "This is an example MCP server."

if __name__ == "__main__":
    mcp.run()