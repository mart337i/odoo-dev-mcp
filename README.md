# Odoo Development MCP Server

A Model Context Protocol (MCP) server for Odoo module development with AI assistance. Provides version-aware official documentation links (17.0, 18.0, 19.0), intelligent code generation, and development workflow automation.

**🚀 [Quick Start](guides/QUICK_START.md)** | **📖 [OpenCode Setup](guides/OPENCODE_SETUP.md)** | **🧪 [Testing Guide](guides/TESTING.md)** | **🔧 [Troubleshooting](.github/TROUBLESHOOTING.md)** | **📋 [Guides Index](guides/README.md)** | **📝 [Changelog](CHANGELOG.md)**

## Features

- **📚 Official Documentation Links**: Version-aware links to Odoo's developer reference at `https://www.odoo.com/documentation/<version>/developer/reference.html`
- **🧭 Skill-Informed Odoo Guardrails**: Built-in guidance learned from [mart337i/odoo-skills](https://github.com/mart337i/odoo-skills) without requiring that repo at runtime
- **🔧 Version-Aware Code Generation**: All generated code includes version info and relevant documentation links
- **🦉 OWL Frontend Scaffolds**: Generate Odoo OWL components, client actions, field widgets, services, and frontend tests
- **📋 Integrated Development Guidelines**: Built-in Odoo coding standards and best practices enforcement
- **💡 Smart Prompts**: Guided workflows with rules-aware feature development, debugging, and upgrades
- **🎯 Automatic Context**: Generated code includes references to official Odoo documentation and development rules

## Works Great With Odoo Skills

This MCP server pairs well with the companion Odoo skill set at [mart337i/odoo-skills](https://github.com/mart337i/odoo-skills). Use those skills in your agent/client for deeper Odoo workflows like addon planning, migrations, code review, testing, OWL frontend work, and debugging. The MCP server does not require that repo at runtime; it only generates tools, guardrails, and references that complement skill-driven work.

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
   mcp install src/odoo_mcp/server.py --name "Odoo Dev"
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
         "args": ["/absolute/path/to/odoo-dev-mcp/src/odoo_mcp/server.py"]
       }
     }
   }
   ```

3. Restart Claude Desktop

### For OpenCode

**📖 [Complete OpenCode Setup Guide →](guides/OPENCODE_SETUP.md)**

Quick setup - add to `~/.opencode/config.jsonc`:

#### Option 1: Using uv (Recommended)

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["uv", "run", "/absolute/path/to/odoo-dev-mcp/src/odoo_mcp/server.py"],
      "enabled": true,
      "environment": {
        "PATH": "/home/user/.local/bin:/usr/local/bin:/usr/bin:/bin",
        "ODOO_SOURCE": "/path/to/odoo",
        "ODOO_BASE_COMMAND": "/path/to/odoo/odoo-bin -c /path/to/odoo.conf --addons-path=/path/to/addons",
        "ODOO_TOOL_README": "/path/to/local-development/README.md"
      }
    }
  }
}
```

First, install dependencies:
```bash
cd /path/to/odoo-dev-mcp
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

#### Option 2: Using Python directly

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["python3", "/absolute/path/to/odoo-dev-mcp/src/odoo_mcp/server.py"],
      "enabled": true,
      "environment": {
        "PYTHONPATH": "/absolute/path/to/odoo-dev-mcp"
      }
    }
  }
}
```

See [examples/opencode.jsonc.example](examples/opencode.jsonc.example) for a complete working example.

Note: Requires `pip install mcp` first.

Then use in OpenCode:
```
Search Odoo documentation for "fields.Command"
Set Odoo version to 19.0
Get Odoo local context
Get documentation URL for reference/backend/orm
Create model library.book with fields: name, author
Get development guidelines
```

### Local Odoo Environment Context

Configure these optional environment variables so the MCP can point agents at your local Odoo source, command template, and local development guide:

```bash
export ODOO_SOURCE=/path/to/odoo
export ODOO_BASE_COMMAND="/path/to/odoo/odoo-bin -c /path/to/odoo.conf --addons-path=/path/to/addons"
export ODOO_TOOL_README=/path/to/local-development/README.md
```

