from html import escape
from pathlib import Path
from typing import Any
import sys
from mcp.server.fastmcp import FastMCP

ODOO_VERSIONS = ["17.0", "18.0", "19.0"]
# Legacy local docs path. Official docs links are the primary source now.
DOCS_BASE_PATH = Path(__file__).parent.parent.parent / "docs"
RULES_BASE_PATH = Path(__file__).parent.parent.parent / "rules"
ODOO_DOCS_BASE_URL = "https://www.odoo.com/documentation"

REFERENCE_TOPICS: list[dict[str, Any]] = [
    {
        "section": "Reference",
        "title": "Developer Reference",
        "path": "",
        "keywords": ["reference", "developer", "index", "overview"],
    },
    {
        "section": "Server framework",
        "title": "Server framework",
        "path": "reference/backend",
        "keywords": ["server", "backend", "python", "framework"],
    },
    {
        "section": "Server framework",
        "title": "ORM API",
        "path": "reference/backend/orm",
        "keywords": ["orm", "models", "fields", "recordsets", "environment", "api", "decorators", "constraints", "indexes", "exceptions"],
    },
    {
        "section": "Server framework",
        "title": "ORM Changelog",
        "path": "reference/backend/orm/changelog",
        "keywords": ["orm", "changelog", "migration", "version changes"],
    },
    {
        "section": "Server framework",
        "title": "Data Files",
        "path": "reference/backend/data",
        "keywords": ["xml", "csv", "data", "records", "noupdate", "shortcuts"],
    },
    {
        "section": "Server framework",
        "title": "Actions",
        "path": "reference/backend/actions",
        "keywords": ["actions", "window action", "server action", "report action", "client action", "cron", "ir.actions", "ir.cron"],
    },
    {
        "section": "Server framework",
        "title": "QWeb Reports",
        "path": "reference/backend/reports",
        "keywords": ["reports", "qweb", "pdf", "paper format", "templates"],
    },
    {
        "section": "Server framework",
        "title": "Module Manifests",
        "path": "reference/backend/module",
        "keywords": ["module", "manifest", "__manifest__.py", "dependencies", "assets", "hooks"],
    },
    {
        "section": "Server framework",
        "title": "Security in Odoo",
        "path": "reference/backend/security",
        "keywords": ["security", "access rights", "acl", "record rules", "groups", "field access", "sudo"],
    },
    {
        "section": "Server framework",
        "title": "Performance",
        "path": "reference/backend/performance",
        "keywords": ["performance", "profiling", "n+1", "batch", "prefetch", "queries", "optimization"],
    },
    {
        "section": "Server framework",
        "title": "Testing Odoo",
        "path": "reference/backend/testing",
        "keywords": ["testing", "tests", "transactioncase", "httptest", "httpcase", "form", "tags", "mock"],
    },
    {
        "section": "Server framework",
        "title": "Web Controllers",
        "path": "reference/backend/http",
        "keywords": ["controllers", "http", "routes", "request", "auth", "csrf", "endpoint"],
    },
    {
        "section": "Server framework",
        "title": "Mixins and Useful Classes",
        "path": "reference/backend/mixins",
        "keywords": ["mixins", "mail.thread", "activity", "portal", "website", "utm", "alias"],
    },
    {
        "section": "Web framework",
        "title": "Web framework",
        "path": "reference/frontend",
        "keywords": ["frontend", "web", "javascript", "owl", "framework"],
    },
    {
        "section": "Web framework",
        "title": "Framework Overview",
        "path": "reference/frontend/framework_overview",
        "keywords": ["frontend", "overview", "webclient", "environment", "building blocks", "domain", "bus"],
    },
    {
        "section": "Web framework",
        "title": "Assets",
        "path": "reference/frontend/assets",
        "keywords": ["assets", "bundles", "lazy loading", "ir.asset", "scss", "javascript"],
    },
    {
        "section": "Web framework",
        "title": "Javascript Modules",
        "path": "reference/frontend/javascript_modules",
        "keywords": ["javascript", "modules", "esm", "odoo module system", "native modules"],
    },
    {
        "section": "Web framework",
        "title": "Owl components",
        "path": "reference/frontend/owl_components",
        "keywords": ["owl", "components", "templates", "props", "hooks", "frontend"],
    },
    {
        "section": "Web framework",
        "title": "Registries",
        "path": "reference/frontend/registries",
        "keywords": ["registries", "registry", "fields", "views", "services", "client actions"],
    },
    {
        "section": "Web framework",
        "title": "Services",
        "path": "reference/frontend/services",
        "keywords": ["services", "frontend", "notification", "rpc", "action", "router", "effect"],
    },
    {
        "section": "Web framework",
        "title": "Hooks",
        "path": "reference/frontend/hooks",
        "keywords": ["hooks", "useassets", "useautofocus", "usebus", "usepager", "useposition", "usespellcheck"],
    },
    {
        "section": "Web framework",
        "title": "Patching code",
        "path": "reference/frontend/patching_code",
        "keywords": ["patch", "patching", "javascript", "component", "class"],
    },
    {
        "section": "Web framework",
        "title": "Error handling",
        "path": "reference/frontend/error_handling",
        "keywords": ["errors", "error handling", "javascript", "lifecycle", "exceptions"],
    },
    {
        "section": "Web framework",
        "title": "Javascript Reference",
        "path": "reference/frontend/javascript_reference",
        "keywords": ["javascript", "web client", "notifications", "systray", "translations", "session", "views", "fields"],
    },
    {
        "section": "Web framework",
        "title": "Mobile JavaScript",
        "path": "reference/frontend/mobile",
        "keywords": ["mobile", "javascript", "app", "device"],
    },
    {
        "section": "Web framework",
        "title": "QWeb Templates",
        "path": "reference/frontend/qweb",
        "keywords": ["qweb", "templates", "t-out", "t-if", "t-foreach", "frontend"],
    },
    {
        "section": "Web framework",
        "title": "Odoo Editor",
        "path": "reference/frontend/odoo_editor",
        "keywords": ["editor", "powerbox", "html", "wysiwyg"],
    },
    {
        "section": "Web framework",
        "title": "JavaScript Unit Testing",
        "path": "reference/frontend/unit_testing",
        "keywords": ["javascript", "unit testing", "qunit", "frontend tests"],
    },
    {
        "section": "User interface",
        "title": "User interface",
        "path": "reference/user_interface",
        "keywords": ["ui", "user interface", "views", "icons", "scss"],
    },
    {
        "section": "User interface",
        "title": "View records",
        "path": "reference/user_interface/view_records",
        "keywords": ["view records", "views", "inheritance", "fields", "model commons"],
    },
    {
        "section": "User interface",
        "title": "View architectures",
        "path": "reference/user_interface/view_architectures",
        "keywords": ["views", "view architectures", "form", "list", "tree", "search", "kanban", "graph", "pivot", "calendar", "gantt", "map"],
    },
    {
        "section": "User interface",
        "title": "SCSS inheritance",
        "path": "reference/user_interface/scss_inheritance",
        "keywords": ["scss", "css", "inheritance", "themes"],
    },
    {
        "section": "User interface",
        "title": "UI icons",
        "path": "reference/user_interface/icons",
        "keywords": ["icons", "ui icons", "spreadsheet icons"],
    },
    {
        "section": "Standard modules",
        "title": "Standard modules",
        "path": "reference/standard_modules",
        "keywords": ["standard modules", "account", "payment"],
    },
    {
        "section": "Standard modules",
        "title": "Accounting",
        "path": "reference/standard_modules/account",
        "keywords": ["account", "accounting", "tax", "fiscal position", "report"],
    },
    {
        "section": "Standard modules",
        "title": "Account Tag",
        "path": "reference/standard_modules/account/account_account_tag",
        "keywords": ["account", "tag", "account tag"],
    },
    {
        "section": "Standard modules",
        "title": "Account",
        "path": "reference/standard_modules/account/account_account",
        "keywords": ["account", "chart of accounts"],
    },
    {
        "section": "Standard modules",
        "title": "Fiscal Position",
        "path": "reference/standard_modules/account/account_fiscal_position",
        "keywords": ["account", "fiscal position", "tax mapping"],
    },
    {
        "section": "Standard modules",
        "title": "Account Group",
        "path": "reference/standard_modules/account/account_group",
        "keywords": ["account", "account group"],
    },
    {
        "section": "Standard modules",
        "title": "Account Report",
        "path": "reference/standard_modules/account/account_report",
        "keywords": ["account", "report", "financial report"],
    },
    {
        "section": "Standard modules",
        "title": "Account Report Line",
        "path": "reference/standard_modules/account/account_report_line",
        "keywords": ["account", "report line", "financial report"],
    },
    {
        "section": "Standard modules",
        "title": "Taxes",
        "path": "reference/standard_modules/account/account_tax",
        "keywords": ["account", "tax", "taxes"],
    },
    {
        "section": "Standard modules",
        "title": "Tax Repartitions",
        "path": "reference/standard_modules/account/account_tax_repartition",
        "keywords": ["account", "tax", "tax repartition"],
    },
    {
        "section": "Standard modules",
        "title": "Payment",
        "path": "reference/standard_modules/payment",
        "keywords": ["payment", "provider", "token", "transaction", "method"],
    },
    {
        "section": "Standard modules",
        "title": "Payment Method",
        "path": "reference/standard_modules/payment/payment_method",
        "keywords": ["payment", "payment method"],
    },
    {
        "section": "Standard modules",
        "title": "Payment Provider",
        "path": "reference/standard_modules/payment/payment_provider",
        "keywords": ["payment", "payment provider", "acquirer"],
    },
    {
        "section": "Standard modules",
        "title": "Payment Token",
        "path": "reference/standard_modules/payment/payment_token",
        "keywords": ["payment", "payment token", "tokenization"],
    },
    {
        "section": "Standard modules",
        "title": "Payment Transaction",
        "path": "reference/standard_modules/payment/payment_transaction",
        "keywords": ["payment", "payment transaction", "transaction"],
    },
    {
        "section": "Command-line interface",
        "title": "Command-line interface (CLI)",
        "path": "reference/cli",
        "keywords": ["cli", "command line", "server", "shell", "db", "module", "scaffold", "upgrade_code"],
    },
    {
        "section": "Upgrades",
        "title": "Upgrades",
        "path": "reference/upgrades",
        "keywords": ["upgrades", "migration", "upgrade scripts", "upgrade utils"],
    },
    {
        "section": "Upgrades",
        "title": "Upgrade scripts",
        "path": "reference/upgrades/upgrade_scripts",
        "keywords": ["upgrade scripts", "migrations", "pre", "post", "end"],
    },
    {
        "section": "Upgrades",
        "title": "Upgrade utils",
        "path": "reference/upgrades/upgrade_utils",
        "keywords": ["upgrade utils", "migration", "testing upgrade scripts"],
    },
    {
        "section": "External APIs",
        "title": "External JSON-2 API",
        "path": "reference/external_api",
        "keywords": ["external api", "json-2", "api key", "transaction", "rpc migration"],
    },
    {
        "section": "External APIs",
        "title": "External RPC API",
        "path": "reference/external_rpc_api",
        "keywords": ["external rpc", "xml-rpc", "json-rpc", "search_read", "create", "write", "unlink"],
    },
    {
        "section": "External APIs",
        "title": "Extract API",
        "path": "reference/extract_api",
        "keywords": ["extract api", "parse", "routes", "integration testing"],
    },
]

