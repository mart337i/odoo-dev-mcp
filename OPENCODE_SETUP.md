# OpenCode Setup Guide for Odoo Development MCP Server

Complete guide to set up and use the Odoo Development MCP Server with OpenCode.

## Prerequisites

1. **OpenCode** installed 
2. **Python 3.12+** installed
3. **This repository** cloned to your local machine

## Installation Steps

### Step 1: Install Dependencies

Navigate to the project directory and install required packages:

```bash
cd /path/to/odoo-dev-mcp

# Using uv (recommended)
uv sync

# OR using pip
pip install "mcp[cli]"
```

### Step 2: Test the Server

Verify the server works correctly:

```bash
python test_server.py
```

You should see:
```
✓ All tests passed!
✓ Server is ready to use!
```

### Step 3: Configure OpenCode

Create or edit your OpenCode configuration file:

**Location**: `.opencode.jsonc` in your workspace root or `~/.opencode/config.jsonc` for global config

**Configuration**:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["python", "/absolute/path/to/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "PYTHONPATH": "/absolute/path/to/odoo-dev-mcp"
      }
    }
  }
}
```

**Using uv (alternative)**:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["uv", "run", "--directory", "/absolute/path/to/odoo-dev-mcp", "odoo_mcp_server.py"],
      "enabled": true
    }
  }
}
```

## Verification

### Check MCP Server Status

1. Open OpenCode output panel
2. Look for "MCP Servers" or similar section
3. Verify "odoo-dev" server is running

### Test the Connection

In OpenCode chat, try these commands:

```
@odoo-dev get current Odoo version
```

You should see a response about the current version (default: 19.0).

## Usage in OpenCode

### Basic Commands

#### 1. Set Odoo Version
```
@odoo-dev set Odoo version to 19.0
```

#### 2. Search Documentation
```
@odoo-dev search documentation for "computed fields"
```

#### 3. Get Development Guidelines
```
@odoo-dev get development guidelines for models
```

#### 4. Create Module
```
@odoo-dev create an Odoo module called "inventory_custom" 
with display name "Custom Inventory" and description "Custom inventory features"
```

#### 5. Create Model
```
@odoo-dev create a model inventory.custom.product with fields:
- name (char, required)
- quantity (integer)
- price (float)
- supplier_id (many2one to res.partner)
```

#### 6. Create View
```
@odoo-dev create a form view for inventory.custom.product 
with fields: name, quantity, price, supplier_id
```

#### 7. Create Security
```
@odoo-dev create security rules for inventory.custom.product 
in module inventory_custom
```

### Access Resources

#### Documentation
```
@odoo-dev show me odoo://docs/19.0/reference/backend/orm
```

#### Development Rules
```
@odoo-dev show me odoo://rules/odoo-development
```

#### All Guidelines
```
@odoo-dev show me odoo://rules/all
```

### Use Prompts

#### Develop Feature
```
@odoo-dev /develop_odoo_feature "task management with priorities and deadlines"
```

#### Debug Error
```
@odoo-dev /debug_odoo_error "ValidationError: Missing required field 'name'" 
context: "Creating a new record in custom model"
```

#### Review Code
```
@odoo-dev /review_odoo_code "
class MyModel(models.Model):
    _name = 'my.model'
    field1 = fields.Char()
"
```

#### Upgrade Module
```
@odoo-dev /upgrade_odoo_module "sale_custom" from_version: "17.0" to_version: "19.0"
```

## Advanced Configuration

### Multiple Odoo Versions

If you work with multiple Odoo versions, you can create separate server instances:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-17": {
      "type": "local",
      "command": ["python", "/path/to/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "DEFAULT_ODOO_VERSION": "17.0"
      }
    },
    "odoo-19": {
      "type": "local",
      "command": ["python", "/path/to/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "DEFAULT_ODOO_VERSION": "19.0"
      }
    }
  }
}
```

### Custom Environment Variables

Add custom paths or settings:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["python", "/path/to/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "PYTHONPATH": "/path/to/odoo-dev-mcp",
        "ODOO_DOCS_PATH": "/custom/path/to/docs",
        "ODOO_RULES_PATH": "/custom/path/to/rules"
      }
    }
  }
}
```

