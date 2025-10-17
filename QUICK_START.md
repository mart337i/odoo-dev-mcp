# Quick Start Guide - Odoo Development MCP Server

## 🚀 Setup in 3 Steps

### 1. Install Dependencies
```bash
cd /path/to/odoo-dev-mcp
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv sync
```

### 2. Configure OpenCode
Edit `~/.opencode/config.jsonc`:
```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["uv", "run", "/absolute/path/to/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "PATH": "/home/user/.local/bin:/usr/local/bin:/usr/bin:/bin"
      }
    }
  }
}
```

**Important**: Replace paths with your actual paths!

### 3. Restart OpenCode
The MCP server will start automatically.

## ✅ Verify It Works

In OpenCode, ask Claude:
```
What's the current Odoo version?
```

You should see: "Current Odoo development version: 19.0"

## 💡 Common Commands

### Documentation
```
Search Odoo documentation for "fields.Command"
How do I link records using Many2many fields?
Show me the ORM reference for Odoo 19.0
```

### Code Generation
```
Set Odoo version to 19.0

Create module "library_management" with display name "Library System"

Create model library.book with fields:
- title (char, required)
- isbn (char)
- author_id (many2one to res.partner)

Create form view for library.book

Create security rules for library.book in library_management
```

### Development Help
```
Get development guidelines for models
Review this Odoo code: [paste code]
Debug this error: ValidationError in model creation
```

## 🎯 Key Points

1. **No @ mentions needed** - Just talk to Claude naturally
2. **Tools work everywhere** - Available in all OpenCode sessions
3. **Version-aware** - Set your Odoo version once, all code adapts
4. **Full documentation** - 300+ Odoo docs files searchable
5. **Best practices** - Auto-included in generated code

## 📚 More Help

- Full setup: [OPENCODE_SETUP.md](OPENCODE_SETUP.md)
- All features: [README.md](README.md)
- Troubleshooting: See OPENCODE_SETUP.md § Troubleshooting

## 🐛 Not Working?

```bash
# Test the server
python test_server.py

# Check if running
ps aux | grep odoo_mcp_server

# Verify uv is installed
which uv

# Check OpenCode logs
# View > Output > Select "OpenCode" from dropdown
```

## 📖 Example Session

```
You: Set Odoo version to 19.0
Claude: Odoo version set to 19.0

You: How do I use fields.Command to link a record?
Claude: [Searches documentation and provides answer with examples]

You: Create a model task.task with name and priority fields
Claude: [Generates model with proper naming conventions and documentation links]

You: Review this code: [paste code]
Claude: [Reviews against Odoo best practices and suggests improvements]
```

## 🎉 You're Ready!

Start building Odoo modules with AI assistance. The server provides:
- ✅ Smart documentation search
- ✅ Version-aware code generation  
- ✅ Best practices enforcement
- ✅ Naming convention warnings
- ✅ Complete development workflows

Happy coding! 🚀