TOPIC_SHORTCUTS: list[dict[str, Any]] = [
    {
        "section": "Server framework shortcuts",
        "title": "Computed fields",
        "path": "reference/backend/orm#computed-fields",
        "keywords": ["computed fields", "compute", "api.depends", "depends", "store", "inverse", "search"],
    },
    {
        "section": "Server framework shortcuts",
        "title": "Field types",
        "path": "reference/backend/orm#fields",
        "keywords": ["field types", "char", "many2one", "one2many", "many2many", "selection", "monetary"],
    },
    {
        "section": "Server framework shortcuts",
        "title": "Method decorators",
        "path": "reference/backend/orm#module-odoo.api",
        "keywords": ["decorators", "api.depends", "api.constrains", "api.onchange", "api.model", "api.ondelete"],
    },
    {
        "section": "Server framework shortcuts",
        "title": "Constraints and indexes",
        "path": "reference/backend/orm#constraints-and-indexes",
        "keywords": ["constraints", "indexes", "sql constraints", "unique", "models.Constraint", "models.Index"],
    },
    {
        "section": "Server framework shortcuts",
        "title": "Common ORM methods",
        "path": "reference/backend/orm#common-orm-methods",
        "keywords": ["search", "browse", "create", "write", "unlink", "read_group", "mapped", "filtered", "sorted"],
    },
    {
        "section": "Security shortcuts",
        "title": "Access rights",
        "path": "reference/backend/security#access-rights",
        "keywords": ["access rights", "acl", "ir.model.access.csv", "perm_read", "perm_write", "perm_create", "perm_unlink"],
    },
    {
        "section": "Security shortcuts",
        "title": "Record rules",
        "path": "reference/backend/security#record-rules",
        "keywords": ["record rules", "ir.rule", "domain_force", "row-level security", "multi-company"],
    },
    {
        "section": "Security shortcuts",
        "title": "Security pitfalls",
        "path": "reference/backend/security#security-pitfalls",
        "keywords": ["sudo", "security pitfalls", "sql injection", "public", "portal", "access checks"],
    },
    {
        "section": "Actions shortcuts",
        "title": "Window actions",
        "path": "reference/backend/actions#window-actions-ir-actions-act-window",
        "keywords": ["window actions", "act_window", "view_mode", "menu", "action"],
    },
    {
        "section": "Actions shortcuts",
        "title": "Scheduled actions",
        "path": "reference/backend/actions#module-odoo.addons.base.models.ir_cron",
        "keywords": ["cron", "scheduled action", "ir.cron", "background job"],
    },
    {
        "section": "Actions shortcuts",
        "title": "Automated actions",
        "path": "reference/backend/actions#server-actions-ir-actions-server",
        "keywords": ["automated actions", "base automation", "base.automation", "automation rule", "server action", "ir.actions.server"],
    },
    {
        "section": "Testing shortcuts",
        "title": "Testing Python code",
        "path": "reference/backend/testing#testing-python-code",
        "keywords": ["transactioncase", "singletransactioncase", "form helper", "python tests", "tagged"],
    },
    {
        "section": "Testing shortcuts",
        "title": "Integration testing",
        "path": "reference/backend/testing#integration-testing",
        "keywords": ["httpcase", "integration testing", "browser", "controller test", "tour"],
    },
    {
        "section": "Controller shortcuts",
        "title": "HTTP controllers",
        "path": "reference/backend/http#controllers",
        "keywords": ["controllers", "route", "auth", "csrf", "request", "portal", "public endpoint"],
    },
    {
        "section": "Frontend shortcuts",
        "title": "Owl best practices",
        "path": "reference/frontend/owl_components#best-practices",
        "keywords": ["owl", "component", "template", "props", "hooks", "best practices"],
    },
    {
        "section": "Frontend shortcuts",
        "title": "Service usage",
        "path": "reference/frontend/services#using-a-service",
        "keywords": ["services", "useService", "notification", "action service", "rpc"],
    },
    {
        "section": "User interface shortcuts",
        "title": "List view architecture",
        "path": "reference/user_interface/view_architectures#list",
        "keywords": ["list view", "tree view", "view architecture", "columns", "editable"],
    },
    {
        "section": "User interface shortcuts",
        "title": "Form view architecture",
        "path": "reference/user_interface/view_architectures#form",
        "keywords": ["form view", "sheet", "notebook", "group", "header", "buttons"],
    },
    {
        "section": "Upgrade shortcuts",
        "title": "Writing upgrade scripts",
        "path": "reference/upgrades/upgrade_scripts#writing-upgrade-scripts",
        "keywords": ["upgrade scripts", "migration scripts", "pre-migration", "post-migration", "end-migration"],
    },
    {
        "section": "Upgrade shortcuts",
        "title": "Upgrade utilities",
        "path": "reference/upgrades/upgrade_utils",
        "keywords": ["upgrade utils", "rename model", "rename field", "rename xmlid", "data migration", "module migration"],
    },
]

mcp = FastMCP("Odoo Development Assistant")

current_version = {"value": "19.0"}


def get_all_rst_files(version: str) -> list[tuple[Path, str]]:
    """Return local RST files if present. Kept for backward-compatible tests/imports."""
    version_path = DOCS_BASE_PATH / version
    if not version_path.exists():
        return []

    files = []
    for rst_file in version_path.rglob("*.rst"):
        relative = rst_file.relative_to(version_path)
        uri_path = str(relative).replace("\\", "/").removesuffix(".rst")
        files.append((rst_file, uri_path))

    return files


def normalize_reference_path(path: str = "") -> str:
    clean_path = path.strip().strip("/")
    clean_path = clean_path.split("#", 1)[0].split("?", 1)[0]
    clean_path = clean_path.removesuffix(".html").removesuffix(".rst")

    if clean_path in {"", "reference", "developer/reference"}:
        return ""
    if clean_path.startswith("developer/reference/"):
        clean_path = clean_path.removeprefix("developer/")
    elif not clean_path.startswith("reference/"):
        clean_path = f"reference/{clean_path}"

    return clean_path


def get_reference_fragment(path: str = "") -> str:
    if "#" not in path:
        return ""
    return path.split("#", 1)[1].split("?", 1)[0].strip()


def get_reference_target(path: str = "") -> str:
    reference_path = normalize_reference_path(path)
    fragment = get_reference_fragment(path)
    if fragment:
        return f"{reference_path}#{fragment}" if reference_path else f"#{fragment}"
    return reference_path


def get_all_reference_topics() -> list[dict[str, Any]]:
    return REFERENCE_TOPICS + TOPIC_SHORTCUTS


def get_official_documentation_url(version: str, path: str = "") -> str:
    reference_path = normalize_reference_path(path)
    fragment = get_reference_fragment(path)
    suffix = f"#{fragment}" if fragment else ""
    if not reference_path:
        return f"{ODOO_DOCS_BASE_URL}/{version}/developer/reference.html{suffix}"
    return f"{ODOO_DOCS_BASE_URL}/{version}/developer/{reference_path}.html{suffix}"


def get_reference_topics(version: str) -> list[dict[str, str]]:
    return [
        {
            "section": topic["section"],
            "title": topic["title"],
            "path": topic["path"],
            "url": get_official_documentation_url(version, topic["path"]),
        }
        for topic in get_all_reference_topics()
    ]


def find_reference_topic(path: str) -> dict[str, Any] | None:
    reference_target = get_reference_target(path)
    reference_path = normalize_reference_path(path)
    for topic in get_all_reference_topics():
        if get_reference_target(topic["path"]) == reference_target:
            return topic
    for topic in get_all_reference_topics():
        if normalize_reference_path(topic["path"]) == reference_path:
            return topic
    return None


