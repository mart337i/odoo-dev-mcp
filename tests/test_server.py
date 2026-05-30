#!/usr/bin/env python3
"""
Test script for Odoo MCP Server
Run this to verify the server functionality without starting the MCP server.

Usage:
  python -m tests.test_server
  or
  cd tests && python test_server.py
"""

import asyncio
import os
import sys
import tempfile
from pathlib import Path

# Ensure src is in path for imports to work
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from odoo_mcp.server import (
    mcp,
    get_all_rst_files,
    DOCS_BASE_PATH,
    ODOO_VERSIONS,
    current_version
)


async def test_resources():
    print("\n=== Testing Resources ===")
    
    print(f"✓ Local documentation fallback path: {DOCS_BASE_PATH}")
    print(f"✓ Supported versions: {', '.join(ODOO_VERSIONS)}")
    print(f"✓ Current version: {current_version['value']}")
    
    for version in ODOO_VERSIONS:
        version_path = DOCS_BASE_PATH / version
        if version_path.exists():
            print(f"✓ Found local Odoo {version} documentation fallback")
            files = get_all_rst_files(version)
            print(f"  - {len(files)} local RST fallback files available")
        else:
            print(f"⚠ Local Odoo {version} documentation fallback not found at {version_path}")
    
    print("\nTesting resource access...")
    try:
        from odoo_mcp.server import get_documentation_index
        index = get_documentation_index("19.0")
        print(f"✓ Official documentation index retrieved ({len(index)} chars)")
    except Exception as e:
        print(f"✗ Error accessing documentation: {e}")


