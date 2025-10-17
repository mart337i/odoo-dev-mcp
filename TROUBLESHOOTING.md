# Troubleshooting Guide

## Quick Diagnostics

Run these commands to diagnose issues:

```bash
# 1. Check if uv is installed
which uv
# Expected: /home/user/.local/bin/uv

# 2. Test the server
cd /path/to/odoo-dev-mcp
python test_server.py
# Expected: All tests pass with ✓ marks

# 3. Check if server is running
ps aux | grep odoo_mcp_server
# Expected: Should show python process if OpenCode is running

# 4. Try running server manually
uv run odoo_mcp_server.py
# Expected: Server starts and waits (Ctrl+C to stop)
```

## Common Issues & Solutions

### Issue 1: "Connection Failure" in OpenCode

**Symptoms:**
- MCP server shows as not connected
- No response to Odoo queries

**Solutions:**

1. **Check config path is absolute:**
   ```jsonc
   // ❌ WRONG
   "command": ["uv", "run", "~/odoo-dev-mcp/odoo_mcp_server.py"]
   
   // ✅ CORRECT
   "command": ["uv", "run", "/home/user/odoo-dev-mcp/odoo_mcp_server.py"]
   ```

2. **Verify uv is in PATH:**
   ```jsonc
   "environment": {
     "PATH": "/home/user/.local/bin:/usr/local/bin:/usr/bin:/bin"
   }
   ```

3. **Check file permissions:**
   ```bash
   chmod +x /path/to/odoo-dev-mcp/odoo_mcp_server.py
   ```

4. **Restart OpenCode completely:**
   - Close all VS Code windows
   - Reopen and wait for MCP to initialize

### Issue 2: "ModuleNotFoundError: No module named 'mcp'"

**Symptoms:**
- Server fails to start
- Import errors in logs

**Solutions:**

1. **Install dependencies:**
   ```bash
   cd /path/to/odoo-dev-mcp
   uv sync
   ```

2. **Or use Python option:**
   ```bash
   pip install mcp
   # Update config to use python3 instead of uv
   ```

3. **Check virtual environment:**
   ```bash
   # Ensure .venv exists
   ls -la /path/to/odoo-dev-mcp/.venv
   ```

### Issue 3: Server Starts But Doesn't Respond

**Symptoms:**
- Server process is running
- Queries don't get responses

**Solutions:**

1. **Check OpenCode logs:**
   - View > Output
   - Select "OpenCode" from dropdown
   - Look for error messages

2. **Verify configuration:**
   ```bash
   cat ~/.opencode/config.jsonc
   # Check for syntax errors (trailing commas, quotes, etc.)
   ```

3. **Test server manually:**
   ```bash
   cd /path/to/odoo-dev-mcp
   python test_server.py
   ```

### Issue 4: "Documentation not found" Errors

**Symptoms:**
- Search returns no results
- Documentation access fails

**Solutions:**

1. **Verify docs directory exists:**
   ```bash
   ls /path/to/odoo-dev-mcp/docs/
   # Should show: 17.0/ 18.0/ 19.0/
   ```

2. **Check permissions:**
   ```bash
   chmod -R 755 /path/to/odoo-dev-mcp/docs/
   ```

3. **Verify RST files:**
   ```bash
   find /path/to/odoo-dev-mcp/docs -name "*.rst" | wc -l
   # Should show ~300 files
   ```

### Issue 5: uv Command Not Found

**Symptoms:**
- `uv: command not found`
- Config fails to start server

**Solutions:**

1. **Install uv:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   export PATH="$HOME/.local/bin:$PATH"
   ```

2. **Add to shell profile:**
   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. **Or use Python option:**
   Update config to use `python3` instead of `uv`

### Issue 6: Build Errors with hatchling

**Symptoms:**
- "Unable to determine which files to ship"
- Build fails during uv sync

**Solution:**

This is already fixed in the current version. If you still see it:

```bash
cd /path/to/odoo-dev-mcp
git pull  # Get latest updates
uv sync
```

The `pyproject.toml` should have:
```toml
[tool.hatch.build.targets.wheel]
packages = ["."]
```

### Issue 7: Deprecation Warning for dev-dependencies

**Symptoms:**
- Warning about tool.uv.dev-dependencies

**Solution:**

Already fixed in current version. The file uses:
```toml
[dependency-groups]
dev = []
```

### Issue 8: Tools Not Available in OpenCode

**Symptoms:**
- Can't search documentation
- Can't create models
- Natural language queries don't work

**Solutions:**

1. **Check server is running:**
   ```bash
   ps aux | grep odoo_mcp_server
   ```

2. **Restart OpenCode:**
   - Completely close VS Code
   - Reopen project

3. **Try explicit test:**
   Ask Claude: "What's the current Odoo version?"
   Expected: "Current Odoo development version: 19.0"

4. **Check MCP logs in OpenCode:**
   - Output panel > OpenCode
   - Look for "odoo-dev" server status

## Configuration Validation

### Valid Configuration Template (uv)

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["uv", "run", "/home/user/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "PATH": "/home/user/.local/bin:/usr/local/bin:/usr/bin:/bin"
      }
    }
  }
}
```

### Valid Configuration Template (Python)

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["python3", "/home/user/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "PYTHONPATH": "/home/user/odoo-dev-mcp"
      }
    }
  }
}
```

## Verification Checklist

Use this checklist to verify your installation:

- [ ] uv is installed: `which uv`
- [ ] Dependencies installed: `uv sync` completes
- [ ] Tests pass: `python test_server.py` shows all ✓
- [ ] Config file exists: `cat ~/.opencode/config.jsonc`
- [ ] Config uses absolute paths (no ~ or relative paths)
- [ ] PATH includes uv location
- [ ] Server starts manually: `uv run odoo_mcp_server.py`
- [ ] OpenCode restarted completely
- [ ] Server appears in MCP list
- [ ] Test query works: "What's the current Odoo version?"

## Getting More Help

1. **Check the guides:**
   - [QUICK_START.md](QUICK_START.md) - Fast setup
   - [OPENCODE_SETUP.md](OPENCODE_SETUP.md) - Detailed guide
   - [README.md](README.md) - Full documentation

2. **Run diagnostics:**
   ```bash
   python test_server.py
   ```

3. **Check OpenCode logs:**
   - View > Output > OpenCode

4. **Verify file structure:**
   ```bash
   tree -L 2 /path/to/odoo-dev-mcp
   ```

## Still Having Issues?

Collect this information:

1. **System info:**
   ```bash
   python --version
   which uv
   cat ~/.opencode/config.jsonc
   ```

2. **Server test:**
   ```bash
   cd /path/to/odoo-dev-mcp
   python test_server.py
   ```

3. **OpenCode logs:**
   Copy from Output > OpenCode panel

4. **Error messages:**
   Any errors when trying to use the server

Then check the project issues or create a new one with this information.