def get_skill_informed_guidance() -> str:
    return """## Odoo Operating Discipline

- Detect the target Odoo version before version-sensitive work.
- Inspect existing manifests, models, views, security, controllers, assets, tests, and docs before proposing changes.
- Treat models, views, controllers, workflows, and access behavior as security-sensitive; check ACLs, record rules, groups, `sudo()`, and multi-company boundaries together.
- Prefer small idiomatic changes that follow existing addon structure.
- Verify behavior at the Odoo seam: ORM, form helper, access test, controller test, report rendering, or mocked integration.
- Ask before running commands that touch a database or local service.
"""


@mcp.resource("odoo://docs/{version}/index")
def get_documentation_index(version: str) -> str:
    if version not in ODOO_VERSIONS:
        return f"Error: Unknown Odoo version {version}. Available: {', '.join(ODOO_VERSIONS)}"

    content = f"# Odoo {version} Official Developer Reference\n\n"
    content += f"Current development version: {current_version['value']}\n\n"
    content += f"Primary reference: {get_official_documentation_url(version)}\n\n"
    content += "This MCP server points to official Odoo documentation instead of vendoring documentation content.\n\n"

    current_section = ""
    for topic in get_reference_topics(version):
        if topic["section"] != current_section:
            current_section = topic["section"]
            content += f"\n## {current_section}\n\n"
        path = topic["path"] or "reference"
        content += f"- {topic['title']}: {topic['url']} (`{path}`)\n"

    return content


@mcp.resource("odoo://docs/{version}/{path}")
def get_documentation_content(version: str, path: str) -> str:
    if version not in ODOO_VERSIONS:
        return f"Error: Unknown Odoo version {version}"

    topic = find_reference_topic(path)
    url = get_official_documentation_url(version, path)
    title = topic["title"] if topic else normalize_reference_path(path) or "Developer Reference"

    content = f"# {title} (Odoo {version})\n\n"
    content += f"Official documentation: {url}\n\n"
    content += "Use the official page as the source of truth for this version. "
    content += "This server intentionally returns stable documentation links rather than stale local copies.\n"

    if topic:
        keywords = ", ".join(topic.get("keywords", []))
        content += f"\nRelated keywords: {keywords}\n"

    return content


@mcp.resource("odoo://rules/{rule_name}")
def get_development_rules(rule_name: str) -> str:
    valid_rules = {
        "clean-code": "clean-code.mdc",
        "odoo-development": "odoo-development.mdc",
        "all": None
    }
    
    if rule_name not in valid_rules:
        return f"Unknown rule set. Available: {', '.join(valid_rules.keys())}"
    
    if rule_name == "all":
        content = "# Complete Development Guidelines\n\n"
        for rule_file in RULES_BASE_PATH.glob("*.mdc"):
            try:
                rule_content = rule_file.read_text(encoding="utf-8")
                content += f"\n\n---\n\n{rule_content}\n\n"
            except Exception:
                continue
        return content
    
    rule_file = RULES_BASE_PATH / valid_rules[rule_name]
    if not rule_file.exists():
        return f"Rule file not found: {rule_name}"
    
    try:
        content = rule_file.read_text(encoding="utf-8")
        return content
    except Exception as e:
        return f"Error reading rules: {str(e)}"


@mcp.tool()
def set_odoo_version(version: str) -> str:
    if version not in ODOO_VERSIONS:
        return f"Invalid version. Available versions: {', '.join(ODOO_VERSIONS)}"
    
    current_version["value"] = version
    return f"Odoo version set to {version}"


@mcp.tool()
def get_current_version() -> str:
    return f"Current Odoo development version: {current_version['value']}"


@mcp.tool()
def get_documentation_url(path: str = "", version: str = "") -> str:
    search_version = version if version and version in ODOO_VERSIONS else current_version["value"]
    url = get_official_documentation_url(search_version, path)
    reference_path = normalize_reference_path(path) or "reference"
    return f"Official Odoo {search_version} documentation for `{reference_path}`: {url}"


@mcp.tool()
def search_documentation(query: str, version: str = "") -> str:
    search_version = version if version and version in ODOO_VERSIONS else current_version["value"]

    results = []
    query_lower = query.lower()

    for topic in get_all_reference_topics():
        searchable = " ".join([
            topic["section"],
            topic["title"],
            topic["path"],
            " ".join(topic.get("keywords", [])),
        ]).lower()
        if query_lower in searchable:
            results.append(topic)

    if not results:
        return (
            f"No catalog results found for '{query}' in Odoo {search_version}.\n\n"
            f"Start from the official developer reference: {get_official_documentation_url(search_version)}"
        )

    output = f"Official Odoo {search_version} documentation links for '{query}':\n\n"
    for result in results[:10]:
        output += f"## {result['title']}\n"
        output += f"Section: {result['section']}\n"
        output += f"Path: `{result['path'] or 'reference'}`\n"
        output += f"Keywords: {', '.join(result.get('keywords', []))}\n"
        output += f"URL: {get_official_documentation_url(search_version, result['path'])}\n\n"

    return output


@mcp.tool()
def get_development_guidelines(context: str = "general") -> str:
    contexts = {
        "general": ["clean-code", "odoo-development"],
        "models": ["odoo-development"],
        "views": ["odoo-development"],
        "security": ["odoo-development"],
        "all": ["clean-code", "odoo-development"]
    }
    
    if context not in contexts:
        context = "general"
    
    guidelines = f"# Development Guidelines for {context.title()} Context\n\n"
    guidelines += f"Current Odoo Version: {current_version['value']}\n\n"
    guidelines += get_skill_informed_guidance() + "\n"
    
    rule_files = contexts[context]
    
    for rule_name in rule_files:
        rule_file = RULES_BASE_PATH / f"{rule_name}.mdc"
        if rule_file.exists():
            try:
                content = rule_file.read_text(encoding="utf-8")
                lines = content.split('\n')
                clean_content = []
                in_frontmatter = False
                frontmatter_count = 0
                
                for line in lines:
                    if line.strip() == '---':
                        frontmatter_count += 1
                        in_frontmatter = not in_frontmatter
                        continue
                    if not in_frontmatter and frontmatter_count >= 2:
                        clean_content.append(line)
                
                guidelines += '\n'.join(clean_content) + "\n\n---\n\n"
            except Exception:
                continue
    
    guidelines += "\n## Quick Reference Links\n\n"
    guidelines += f"- Full rules: odoo://rules/all\n"
    guidelines += f"- Clean code: odoo://rules/clean-code\n"
    guidelines += f"- Odoo conventions: odoo://rules/odoo-development\n"
    guidelines += f"- Official developer reference: {get_official_documentation_url(current_version['value'])}\n"
    guidelines += f"- ORM API: {get_official_documentation_url(current_version['value'], 'reference/backend/orm')}\n"
    guidelines += f"- Security: {get_official_documentation_url(current_version['value'], 'reference/backend/security')}\n"
    guidelines += f"- Testing: {get_official_documentation_url(current_version['value'], 'reference/backend/testing')}\n"
    
    return guidelines


@mcp.tool()
def create_odoo_module(
    module_name: str,
    display_name: str,
    description: str,
    author: str = "Your Company",
    category: str = "Uncategorized",
    depends: list[str] = []
) -> str:
    version = current_version["value"]
    if not depends:
        depends = ["base"]
    
    manifest_content = f'''{{
    'name': '{display_name}',
    'version': '{version}.1.0.0',
    'category': '{category}',
    'summary': '{description}',
    'description': """
        {description}
    """,
    'author': '{author}',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': {depends},
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}}
'''
    
    init_content = '''from . import models
'''
    
    doc_reference = get_official_documentation_url(version, "reference/backend/module")
    rules_reference = "odoo://rules/odoo-development"
    
    structure = f"""# Module Structure for {module_name} (Odoo {version})

## Directory Structure

{module_name}/
├── __init__.py
├── __manifest__.py
├── models/
│   └── __init__.py
├── views/
├── security/
│   └── ir.model.access.csv
├── data/
└── static/
    └── description/
        └── icon.png

## File Contents

### __manifest__.py
```python
{manifest_content}
```

### __init__.py
```python
{init_content}
```

### models/__init__.py
```python
# Import your models here
```

### security/ir.model.access.csv
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_{module_name}_user,{module_name}.user,model_{module_name}_model,base.group_user,1,1,1,1
```

## Naming Convention Rules ⚠️
- **Module name**: Use lowercase_with_underscores (e.g., `sale_extended`)
- **Technical name**: Same as directory name
- **Display name**: Human-readable (e.g., "Sales Extended")
- **Never use hyphens** in module names

## Next Steps
1. Create the directory structure above
2. Add models: `create_odoo_model()`
3. Add views: `create_odoo_view()`
4. Configure security: `create_security_rules()`
5. Review guidelines: `get_development_guidelines("general")`

## References
- Documentation: {doc_reference}
- Development Rules: {rules_reference}
- Naming Conventions: See "Module Structure" in rules
"""
    
    return structure


