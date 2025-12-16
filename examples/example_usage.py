"""Example usage of SAP BDC MCP Server tools.

This file demonstrates how the tools would be called through the MCP protocol.
In practice, these would be invoked by an MCP client like Claude Desktop.
"""

import json

# Example 1: Create a share with ORD metadata
example_create_share = {
    "tool": "create_or_update_share",
    "arguments": {
        "share_name": "customer_analytics_share",
        "ord_metadata": {
            "title": "Customer Analytics Data",
            "description": "Aggregated customer behavior and transaction data",
            "version": "1.0.0",
            "tags": ["customers", "analytics", "transactions"]
        },
        "tables": [
            "customer_profiles",
            "customer_transactions",
            "customer_segments"
        ]
    }
}

# Example 2: Create a share with CSN schema
example_csn_share = {
    "tool": "create_or_update_share_csn",
    "arguments": {
        "share_name": "product_catalog_share",
        "csn_schema": {
            "definitions": {
                "Products": {
                    "kind": "entity",
                    "elements": {
                        "ProductID": {
                            "type": "String",
                            "key": True
                        },
                        "ProductName": {
                            "type": "String"
                        },
                        "Category": {
                            "type": "String"
                        },
                        "Price": {
                            "type": "Decimal",
                            "precision": 10,
                            "scale": 2
                        },
                        "InStock": {
                            "type": "Boolean"
                        }
                    }
                },
                "Categories": {
                    "kind": "entity",
                    "elements": {
                        "CategoryID": {
                            "type": "String",
                            "key": True
                        },
                        "CategoryName": {
                            "type": "String"
                        },
                        "Description": {
                            "type": "String"
                        }
                    }
                }
            }
        }
    }
}

# Example 3: Publish a data product
example_publish = {
    "tool": "publish_data_product",
    "arguments": {
        "share_name": "customer_analytics_share",
        "data_product_name": "CustomerInsights2024"
    }
}

# Example 4: Generate CSN template from existing share
example_generate_csn = {
    "tool": "generate_csn_template",
    "arguments": {
        "share_name": "existing_databricks_share"
    }
}

# Example 5: Delete a share
example_delete = {
    "tool": "delete_share",
    "arguments": {
        "share_name": "deprecated_share"
    }
}


def print_example(name: str, example: dict):
    """Pretty print an example."""
    print(f"\n{'=' * 60}")
    print(f"Example: {name}")
    print('=' * 60)
    print(json.dumps(example, indent=2))


if __name__ == "__main__":
    print("SAP BDC MCP Server - Example Usage")
    print("=" * 60)

    examples = [
        ("Create Share with ORD Metadata", example_create_share),
        ("Create Share with CSN Schema", example_csn_share),
        ("Publish Data Product", example_publish),
        ("Generate CSN Template", example_generate_csn),
        ("Delete Share", example_delete)
    ]

    for name, example in examples:
        print_example(name, example)

    print(f"\n{'=' * 60}")
    print("Note: These examples show the structure of tool calls.")
    print("In practice, the MCP client (e.g., Claude) handles the actual invocation.")
    print('=' * 60)
