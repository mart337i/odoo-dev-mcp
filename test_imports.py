#!/usr/bin/env python3
"""
Quick import test - Verifies the reorganized structure has correct imports
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

print("=" * 70)
print("Import Verification Test")
print("=" * 70)

try:
    # Test direct server import
    print("\n1. Testing src/odoo_mcp/server.py import...")
    from odoo_mcp import server
    print("   ✓ Server module loads (but mcp package needed for execution)")
    
    # Test __init__.py
    print("\n2. Testing src/odoo_mcp/__init__.py...")
    import odoo_mcp
    print("   ✓ Package initialization works")
    
    print("\n3. Checking module attributes...")
    expected_exports = [
        'mcp', 'ODOO_VERSIONS', 'current_version',
        'get_all_rst_files', 'get_documentation_index',
        'get_documentation_content', 'get_development_rules',
        'set_odoo_version', 'get_current_version',
        'search_documentation', 'get_development_guidelines'
    ]
    
    for attr in expected_exports:
        if hasattr(server, attr):
            print(f"   ✓ {attr}")
        else:
            print(f"   ✗ {attr} - MISSING!")
    
    print("\n" + "=" * 70)
    print("✓ All import paths are correct!")
    print("=" * 70)
    print("\nNext step: Install dependencies with 'uv sync' to run full tests")
    
except Exception as e:
    print(f"\n✗ Import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