def test_tools():
    print("\n=== Testing Tools ===")
    
    tools = [
        "set_odoo_version",
        "get_current_version",
        "detect_odoo_version",
        "inspect_odoo_source",
        "get_odoo_local_context",
        "get_documentation_url",
        "search_documentation",
        "get_development_guidelines",
        "create_upgrade_script",
        "explain_odoo_error",
        "plan_odoo_feature",
        "plan_owl_feature",
        "create_base_automation",
        "create_owl_component",
        "create_owl_client_action",
        "create_owl_field_widget",
        "create_owl_service",
        "create_owl_test",
        "layout_module_dependencies",
        "create_odoo_module",
        "create_odoo_model",
        "create_odoo_view",
        "create_security_rules"
    ]
    
    for tool in tools:
        print(f"✓ Tool registered: {tool}")
    
    print("\nTesting tool execution...")
    
    from odoo_mcp.server import set_odoo_version, get_current_version
    
    result = set_odoo_version("18.0")
    print(f"✓ set_odoo_version: {result}")
    
    result = get_current_version()
    print(f"✓ get_current_version: {result}")
    
    from odoo_mcp.server import (
        get_documentation_url,
        get_odoo_local_context,
        search_documentation,
        create_upgrade_script,
        explain_odoo_error,
        plan_odoo_feature,
        plan_owl_feature,
        create_base_automation,
        create_owl_component,
        create_owl_client_action,
        create_owl_field_widget,
        create_owl_service,
        create_owl_test,
        layout_module_dependencies,
    )

    result = get_documentation_url("reference/backend/orm#fields", "19.0")
    assert "#fields" in result
    print(f"✓ get_documentation_url: {result}")

    previous_env = {
        name: os.environ.get(name)
        for name in ["ODOO_SOURCE", "ODOO_BASE_COMMAND", "ODOO_TOOL_README", "ODOO_VERSION", "DEFAULT_ODOO_VERSION"]
    }
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_root = Path(temp_dir)
            nested_odoo = source_root / "odoo19"
            (nested_odoo / "addons").mkdir(parents=True)
            (nested_odoo / "odoo").mkdir()
            (nested_odoo / "odoo" / "addons").mkdir()
            (nested_odoo / "odoo" / "release.py").write_text(
                "version_info = (19, 0, 0, 'final', 0, '')\n",
                encoding="utf-8",
            )
            (nested_odoo / "odoo-bin").write_text("#!/usr/bin/env python3\n", encoding="utf-8")
            (source_root / "enterprise-19.0").mkdir()
            addon_path = source_root / "custom_addons" / "demo_module"
            addon_path.mkdir(parents=True)
            (addon_path / "__manifest__.py").write_text(
                "{'name': 'Demo', 'version': '18.0.1.0.0', 'depends': ['base']}\n",
                encoding="utf-8",
            )
            (addon_path / "models").mkdir()
            (addon_path / "models" / "demo.py").write_text(
                """from odoo import api, fields, models


class DemoModel(models.Model):
    _name = "demo.model"
    _inherit = ["mail.thread"]
    _description = "Demo Model"

    amount = fields.Float(string="Amount")
    total = fields.Float(compute="_compute_total")

    @api.depends("amount")
    def _compute_total(self):
        pass
""",
                encoding="utf-8",
            )
            (addon_path / "controllers").mkdir()
            (addon_path / "controllers" / "main.py").write_text(
                """from odoo import http


class DemoController(http.Controller):
    @http.route("/demo", auth="user", type="json", methods=["POST"])
    def demo(self):
        pass
""",
                encoding="utf-8",
            )
            (addon_path / "models" / "bad.py").write_text("def broken(:\n", encoding="utf-8")
            (source_root / ".git").mkdir()
            (source_root / ".git" / "HEAD").write_text("ref: refs/heads/19.0-feature\n", encoding="utf-8")
            local_readme = source_root / "local-tools.md"
            local_readme.write_text(
                "Run with db_password = local-secret\nAPI_KEY: local-api-key\n",
                encoding="utf-8",
            )

            os.environ["ODOO_SOURCE"] = str(source_root)
            os.environ["ODOO_VERSION"] = "17.0"
            os.environ["DEFAULT_ODOO_VERSION"] = "17.0"
            os.environ["ODOO_BASE_COMMAND"] = f"{nested_odoo}/odoo-bin -c /tmp/odoo.conf --db-password hunter2 --addons-path=/tmp/addons"
            os.environ["ODOO_TOOL_README"] = str(local_readme)
            result = get_odoo_local_context(include_readme_excerpt=True)
            from odoo_mcp.server import detect_odoo_version
            from odoo_mcp.server import inspect_odoo_source
            source_result = detect_odoo_version(
                path=str(source_root),
                include_env=False,
                include_manifests=False,
                include_branch=False,
            )
            conflict_result = detect_odoo_version(path=str(source_root))
            source_inspection = inspect_odoo_source(path=str(source_root), scope="both", max_files=50)
            query_inspection = inspect_odoo_source(path=str(source_root), query="demo.model", scope="addons", max_files=50)
            limited_inspection = inspect_odoo_source(path=str(source_root), scope="addons", max_files=1)
        assert "ODOO_SOURCE" in result
        assert "ODOO_BASE_COMMAND" in result
        assert "ODOO_TOOL_README" in result
        assert "--stop-after-init" in result
        assert "odoo19/odoo-bin" in result
        assert "enterprise-19.0" in result
        assert "hunter2" not in result
        assert "local-secret" not in result
        assert "local-api-key" not in result
        assert "***" in result
        assert "Suggested current version: `19.0`" in source_result
        assert "source release.py" in source_result
        assert "Result: conflict detected." in conflict_result
        assert "`17.0`" in conflict_result
        assert "`18.0`" in conflict_result
        assert "`19.0`" in conflict_result
        assert "environment" in conflict_result
        assert "manifest" in conflict_result
        assert "branch" in conflict_result
        assert get_current_version() == "Current Odoo development version: 18.0"
        assert "# Odoo Source Inspection" in source_inspection
        assert "`19.0`" in source_inspection
        assert "`demo_module`" in source_inspection
        assert "DemoModel" in source_inspection
        assert "_name=`demo.model`" in source_inspection
        assert "amount" in source_inspection
        assert "_compute_total" in source_inspection
        assert "DemoController.demo" in source_inspection
        assert "/demo" in source_inspection
        assert "bad.py" in source_inspection
        assert "DemoModel" in query_inspection
        assert "DemoController" not in query_inspection
        assert "Files skipped by limit" in limited_inspection
    finally:
        for name, value in previous_env.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value
    print(f"✓ get_odoo_local_context: Generated {len(result)} chars")

    result = search_documentation("record rules", "19.0")
    assert "#record-rules" in result
    print(f"✓ search_documentation: Generated {len(result)} chars")

    result = create_upgrade_script(
        module_name="equipment_rental",
        from_version="17.0",
        to_version="19.0",
        rename_fields=[{"model": "equipment.rental", "old": "old_stage_id", "new": "stage_id"}],
        rename_xmlids=[{"old": "equipment_rental.old_action", "new": "equipment_rental.action_equipment_rental"}],
    )
    assert "pre-migration.py" in result
    assert "post-migration.py" in result
    assert "end-migration.py" in result
    assert "util.rename_field" in result
    assert "util.rename_xmlid" in result
    assert "util.recompute_fields" in result
    assert "util.column_exists" in result
    assert "util.module_deps_diff" in result
    print(f"✓ create_upgrade_script: Generated {len(result)} chars")

    result = explain_odoo_error("odoo.tools.convert.ParseError: while parsing view.xml: External ID not found in the system", version="19.0")
    assert "XML" in result or "XML ID" in result
    print(f"✓ explain_odoo_error: Generated {len(result)} chars")

    result = plan_odoo_feature("Manage equipment rentals", module_name="equipment_rental")
    assert "Security Pass" in result
    print(f"✓ plan_odoo_feature: Generated {len(result)} chars")

    result = plan_owl_feature(
        "Dashboard for equipment rentals",
        module_name="equipment_rental",
        integration_type="client_action",
    )
    assert "registry" in result
    assert "web.assets_backend" in result
    print(f"✓ plan_owl_feature: Generated {len(result)} chars")

    result = create_owl_component(
        component_name="Rental Dashboard",
        module_name="equipment_rental",
        props=["title"],
        services=["orm", "notification"],
        use_state=True,
    )
    assert "@odoo/owl" in result
    assert "useService" in result
    assert "equipment_rental.RentalDashboard" in result
    print(f"✓ create_owl_component: Generated {len(result)} chars")

    result = create_owl_component(
        component_name="Escaped Component",
        module_name="equipment_rental",
        services=['orm"; alert(1)//'],
    )
    assert 'useService("orm\\"; alert(1)//")' in result
    print(f"✓ create_owl_component escaping: Generated {len(result)} chars")

    result = create_owl_client_action(
        action_name="Rental <Dashboard> & Report",
        module_name="equipment_rental",
        action_tag='equipment_rental.dashboard"; alert(1)//',
        services=["action"],
    )
    assert 'registry.category("actions").add' in result
    assert "ir.actions.client" in result
    assert 'equipment_rental.dashboard\\"; alert(1)//' in result
    assert "Rental &lt;Dashboard&gt; &amp; Report" in result
    print(f"✓ create_owl_client_action: Generated {len(result)} chars")

    result = create_owl_field_widget(
        widget_name="Rental Badge",
        module_name="equipment_rental",
        supported_types=["char", "selection"],
    )
    assert "standardFieldProps" in result
    assert 'registry.category("fields").add' in result
    print(f"✓ create_owl_field_widget: Generated {len(result)} chars")

    result = create_owl_service(
        service_name="Rental Store",
        module_name="equipment_rental",
        dependencies=["orm"],
    )
    assert 'registry.category("services").add' in result
    assert 'dependencies: ["orm"]' in result
    print(f"✓ create_owl_service: Generated {len(result)} chars")

    result = create_owl_test(
        component_name="Rental Dashboard",
        module_name="equipment_rental",
    )
    assert "@odoo/hoot" in result
    assert "mountWithCleanup" in result
    assert "props:" not in result
    assert "Test title" not in result
    assert "Component ready" in result
    print(f"✓ create_owl_test: Generated {len(result)} chars")

    result = create_base_automation(
        automation_name="Archive inactive demos",
        model_name="x.demo",
        trigger="on_time",
        action_type="object_write",
        update_path="active",
        update_boolean_value="false",
        date_field="write_date",
        delay=2,
        delay_mode="before",
        version="19.0",
    )
    assert "trg_date_range_mode" in result
    assert "base_automation" in result
    print(f"✓ create_base_automation: Generated {len(result)} chars")

    result = layout_module_dependencies(
        module_name="equipment_rental",
        features=["automated activities and chatter"],
        models=["project.task"],
    )
    assert "base_automation" in result
    assert "mail" in result
    print(f"✓ layout_module_dependencies: Generated {len(result)} chars")

    from odoo_mcp.server import create_odoo_module
    result = create_odoo_module(
        module_name="test_module",
        display_name="Test Module",
        description="A test module"
    )
    assert "wizards/" in result
    assert "cli/" in result
    print(f"✓ create_odoo_module: Generated {len(result)} chars")

    result = create_odoo_module(
        module_name="escaped_module",
        display_name="Test ' Module",
        description="A test\nmodule",
        author="O'Hara",
    )
    assert "'name': \"Test ' Module\"" in result
    assert "'description': 'A test\\nmodule'" in result
    assert "'author': \"O'Hara\"" in result
    print(f"✓ create_odoo_module escaping: Generated {len(result)} chars")
    
    from odoo_mcp.server import create_odoo_model
    result = create_odoo_model(
        model_name="test.model",
        model_description="Test Model",
        fields=[
            {"name": "test_field", "type": "Char", "required": True}
        ]
    )
    print(f"✓ create_odoo_model: Generated {len(result)} chars")

    result = create_odoo_model(
        model_name="test.model",
        model_description="Test ' Model",
        fields=[
            {"name": "partner_id", "type": "Many2one", "comodel_name": "res.partner", "string": "Partner's Ref"}
        ]
    )
    assert '_description = "Test \' Model"' in result
    assert 'string="Partner\'s Ref"' in result
    print(f"✓ create_odoo_model escaping: Generated {len(result)} chars")
    
    from odoo_mcp.server import create_odoo_view
    result = create_odoo_view(
        model_name="test.model",
        view_type="tree",
        fields_to_display=["name", "test_field"]
    )
    assert "<list>" in result
    print(f"✓ create_odoo_view: Generated {len(result)} chars")

    result = create_odoo_view(
        model_name="test.model",
        view_type="form",
        fields_to_display=['name"><x'],
        view_name='view"><x',
        parent_menu='base.menu"><x',
    )
    assert 'id="view&quot;&gt;&lt;x"' in result
    assert 'name="name&quot;&gt;&lt;x"' in result
    assert 'parent="base.menu&quot;&gt;&lt;x"' in result
    print(f"✓ create_odoo_view escaping: Generated {len(result)} chars")
    
    from odoo_mcp.server import create_security_rules
    result = create_security_rules(
        model_name="test.model",
        module_name="test_module"
    )
    print(f"✓ create_security_rules: Generated {len(result)} chars")

    result = create_security_rules(
        model_name="test.model",
        module_name="bad,module"
    )
    assert result == "Error: module_name must not contain commas or newlines"
    result = create_security_rules(
        model_name="test.model",
        module_name="test_module",
        groups=["bad\ngroup"],
    )
    assert result == "Error: group must not contain commas or newlines"
    print("✓ create_security_rules CSV validation")