Use `get_odoo_local_context()` or `odoo://local/context` to inspect the configured values. The server treats `ODOO_BASE_COMMAND` as a command template only; agents should still ask before running commands that touch a database or local service.

**See [OPENCODE_SETUP.md](guides/OPENCODE_SETUP.md) for complete guide with examples, troubleshooting, and workflows.**

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

# Search official documentation catalog
Search Odoo documentation for "computed fields"
```

## Available Tools

### Version Management
- `set_odoo_version(version)` - Switch between 17.0, 18.0, 19.0
- `get_current_version()` - Check current version
- `detect_odoo_version(path, ...)` - Detect a likely local Odoo version from env vars, `release.py`, addon manifests, and branch names without changing the active version

### Documentation & Guidelines
- `get_odoo_local_context(include_readme_excerpt)` - Show configured `ODOO_SOURCE`, `ODOO_BASE_COMMAND`, `ODOO_TOOL_README`, source hints, and command templates
- `inspect_odoo_source(path, query, scope, max_files)` - Use AST to compactly inspect Odoo core/addon manifests, models, controllers, routes, imports, and version signals without executing source
- `get_documentation_url(path, version)` - Get an official Odoo documentation URL
- `search_documentation(query, version)` - Search the built-in official reference catalog and return Odoo documentation links
- `get_development_guidelines(context)` - Get context-specific coding guidelines
  - Contexts: `general`, `models`, `views`, `security`, `all`
- `explain_odoo_error(error_text, version, context)` - Diagnose patterned Odoo tracebacks with root cause, inspection steps, and docs links
- `plan_odoo_feature(description, module_name, version)` - Create a skill-informed Odoo implementation plan with security, view, test, and docs guidance
- `plan_owl_feature(description, module_name, integration_type, target_bundle, version)` - Plan Odoo OWL frontend work with asset, registry, service, and test guardrails
- `layout_module_dependencies(module_name, features, models, integrate_with, explicit_dependencies)` - Infer and order manifest dependencies for an Odoo module

### Code Generation (Version-Aware)
- `create_odoo_module(name, display_name, description, ...)` - Generate module structure with version-specific manifest
- `create_odoo_model(model_name, description, fields, inherit)` - Create Python models with ORM documentation links
- `create_odoo_view(model_name, view_type, fields_to_display, view_name, parent_menu)` - Generate safer XML views with version-aware `tree`/`list` handling and no fake menu parent
- `create_security_rules(model_name, module_name, groups)` - Create security config with security documentation
- `create_base_automation(...)` - Generate version-aware `base.automation` and linked `ir.actions.server` XML for automated actions
- `create_upgrade_script(module_name, from_version, to_version, ...)` - Generate version-aware `pre-migration.py`, `post-migration.py`, and `end-migration.py` scaffolds with verified `odoo.upgrade.util` helper examples
- `create_owl_component(component_name, module_name, ...)` - Generate Odoo OWL JS/XML/SCSS component scaffolds and manifest asset entries
- `create_owl_client_action(action_name, module_name, ...)` - Generate an OWL client action, `registry.category("actions")` registration, and `ir.actions.client` XML
- `create_owl_field_widget(widget_name, module_name, ...)` - Generate an OWL field widget using `standardFieldProps` and the fields registry
- `create_owl_service(service_name, module_name, ...)` - Generate a frontend service using the services registry and explicit dependencies
- `create_owl_test(component_name, module_name, ...)` - Generate an Odoo Hoot frontend test scaffold and test asset entry

### Development Prompts
- `develop_odoo_feature(description)` - Guided feature development
- `debug_odoo_error(error, context)` - Error debugging assistance
- `upgrade_odoo_module(module, from_version, to_version)` - Migration guidance
- `review_odoo_code(code)` - Code review with best practices

## Resources

Access Odoo documentation and development rules:

**Documentation:**
- `odoo://docs/19.0/index` - Official developer reference index
- `odoo://docs/19.0/reference/backend/orm` - ORM reference URL and metadata
- `get_documentation_url("reference/backend/security", "19.0")` - Official Odoo security documentation URL

