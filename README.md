# Odoo Development MCP Server

A Model Context Protocol (MCP) server for Odoo module development with AI assistance. Provides version-aware documentation access (17.0, 18.0, 19.0), intelligent code generation, and development workflow automation.

## Features

- **📚 Documentation Access**: 302+ Odoo documentation files searchable across all versions
- **🔧 Version-Aware Code Generation**: All generated code includes version info and relevant documentation links
- **📋 Integrated Development Guidelines**: Built-in Odoo coding standards and best practices enforcement
- **💡 Smart Prompts**: Guided workflows with rules-aware feature development, debugging, and upgrades
- **🎯 Automatic Context**: Generated code includes references to official Odoo documentation and development rules

## Installation

### Prerequisites

```bash
# Ensure Python 3.12+ is installed
python --version

# Install MCP CLI (if not already installed)
pip install "mcp[cli]"
```

### For Claude Desktop

1. **Quick Install** (Recommended):
   ```bash
   mcp install odoo_mcp_server.py --name "Odoo Dev"
   ```

2. **Manual Install**:
   
   Edit your Claude Desktop config file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

   Add this configuration:
   ```json
   {
     "mcpServers": {
       "odoo-dev": {
         "command": "python",
         "args": ["/absolute/path/to/odoo-dev-mcp/odoo_mcp_server.py"]
       }
     }
   }
   ```

3. Restart Claude Desktop

### For OpenCode

**📖 [Complete OpenCode Setup Guide →](OPENCODE_SETUP.md)**

Quick setup - add to `.opencode.jsonc`:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["python", "/absolute/path/to/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true
    }
  }
}
```

Then use in OpenCode:
```
@odoo-dev set Odoo version to 19.0
@odoo-dev create model library.book with fields: name, author
@odoo-dev show odoo://rules/odoo-development
```

**See [OPENCODE_SETUP.md](OPENCODE_SETUP.md) for complete guide with examples, troubleshooting, and workflows.**

## Quick Start

### 1. Test the Server

```bash
python test_server.py
```

You should see all tests pass with ✓ marks.

### 2. Basic Usage in Claude/OpenCode

```
# Set your Odoo version
Set Odoo version to 19.0

# Create a module
Create an Odoo module called "library_management" with display name "Library Management"

# Create a model
Create a model library.book with fields: name (char), author_id (many2one to res.partner), isbn (char)

# Generate views
Create a form view for library.book with fields: name, author_id, isbn

# Add security
Create security rules for library.book in module library_management

# Search documentation
Search Odoo documentation for "computed fields"
```

## Available Tools

### Version Management
- `set_odoo_version(version)` - Switch between 17.0, 18.0, 19.0
- `get_current_version()` - Check current version

### Documentation & Guidelines
- `search_documentation(query, version)` - Full-text search across docs
- `get_development_guidelines(context)` - Get context-specific coding guidelines
  - Contexts: `general`, `models`, `views`, `security`, `all`

### Code Generation (Version-Aware)
- `create_odoo_module(name, display_name, description, ...)` - Generate module structure with version-specific manifest
- `create_odoo_model(model_name, description, fields, inherit)` - Create Python models with ORM documentation links
- `create_odoo_view(model_name, view_type, fields_to_display)` - Generate XML views with architecture references
- `create_security_rules(model_name, module_name, groups)` - Create security config with security documentation

### Development Prompts
- `develop_odoo_feature(description)` - Guided feature development
- `debug_odoo_error(error, context)` - Error debugging assistance
- `upgrade_odoo_module(module, from_version, to_version)` - Migration guidance
- `review_odoo_code(code)` - Code review with best practices

## Resources

Access Odoo documentation and development rules:

**Documentation:**
- `odoo://docs/19.0/index` - Documentation index
- `odoo://docs/19.0/reference/backend/orm` - ORM reference
- `odoo://docs/18.0/howtos/create_reports` - How-to guides

**Development Rules:**
- `odoo://rules/all` - All development guidelines
- `odoo://rules/clean-code` - Clean code principles
- `odoo://rules/odoo-development` - Odoo-specific conventions

## Examples

### Complete Module Creation

