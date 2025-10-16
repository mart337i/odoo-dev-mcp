# MCP Server template for better AI Coding

> Inspired by [MCP Official Tutorial](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)

## Overview

This template provides a streamlined foundation for building Model Context Protocol (MCP) servers in Python. It's designed to make AI-assisted development of MCP tools easier and more efficient.

## Features

- Ready-to-use MCP server implementation
- Configurable transport modes (stdio, SSE)
- Example weather service integration (NWS API)
- Clean, well-documented code structure
- Minimal dependencies
- **Embedded MCP specifications and documentation** for improved AI tool understanding

## Cursor Rules Integration

This project uses Cursor Rules for improved AI coding assistance, with patterns from [Awesome Cursor Rules](https://github.com/PatrickJS/awesome-cursorrules).

- **Clean Code Guidelines**: Built-in clean code rules help maintain consistency and quality
- **Enhanced AI Understanding**: Rules provide context that helps AI assistants generate better code
- **Standardized Patterns**: Follow established best practices for MCP server implementation

Cursor Rules help both AI coding assistants and human developers maintain high code quality standards and follow best practices.

## Integrated MCP Documentation

This template includes comprehensive MCP documentation directly in the project:

- **Complete MCP Specification** (`protocals/mcp.md`): The full Model Context Protocol specification that defines how AI models can interact with external tools and resources. This helps AI assistants understand MCP concepts and implementation details without requiring external references.

- **Python SDK Guide** (`protocals/sdk.md`): Detailed documentation for the MCP Python SDK, making it easier for AI tools to provide accurate code suggestions and understand the library's capabilities.

- **Example Implementation** (`protocals/example_weather.py`): A practical weather service implementation demonstrating real-world MCP server patterns and best practices.

Having these resources embedded in the project enables AI coding assistants to better understand MCP concepts and provide more accurate, contextually relevant suggestions during development.

## Requirements

- Python 3.12+
- Dependencies:
  - `mcp>=1.4.1`
  - `httpx>=0.28.1`
  - `starlette>=0.46.1`
  - `uvicorn>=0.34.0`

## Getting Started

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mcp-server-python-template.git
   cd mcp-server-python-template
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .
   ```

### Running the Example Server

The template includes a weather service example that demonstrates how to build MCP tools:

```bash
# Run with stdio transport (for CLI tools)
python server.py --transport stdio

# Run with SSE transport (for web applications)
python server.py --transport sse --host 0.0.0.0 --port 8080
```

## Creating Your Own MCP Tools

To create your own MCP tools:

1. Import the necessary components from `mcp`:
   ```python
   from mcp.server.fastmcp import FastMCP
   ```

2. Initialize your MCP server with a namespace:
   ```python
   mcp = FastMCP("your-namespace")
   ```

3. Define your tools using the `@mcp.tool()` decorator:
   ```python
   @mcp.tool()
   async def your_tool_function(param1: str, param2: int) -> str:
       """
       Your tool description.
       
       Args:
           param1: Description of param1
           param2: Description of param2
           
       Returns:
           The result of your tool
       """
       # Your implementation here
       return result
   ```

4. Run your server using the appropriate transport:
   ```python
   mcp.run(transport='stdio')  # or set up SSE as shown in server.py
   ```

## Project Structure

- `server.py`: Main MCP server implementation with example weather tools
- `main.py`: Simple entry point for custom code
- `protocals/`: Documentation and example protocols
  - `mcp.md`: Complete MCP specification (~7000 lines)
  - `sdk.md`: MCP Python SDK documentation
  - `example_weather.py`: Example weather service implementation
- `pyproject.toml`: Project dependencies and metadata

## Understanding MCP

The Model Context Protocol (MCP) is a standardized way for AI models to interact with external tools and resources. Key concepts include:

- **Tools**: Functions that models can call to perform actions or retrieve information
- **Resources**: External data sources that models can reference
- **Transports**: Communication channels between clients and MCP servers (stdio, SSE)
- **Namespaces**: Logical groupings of related tools

This template is specifically designed to make working with MCP more accessible, with the integrated documentation helping AI tools better understand and generate appropriate code for MCP implementations.

## Learning Resources

- [MCP Official Documentation](https://modelcontextprotocol.io/docs)
- [Protocol Documentation](./protocals/mcp.md)
- [SDK Guide](./protocals/sdk.md)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