### Workspace-Specific Configuration

Create `.opencode.jsonc` in your Odoo project workspace:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["python", "${workspaceFolder}/../odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "ODOO_VERSION": "19.0"
      }
    }
  }
}
```

## Complete Development Workflow

### Scenario: Creating a Library Management Module

#### Step 1: Set Version
```
@odoo-dev set version to 19.0
```

#### Step 2: Get Guidelines
```
@odoo-dev get development guidelines for general
```

#### Step 3: Create Module
```
@odoo-dev create module "library_management" with display name "Library Management"
and description "Complete library management system"
```

#### Step 4: Create Models
```
@odoo-dev create model library.book with fields:
- title (char, required)
- isbn (char)
- author_id (many2one to res.partner)
- publisher (char)
- publication_date (date)
- available (boolean)
- category_id (many2one to library.category)
```

```
@odoo-dev create model library.category with fields:
- name (char, required)
- description (text)
- parent_id (many2one to library.category)
```

#### Step 5: Create Views
```
@odoo-dev create form view for library.book with all fields
```

```
@odoo-dev create tree view for library.book with fields: 
title, author_id, isbn, available
```

```
@odoo-dev create search view for library.book with fields:
title, author_id, category_id, available
```

#### Step 6: Add Security
```
@odoo-dev create security rules for library.book in library_management
```

```
@odoo-dev create security rules for library.category in library_management
```

#### Step 7: Review Generated Code
```
@odoo-dev review this code: [paste generated model code]
```

## Tips for OpenCode Usage

### 1. Use @ Mentions
Always prefix commands with `@odoo-dev` to direct queries to the MCP server:
```
@odoo-dev [your command]
```

### 2. Reference Resources
Access documentation and rules directly:
```
@odoo-dev show odoo://docs/19.0/reference/backend/orm
@odoo-dev show odoo://rules/odoo-development
```

### 3. Multi-line Commands
OpenCode supports multi-line input. Use Shift+Enter for new lines:
```
@odoo-dev create model library.borrowing with fields:
- book_id (many2one, library.book, required)
- member_id (many2one, res.partner, required)
- borrow_date (date, required)
- return_date (date)
- state (selection: ['borrowed', 'returned'])
```

### 4. Combine with OpenCode Features
- Use OpenCode's code editing with MCP-generated code
- Ask OpenCode to modify generated code
- Use version control integration

### 5. Context Awareness
The server remembers your current Odoo version throughout the session:
```
@odoo-dev set version to 18.0
@odoo-dev create model test.model with name field
# Model will be generated for Odoo 18.0
```

## Troubleshooting

### Server Not Appearing

1. **Check Configuration Path**
   - Ensure absolute paths (no ~, use full path)
   - Verify Python executable path: `which python`

2. **Verify Python Installation**
   ```bash
   python --version  # Should be 3.12+
   ```

3. **Test Server Manually**
   ```bash
   cd /path/to/odoo-dev-mcp
   python odoo_mcp_server.py
   ```

4. **Check OpenCode Logs**
   - Open Output panel in VS Code
   - Select "OpenCode" or "MCP" from dropdown
   - Look for error messages

### Server Starting But Not Responding

1. **Check Dependencies**
   ```bash
   cd /path/to/odoo-dev-mcp
   pip install "mcp[cli]"
   ```

2. **Verify Server Health**
   ```bash
   python test_server.py
   ```

3. **Check Paths in Config**
   - Use absolute paths
   - Verify files exist: `ls /path/to/odoo-dev-mcp/odoo_mcp_server.py`

### Import Errors

1. **Set PYTHONPATH**
   ```jsonc
   "environment": {
     "PYTHONPATH": "/absolute/path/to/odoo-dev-mcp"
   }
   ```

2. **Use Virtual Environment**
   ```jsonc
   "command": ["/path/to/venv/bin/python", "/path/to/odoo_mcp_server.py"]
   ```

### Documentation Not Found

1. **Verify docs Directory**
   ```bash
   ls /path/to/odoo-dev-mcp/docs/
   # Should show: 17.0/ 18.0/ 19.0/
   ```

2. **Check Permissions**
   ```bash
   chmod -R 755 /path/to/odoo-dev-mcp/docs/
   ```

### Rules Not Loading

1. **Verify rules Directory**
   ```bash
   ls /path/to/odoo-dev-mcp/rules/
   # Should show: clean-code.mdc odoo-development.mdc
   ```

2. **Test Rules Access**
   ```
   @odoo-dev show odoo://rules/all
   ```

## Example .opencode.jsonc Templates

### Minimal Configuration
```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["python", "/home/user/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true
    }
  }
}
```

### Full Configuration
```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": ["python", "/home/user/odoo-dev-mcp/odoo_mcp_server.py"],
      "enabled": true,
      "environment": {
        "PYTHONPATH": "/home/user/odoo-dev-mcp",
        "ODOO_VERSION": "19.0",
        "LOG_LEVEL": "INFO"
      }
    }
  }
}
```

### With UV
```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "odoo-dev": {
      "type": "local",
      "command": [
        "uv", 
        "run", 
        "--directory", 
        "/home/user/odoo-dev-mcp",
        "odoo_mcp_server.py"
      ],
      "enabled": true
    }
  }
}
```

## Features Available in OpenCode

### All 8 Tools
✅ `set_odoo_version` - Version switching
✅ `get_current_version` - Version check
✅ `search_documentation` - Doc search
✅ `get_development_guidelines` - Get rules
✅ `create_odoo_module` - Module generation
✅ `create_odoo_model` - Model creation
✅ `create_odoo_view` - View generation
✅ `create_security_rules` - Security setup

### All 6 Resources
✅ `odoo://docs/{version}/index` - Doc index
✅ `odoo://docs/{version}/{path}` - Specific docs
✅ `odoo://rules/clean-code` - Clean code rules
✅ `odoo://rules/odoo-development` - Odoo standards
✅ `odoo://rules/all` - All guidelines