```python
# In Claude/OpenCode:

1. Set Odoo version to 19.0
2. Create module "task_manager" with display name "Task Manager"
3. Create model task.task with fields:
   - name (char, required)
   - description (text)
   - priority (selection: low, medium, high)
   - assigned_to (many2one: res.users)
   - deadline (date)
4. Create form view for task.task
5. Create tree view for task.task
6. Create security rules for task.task
```

### Field Types Examples

All Odoo field types are supported:
```python
fields = [
    {"name": "name", "type": "Char", "required": True},
    {"name": "description", "type": "Text"},
    {"name": "amount", "type": "Float"},
    {"name": "quantity", "type": "Integer"},
    {"name": "active", "type": "Boolean"},
    {"name": "date", "type": "Date"},
    {"name": "partner_id", "type": "Many2one", "comodel_name": "res.partner"},
    {"name": "line_ids", "type": "One2many", "comodel_name": "model.line", "inverse_name": "parent_id"},
    {"name": "tag_ids", "type": "Many2many", "comodel_name": "model.tag"},
    {"name": "state", "type": "Selection", "selection": "[('draft', 'Draft'), ('done', 'Done')]"}
]
```

## Development

### Run Tests
```bash
python test_server.py
```

### Test with MCP Inspector
```bash
mcp dev odoo_mcp_server.py
```

## Architecture

```
odoo_mcp_server.py
├── Resources (Documentation)
│   ├── 302 RST files indexed
│   ├── Version-specific content
│   └── Full-text search
├── Tools (Code Generation)
│   ├── Module scaffolding
│   ├── Model definitions
│   ├── View generation
│   └── Security rules
└── Prompts (Workflows)
    ├── Feature development
    ├── Error debugging
    ├── Module upgrades
    └── Code review
```

## Development Guidelines

The server includes comprehensive Odoo development guidelines that are automatically applied:

### Built-in Rules
- **Clean Code Principles** - General software engineering best practices
- **Odoo Conventions** - Odoo-specific naming, structure, and coding standards
  - Module structure and naming
  - Model and field naming conventions
  - View architecture standards
  - Security rules patterns
  - ORM best practices
  - Performance optimization tips

### Rules Integration
All code generation tools automatically include:
- ⚠️ Naming convention warnings
- 📋 Context-specific guidelines
- 🔗 Links to relevant rules sections
- ✅ Best practice recommendations

### Access Guidelines
```
# Get general guidelines
get_development_guidelines("general")

# Get model-specific rules
get_development_guidelines("models")

# Access all rules
View resource: odoo://rules/all
```

## Documentation Structure

The server provides access to Odoo documentation organized by version:

```
docs/
├── 17.0/ (102 files)
├── 18.0/ (100 files)
└── 19.0/ (100 files)

rules/
├── clean-code.mdc
└── odoo-development.mdc
```
docs/
├── 17.0/ (102 files)
├── 18.0/ (100 files)
└── 19.0/ (100 files)
```

## Supported Platforms

- ✅ Windows, macOS, Linux
- ✅ Claude Desktop
- ✅ OpenCode (VS Code extension)
- ✅ Any MCP-compatible client

## Requirements

- Python 3.12+
- MCP SDK 1.4.1+
- FastMCP

## Troubleshooting

### Server not showing in Claude?
1. Check config file is valid JSON
2. Verify absolute paths
3. Restart Claude Desktop completely

### Import errors?
```bash
pip install "mcp[cli]"
```

### Documentation not found?
Ensure `docs/` directory exists with version folders (17.0, 18.0, 19.0)

## Tips

1. **Always set the Odoo version first** - All code generation adapts to the selected version
2. **Review development guidelines** - Use `get_development_guidelines()` for context-specific rules
3. **Follow naming conventions** - Generated code includes rules warnings for common mistakes
4. **Use descriptive model names** - e.g., `library.book` (with dots), not `lib_b` (with underscores)
5. **Check rules in generated code** - Each tool output includes relevant naming and coding rules
6. **Search before asking** - Use `search_documentation()` for specific questions
7. **Test incrementally** - module → models → views → security
8. **Review code against rules** - Use the `review_odoo_code` prompt for rule compliance checks

## License

MIT License

## Contributing

Contributions welcome! This server follows clean code principles and Odoo best practices.