@mcp.tool()
def create_odoo_model(
    model_name: str,
    model_description: str,
    fields: list[dict[str, Any]],
    inherit: str = ""
) -> str:
    class_name = "".join(word.capitalize() for word in model_name.split("."))
    
    field_definitions = []
    for field in fields:
        field_name = field.get("name", "field")
        field_type = field.get("type", "Char")
        field_string = field.get("string", field_name.replace("_", " ").title())
        required = field.get("required", False)
        
        if field_type == "Many2one":
            comodel = field.get("comodel_name", "res.partner")
            field_def = f'    {field_name} = fields.Many2one(\'{comodel}\', string=\'{field_string}\', required={required})'
        elif field_type == "One2many":
            comodel = field.get("comodel_name")
            inverse = field.get("inverse_name")
            field_def = f'    {field_name} = fields.One2many(\'{comodel}\', \'{inverse}\', string=\'{field_string}\')'
        elif field_type == "Many2many":
            comodel = field.get("comodel_name")
            field_def = f'    {field_name} = fields.Many2many(\'{comodel}\', string=\'{field_string}\')'
        elif field_type == "Selection":
            selection = field.get("selection", "[('draft', 'Draft'), ('done', 'Done')]")
            field_def = f'    {field_name} = fields.Selection({selection}, string=\'{field_string}\', required={required})'
        else:
            field_def = f'    {field_name} = fields.{field_type}(string=\'{field_string}\', required={required})'
        
        field_definitions.append(field_def)
    
    fields_code = "\n".join(field_definitions)
    version = current_version["value"]
    
    if inherit:
        model_code = f'''from odoo import models, fields, api


class {class_name}(models.Model):
    _inherit = '{inherit}'

{fields_code}
'''
    else:
        model_code = f'''from odoo import models, fields, api


class {class_name}(models.Model):
    _name = '{model_name}'
    _description = '{model_description}'

    name = fields.Char(string='Name', required=True)
{fields_code}
'''
    
    doc_reference = get_official_documentation_url(version, "reference/backend/orm")
    rules_reference = "odoo://rules/odoo-development"
    
    return f"""# Model Definition for {model_name} (Odoo {version})

**File**: models/{model_name.replace('.', '_')}.py

```python
{model_code}
```

## Naming Convention Rules ⚠️
- **Model name**: Use dots (e.g., `sale.order.line`, not `sale_order_line`)
- **Class name**: CamelCase (e.g., `SaleOrderLine`)
- **Field naming**:
  - Boolean: Start with `is_`, `has_`, `can_`
  - Many2one: End with `_id`
  - One2many/Many2many: End with `_ids`
- **Method naming**: Use `_compute_`, `_onchange_`, `_check_` prefixes

## Next Steps
1. Import in models/__init__.py: `from . import {model_name.replace('.', '_')}`
2. Add security: `create_security_rules("{model_name}", "module_name")`
3. Create views: `create_odoo_view("{model_name}", "form", [fields])`
4. Review guidelines: `get_development_guidelines("models")`

## References
- ORM Documentation: {doc_reference}
- Development Rules: {rules_reference}
- See "Python Coding Standards" section in rules
"""


@mcp.tool()
def create_odoo_view(
    model_name: str,
    view_type: str,
    fields_to_display: list[str],
    view_name: str = "",
    parent_menu: str = ""
) -> str:
    version = current_version["value"]
    requested_view_type = view_type.lower().strip()
    collection_view_type = "list" if version in {"18.0", "19.0"} else "tree"
    normalized_view_type = collection_view_type if requested_view_type in {"tree", "list"} else requested_view_type

    if normalized_view_type not in {"list", "tree", "form", "search", "kanban"}:
        return f"Unsupported view type: {view_type}. Supported types: list/tree, form, search, kanban"

    if not view_name:
        view_name = f"{model_name.replace('.', '_')}_{normalized_view_type}_view"

    model_underscore = model_name.replace(".", "_")
    display_name = model_name.split(".")[-1].replace("_", " ").title()

    if normalized_view_type in {"tree", "list"}:
        fields_xml = "\n            ".join([f'<field name="{field}"/>' for field in fields_to_display])
        view_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="{view_name}" model="ir.ui.view">
        <field name="name">{model_name}.{normalized_view_type}</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <{normalized_view_type}>
                {fields_xml}
            </{normalized_view_type}>
        </field>
    </record>
</odoo>'''

    elif normalized_view_type == "form":
        fields_xml = "\n                    ".join([f'<field name="{field}"/>' for field in fields_to_display])
        view_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="{view_name}" model="ir.ui.view">
        <field name="name">{model_name}.form</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        {fields_xml}
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>'''

    elif normalized_view_type == "search":
        fields_xml = "\n                ".join([f'<field name="{field}"/>' for field in fields_to_display])
        view_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="{view_name}" model="ir.ui.view">
        <field name="name">{model_name}.search</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <search>
                {fields_xml}
            </search>
        </field>
    </record>
</odoo>'''

    else:
        kanban_fields = fields_to_display or ["name"]
        field_declarations = "\n                ".join([f'<field name="{field}"/>' for field in kanban_fields])
        card_lines = "\n                                    ".join([f'<div><field name="{field}"/></div>' for field in kanban_fields[:4]])
        view_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="{view_name}" model="ir.ui.view">
        <field name="name">{model_name}.kanban</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <kanban>
                {field_declarations}
                <templates>
                    <t t-name="kanban-box">
                        <div class="oe_kanban_card">
                            <div class="oe_kanban_content">
                                {card_lines}
                            </div>
                        </div>
                    </t>
                </templates>
            </kanban>
        </field>
    </record>
</odoo>'''

    if parent_menu:
        menu_xml = f'''    <menuitem id="menu_{model_underscore}"
              name="{display_name}"
              action="action_{model_underscore}"
              parent="{parent_menu}"/>'''
    else:
        menu_xml = f'''    <!-- Add a menu only after choosing a real parent menu:
    <menuitem id="menu_{model_underscore}"
              name="{display_name}"
              action="action_{model_underscore}"
              parent="your_module.menu_parent"/>
    -->'''

    action_xml = f'''    <record id="action_{model_underscore}" model="ir.actions.act_window">
        <field name="name">{display_name}</field>
        <field name="res_model">{model_name}</field>
        <field name="view_mode">{collection_view_type},form</field>
    </record>

{menu_xml}'''

    doc_reference = get_official_documentation_url(version, "reference/user_interface/view_architectures")
    action_reference = get_official_documentation_url(version, "reference/backend/actions#window-actions-ir-actions-act-window")
    test_reference = get_official_documentation_url(version, "reference/backend/testing")
    rules_reference = "odoo://rules/odoo-development"
    alias_note = ""
    if requested_view_type in {"tree", "list"} and requested_view_type != normalized_view_type:
        alias_note = f"\nRequested `{requested_view_type}`; generated `{normalized_view_type}` because Odoo {version} uses `{normalized_view_type}` for collection views.\n"

    return f"""# {normalized_view_type.title()} View for {model_name} (Odoo {version})

**File**: views/{model_underscore}_views.xml
{alias_note}
```xml
{view_xml}
```

## Action and Menu

The action uses `{collection_view_type},form` for Odoo {version}. A menu item is only generated when `parent_menu` is provided; otherwise choose a real parent menu from your module or dependency.

```xml
<odoo>
{action_xml}
</odoo>
```

## Manifest Configuration

Add to __manifest__.py 'data' section after security files:
```python
'data': [
    'security/ir.model.access.csv',
    'views/{model_underscore}_views.xml',
],
```

## Odoo View Guardrails
- **Collection views**: Odoo 17 uses `tree`; Odoo 18/19 use `list`.
- **Action view_mode**: Keep it aligned with the generated collection view type.
- **Menu parent**: Do not use placeholder parents like `base.menu_custom`; pass a real `parent_menu` XML ID or add the menu later.
- **Security**: Views do not grant access. Add ACLs and record rules separately.
- **Tests**: For important workflows, add a Form helper test or access test covering the generated view's model.

## Next Steps
1. Add this file to your manifest's 'data' section after security files
2. Add or confirm ACLs with `create_security_rules("{model_name}", "module_name")`
3. Test the view in Odoo with a user matching the intended group
4. Review guidelines: `get_development_guidelines("views")`

## References
- View Architecture: {doc_reference}
- Window Actions: {action_reference}
- Testing: {test_reference}
- Development Rules: {rules_reference}
"""


@mcp.tool()
def create_security_rules(
    model_name: str,
    module_name: str,
    groups: list[str] = []
) -> str:
    if not groups:
        groups = ["user", "manager"]
    
    model_underscore = model_name.replace(".", "_")
    
    csv_lines = ["id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink"]
    
    for group in groups:
        if group == "user":
            perms = "1,0,0,0"
        elif group == "manager":
            perms = "1,1,1,1"
        else:
            perms = "1,1,1,1"
        
        line = f"access_{model_underscore}_{group},{module_name}.{group},model_{model_underscore},base.group_{group},{perms}"
        csv_lines.append(line)
    
    csv_content = "\n".join(csv_lines)
    version = current_version["value"]
    doc_reference = get_official_documentation_url(version, "reference/backend/security")
    rules_reference = "odoo://rules/odoo-development"
    
    return f"""# Security Rules for {model_name} (Odoo {version})

## Access Rights (CSV)

**File**: security/ir.model.access.csv

```csv
{csv_content}
```

## Record Rules (XML) - Optional

**File**: security/{module_name}_security.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="{model_underscore}_rule_own" model="ir.rule">
        <field name="name">{model_name}: See own records</field>
        <field name="model_id" ref="model_{model_underscore}"/>
        <field name="domain_force">[('create_uid', '=', user.id)]</field>
        <field name="groups" eval="[(4, ref('base.group_user'))]"/>
    </record>
</odoo>
```

## Security Rules Guidelines ⚠️
- **Naming**: Use `access_{{model}}_{{group}}` format
- **Permissions**: Format is (read, write, create, unlink)
  - User group: Usually (1,0,0,0) - read-only
  - Manager group: Usually (1,1,1,1) - full access
- **Record Rules**: Use for row-level security
- **Testing**: Always test security with different user groups

## Manifest Configuration

Add to __manifest__.py 'data' section (order matters):
```python
'data': [
    'security/{module_name}_security.xml',  # Groups first (if any)
    'security/ir.model.access.csv',         # Access rights
    'views/{model_underscore}_views.xml',   # Views last
],
```

## Next Steps
1. Add security files to manifest in correct order
2. Test with different user roles
3. Review guidelines: `get_development_guidelines("security")`

## References
- Security Documentation: {doc_reference}
- Development Rules: {rules_reference}
- See "Security Standards" section in rules
"""


