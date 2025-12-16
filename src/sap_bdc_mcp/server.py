"""SAP Business Data Cloud MCP Server implementation."""

import asyncio
import json
import logging
from typing import Any, Optional

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sap-bdc-mcp")

# Initialize MCP server
app = Server("sap-bdc-mcp-server")


class BDCClientManager:
    """Manages SAP BDC Connect SDK client instances."""

    def __init__(self):
        self._client = None
        self._databricks_client = None

    def initialize(self, recipient_name: str, databricks_utils: Any = None):
        """Initialize the BDC clients.

        Args:
            recipient_name: Name of the Databricks recipient
            databricks_utils: Databricks utilities object (dbutils)
        """
        try:
            from sap_bdc_connect_sdk import BdcConnectClient, DatabricksClient

            # Initialize Databricks client
            self._databricks_client = DatabricksClient(
                dbutils=databricks_utils,
                recipient_name=recipient_name
            )

            # Initialize BDC Connect client
            self._client = BdcConnectClient(self._databricks_client)
            logger.info("SAP BDC clients initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize BDC clients: {e}")
            raise

    @property
    def client(self):
        """Get the BDC Connect client."""
        if self._client is None:
            raise RuntimeError("BDC client not initialized. Call initialize() first.")
        return self._client


# Global client manager
client_manager = BDCClientManager()


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available SAP BDC tools."""
    return [
        Tool(
            name="create_or_update_share",
            description="Create or update a share for data distribution in SAP BDC. "
                       "Shares enable secure data sharing using Delta Sharing protocol.",
            inputSchema={
                "type": "object",
                "properties": {
                    "share_name": {
                        "type": "string",
                        "description": "Name of the share to create or update"
                    },
                    "ord_metadata": {
                        "type": "object",
                        "description": "ORD (Open Resource Discovery) metadata for the share"
                    },
                    "tables": {
                        "type": "array",
                        "description": "List of table names to include in the share",
                        "items": {"type": "string"}
                    }
                },
                "required": ["share_name"]
            }
        ),
        Tool(
            name="create_or_update_share_csn",
            description="Create or update a share using CSN (Common Semantic Notation) format. "
                       "CSN provides a standardized way to describe data schemas.",
            inputSchema={
                "type": "object",
                "properties": {
                    "share_name": {
                        "type": "string",
                        "description": "Name of the share"
                    },
                    "csn_schema": {
                        "type": "object",
                        "description": "CSN schema definition"
                    }
                },
                "required": ["share_name", "csn_schema"]
            }
        ),
        Tool(
            name="publish_data_product",
            description="Publish a data product to make it available for consumption. "
                       "This makes the shared data discoverable and accessible.",
            inputSchema={
                "type": "object",
                "properties": {
                    "share_name": {
                        "type": "string",
                        "description": "Name of the share to publish"
                    },
                    "data_product_name": {
                        "type": "string",
                        "description": "Name of the data product"
                    }
                },
                "required": ["share_name", "data_product_name"]
            }
        ),
        Tool(
            name="delete_share",
            description="Delete a share and withdraw the shared resources. "
                       "This removes the share and makes the data no longer accessible.",
            inputSchema={
                "type": "object",
                "properties": {
                    "share_name": {
                        "type": "string",
                        "description": "Name of the share to delete"
                    }
                },
                "required": ["share_name"]
            }
        ),
        Tool(
            name="generate_csn_template",
            description="Generate a CSN template from an existing Databricks share. "
                       "This utility creates a CSN schema that can be modified as needed.",
            inputSchema={
                "type": "object",
                "properties": {
                    "share_name": {
                        "type": "string",
                        "description": "Name of the Databricks share"
                    }
                },
                "required": ["share_name"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool execution requests."""
    try:
        client = client_manager.client

        if name == "create_or_update_share":
            share_name = arguments["share_name"]
            ord_metadata = arguments.get("ord_metadata", {})
            tables = arguments.get("tables", [])

            result = client.create_or_update_share(
                share_name=share_name,
                ord_metadata=ord_metadata,
                tables=tables
            )

            return [TextContent(
                type="text",
                text=f"Successfully created/updated share '{share_name}'.\n"
                     f"Result: {json.dumps(result, indent=2)}"
            )]

        elif name == "create_or_update_share_csn":
            share_name = arguments["share_name"]
            csn_schema = arguments["csn_schema"]

            result = client.create_or_update_share_csn(
                share_name=share_name,
                csn_schema=csn_schema
            )

            return [TextContent(
                type="text",
                text=f"Successfully created/updated share '{share_name}' with CSN schema.\n"
                     f"Result: {json.dumps(result, indent=2)}"
            )]

        elif name == "publish_data_product":
            share_name = arguments["share_name"]
            data_product_name = arguments["data_product_name"]

            result = client.publish_data_product(
                share_name=share_name,
                data_product_name=data_product_name
            )

            return [TextContent(
                type="text",
                text=f"Successfully published data product '{data_product_name}' "
                     f"from share '{share_name}'.\n"
                     f"Result: {json.dumps(result, indent=2)}"
            )]

        elif name == "delete_share":
            share_name = arguments["share_name"]

            result = client.delete_share(share_name=share_name)

            return [TextContent(
                type="text",
                text=f"Successfully deleted share '{share_name}'.\n"
                     f"Result: {json.dumps(result, indent=2)}"
            )]

        elif name == "generate_csn_template":
            share_name = arguments["share_name"]

            from sap_bdc_connect_sdk import csn_generator

            csn_template = csn_generator.generate_csn_from_share(share_name)

            return [TextContent(
                type="text",
                text=f"Generated CSN template for share '{share_name}':\n"
                     f"{json.dumps(csn_template, indent=2)}"
            )]

        else:
            return [TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]

    except Exception as e:
        logger.error(f"Error executing tool {name}: {e}")
        return [TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]


async def main():
    """Run the MCP server."""
    logger.info("Starting SAP BDC MCP Server...")

    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
