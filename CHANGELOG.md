# Changelog

All notable changes to the Odoo Development MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `detect_odoo_version` tool to report likely local Odoo versions from environment variables, `release.py`, addon manifests, and branch names without changing the active MCP version.
- `inspect_odoo_source` tool to read Odoo core and addon source with AST and return compact summaries of manifests, models, controllers, routes, imports, parse issues, and suggested next reads.

## [1.2.0] - 2026-05-08

### Added

- Local Odoo environment context support through `ODOO_SOURCE`, `ODOO_BASE_COMMAND`, and `ODOO_TOOL_README`, exposed via `get_odoo_local_context()` and `odoo://local/context`.
- OWL frontend planning and scaffold tools for Odoo components, client actions, field widgets, services, and Hoot tests.
- Export/import/test coverage for the new OWL tool set.

### Fixed

- Redact sensitive local command and README values from local context output.
- Escape generated OWL JavaScript/XML snippets and avoid undeclared default test props.
- Detect nested local Odoo source layouts such as `odoo*/odoo-bin` and `enterprise-*`.

## [1.1.0] - 2026-05-08

### Changed

- Documentation tools now prefer official Odoo developer reference URLs using `https://www.odoo.com/documentation/<version>/developer/reference.html`.
- `search_documentation` now searches a built-in official reference catalog and returns stable Odoo documentation links instead of reading local `.rst` files.
- Generated module, model, view, security, and prompt outputs now point to official Odoo documentation URLs.
- `create_odoo_view` now generates version-aware collection views (`tree` for 17.0, `list` for 18.0/19.0), avoids fake menu parents, and includes view/action/security/test guardrails.

### Added

- `get_documentation_url` tool for direct official Odoo documentation URL lookup.
- `plan_odoo_feature` tool for skill-informed implementation plans covering models, views, security, tests, and official references.
- `create_base_automation` tool for version-aware automated action XML using `base.automation` and linked `ir.actions.server` records.
- `layout_module_dependencies` tool for ordering and explaining Odoo manifest dependencies.
- `create_upgrade_script` tool for version-aware `pre-migration.py`, `post-migration.py`, and `end-migration.py` scaffolds.
- `create_upgrade_script` now includes verified `odoo.upgrade.util` examples for model, field, XML ID, module, SQL, and ORM migration helpers.
- `explain_odoo_error` tool for patterned Odoo traceback diagnosis with likely area, root cause, minimal reproduction, and docs links.
- Anchored documentation shortcuts for common Odoo topics like computed fields, record rules, access rights, controllers, testing, OWL, and upgrade scripts.

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