def model_external_id(model_name: str, model_xml_id: str = "") -> str:
    if model_xml_id:
        return model_xml_id
    return f"model_{model_name.replace('.', '_')}"


def field_external_id(model_name: str, field_name: str, module_name: str = "") -> str:
    external_id = f"field_{model_name.replace('.', '_')}__{field_name}"
    return f"{module_name}.{external_id}" if module_name else external_id


def xml_field(name: str, value: str, *, eval_value: bool = False) -> str:
    if eval_value:
        return f'            <field name="{name}" eval="{escape(value, quote=True)}"/>'
    return f'            <field name="{name}">{escape(value)}</field>'


@mcp.tool()
def create_base_automation(
    automation_name: str,
    model_name: str,
    trigger: str = "on_create_or_write",
    action_type: str = "code",
    code: str = "",
    module_name: str = "",
    model_xml_id: str = "",
    trigger_fields: list[str] = [],
    filter_domain: str = "",
    filter_pre_domain: str = "",
    update_path: str = "",
    update_value: str = "",
    update_boolean_value: str = "",
    date_field: str = "",
    date_field_xml_id: str = "",
    delay: int = 0,
    delay_unit: str = "hour",
    delay_mode: str = "after",
    webhook_url: str = "",
    webhook_fields: list[str] = [],
    xml_id: str = "",
    noupdate: bool = True,
    version: str = "",
) -> str:
    automation_version = version if version in ODOO_VERSIONS else current_version["value"]
    trigger = trigger.strip() or "on_create_or_write"
    action_type = action_type.strip() or "code"
    module_name = module_name.strip()
    model_ref = model_external_id(model_name, model_xml_id.strip())
    xml_stem = xml_id.strip() or f"automation_{model_name.replace('.', '_')}_{trigger}"
    action_xml_id = f"{xml_stem}_action"
    data_noupdate = "1" if noupdate else "0"
    time_triggers = {"on_time", "on_time_created", "on_time_updated"}

    automation_fields = [
        xml_field("name", automation_name),
        f'            <field name="model_id" ref="{escape(model_ref, quote=True)}"/>',
        xml_field("trigger", trigger),
    ]

    if filter_domain:
        automation_fields.append(xml_field("filter_domain", filter_domain))
    if filter_pre_domain:
        automation_fields.append(xml_field("filter_pre_domain", filter_pre_domain))

    if trigger_fields:
        refs = []
        for field in trigger_fields:
            field_ref = field if "." in field else field_external_id(model_name, field, module_name)
            refs.append(f"ref('{field_ref}')")
        automation_fields.append(xml_field("trigger_field_ids", f"[(6, 0, [{', '.join(refs)}])]", eval_value=True))

    if trigger in time_triggers:
        if date_field_xml_id or date_field:
            date_ref = date_field_xml_id or field_external_id(model_name, date_field, module_name)
            automation_fields.append(f'            <field name="trg_date_id" ref="{escape(date_ref, quote=True)}"/>')
        signed_delay = abs(delay)
        if automation_version in {"17.0", "18.0"} and delay_mode == "before":
            signed_delay = -signed_delay
        automation_fields.append(xml_field("trg_date_range", str(signed_delay), eval_value=True))
        automation_fields.append(xml_field("trg_date_range_type", delay_unit))
        if automation_version == "19.0":
            automation_fields.append(xml_field("trg_date_range_mode", "before" if delay_mode == "before" else "after"))

    if trigger == "on_webhook" and code == "":
        code = "# payload is available in the automation context\n# record is resolved by base.automation.record_getter\nrecord.message_post(body='Webhook automation triggered') if hasattr(record, 'message_post') else None"

    action_fields = [
        xml_field("name", f"{automation_name}: action"),
        f'            <field name="model_id" ref="{escape(model_ref, quote=True)}"/>',
        xml_field("usage", "base_automation"),
        f'            <field name="base_automation_id" ref="{escape(xml_stem, quote=True)}"/>',
        xml_field("state", action_type),
    ]

    if action_type == "code":
        action_fields.append(xml_field("code", code or "# Write safe automation code here\n# Available: env, model, record, records, user, time, datetime, dateutil\npass"))
    elif action_type == "object_write":
        action_fields.append(xml_field("update_path", update_path or "active"))
        if update_boolean_value:
            action_fields.append(xml_field("update_boolean_value", update_boolean_value))
        elif update_value:
            action_fields.append(xml_field("value", update_value))
    elif action_type == "webhook":
        action_fields.append(xml_field("webhook_url", webhook_url or "https://example.com/webhook"))
        if webhook_fields:
            refs = []
            for field in webhook_fields:
                field_ref = field if "." in field else field_external_id(model_name, field, module_name)
                refs.append(f"ref('{field_ref}')")
            action_fields.append(xml_field("webhook_field_ids", f"[(6, 0, [{', '.join(refs)}])]", eval_value=True))
    elif action_type == "object_create":
        action_fields.append(f'            <field name="crud_model_id" ref="{escape(model_ref, quote=True)}"/>')
        action_fields.append(xml_field("value", update_value or automation_name))

    warnings = []
    if trigger == "on_write":
        warnings.append("`on_write` is deprecated; prefer `on_create_or_write` plus `trigger_field_ids`.")
    if trigger == "on_create" and automation_version in {"17.0", "18.0"}:
        warnings.append("`on_create` is deprecated in this version; prefer `on_create_or_write` when possible.")
    if trigger == "on_change" and action_type != "code":
        warnings.append("`on_change` automations can only use `code` actions.")
    if trigger == "on_unlink" and action_type in {"mail_post", "followers", "next_activity"}:
        warnings.append("`on_unlink` cannot use mail, follower, or activity actions because the record is being deleted.")
    if trigger in {"on_message_received", "on_message_sent"}:
        warnings.append("Mail triggers require the target model to inherit `mail.thread`.")
    if trigger in time_triggers and not (date_field or date_field_xml_id) and trigger == "on_time":
        warnings.append("`on_time` requires a date/datetime trigger field; pass `date_field` or `date_field_xml_id`.")
    if trigger == "on_create_or_write" and not trigger_fields:
        warnings.append("No `trigger_fields` were provided; Odoo will consider all stored field updates as possible triggers.")
    if action_type == "object_write" and not update_path:
        warnings.append("`object_write` needs `update_path`; this helper defaulted to `active`.")
    if not model_xml_id and not module_name and not model_name.startswith("x."):
        warnings.append(f"Model XML ID guessed as `{model_ref}`. For dependency models, pass an explicit value such as `project.model_project_task` or `base.model_res_partner`.")

    version_notes = [
        "Odoo 17 uses `tree` in views; Odoo 18/19 use `list`.",
        "Odoo 17/18 represent time-based 'before' delays with negative `trg_date_range`.",
        "Odoo 19 uses positive `trg_date_range` plus `trg_date_range_mode` (`before`/`after`).",
        "Creating or editing automations updates registry patches and may affect create/write/unlink/onchange behavior immediately after module update.",
    ]

    xml = f'''<odoo>
    <data noupdate="{data_noupdate}">
        <record id="{escape(xml_stem, quote=True)}" model="base.automation">
{chr(10).join(automation_fields)}
        </record>

        <record id="{escape(action_xml_id, quote=True)}" model="ir.actions.server">
{chr(10).join(action_fields)}
        </record>
    </data>
</odoo>'''

    warning_output = "\n".join(f"- {warning}" for warning in warnings) or "- No blocking warnings from helper inputs. Still test the automation on a disposable database."
    version_output = "\n".join(f"- {note}" for note in version_notes)

    return f"""# Base Automation Helper: {automation_name} (Odoo {automation_version})

**File**: data/{xml_stem}.xml

```xml
{xml}
```

## Manifest Changes

```python
'depends': ['base_automation'],
'data': [
    'security/ir.model.access.csv',
    'data/{xml_stem}.xml',
],
```

## Version-Sensitive Notes

{version_output}

## Guardrails

{warning_output}

## Test Checklist

- Create a record that should trigger the automation and assert the action side effect.
- Create or update a record outside `filter_domain` and assert nothing happens.
- If `trigger_fields` is set, update an unrelated field and assert the action does not run.
- If this automation uses code, test recursion risk when the code writes back to the same model.
- If this automation uses time triggers, run the base automation cron in a test/frozen time scenario.

## References

- Server actions: {get_official_documentation_url(automation_version, 'reference/backend/actions#server-actions-ir-actions-server')}
- Scheduled actions: {get_official_documentation_url(automation_version, 'reference/backend/actions#module-odoo.addons.base.models.ir_cron')}
- Security: {get_official_documentation_url(automation_version, 'reference/backend/security')}
"""


MODULE_DEPENDENCIES: dict[str, list[str]] = {
    "base": [],
    "web": ["base"],
    "mail": ["base"],
    "resource": ["base"],
    "digest": ["mail"],
    "sms": ["mail"],
    "base_automation": ["base", "digest", "resource", "mail", "sms"],
    "contacts": ["base"],
    "product": ["base", "mail", "uom"],
    "uom": ["base"],
    "account": ["base", "mail", "uom", "product"],
    "payment": ["account", "website"],
    "sale": ["base", "mail", "account", "product"],
    "sale_management": ["sale"],
    "purchase": ["base", "mail", "account", "product"],
    "stock": ["product", "mail"],
    "mrp": ["stock"],
    "project": ["mail", "web"],
    "hr": ["resource", "mail"],
    "crm": ["mail", "contacts"],
    "portal": ["web", "mail"],
    "website": ["web", "portal"],
    "website_sale": ["website", "sale_management", "payment"],
    "analytic": ["base"],
}


