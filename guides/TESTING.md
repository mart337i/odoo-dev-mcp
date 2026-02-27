# Testing Guide

## ⚠️ Important: Do NOT Run MCP Server Directly

**NEVER** run the MCP server directly from the terminal:
```bash
# ❌ WRONG - This will cause JSON parsing errors
python src/odoo_mcp/server.py
uv run src/odoo_mcp/server.py
```

MCP servers communicate via JSON-RPC over stdin/stdout and must be run through an MCP client.

## ✅ How to Test the Server

### Option 1: Run the Test Suite (Recommended)

Test all functionality without starting the MCP server:

```bash
# Using Python directly
python -m tests.test_server
python tests/test_server.py

# Using uv
uv run tests/test_server.py
```

This will verify:
- ✓ Documentation files are accessible
- ✓ All tools work correctly
- ✓ Resources can be loaded
- ✓ Prompts are registered
- ✓ Server configuration is valid

### Option 2: Use MCP Inspector

The MCP Inspector provides an interactive testing environment:

```bash
# Install MCP CLI if needed
pip install "mcp[cli]"

# Run inspector
mcp dev src/odoo_mcp/server.py
```

### Option 3: Configure in an MCP Client

The proper way to use the server:

#### For Claude Desktop
See [../README.md](../README.md) for configuration instructions.

#### For OpenCode
See [OPENCODE_SETUP.md](OPENCODE_SETUP.md) for configuration instructions.

## Common Errors and Solutions

### Error: "EOF while parsing a value"
**Cause**: Running the MCP server directly from terminal  
**Solution**: Use `python -m tests.test_server` instead, or configure in an MCP client

### Error: "Invalid JSON: EOF while parsing"
**Cause**: Same as above - the server is receiving terminal input instead of JSON-RPC messages  
**Solution**: Never run the server directly; use the test suite or MCP client

### Error: "Received exception from stream"
**Cause**: MCP server received non-JSON input  
**Solution**: Make sure you're using the server through an MCP client, not running it directly

## Validation Checklist

Before deploying or using the server, verify:

- [ ] `python -m tests.test_server` passes all tests
- [ ] Documentation files exist in `docs/17.0/`, `docs/18.0/`, `docs/19.0/`
- [ ] Rule files exist in `rules/`
- [ ] MCP client configuration is correct
- [ ] Server appears in MCP client after restart

## Debugging Tips

1. **Check file structure**: Ensure docs and rules directories exist
   ```bash
   ls -la docs/
   ls -la rules/
   ```

2. **Verify Python environment**:
   ```bash
   python --version  # Should be 3.12+
   pip list | grep mcp
   ```

3. **Test individual functions**: Edit `tests/test_server.py` to test specific code

4. **Check MCP client logs**:
   - Claude Desktop: Check application logs
   - OpenCode: Check developer console

## Development Workflow

1. Make changes to `src/odoo_mcp/server.py`
2. Run `python -m tests.test_server` to verify
3. If tests pass, restart your MCP client
4. Test the changes in the MCP client environment

## Getting Help

If you encounter issues:

1. Run the test suite and note any failures
2. Check [../.github/TROUBLESHOOTING.md](../.github/TROUBLESHOOTING.md)
3. Verify your configuration matches the setup guides
4. Check that all dependencies are installed: `uv sync` or `pip install mcp`
