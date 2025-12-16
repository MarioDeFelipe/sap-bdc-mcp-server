"""Tests for SAP BDC MCP Server."""

import pytest
from unittest.mock import Mock, patch, AsyncMock

from sap_bdc_mcp.server import app, BDCClientManager


@pytest.fixture
def mock_bdc_client():
    """Create a mock BDC client."""
    client = Mock()
    client.create_or_update_share = Mock(return_value={"status": "success"})
    client.create_or_update_share_csn = Mock(return_value={"status": "success"})
    client.publish_data_product = Mock(return_value={"status": "published"})
    client.delete_share = Mock(return_value={"status": "deleted"})
    return client


@pytest.fixture
def mock_client_manager(mock_bdc_client):
    """Create a mock client manager."""
    manager = BDCClientManager()
    manager._client = mock_bdc_client
    return manager


@pytest.mark.asyncio
async def test_list_tools():
    """Test that tools are properly listed."""
    tools = await app.list_tools()

    assert len(tools) == 5
    tool_names = [tool.name for tool in tools]

    assert "create_or_update_share" in tool_names
    assert "create_or_update_share_csn" in tool_names
    assert "publish_data_product" in tool_names
    assert "delete_share" in tool_names
    assert "generate_csn_template" in tool_names


@pytest.mark.asyncio
async def test_create_share_tool(mock_client_manager):
    """Test create_or_update_share tool."""
    with patch("sap_bdc_mcp.server.client_manager", mock_client_manager):
        arguments = {
            "share_name": "test_share",
            "ord_metadata": {"title": "Test"},
            "tables": ["table1", "table2"]
        }

        result = await app.call_tool("create_or_update_share", arguments)

        assert len(result) == 1
        assert "Successfully created/updated share" in result[0].text
        mock_client_manager.client.create_or_update_share.assert_called_once()


@pytest.mark.asyncio
async def test_create_csn_share_tool(mock_client_manager):
    """Test create_or_update_share_csn tool."""
    with patch("sap_bdc_mcp.server.client_manager", mock_client_manager):
        arguments = {
            "share_name": "test_share",
            "csn_schema": {"definitions": {}}
        }

        result = await app.call_tool("create_or_update_share_csn", arguments)

        assert len(result) == 1
        assert "Successfully created/updated share" in result[0].text
        mock_client_manager.client.create_or_update_share_csn.assert_called_once()


@pytest.mark.asyncio
async def test_publish_data_product_tool(mock_client_manager):
    """Test publish_data_product tool."""
    with patch("sap_bdc_mcp.server.client_manager", mock_client_manager):
        arguments = {
            "share_name": "test_share",
            "data_product_name": "TestProduct"
        }

        result = await app.call_tool("publish_data_product", arguments)

        assert len(result) == 1
        assert "Successfully published data product" in result[0].text
        mock_client_manager.client.publish_data_product.assert_called_once()


@pytest.mark.asyncio
async def test_delete_share_tool(mock_client_manager):
    """Test delete_share tool."""
    with patch("sap_bdc_mcp.server.client_manager", mock_client_manager):
        arguments = {"share_name": "test_share"}

        result = await app.call_tool("delete_share", arguments)

        assert len(result) == 1
        assert "Successfully deleted share" in result[0].text
        mock_client_manager.client.delete_share.assert_called_once()


@pytest.mark.asyncio
async def test_unknown_tool():
    """Test handling of unknown tool."""
    mock_manager = Mock()
    mock_manager.client = Mock()

    with patch("sap_bdc_mcp.server.client_manager", mock_manager):
        result = await app.call_tool("unknown_tool", {})

        assert len(result) == 1
        assert "Unknown tool" in result[0].text


@pytest.mark.asyncio
async def test_tool_error_handling(mock_client_manager):
    """Test error handling in tool execution."""
    mock_client_manager.client.create_or_update_share.side_effect = Exception("Test error")

    with patch("sap_bdc_mcp.server.client_manager", mock_client_manager):
        arguments = {"share_name": "test_share"}

        result = await app.call_tool("create_or_update_share", arguments)

        assert len(result) == 1
        assert "Error executing" in result[0].text
        assert "Test error" in result[0].text


def test_client_manager_initialization():
    """Test BDCClientManager initialization."""
    manager = BDCClientManager()

    with pytest.raises(RuntimeError, match="BDC client not initialized"):
        _ = manager.client
