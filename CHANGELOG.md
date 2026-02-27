# Changelog

All notable changes to the Odoo Development MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-27

### Added

#### Core Features
- **MCP Server Implementation**: FastMCP-based server for Odoo development assistance
- **Version-Aware Documentation**: Support for Odoo versions 17.0, 18.0, and 19.0
- **Documentation Search**: Search across 302+ Odoo RST documentation files
- **Development Guidelines**: Access to clean code and Odoo-specific development rules

#### Tools (7 total)
- `set_odoo_version`: Switch between Odoo versions (17.0, 18.0, 19.0)
- `get_current_version`: Retrieve the currently selected Odoo version
- `search_documentation`: Search Odoo documentation with version-awareness
- `get_development_guidelines`: Access coding standards and best practices
- `create_odoo_module`: Generate complete Odoo module scaffolding
- `create_odoo_model`: Create Odoo models with fields and validation
- `create_odoo_view`: Generate Odoo views (form, tree, search, kanban)
- `create_security_rules`: Create security rules (ir.model.access.csv, record rules)

#### Resources (3 total)
- `odoo://docs/{version}/index`: List all available documentation files
- `odoo://docs/{version}/{path}`: Access specific documentation content
- `odoo://rules/{rule_name}`: Access development rules (clean-code, odoo-development)

#### Prompts (4 total)
- `develop_odoo_feature`: Guided workflow for feature development
- `debug_odoo_error`: Structured debugging assistance
- `upgrade_odoo_module`: Module upgrade workflow with version migration
- `review_odoo_code`: Code review with best practices validation

#### Documentation
- Quick Start guide with installation instructions
- OpenCode setup guide for VS Code integration
- Comprehensive testing guide explaining MCP architecture
- Troubleshooting guide for common issues
- Reorganization documentation and migration summary

#### Testing
- Complete test suite covering all tools, resources, and prompts
- Import verification script for structure validation
- Async test support with Python 3.12+

### Changed

#### Project Structure Reorganization
- **Adopted src-layout**: Moved to standard Python packaging structure
- **Package Location**: `odoo_mcp_server.py` → `src/odoo_mcp/server.py`
- **Test Suite**: `test_server.py` → `tests/test_server.py`
- **Documentation**: Consolidated guides into `guides/` directory
  - `QUICK_START.md` → `guides/QUICK_START.md`
  - `OPENCODE_SETUP.md` → `guides/OPENCODE_SETUP.md`
  - `TESTING.md` → `guides/TESTING.md`
- **Troubleshooting**: Moved to GitHub standard location `.github/TROUBLESHOOTING.md`
- **Examples**: Configuration templates moved to `examples/` directory
  - `opencode.jsonc.example` → `examples/opencode.jsonc.example`

#### Configuration Updates
- Updated `pyproject.toml` to build from `src/odoo_mcp` package
- Updated all documentation links to reflect new directory structure
- Created `src/odoo_mcp/__init__.py` with proper package exports
- Updated import paths throughout codebase

#### Path Resolution
- Updated documentation base path to work with new src-layout structure
- Fixed relative path references in server module
- Adjusted test imports to use proper package structure

### Fixed
- **Direct Execution Prevention**: Added stdin detection to prevent running MCP server directly from terminal
- **User Guidance**: Clear error messages when attempting direct execution
- **Import Structure**: Proper package initialization for clean imports

### Technical Details

#### Dependencies
- Python >= 3.12
- mcp >= 1.4.1 (FastMCP framework)
- hatchling (build system)

#### Supported MCP Clients
- Claude Desktop
- OpenCode (VS Code extension)
- MCP Inspector (development/testing)

#### Documentation Coverage
- 302+ RST files covering:
  - Backend development (models, views, controllers, ORM)
  - Frontend development (Owl components, JavaScript, SCSS)
  - API references (XML-RPC, JSON-RPC, external API)
  - Howtos (translations, web services, themes, reports)
  - Standard modules reference
  - Upgrade guides and CLI reference

---

## Version History

### [1.0.0] - 2026-02-27
- Initial release with complete MCP server implementation
- Full src-layout reorganization
- Comprehensive documentation and testing suite

---

## Migration Guide

### Updating from Pre-1.0.0 (Root Structure)

If you were using the previous structure with `odoo_mcp_server.py` in the root:

1. **Update MCP Client Configuration**:
   ```jsonc
   // Old path
   "command": "uv",
   "args": ["run", "odoo_mcp_server.py"]
   
   // New path
   "command": "uv",
   "args": ["--directory", "/path/to/odoo-mcp", "run", "src/odoo_mcp/server.py"]
   ```

2. **Update Imports** (if using as library):
   ```python
   # Old import
   from odoo_mcp_server import mcp, ODOO_VERSIONS
   
   # New import
   from odoo_mcp.server import mcp, ODOO_VERSIONS
   ```

3. **Install Dependencies**:
   ```bash
   uv sync
   ```

4. **Run Tests**:
   ```bash
   python -m tests.test_server
   ```

---

## Future Plans

- [ ] Add support for Odoo 20.0 documentation
- [ ] Implement custom module scanning and analysis
- [ ] Add code refactoring tools
- [ ] Expand testing framework with more edge cases
- [ ] Add performance optimization tools
- [ ] Implement module dependency analyzer

---

**For detailed reorganization information**, see [REORGANIZATION_SUMMARY.md](REORGANIZATION_SUMMARY.md)

**For development guidelines**, see:
- [guides/QUICK_START.md](guides/QUICK_START.md)
- [guides/TESTING.md](guides/TESTING.md)
- [.github/TROUBLESHOOTING.md](.github/TROUBLESHOOTING.md)