FEATURE_MODULE_HINTS: list[tuple[set[str], str]] = [
    ({"automation", "automated", "base.automation", "server action"}, "base_automation"),
    ({"mail", "message", "chatter", "activity", "followers", "notification"}, "mail"),
    ({"portal", "customer portal"}, "portal"),
    ({"website", "webpage", "web controller"}, "website"),
    ({"frontend", "owl", "asset", "javascript", "webclient"}, "web"),
    ({"sale", "sales", "quotation", "sale.order"}, "sale_management"),
    ({"purchase", "vendor", "purchase.order"}, "purchase"),
    ({"stock", "inventory", "warehouse", "picking", "stock.move"}, "stock"),
    ({"invoice", "account", "accounting", "account.move", "tax"}, "account"),
    ({"payment", "transaction", "provider"}, "payment"),
    ({"project", "task", "project.task"}, "project"),
    ({"employee", "hr", "attendance", "leave"}, "hr"),
    ({"crm", "lead", "opportunity"}, "crm"),
    ({"product", "product.template", "product.product"}, "product"),
    ({"manufacturing", "mrp", "bom"}, "mrp"),
    ({"analytic", "budget"}, "analytic"),
]


def collect_module_dependencies(module: str, seen: set[str], ordered: list[str]) -> None:
    if module in seen:
        return
    seen.add(module)
    for dependency in MODULE_DEPENDENCIES.get(module, []):
        collect_module_dependencies(dependency, seen, ordered)
    ordered.append(module)


@mcp.tool()
def layout_module_dependencies(
    module_name: str,
    features: list[str] = [],
    models: list[str] = [],
    integrate_with: list[str] = [],
    explicit_dependencies: list[str] = [],
    include_transitive: bool = False,
    version: str = "",
) -> str:
    dependency_version = version if version in ODOO_VERSIONS else current_version["value"]
    requested_modules = {dep.strip() for dep in explicit_dependencies if dep.strip()}
    requested_modules.add("base")

    searchable_inputs = " ".join([module_name, *features, *models, *integrate_with]).lower()
    for keywords, module in FEATURE_MODULE_HINTS:
        if any(keyword in searchable_inputs for keyword in keywords):
            requested_modules.add(module)
    for integration in integrate_with:
        integration = integration.strip()
        if integration:
            requested_modules.add(integration)

    ordered_with_transitive: list[str] = []
    seen: set[str] = set()
    for module in sorted(requested_modules):
        collect_module_dependencies(module, seen, ordered_with_transitive)

    if include_transitive:
        manifest_depends = ordered_with_transitive
    else:
        # Keep direct module intent in the manifest; Odoo installs transitive dependencies automatically.
        manifest_depends = [module for module in ordered_with_transitive if module in requested_modules]

    unknown_modules = sorted(module for module in requested_modules if module not in MODULE_DEPENDENCIES)
    manifest_list = ", ".join(f"'{module}'" for module in manifest_depends)
    transitive_list = ", ".join(f"'{module}'" for module in ordered_with_transitive)
    unknown_output = "\n".join(f"- `{module}` is not in the built-in dependency map; verify its manifest manually." for module in unknown_modules) or "- No unknown modules detected."

    return f"""# Dependency Layout for `{module_name}` (Odoo {dependency_version})

## Recommended Manifest Dependencies

```python
'depends': [{manifest_list}],
```

## Full Installation Order

```python
[{transitive_list}]
```

## Why These Dependencies

""" + "\n".join(
        f"- `{module}`: requested directly or inferred from feature/model/integration inputs."
        for module in manifest_depends
    ) + f"""

## Unknowns To Verify

{unknown_output}

## Manifest Data Order Reminder

Use dependency order for modules, then data order inside your module:

```python
'data': [
    'security/groups.xml',
    'security/ir.model.access.csv',
    'security/record_rules.xml',
    'data/sequences.xml',
    'data/automations.xml',
    'views/model_views.xml',
    'views/menus.xml',
],
```

## Guardrails

- Add a dependency when you reference another module's model, field, view, group, menu, report, asset, or XML ID.
- Do not depend on a module just because it is installed in your database.
- Prefer the narrowest module that owns the XML IDs you use.
- For automated actions generated by `create_base_automation`, add `base_automation` explicitly.
- For chatter, activities, followers, or message posting, add `mail` explicitly.
"""


def migration_versions_between(from_version: str, to_version: str) -> list[str]:
    try:
        start = int(float(from_version)) + 1
        end = int(float(to_version))
    except ValueError:
        return [to_version] if to_version else []
    return [f"{version}.0" for version in range(start, end + 1)]


def migration_operation_list(title: str, items: list[dict[str, str]], formatter) -> str:
    if not items:
        return f"# {title}: none declared\n"
    lines = [f"# {title}"]
    for item in items:
        lines.extend(formatter(item))
    return "\n".join(lines) + "\n"


@mcp.tool()
def create_upgrade_script(
    module_name: str,
    from_version: str,
    to_version: str,
    migration_version: str = "",
    rename_models: list[dict[str, str]] = [],
    rename_fields: list[dict[str, str]] = [],
    rename_xmlids: list[dict[str, str]] = [],
    data_migrations: list[str] = [],
    oca_style: bool = True,
) -> str:
    target_version = migration_version or to_version or current_version["value"]
    migration_dir = f"migrations/{target_version}"
    intermediate_versions = migration_versions_between(from_version, to_version)
    oca_note = "OCA-style migration layout" if oca_style else "Generic Odoo migration layout"

    def model_formatter(item: dict[str, str]) -> list[str]:
        old = item.get("old", "old.model")
        new = item.get("new", "new.model")
        return [
            f"# TODO: rename model `{old}` -> `{new}`.",
            f"# util.rename_model(cr, '{old}', '{new}', rename_table=True)",
            f"# Caveat: m2m table rename defaults differ before/after saas~18.1; pass ignored_m2ms explicitly when needed.",
        ]

    def field_formatter(item: dict[str, str]) -> list[str]:
        model = item.get("model", "your.model")
        old = item.get("old", "old_field")
        new = item.get("new", "new_field")
        return [
            f"# TODO: rename field `{model}.{old}` -> `{model}.{new}`.",
            f"# util.rename_field(cr, '{model}', '{old}', '{new}', update_references=True)",
        ]

    def xmlid_formatter(item: dict[str, str]) -> list[str]:
        old = item.get("old", f"{module_name}.old_xmlid")
        new = item.get("new", f"{module_name}.new_xmlid")
        return [
            f"# TODO: rename XML ID `{old}` -> `{new}`.",
            f"# util.rename_xmlid(cr, '{old}', '{new}', on_collision='fail')",
        ]

    pre_ops = "".join([
        migration_operation_list("Model renames", rename_models, model_formatter),
        migration_operation_list("Field renames", rename_fields, field_formatter),
        migration_operation_list("XML ID renames", rename_xmlids, xmlid_formatter),
    ])
    data_ops = "\n".join(f"    # TODO: {item}" for item in data_migrations) or "    # TODO: Add data migrations that require the upgraded registry."
    pre_helper_notes = '''    # Common pre-migration helpers from odoo.upgrade.util:
    # - util.column_exists(cr, "your_table", "old_column")
    # - util.table_exists(cr, "your_table")
    # - util.remove_field(cr, "your.model", "old_field", drop_column=False)
    # - util.copy_column(cr, "your_table", "old_column", "old_column_upg_copy")
    # - util.alter_column_type(cr, "your_table", "amount", "numeric", using="{0}::numeric")
    # - util.remove_model(cr, "old.model", drop_table=True)
    # - util.merge_model(cr, "old.model", "new.model", fields_mapping={"old_field": "new_field"})
'''

    pre_script = f'''# Copyright <year> <author>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo.upgrade import util


def migrate(cr, version):
    if not version:
        return

{''.join('    ' + line + chr(10) for line in pre_ops.splitlines())}
{pre_helper_notes}'''

    post_script = f'''# Copyright <year> <author>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo.upgrade import util


def migrate(cr, version):
    if not version:
        return
    env = util.env(cr)

{data_ops}
    # Recompute stored fields in batches after data changes.
    # util.recompute_fields(cr, "your.model", ["field_name"], query="SELECT id FROM your_table")

    # Iterate safely over large recordsets when ORM writes are required.
    # Model = env["your.model"]
    # ids = Model.search([]).ids
    # for record in util.iter_browse(Model, ids, chunk_size=1000):
    #     record.field_name = "value"
    # util.flush(Model)
    # util.invalidate(Model)
'''

    end_script = f'''# Copyright <year> <author>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo.upgrade import util


def migrate(cr, version):
    if not version:
        return
    env = util.env(cr)

    # TODO: Add final checks that require all modules to be loaded.
    # - Validate migrated records.
    # - Remove temporary bridge data.
    # - Backfill values depending on other upgraded modules.
    # - Refresh noupdate XML records only when appropriate.
    # util.update_record_from_xml(cr, "{module_name}.record_xmlid", fields={{"name"}})
'''

    upgrade_util_helpers = f"""
## Verified `odoo.upgrade.util` Helper Map

These helpers come from `odoo.upgrade.util` and are intended as examples to adapt, not blind substitutions. Keep scripts idempotent and verify each old/new name against the database you are upgrading.

### Pre-Migration Schema Helpers

```python
from odoo.upgrade import util

# Models: update ir.model, references, xmlids, and optionally database tables.
util.rename_model(cr, "old.model", "new.model", rename_table=True)
util.remove_model(cr, "old.model", drop_table=True)
util.merge_model(cr, "old.model", "new.model", fields_mapping={{"old_field": "new_field"}})

# Fields: update metadata, filters, domains, exports, server actions, attachments, and inherited models.
util.rename_field(cr, "your.model", "old_field", "new_field", update_references=True)
util.remove_field(cr, "your.model", "old_field", drop_column=False)
util.move_field_to_module(cr, "your.model", "field_name", "old_module", "{module_name}")

# Raw SQL safety helpers for tables and columns.
if util.table_exists(cr, "your_table") and util.column_exists(cr, "your_table", "old_column"):
    util.copy_column(cr, "your_table", "old_column", "old_column_upg_copy")
    util.alter_column_type(cr, "your_table", "old_column", "text")
```

### XML ID And Record Helpers

```python
from odoo.upgrade import util

util.rename_xmlid(cr, "{module_name}.old_xmlid", "{module_name}.new_xmlid", on_collision="fail")
util.force_noupdate(cr, "{module_name}.record_xmlid", noupdate=True)
util.if_unchanged(cr, "{module_name}.record_xmlid", util.update_record_from_xml)
util.delete_unused(cr, "{module_name}.old_record_xmlid", deactivate=True)
```

### Post/End ORM Helpers

```python
from odoo.upgrade import util

env = util.env(cr)
util.recompute_fields(cr, "your.model", ["stored_field"], query="SELECT id FROM your_table")

Model = env["your.model"]
for record in util.iter_browse(Model, Model.search([]).ids, chunk_size=1000):
    record.active = True
util.flush(Model)
util.invalidate(Model)
```

### Module-Level Helpers

Module operations usually belong in a `base` migration script or an Odoo 16+ `--pre-upgrade-scripts` path before `base` loads, not in an arbitrary addon migration file.

```python
from odoo.upgrade import util

util.rename_module(cr, "old_module", "{module_name}")
util.merge_module(cr, "old_module", "{module_name}", update_dependers=True)
util.remove_module(cr, "old_module")
util.module_deps_diff(cr, "{module_name}", plus=("mail",), minus=("old_dependency",))
util.force_install_module(cr, "new_dependency", if_installed=["{module_name}"])
```
"""

    intermediate_output = ", ".join(intermediate_versions) if intermediate_versions else "No intermediate versions detected."
    oca_checks = """
- Keep migration-only compatibility changes separate from behavior changes.
- Do not change original authors or copyright years while migrating.
- Apply every intermediate version checklist when jumping multiple major versions.
- Prefer the migration conventions already used by the repository.
- Do not run module update/test commands against a database until the local command is confirmed.
""" if oca_style else "- Follow the migration conventions used by this project."

    return f"""# Upgrade Script Scaffold: `{module_name}` {from_version} -> {to_version}

Style: {oca_note}
Target migration directory: `{migration_dir}/`
Intermediate version checkpoints: {intermediate_output}

## File: `{migration_dir}/pre-migration.py`

Use this for schema-level compatibility work before the registry for the new module version is fully loaded.

```python
{pre_script}
```

## File: `{migration_dir}/post-migration.py`

Use this for data migrations after the upgraded registry is available.

```python
{post_script}
```

## File: `{migration_dir}/end-migration.py`

Use this for final checks after all modules in the upgrade set are loaded.

```python
{end_script}
```

## Data Migration Checklist

- Confirm renamed models, fields, and XML IDs against the old and new code.
- Check security CSVs, record rules, actions, views, reports, mail templates, and automations for old model/field/XML ID references.
- Add idempotency: migration scripts should tolerate being retried after partial failure.
- Backfill required fields before constraints make records invalid.
- Recompute stored computed fields only after source data is migrated.
- Add a test or manual verification query for each important migration rule.

{upgrade_util_helpers}

## OCA-Style Notes

{oca_checks}

## References

- Upgrade scripts: {get_official_documentation_url(to_version if to_version in ODOO_VERSIONS else current_version['value'], 'reference/upgrades/upgrade_scripts#writing-upgrade-scripts')}
- Upgrade utils: {get_official_documentation_url(to_version if to_version in ODOO_VERSIONS else current_version['value'], 'reference/upgrades/upgrade_utils')}
"""


