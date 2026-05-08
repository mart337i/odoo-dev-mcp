# Odoo Documentation Files

This directory contains legacy local Odoo documentation files organized by version.

The MCP server now prefers official Odoo documentation URLs instead of local copies. The official developer reference URL pattern is:

```text
https://www.odoo.com/documentation/<version>/developer/reference.html
```

## Structure

```
docs/
├── 17.0/          # Odoo 17.0 documentation (102 files)
├── 18.0/          # Odoo 18.0 documentation (100 files)
└── 19.0/          # Odoo 19.0 documentation (100 files)
```

## Contents

Each legacy version directory contains:
- **howtos/** - Step-by-step guides for common tasks
- **reference/** - Complete API and technical reference
  - backend/ - Python ORM, security, testing
  - frontend/ - JavaScript, Owl components, views
  - user_interface/ - View architectures, SCSS, icons
  - standard_modules/ - Account, payment modules

## Usage

### Via MCP Server

The MCP server provides official documentation links:

```
Search Odoo documentation for "fields.Command"
Show me ORM documentation for Odoo 19.0
Get documentation URL for reference/backend/orm
Search Odoo documentation for "base automation"
How do I create computed fields?
```

### Direct File Access

All files are in reStructuredText (.rst) format:

```bash
# Browse documentation
ls docs/19.0/reference/backend/

# Read a specific file
cat docs/19.0/reference/backend/orm.rst
```

## Legacy File Count by Version

- **17.0**: 102 documentation files
- **18.0**: 100 documentation files  
- **19.0**: 100 documentation files
- **Total**: 302+ local fallback documentation files

## Common Topics

### ORM & Models
- `reference/backend/orm.rst` - Complete ORM API
- `howtos/frontend_owl_components.rst` - Owl components

### Views & UI
- `reference/user_interface/view_architectures.rst` - All view types
- `howtos/website_themes.rst` - Website theming

### Security
- `reference/backend/security.rst` - Access control, rules

### Development
- `howtos/company.rst` - Multi-company patterns
- `howtos/create_reports.rst` - Custom reports

## Searching Documentation

The MCP server searches a built-in official reference catalog and returns official Odoo URLs:

1. **By topic**: "Search for computed fields"
2. **By feature**: "How to use Many2many relationships"
3. **By version**: "Show ORM docs for Odoo 18.0"
4. **By URL**: "Get documentation URL for reference/backend/security"

## Version Differences

While most concepts are similar across versions, each version may have:
- New features and APIs
- Deprecated methods
- Updated best practices
- Performance improvements

Always check the documentation for your target Odoo version.

## Contributing

To update documentation behavior, update the official reference catalog in `src/odoo_mcp/server.py`. Local `.rst` files are fallback material only.

## Resources

- Official Odoo Docs: https://www.odoo.com/documentation/
- MCP Server: [odoo_mcp_server.py](../odoo_mcp_server.py)
- Usage Guide: [OPENCODE_SETUP.md](../OPENCODE_SETUP.md)