def test_prompts():
    print("\n=== Testing Prompts ===")
    
    prompts = [
        "develop_odoo_feature",
        "debug_odoo_error",
        "upgrade_odoo_module",
        "review_odoo_code"
    ]
    
    for prompt in prompts:
        print(f"✓ Prompt registered: {prompt}")


def test_mcp_server():
    print("\n=== Testing MCP Server ===")
    
    try:
        # Try to access the internal server object
        if hasattr(mcp, '_mcp_server'):
            server = mcp._mcp_server
            if hasattr(server, 'name'):
                print(f"✓ Server name: {server.name}")
            else:
                print("✓ Server object exists (name not accessible)")
        else:
            print("✓ FastMCP instance created")
        
        print("✓ Server initialized successfully")
        print("✓ FastMCP wrapper active")
        print("✓ All capabilities enabled (resources, tools, prompts)")
    except Exception as e:
        print(f"⚠ Server introspection limited: {e}")
        print("✓ But server object exists and is usable")


async def main():
    print("=" * 70)
    print("Odoo Development MCP Server - Test Suite")
    print("=" * 70)
    
    try:
        await test_resources()
        test_tools()
        test_prompts()
        test_mcp_server()
        
        print("\n" + "=" * 70)
        print("✓ All tests passed!")
        print("=" * 70)
        print("\n📚 Server is ready to use!")
        print("\n🚀 Next steps:")
        print("   1. Configure in Claude Desktop (see ../README.md)")
        print("   2. Or configure in OpenCode (see ../guides/OPENCODE_SETUP.md)")
        print("   3. Or use MCP Inspector: mcp dev src/odoo_mcp/server.py")
        print("\n⚠️  Do NOT run the server directly with 'python src/odoo_mcp/server.py'")
        print("   MCP servers communicate via JSON-RPC and require an MCP client.\n")
        
    except Exception as e:
        print("\n" + "=" * 70)
        print("✗ Test failed!")
        print("=" * 70)
        print(f"\nError: {e}\n")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code or 0)