ERROR_PATTERNS: list[dict[str, Any]] = [
    {
        "needles": ["parseerror", "while parsing", "xmlsyntaxerror"],
        "area": "XML data or view loading",
        "cause": "Malformed XML, invalid field in a view, bad xpath, or data loaded before its dependency.",
        "docs": ["reference/backend/data", "reference/user_interface/view_architectures"],
        "repro": "Update the module with only the XML file that fails, then inspect the record and line reported by the parser.",
    },
    {
        "needles": ["external id not found", "xmlid", "not found in the system"],
        "area": "XML ID / dependency / data load order",
        "cause": "A referenced XML ID is missing, loaded later, renamed, or owned by a module missing from `depends`.",
        "docs": ["reference/backend/data", "reference/backend/module"],
        "repro": "Search for the referenced XML ID, verify the owning module is in `depends`, and check data file order.",
    },
    {
        "needles": ["accesserror", "access rights", "ir.model.access"],
        "area": "Security ACLs",
        "cause": "The user lacks model-level read/write/create/unlink access or the ACL CSV is missing/wrong.",
        "docs": ["reference/backend/security#access-rights"],
        "repro": "Reproduce as the failing user and check `security/ir.model.access.csv` plus implied groups.",
    },
    {
        "needles": ["record rules", "record rule", "due to security restrictions"],
        "area": "Record rules",
        "cause": "A row-level domain blocks access even though ACLs allow the operation.",
        "docs": ["reference/backend/security#record-rules"],
        "repro": "Reproduce as the failing user, then compare accessible records with and without each relevant rule.",
    },
    {
        "needles": ["undefinedcolumn", "column", "does not exist"],
        "area": "Database schema / field migration",
        "cause": "The database schema is not aligned with the model fields, often after a missing module update or field rename.",
        "docs": ["reference/backend/orm#fields", "reference/upgrades/upgrade_scripts#writing-upgrade-scripts"],
        "repro": "Upgrade the owning module on a copy of the database and verify whether the missing column exists after registry init.",
    },
    {
        "needles": ["undefinedtable", "relation", "does not exist"],
        "area": "Database table / module installation",
        "cause": "A model table is missing because its module is not installed, not upgraded, or `_auto`/model naming changed.",
        "docs": ["reference/backend/orm#models", "reference/backend/module"],
        "repro": "Check the model's owning module, manifest dependencies, and whether the module update created the table.",
    },
    {
        "needles": ["invalid field", "unknown field"],
        "area": "Model field / view / domain",
        "cause": "A field name in Python, XML, domain, or data does not exist on the target model for this version.",
        "docs": ["reference/backend/orm#fields", "reference/user_interface/view_architectures"],
        "repro": "Inspect the target model fields in Odoo shell and check whether a dependency module adds the field.",
    },
    {
        "needles": ["expected singleton"],
        "area": "ORM recordset handling",
        "cause": "Code assumes one record but receives multiple records; missing loop, `ensure_one()`, or batching logic.",
        "docs": ["reference/backend/orm#recordsets", "reference/backend/performance#batch-operations"],
        "repro": "Call the method with a multi-record recordset and inspect the line that dereferences a singleton-only field/method.",
    },
    {
        "needles": ["xpath", "cannot be located", "element '<xpath"],
        "area": "View inheritance",
        "cause": "An inherited view xpath no longer matches the parent architecture or the parent view dependency is wrong.",
        "docs": ["reference/user_interface/view_architectures"],
        "repro": "Open the final parent view architecture in developer mode and test the xpath against the actual XML.",
    },
    {
        "needles": ["qwebexception", "template", "t-call", "t-field"],
        "area": "QWeb report/template",
        "cause": "A template expression, field access, or template inheritance failed during rendering.",
        "docs": ["reference/frontend/qweb", "reference/backend/reports"],
        "repro": "Render the report/template with the smallest recordset that fails and inspect the template path in the traceback.",
    },
    {
        "needles": ["modulenotfounderror", "importerror", "no module named"],
        "area": "Python imports / dependencies",
        "cause": "A Python dependency or addon import is missing from the environment or manifest dependencies.",
        "docs": ["reference/backend/module"],
        "repro": "Import the module in the same Python environment used by Odoo and verify manifest dependencies.",
    },
    {
        "needles": ["owlerror", "uncaughtpromiseerror", "javascript error"],
        "area": "Odoo web / OWL frontend",
        "cause": "A frontend component, service, registry entry, asset, or template failed in the browser.",
        "docs": ["reference/frontend/owl_components", "reference/frontend/services", "reference/frontend/assets"],
        "repro": "Reproduce with browser dev tools open, check loaded asset bundle, and isolate the component/template mentioned in the stack.",
    },
]


@mcp.tool()
def explain_odoo_error(error_text: str, version: str = "", context: str = "") -> str:
    error_version = version if version in ODOO_VERSIONS else current_version["value"]
    text_lower = error_text.lower()
    matches = [
        pattern for pattern in ERROR_PATTERNS
        if any(needle in text_lower for needle in pattern["needles"])
    ]
    if not matches:
        matches = [{
            "area": "Unknown / needs reproduction",
            "cause": "No strong Odoo error pattern matched. Start by reproducing with full traceback and module update logs.",
            "docs": ["reference/backend/orm", "reference/backend/testing"],
            "repro": "Capture the complete traceback, current module being loaded, Odoo version, installed dependencies, and the exact action that triggers the error.",
        }]

    primary = matches[0]
    docs_output = []
    for doc_path in primary["docs"]:
        docs_output.append(f"- {doc_path}: {get_official_documentation_url(error_version, doc_path)}")

    secondary_output = "\n".join(
        f"- {match['area']}: {match['cause']}"
        for match in matches[1:4]
    ) or "- No secondary pattern matched."

    context_output = f"\n## Supplied Context\n\n{context}\n" if context else ""

    return f"""# Odoo Error Explanation (Odoo {error_version})

## Likely Area

{primary['area']}

## Likely Root Cause

{primary['cause']}

## Minimal Reproduction

{primary['repro']}

## What To Inspect First

- The first custom addon frame in the traceback.
- The model, XML record, field, view, or security rule named closest to the original exception.
- The manifest `depends` and data file order for the module currently loading.
- Whether the behavior changes between a fresh install and `-u module_name` upgrade.

## Secondary Matches

{secondary_output}
{context_output}
## Relevant Documentation

{chr(10).join(docs_output)}
"""


