from mcp.server.fastmcp import FastMCP
import os

# here we will initialize mcp server, this is the entry point in the server, after this we can define tools and resources
mcp = FastMCP("MyExampleServer")

# defining a tool, this is the basic tool for greeting
@mcp.tool()
def greet(name: str) -> str:
    print('1')
    """Greets the user by name."""
    return f"Hello, {name}!"

# defining a tool, this is also a basic tool for addition
@mcp.tool()
def add(a: int, b: int) -> int:
  print('2')
  """Adds two numbers."""
  return a + b

# defining a resource, this is the basic tool for providing a description of the server
@mcp.resource("info://description")
def description() -> str:
    print('3')
    """Provides a description of the server."""
    return "This is an example MCP server."

if __name__ == "__main__":
    mcp.run()


#here we are intitializing a tool to seatch notes in the notes folder
@mcp.tool()
def search_notes(keyword: str) -> str:
    """
    Searches all text files inside the notes folder.
    Returns every note containing the keyword.
    """

    notes_folder = "notes"

    if not os.path.exists(notes_folder):
        return "Notes folder not found."

    results = []

    for file in os.listdir(notes_folder):

        if file.endswith(".txt"):

            path = os.path.join(notes_folder, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

                if keyword.lower() in content.lower():
                    results.append(
                        f"File: {file}\n{content}\n"
                    )

    if not results:
        return "No matching notes found."

    return "\n-----------------\n".join(results)    


#with this tool we can add a new note to the notes folder
@mcp.tool()
def add_note(title: str, content: str) -> str:
    """
    Creates a new note.
    """

    os.makedirs("notes", exist_ok=True)

    filename = f"{title}.txt"

    with open(
        os.path.join("notes", filename),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)

    return f"Note '{title}' created successfully."



# this tool will delete a note from the notes folder
@mcp.tool()
def delete_note(title: str) ->str:
    """
    Deletes a note.
    """

    path = os.path.join("notes", f"{title}.txt")

    if not os.path.exists(path):
        return "Note not found."

    os.remove(path)

    return "Note deleted successfully."


#this tool will be able to list all the notes
@mcp.tool()
def list_notes() -> list:
    """
    Lists all available notes.
    """
    os.makedirs("notes", exist_ok=True)

    notes = [
        file[:-4]
        for file in os.listdir("notes")
        if file.endswith(".txt")
    ]

    return notes



#this tool will tell if the given note exists or not
@mcp.tool()
def read_note(title: str) -> str:
    """
    Reads a note.
    """

    path = os.path.join("notes", f"{title}.txt")

    if not os.path.exists(path):
        return "Note not found."

    with open(path, "r", encoding="utf-8") as f:
        return f.read()
