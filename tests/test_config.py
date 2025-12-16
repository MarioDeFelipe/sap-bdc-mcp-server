"""Tests for configuration module."""

import os
import pytest
from sap_bdc_mcp.config import BDCConfig


def test_config_from_env(monkeypatch):
    """Test loading configuration from environment."""
    monkeypatch.setenv("DATABRICKS_RECIPIENT_NAME", "test_recipient")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    config = BDCConfig.from_env()

    assert config.recipient_name == "test_recipient"
    assert config.log_level == "DEBUG"


def test_config_missing_recipient_name(monkeypatch):
    """Test that missing recipient name raises error."""
    monkeypatch.delenv("DATABRICKS_RECIPIENT_NAME", raising=False)

    with pytest.raises(ValueError, match="DATABRICKS_RECIPIENT_NAME"):
        BDCConfig.from_env()


def test_config_default_log_level(monkeypatch):
    """Test default log level."""
    monkeypatch.setenv("DATABRICKS_RECIPIENT_NAME", "test_recipient")
    monkeypatch.delenv("LOG_LEVEL", raising=False)

    config = BDCConfig.from_env()

    assert config.log_level == "INFO"


def test_config_to_dict():
    """Test converting config to dictionary."""
    config = BDCConfig(recipient_name="test_recipient", log_level="DEBUG")

    config_dict = config.to_dict()

    assert config_dict == {
        "recipient_name": "test_recipient",
        "log_level": "DEBUG"
    }