@mcp.tool()
def plan_odoo_feature(feature_description: str, module_name: str = "", version: str = "") -> str:
    """Create a skill-informed implementation plan for an Odoo feature."""
    plan_version = version if version in ODOO_VERSIONS else current_version["value"]
    words = [
        word
        for word in "".join(char.lower() if char.isalnum() else " " for char in feature_description).split()
        if len(word) > 2
    ]
    if not module_name:
        module_name = "_".join(words[:3]) if words else "custom_feature"
    else:
        module_name = "_".join(
            word
            for word in "".join(char.lower() if char.isalnum() else " " for char in module_name).split()
            if word
        ) or "custom_feature"

    model_stem = module_name.replace("_management", "").replace("_", ".")
    primary_model = f"{model_stem}.record" if "." not in model_stem else f"{model_stem}.record"
    collection_view = "list" if plan_version in {"18.0", "19.0"} else "tree"
    safe_description = feature_description[:80].replace("'", "\\'")

    doc_links = {
        "Module manifests": get_official_documentation_url(plan_version, "reference/backend/module"),
        "ORM fields and models": get_official_documentation_url(plan_version, "reference/backend/orm#fields"),
        "Actions and menus": get_official_documentation_url(plan_version, "reference/backend/actions#window-actions-ir-actions-act-window"),
        "View architectures": get_official_documentation_url(plan_version, "reference/user_interface/view_architectures"),
        "Access rights": get_official_documentation_url(plan_version, "reference/backend/security#access-rights"),
        "Record rules": get_official_documentation_url(plan_version, "reference/backend/security#record-rules"),
        "Testing": get_official_documentation_url(plan_version, "reference/backend/testing#testing-python-code"),
    }

    return f"""# Odoo Feature Plan: {feature_description}

Target version: Odoo {plan_version}
Suggested module: `{module_name}`
Suggested primary model: `{primary_model}`

## Implementation Shape

1. Confirm scope and version-sensitive behavior.
2. Create or update module manifest and dependencies.
3. Add the primary model with only the fields needed for the first workflow.
4. Add ACLs before loading views.
5. Add `{collection_view}`, form, and search views.
6. Add an `ir.actions.act_window` and menu only under a real parent menu XML ID.
7. Add tests at the Odoo behavior seam before expanding the feature.

## Model Sketch

Start with a small model and add business fields only when the workflow needs them:

```python
from odoo import fields, models


class {''.join(part.title() for part in primary_model.split('.'))}(models.Model):
    _name = '{primary_model}'
    _description = '{safe_description}'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
```

## Security Pass

- Add `security/ir.model.access.csv` for every new model.
- Decide whether normal internal users need read-only, create/write, or manager-only access.
- Add record rules when users must only see own, company, portal, or team records.
- Check `company_id`, default company behavior, domains, and cross-company reads/writes for business data.
- Do not use `sudo()` to hide missing access design.

## View And Action Pass

- Use `{collection_view}` collection views for Odoo {plan_version}.
- Keep form views minimal first: required fields, status fields, and primary relations.
- Keep search views focused on fields users actually filter by.
- Avoid placeholder menu parents. Pass a real parent XML ID to `create_odoo_view(..., parent_menu="module.menu_parent")` or add the menu later.

## Test Pass

- Add a `TransactionCase` for core ORM behavior.
- Add a Form helper test if the feature depends on form defaults/onchanges.
- Add an access test for intended groups and forbidden operations.
- Add an `HttpCase` only if the feature exposes controllers, portal routes, reports, or frontend flows.

## Suggested Tool Calls

```text
set_odoo_version("{plan_version}")
create_odoo_module("{module_name}", "{module_name.replace('_', ' ').title()}", "{feature_description}")
create_odoo_model("{primary_model}", "{safe_description}", fields=[{{"name": "active", "type": "Boolean"}}])
create_security_rules("{primary_model}", "{module_name}")
create_odoo_view("{primary_model}", "{collection_view}", ["name", "active"])
create_odoo_view("{primary_model}", "form", ["name", "active"])
```

## Official References

""" + "\n".join(f"- {title}: {url}" for title, url in doc_links.items()) + "\n"


@mcp.prompt()
def develop_odoo_feature(feature_description: str) -> str:
    return f"""I need to develop a new feature for Odoo {current_version['value']}:

Feature: {feature_description}

Official reference: {get_official_documentation_url(current_version['value'])}

Please help me following Odoo development guidelines:

1. Design the data model (models and fields needed)
   - Follow naming conventions (models use dots, fields use underscores)
   - Use proper field types and parameters
   
2. Create the necessary views (form, tree, search)
   - Follow view naming conventions
   - Use proper XML structure
   
3. Set up security rules
   - Define access rights in CSV
   - Add record rules if needed
   
4. Implement any business logic needed
   - Use proper decorators (@api.depends, @api.constrains, etc.)
   - Follow method naming conventions
   
5. Follow Odoo best practices and coding guidelines
   - Review: get_development_guidelines("general")
   - Check: odoo://rules/odoo-development

What models, views, and logic do I need to implement this feature?
"""


@mcp.prompt()
def debug_odoo_error(error_message: str, context: str = "") -> str:
    return f"""I'm encountering an error in Odoo {current_version['value']}:

Error: {error_message}

Context: {context}

Official reference: {get_official_documentation_url(current_version['value'])}

Please help me following Odoo debugging best practices:

1. Identify the root cause of this error
   - Check common Odoo pitfalls (see guidelines)
   - Verify naming conventions
   - Check for SQL constraints violations
   
2. Suggest solutions based on Odoo best practices
   - Use proper ORM methods
   - Follow Odoo patterns
   - Avoid common mistakes
   
3. Provide code examples if needed
   - Show correct implementation
   - Reference Odoo documentation
   
4. Explain how to prevent this error in the future
   - Follow guidelines: get_development_guidelines()
   - Review: odoo://rules/odoo-development

What's causing this error and how can I fix it?
"""


@mcp.prompt()
def upgrade_odoo_module(module_name: str, from_version: str, to_version: str) -> str:
    return f"""I need to upgrade the Odoo module '{module_name}' from version {from_version} to {to_version}.

Official upgrade reference: {get_official_documentation_url(to_version, 'reference/upgrades')}

Please help me:
1. Identify breaking changes between versions
2. List deprecated APIs that need updating
3. Suggest migration steps
4. Provide code examples for common migration patterns
5. Highlight any new features I should consider using

What changes do I need to make to upgrade this module?
"""


@mcp.prompt()
def review_odoo_code(code: str) -> str:
    return f"""Please review this Odoo code for version {current_version['value']} against Odoo development guidelines:

Official reference: {get_official_documentation_url(current_version['value'])}

```python
{code}
```

Check for compliance with Odoo standards:

1. **Naming Conventions**
   - Model names use dots (e.g., sale.order)
   - Field names: _id for Many2one, _ids for Many2many/One2many
   - Method names: _compute_, _onchange_, _check_ prefixes
   
2. **API Decorators**
   - Proper use of @api.depends, @api.constrains, @api.onchange
   - Correct decorator order
   
3. **ORM Best Practices**
   - Avoid SQL unless necessary
   - Use mapped(), filtered(), sorted()
   - Batch operations
   
4. **Performance Issues**
   - Check for N+1 queries
   - Inefficient loops
   - Missing indices
   
5. **Security Concerns**
   - SQL injection risks
   - Proper access control
   - Input validation
   
6. **Code Quality**
   - DRY principle
   - Single responsibility
   - Clear naming

Reference guidelines: odoo://rules/odoo-development

Provide specific suggestions for improvement.
"""


def main():
    """Run the MCP server with proper error handling."""
    # Check if stdin is a terminal (interactive mode)
    if sys.stdin.isatty():
        print("\n" + "=" * 70, file=sys.stderr)
        print("⚠️  WARNING: MCP Server cannot be run directly from terminal!", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
        print("\nMCP servers communicate via JSON-RPC over stdin/stdout.", file=sys.stderr)
        print("They must be run through an MCP client.\n", file=sys.stderr)
        print("To TEST the server functionality:", file=sys.stderr)
        print("  python -m tests.test_server\n", file=sys.stderr)
        print("To USE the server:", file=sys.stderr)
        print("  1. Configure in Claude Desktop or OpenCode (see README.md)", file=sys.stderr)
        print("  2. Or use MCP Inspector: mcp dev src/odoo_mcp/server.py\n", file=sys.stderr)
        print("For more information, see:", file=sys.stderr)
        print("  - README.md", file=sys.stderr)
        print("  - guides/QUICK_START.md", file=sys.stderr)
        print("  - guides/OPENCODE_SETUP.md\n", file=sys.stderr)
        sys.exit(1)
    
    # Run the MCP server
    try:
        mcp.run()
    except KeyboardInterrupt:
        print("\nServer stopped by user", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"\nServer error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
