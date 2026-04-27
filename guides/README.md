# Guides Index

## Getting Started

- **[QUICK_START.md](QUICK_START.md)** - Setup in 3 steps (recommended for new users)
- **[OPENCODE_SETUP.md](OPENCODE_SETUP.md)** - Complete OpenCode configuration guide
- **[TESTING.md](TESTING.md)** - How to test the server locally

## Troubleshooting

- **[../.github/TROUBLESHOOTING.md](../.github/TROUBLESHOOTING.md)** - Common issues and solutions

## Main Documentation

- **[../README.md](../README.md)** - Main project README with features and installation
- **[../CHANGELOG.md](../CHANGELOG.md)** - Version history and release notes
- **[../REORGANIZATION_PLAN.md](../REORGANIZATION_PLAN.md)** - Plan for codebase reorganization
- **[../REORGANIZATION_SUMMARY.md](../REORGANIZATION_SUMMARY.md)** - Summary of codebase reorganization

## Quick Links

| Guide | Purpose |
|-------|---------|
| QUICK_START.md | 3-step setup for beginners |
| OPENCODE_SETUP.md | Detailed OpenCode configuration |
| TESTING.md | Local testing without MCP client |
| TROUBLESHOOTING.md | Fix common problems |
| CHANGELOG.md | Version history and changes |

## Directory Structure

```
.
├── guides/                           # You are here
│   ├── README.md                     # This file
│   ├── QUICK_START.md                # Fast setup guide
│   ├── OPENCODE_SETUP.md             # Complete setup guide
│   └── TESTING.md                    # Testing guide
├── examples/
│   └── opencode.jsonc.example        # Example configuration
├── .github/
│   └── TROUBLESHOOTING.md            # Troubleshooting guide
├── src/
│   └── odoo_mcp/
│       ├── server.py                 # Main MCP server
│       └── __init__.py               # Package initialization
├── tests/
│   ├── test_server.py                # Test suite
│   └── __init__.py
├── docs/                             # Odoo documentation (data)
├── rules/                            # Development rules (data)
└── README.md                         # Main project documentation
```

## Next Steps

1. **New to this project?** Start with [QUICK_START.md](QUICK_START.md)
2. **Setting up OpenCode?** Follow [OPENCODE_SETUP.md](OPENCODE_SETUP.md)
3. **Testing locally?** Use [TESTING.md](TESTING.md)
4. **Having issues?** Check [../.github/TROUBLESHOOTING.md](../.github/TROUBLESHOOTING.md)

## About the Server

The Odoo Development MCP Server provides:
- ✅ Version-aware Odoo documentation search (17.0, 18.0, 19.0)
- ✅ AI-powered code generation for modules, models, views, and security
- ✅ Development guidelines and naming convention enforcement
- ✅ Multi-prompt workflows for common Odoo tasks

For more information, see [../README.md](../README.md).