### All 4 Prompts
✅ `develop_odoo_feature` - Feature development
✅ `debug_odoo_error` - Error debugging
✅ `upgrade_odoo_module` - Version upgrades
✅ `review_odoo_code` - Code review

## Getting Help

### In OpenCode
```
@odoo-dev help me with [your question]
@odoo-dev what can you do?
@odoo-dev show me examples
```

### Check Documentation
- This file: `OPENCODE_SETUP.md`
- Main README: `README.md`
- Rules: `rules/odoo-development.mdc`

### Test Commands
```bash
# Test server
python test_server.py

# Test with MCP inspector
mcp dev odoo_mcp_server.py
```

## Quick Reference Card

| Task | Command |
|------|---------|
| Set version | `@odoo-dev set version to 19.0` |
| Search docs | `@odoo-dev search for "orm methods"` |
| Get guidelines | `@odoo-dev get guidelines for models` |
| Create module | `@odoo-dev create module "name" ...` |
| Create model | `@odoo-dev create model name.model ...` |
| Create view | `@odoo-dev create form view for ...` |
| Add security | `@odoo-dev create security for ...` |
| Review code | `@odoo-dev review this: [code]` |
| View rules | `@odoo-dev show odoo://rules/all` |
| Debug error | `@odoo-dev debug error: [error]` |

## Success Indicators

✅ Server shows in OpenCode MCP list
✅ `@odoo-dev` responds to queries
✅ Can access documentation resources
✅ Can generate Odoo code
✅ Code includes naming convention warnings
✅ Guidelines accessible on demand

## Next Steps

1. ✅ Complete this setup guide
2. ✅ Test basic commands
3. ✅ Try creating a sample module
4. ✅ Review generated code
5. ✅ Explore development guidelines
6. 🚀 Start building your Odoo modules with AI assistance!

---

**Need Help?** 
- Test the server: `python test_server.py`
- Check logs in OpenCode Output panel
- Verify paths in configuration
- Review troubleshooting section above
