# Odoo Documentation Files

This directory contains Odoo documentation files organized by version.

## Structure

```
docs/
├── 17.0/          # Odoo 17.0 documentation (102 files)
├── 18.0/          # Odoo 18.0 documentation (100 files)
└── 19.0/          # Odoo 19.0 documentation (100 files)
```

## Contents

Each version directory contains:
- **howtos/** - Step-by-step guides for common tasks
- **reference/** - Complete API and technical reference
  - backend/ - Python ORM, security, testing
  - frontend/ - JavaScript, Owl components, views
  - user_interface/ - View architectures, SCSS, icons
  - standard_modules/ - Account, payment modules

## Usage

### Via MCP Server

The MCP server provides access to all documentation:

```
Search Odoo documentation for "fields.Command"
Show me ORM documentation for Odoo 19.0
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

## File Count by Version

- **17.0**: 102 documentation files
- **18.0**: 100 documentation files  
- **19.0**: 100 documentation files
- **Total**: 302+ searchable documentation files

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

The MCP server provides full-text search across all files:

1. **By topic**: "Search for computed fields"
2. **By feature**: "How to use Many2many relationships"
3. **By version**: "Show ORM docs for Odoo 18.0"

## Version Differences

While most concepts are similar across versions, each version may have:
- New features and APIs
- Deprecated methods
- Updated best practices
- Performance improvements

Always check the documentation for your target Odoo version.

## Contributing

To add or update documentation:
1. Place .rst files in appropriate version directory
2. Follow existing directory structure
3. Use proper reStructuredText formatting
4. Test with MCP server search

## Resources

- Official Odoo Docs: https://www.odoo.com/documentation/
- MCP Server: [odoo_mcp_server.py](../odoo_mcp_server.py)
- Usage Guide: [OPENCODE_SETUP.md](../OPENCODE_SETUP.md)
