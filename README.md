# SAP Business Data Cloud MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)

An MCP (Model Context Protocol) server that provides integration with SAP Business Data Cloud (BDC) Connect SDK. This server enables AI assistants like Claude to interact with SAP BDC for data sharing, Delta Sharing protocol operations, and data product management.

> **Status**: Initial Release - Ready for validation testing

## Features

This MCP server exposes the following SAP BDC capabilities:

- **Create/Update Shares**: Manage data shares with ORD metadata
- **CSN Schema Management**: Configure shares using Common Semantic Notation
- **Data Product Publishing**: Publish and unpublish data products
- **Share Deletion**: Remove and withdraw shared resources
- **CSN Template Generation**: Auto-generate CSN templates from Databricks shares

## Prerequisites

- Python 3.9 or higher
- Access to a Databricks environment
- SAP Business Data Cloud account
- Databricks recipient configured for Delta Sharing

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/sap-bdc-mcp-server.git
cd sap-bdc-mcp-server
```

### 2. Install Dependencies

```bash
pip install -e .
```

Or for development:

```bash
pip install -e ".[dev]"
```

### 3. Configure Environment

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` and set your Databricks recipient name:

```
DATABRICKS_RECIPIENT_NAME=your_recipient_name
LOG_LEVEL=INFO
```

## Usage

### Running the Server

The MCP server runs as a stdio-based service:

```bash
python -m sap_bdc_mcp.server
```

Or using the installed script:

```bash
sap-bdc-mcp
```

### Integration with Claude Desktop

Add this server to your Claude Desktop configuration file:

**On MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**On Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "sap-bdc": {
      "command": "python",
      "args": ["-m", "sap_bdc_mcp.server"],
      "env": {
        "DATABRICKS_RECIPIENT_NAME": "your_recipient_name"
      }
    }
  }
}
```

Alternatively, if installed in a virtual environment:

```json
{
  "mcpServers": {
    "sap-bdc": {
      "command": "C:\\path\\to\\venv\\Scripts\\python.exe",
      "args": ["-m", "sap_bdc_mcp.server"],
      "env": {
        "DATABRICKS_RECIPIENT_NAME": "your_recipient_name"
      }
    }
  }
}
```

## Available Tools

### 1. create_or_update_share

Create or update a data share with ORD metadata.

**Parameters:**
- `share_name` (required): Name of the share
- `ord_metadata` (optional): ORD metadata object
- `tables` (optional): Array of table names to include

**Example:**
```json
{
  "share_name": "customer_data_share",
  "ord_metadata": {
    "title": "Customer Data",
    "description": "Shared customer information"
  },
  "tables": ["customers", "orders"]
}
```

### 2. create_or_update_share_csn

Create or update a share using CSN format.

**Parameters:**
- `share_name` (required): Name of the share
- `csn_schema` (required): CSN schema definition object

**Example:**
```json
{
  "share_name": "product_share",
  "csn_schema": {
    "definitions": {
      "Products": {
        "kind": "entity",
        "elements": {
          "ID": {"type": "String"},
          "name": {"type": "String"}
        }
      }
    }
  }
}
```

### 3. publish_data_product

Publish a data product to make it available for consumption.

**Parameters:**
- `share_name` (required): Name of the share
- `data_product_name` (required): Name of the data product

**Example:**
```json
{
  "share_name": "customer_data_share",
  "data_product_name": "CustomerAnalytics"
}
```

### 4. delete_share

Delete a share and withdraw shared resources.

**Parameters:**
- `share_name` (required): Name of the share to delete

**Example:**
```json
{
  "share_name": "old_share"
}
```

### 5. generate_csn_template

Generate a CSN template from an existing Databricks share.

**Parameters:**
- `share_name` (required): Name of the Databricks share

**Example:**
```json
{
  "share_name": "existing_databricks_share"
}
```

## Architecture

The server uses:
- **MCP SDK**: For protocol implementation
- **SAP BDC Connect SDK**: For SAP Business Data Cloud operations
- **Delta Sharing**: Open protocol for secure data sharing
- **ORD Protocol**: For resource discovery and metadata

## Development

### Running Tests

```bash
pytest
```

### Project Structure

```
sap-bdc-mcp-server/
├── src/
│   └── sap_bdc_mcp/
│       ├── __init__.py
│       ├── server.py       # Main MCP server implementation
│       └── config.py       # Configuration management
├── pyproject.toml          # Project dependencies
├── .env.example           # Environment variable template
└── README.md              # This file
```

## Important Notes

### Databricks Integration

The SAP BDC Connect SDK requires integration with Databricks. The server needs:
- A valid Databricks environment with `dbutils` available
- A configured recipient for Delta Sharing

**Note**: When running outside Databricks (e.g., local development), you may need to mock or provide alternative implementations for Databricks utilities.

### Authentication

Authentication is handled through:
1. Databricks workspace credentials
2. Recipient configuration in Databricks
3. SAP BDC service credentials (configured in Databricks)

## Troubleshooting

### "BDC client not initialized" Error

The client requires initialization with Databricks utilities. If running in a non-Databricks environment, you may need to:
- Run the server within a Databricks notebook
- Use Databricks Connect for local development
- Mock the required Databricks utilities for testing

### Missing Environment Variables

Ensure `DATABRICKS_RECIPIENT_NAME` is set in your environment or `.env` file.

## Resources

- [SAP BDC Connect SDK on PyPI](https://pypi.org/project/sap-bdc-connect-sdk/)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
- [Delta Sharing Protocol](https://delta.io/sharing/)
- [SAP Business Data Cloud](https://www.sap.com)

## License

This MCP server is provided as-is. Please review the SAP BDC Connect SDK license terms when using this integration.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on:
- Setting up your development environment
- Running tests
- Submitting pull requests
- Code style guidelines

## Roadmap

- [ ] Initial validation with Databricks environment
- [ ] PyPI package publication
- [ ] npm package for Node.js environments
- [ ] Additional SAP BDC SDK features
- [ ] Enhanced error handling and logging
- [ ] Integration examples and tutorials

## Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/sap-bdc-mcp-server/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/sap-bdc-mcp-server/discussions)
- **Documentation**: [Wiki](https://github.com/YOUR_USERNAME/sap-bdc-mcp-server/wiki)

## Acknowledgments

- SAP for the BDC Connect SDK
- Anthropic for the Model Context Protocol
- The MCP community for inspiration and support
