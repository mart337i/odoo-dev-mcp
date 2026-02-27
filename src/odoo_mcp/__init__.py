"""
Odoo Development MCP Server

A Model Context Protocol (MCP) server for Odoo module development with AI assistance.
Provides version-aware documentation access, intelligent code generation, and development workflow automation.
"""

__version__ = "1.0.0"
__author__ = "Martin Egeskov"

from .server import (
    mcp,
    ODOO_VERSIONS,
    current_version,
    get_all_rst_files,
    get_documentation_index,
    get_documentation_content,
    get_development_rules,
    set_odoo_version,
    get_current_version,
    search_documentation,
    get_development_guidelines,
    create_odoo_module,
    create_odoo_model,
    create_odoo_view,
    create_security_rules,
    develop_odoo_feature,
    debug_odoo_error,
    upgrade_odoo_module,
    review_odoo_code,
    main,
)

__all__ = [
    "mcp",
    "ODOO_VERSIONS",
    "current_version",
    "get_all_rst_files",
    "get_documentation_index",
    "get_documentation_content",
    "get_development_rules",
    "set_odoo_version",
    "get_current_version",
    "search_documentation",
    "get_development_guidelines",
    "create_odoo_module",
    "create_odoo_model",
    "create_odoo_view",
    "create_security_rules",
    "develop_odoo_feature",
    "debug_odoo_error",
    "upgrade_odoo_module",
    "review_odoo_code",
    "main",
]
