# SAP BDC MCP Server - Validation Guide

This guide is for Kiro to validate the MCP server installation and functionality.

## Prerequisites Verification

Before starting, ensure you have:

- [ ] Python 3.9 or higher installed
- [ ] Access to a Databricks workspace
- [ ] SAP Business Data Cloud account with proper permissions
- [ ] Databricks recipient configured for Delta Sharing
- [ ] Claude Desktop installed (for MCP testing)

## Installation Steps

### 1. Clone and Install

```bash
# Clone the repository
cd C:\Users\mariodefe
cd sap-bdc-mcp-server

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install the package
pip install -e ".[dev]"
```

### 2. Configuration

```bash
# Copy environment template
copy .env.example .env

# Edit .env file and set:
# DATABRICKS_RECIPIENT_NAME=your_actual_recipient_name
# LOG_LEVEL=INFO
```

### 3. Verify Installation

```bash
# Run tests
pytest -v

# Check if server starts (press Ctrl+C to stop)
python -m sap_bdc_mcp.server
```

Expected output: Server should start without errors and wait for input.

## Validation Tests

### Test 1: Basic Server Functionality

**Objective**: Verify the server can start and list tools.

**Steps**:
1. Start the server: `python -m sap_bdc_mcp.server`
2. Server should initialize without errors
3. Press Ctrl+C to stop

**Expected Result**: No initialization errors.

### Test 2: Claude Desktop Integration

**Objective**: Test MCP integration with Claude Desktop.

**Steps**:

1. Locate Claude Desktop config file:
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`

2. Add configuration:
```json
{
  "mcpServers": {
    "sap-bdc": {
      "command": "C:\\Users\\mariodefe\\sap-bdc-mcp-server\\venv\\Scripts\\python.exe",
      "args": ["-m", "sap_bdc_mcp.server"],
      "env": {
        "DATABRICKS_RECIPIENT_NAME": "YOUR_RECIPIENT_NAME"
      }
    }
  }
}
```

3. Restart Claude Desktop

4. In Claude, check if the server is connected:
   - Look for "sap-bdc" in available servers
   - Should show 5 available tools

**Expected Result**: Server appears in Claude Desktop with 5 tools listed.

### Test 3: Tool Execution - List Tools

**Objective**: Verify all tools are accessible.

**In Claude Desktop, ask**:
```
What tools are available from the SAP BDC server?
```

**Expected Result**: Claude should list:
1. create_or_update_share
2. create_or_update_share_csn
3. publish_data_product
4. delete_share
5. generate_csn_template

### Test 4: Create Share (Simple)

**Objective**: Test basic share creation.

**In Claude Desktop, ask**:
```
Use the SAP BDC server to create a test share named "validation_test_share"
with a simple table configuration.
```

**Expected Result**:
- Tool should execute
- Either success or descriptive error message
- No server crashes

### Test 5: Generate CSN Template

**Objective**: Test CSN generation from existing share.

**Prerequisite**: Have an existing Databricks share name ready.

**In Claude Desktop, ask**:
```
Generate a CSN template from the Databricks share named "EXISTING_SHARE_NAME"
```

**Expected Result**:
- CSN template generated in JSON format
- Schema structure visible
- No errors

### Test 6: Error Handling

**Objective**: Verify graceful error handling.

**In Claude Desktop, ask**:
```
Try to delete a share named "nonexistent_share_xyz"
```

**Expected Result**:
- Error message returned (not crash)
- Error is descriptive
- Server continues running

## Validation Checklist

### Basic Functionality
- [ ] Server starts without errors
- [ ] All 5 tools listed correctly
- [ ] Configuration loads properly
- [ ] Environment variables recognized

### Claude Desktop Integration
- [ ] Server appears in MCP servers list
- [ ] Tools are accessible from Claude
- [ ] Commands execute (success or fail gracefully)
- [ ] Error messages are clear and helpful

### Databricks Integration
- [ ] Can connect to Databricks
- [ ] Recipient authentication works
- [ ] Share operations execute
- [ ] CSN generation works

### Error Handling
- [ ] Invalid share names handled gracefully
- [ ] Missing parameters reported clearly
- [ ] Authentication errors descriptive
- [ ] Server doesn't crash on errors

## Common Issues and Solutions

### Issue: "BDC client not initialized"

**Solution**: This typically means:
1. Running outside Databricks environment
2. Missing dbutils
3. Need to use Databricks Connect for local development

### Issue: "DATABRICKS_RECIPIENT_NAME not set"

**Solution**:
1. Check .env file exists
2. Verify environment variable is set correctly
3. Restart server after changing config

### Issue: Server not appearing in Claude Desktop

**Solution**:
1. Check config file path is correct
2. Verify JSON syntax is valid
3. Ensure Python path in config is correct
4. Restart Claude Desktop
5. Check Claude Desktop logs

### Issue: Import errors

**Solution**:
1. Ensure virtual environment is activated
2. Reinstall: `pip install -e ".[dev]"`
3. Check Python version (3.9+)

## Reporting Issues

When reporting issues, please include:

1. **Environment**:
   - OS and version
   - Python version
   - SAP BDC Connect SDK version
   - Claude Desktop version (if applicable)

2. **Error messages**:
   - Full error text
   - Stack traces
   - Server logs

3. **Steps to reproduce**:
   - Exact commands run
   - Configuration used
   - Expected vs actual behavior

4. **Context**:
   - Running in Databricks? (Yes/No)
   - Local development? (Yes/No)
   - First time setup? (Yes/No)

## Success Criteria

The validation is successful if:

1. ✅ Server starts without errors
2. ✅ All 5 tools are accessible
3. ✅ At least one tool executes successfully
4. ✅ Errors are handled gracefully (no crashes)
5. ✅ Integration with Claude Desktop works

## Next Steps After Validation

Once validation is complete:

1. Document any issues found
2. Verify fixes for critical issues
3. Approve for GitHub publication
4. Plan PyPI release
5. Consider npm package needs

## Contact

For questions during validation:
- Open an issue in the repository
- Contact the development team
- Check documentation in README.md