**Local Odoo Context:**
- `odoo://local/context` - Configured local Odoo source path, base command, and tooling README excerpt

**Development Rules:**
- `odoo://rules/all` - All development guidelines
- `odoo://rules/clean-code` - Clean code principles
- `odoo://rules/odoo-development` - Odoo-specific conventions

## Examples

### Complete Module Creation

```python
# In Claude/OpenCode:

1. Set Odoo version to 19.0
2. Plan the feature: task management with priorities and deadlines
3. Layout dependencies for task management with chatter and automations
4. Create module "task_manager" with display name "Task Manager"
5. Create model task.task with fields:
   - name (char, required)
   - description (text)
   - priority (selection: low, medium, high)
   - assigned_to (many2one: res.users)
   - deadline (date)
6. Create form view for task.task
7. Create list view for task.task
8. Create security rules for task.task
9. Create an automated action that assigns overdue tasks
```

### Automated Action Example

```text
Create a base automation for task.task that runs on create or write, watches stage_id and deadline, and executes Python code.
```

The helper will include `base_automation` manifest dependency guidance and version-specific notes for time-based triggers.

### OWL Frontend Examples

```text
Plan an OWL client action for an equipment rental dashboard in equipment_rental.
```

```text
Create an OWL component called Rental Dashboard in equipment_rental with title prop, orm service, and local state.
```

```text
Create an OWL field widget called Rental Badge in equipment_rental for char and selection fields.
```

The OWL helpers generate Odoo asset bundle entries, `@odoo/owl` imports, registry wiring, XML templates, SCSS, and frontend test guidance.

### Migration And Error Examples

```text
Create upgrade scripts for equipment_rental from 17.0 to 19.0, renaming old_stage_id to stage_id and old XML IDs.
```

The migration scaffold includes phase-specific `odoo.upgrade.util` examples for model, field, XML ID, module, SQL, and ORM data-migration helpers.

```text
Explain this Odoo error: odoo.tools.convert.ParseError: while parsing views/equipment_views.xml, External ID not found in the system
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
uv run python -m tests.test_server
```

### Test with MCP Inspector
```bash
mcp dev odoo_mcp_server.py
```

## Architecture

```
odoo_mcp_server.py
├── Resources (Documentation)
│   ├── Official Odoo reference URL catalog
│   ├── Version-specific links
│   └── Topic search
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

## Documentation Strategy

The server points to official Odoo documentation instead of vendoring stale local copies. The base URL pattern is:

```text
https://www.odoo.com/documentation/<version>/developer/reference.html
```

Common topic links follow the same structure:

```text
https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html
https://www.odoo.com/documentation/19.0/developer/reference/backend/security.html
https://www.odoo.com/documentation/19.0/developer/reference/frontend/owl_components.html
```

The repository still contains `docs/` as a legacy local fallback, but MCP tools prefer official documentation URLs.

```
docs/
├── 17.0/ (legacy fallback)
├── 18.0/ (legacy fallback)
└── 19.0/ (legacy fallback)

rules/
├── clean-code.mdc
└── odoo-development.mdc
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
Use `get_documentation_url()` or `odoo://docs/<version>/index`. The server returns official Odoo URLs and does not require local docs for normal use.

## Tips

1. **Detect, then set the Odoo version** - Use `detect_odoo_version()` to inspect local evidence, then `set_odoo_version()` if the active version should change
2. **Review development guidelines** - Use `get_development_guidelines()` for context-specific rules
3. **Follow naming conventions** - Generated code includes rules warnings for common mistakes
4. **Use descriptive model names** - e.g., `library.book` (with dots), not `lib_b` (with underscores)
5. **Check rules in generated code** - Each tool output includes relevant naming and coding rules
6. **Search before asking** - Use `search_documentation()` for official reference links
7. **Test incrementally** - module → models → views → security
8. **Review code against rules** - Use the `review_odoo_code` prompt for rule compliance checks

## License

MIT License

## Contributing

Contributions welcome! This server follows clean code principles and Odoo best practices.
