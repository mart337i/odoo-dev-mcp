from pathlib import Path
from typing import Any
import re
from mcp.server.fastmcp import FastMCP, Context

ODOO_VERSIONS = ["17.0", "18.0", "19.0"]
DOCS_BASE_PATH = Path(__file__).parent / "docs"
RULES_BASE_PATH = Path(__file__).parent / "rules"

mcp = FastMCP("Odoo Development Assistant")

current_version = {"value": "19.0"}


def get_all_rst_files(version: str) -> list[tuple[Path, str]]:
    version_path = DOCS_BASE_PATH / version
    if not version_path.exists():
        return []
    
    files = []
    for rst_file in version_path.rglob("*.rst"):
        relative = rst_file.relative_to(version_path)
        uri_path = str(relative).replace("\\", "/").replace(".rst", "")
        files.append((rst_file, uri_path))
    
    return files


@mcp.resource("odoo://docs/{version}/index")
def get_documentation_index(version: str) -> str:
    if version not in ODOO_VERSIONS:
        return f"Error: Unknown Odoo version {version}. Available: {', '.join(ODOO_VERSIONS)}"
    
    version_path = DOCS_BASE_PATH / version
    if not version_path.exists():
        return f"Documentation for Odoo {version} not found"
    
    content = f"# Odoo {version} Documentation Index\n\n"
    content += f"Current development version: {current_version['value']}\n\n"
    
    for category in ["howtos", "reference"]:
        cat_path = version_path / category
        if cat_path.exists():
            content += f"\n## {category.title()}\n\n"
            for rst_file in sorted(cat_path.glob("*.rst")):
                topic = rst_file.stem
                content += f"- {topic}\n"
    
    return content


@mcp.resource("odoo://docs/{version}/{path}")
def get_documentation_content(version: str, path: str) -> str:
    if version not in ODOO_VERSIONS:
        return f"Error: Unknown Odoo version {version}"
    
    file_path = DOCS_BASE_PATH / version / f"{path}.rst"
    
    if not file_path.exists():
        parts = path.split("/")
        if len(parts) > 1:
            file_path = DOCS_BASE_PATH / version / parts[0] / f"{'/'.join(parts[1:])}.rst"
    
    if not file_path.exists():
        return f"Documentation file not found: {path}"
    
    try:
        content = file_path.read_text(encoding="utf-8")
        return f"# {path} (Odoo {version})\n\n{content}"
    except Exception as e:
        return f"Error reading file: {str(e)}"


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
def search_documentation(query: str, version: str = "") -> str:
    search_version = version if version and version in ODOO_VERSIONS else current_version["value"]
    
    results = []
    files = get_all_rst_files(search_version)
    
    query_lower = query.lower()
    
    for file_path, uri_path in files:
        try:
            content = file_path.read_text(encoding="utf-8")
            content_lower = content.lower()
            
            if query_lower in content_lower:
                lines = content.split("\n")
                matching_lines = []
                
                for i, line in enumerate(lines):
                    if query_lower in line.lower():
                        start = max(0, i - 2)
                        end = min(len(lines), i + 3)
                        context = "\n".join(lines[start:end])
                        matching_lines.append(f"Line {i+1}:\n{context}")
                        if len(matching_lines) >= 3:
                            break
                
                if matching_lines:
                    results.append({
                        "file": uri_path,
                        "matches": matching_lines[:3]
                    })
        except Exception:
            continue
    
    if not results:
        return f"No results found for '{query}' in Odoo {search_version} documentation"
    
    output = f"Search results for '{query}' in Odoo {search_version}:\n\n"
    for result in results[:10]:
        output += f"## {result['file']}\n"
        for match in result['matches']:
            output += f"{match}\n\n"
        output += "---\n\n"
    
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
    guidelines += f"- Documentation: odoo://docs/{current_version['value']}/index\n"
    
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
    
    doc_reference = f"odoo://docs/{version}/reference/backend"
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
    
    doc_reference = f"odoo://docs/{version}/reference/backend/orm"
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
    view_name: str = ""
) -> str:
    version = current_version["value"]
    if not view_name:
        view_name = f"{model_name.replace('.', '_')}_{view_type}_view"
    
    model_underscore = model_name.replace(".", "_")
    
    if view_type == "tree":
        fields_xml = "\n            ".join([f'<field name="{field}"/>' for field in fields_to_display])
        view_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="{view_name}" model="ir.ui.view">
        <field name="name">{model_name}.tree</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <tree>
                {fields_xml}
            </tree>
        </field>
    </record>
</odoo>'''
    
    elif view_type == "form":
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
    
    elif view_type == "search":
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
    
    elif view_type == "kanban":
        view_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="{view_name}" model="ir.ui.view">
        <field name="name">{model_name}.kanban</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <kanban>
                <field name="name"/>
                <templates>
                    <t t-name="kanban-box">
                        <div class="oe_kanban_card">
                            <div class="oe_kanban_content">
                                <div><field name="name"/></div>
                            </div>
                        </div>
                    </t>
                </templates>
            </kanban>
        </field>
    </record>
</odoo>'''
    
    else:
        return f"Unsupported view type: {view_type}. Supported types: tree, form, search, kanban"
    
    action_xml = f'''    <record id="action_{model_underscore}" model="ir.actions.act_window">
        <field name="name">{model_name.split('.')[-1].title()}</field>
        <field name="res_model">{model_name}</field>
        <field name="view_mode">tree,form</field>
    </record>

    <menuitem id="menu_{model_underscore}"
              name="{model_name.split('.')[-1].title()}"
              action="action_{model_underscore}"
              parent="base.menu_custom"/>'''
    
    doc_reference = f"odoo://docs/{version}/reference/user_interface/view_architectures"
    rules_reference = "odoo://rules/odoo-development"
    
    return f"""# {view_type.title()} View for {model_name} (Odoo {version})

**File**: views/{model_underscore}_views.xml

```xml
{view_xml}
```

## Action and Menu

```xml
<odoo>
{action_xml}
</odoo>
```

## Manifest Configuration

Add to __manifest__.py 'data' section:
```python
'data': [
    'security/ir.model.access.csv',
    'views/{model_underscore}_views.xml',
],
```

## Naming Convention Rules ⚠️
- **View ID**: Format as `view_{{model}}_{{type}}` (e.g., `view_sale_order_form`)
- **Action ID**: Format as `action_{{model}}` (e.g., `action_sale_order`)
- **Menu ID**: Format as `menu_{{model}}` (e.g., `menu_sale_order`)
- **File naming**: Use underscores (e.g., `sale_order_views.xml`)

## Next Steps
1. Add this file to your manifest's 'data' section
2. Test the view in Odoo interface
3. Review guidelines: `get_development_guidelines("views")`

## References
- View Architecture: {doc_reference}
- Development Rules: {rules_reference}
- See "View (XML) Standards" section in rules
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
    doc_reference = f"odoo://docs/{version}/reference/backend/security"
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


@mcp.prompt()
def develop_odoo_feature(feature_description: str) -> str:
    return f"""I need to develop a new feature for Odoo {current_version['value']}:

Feature: {feature_description}

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
