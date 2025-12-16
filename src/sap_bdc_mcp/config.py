"""Configuration management for SAP BDC MCP Server."""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class BDCConfig:
    """Configuration for SAP BDC Connect SDK."""

    recipient_name: str
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "BDCConfig":
        """Load configuration from environment variables."""
        recipient_name = os.getenv("DATABRICKS_RECIPIENT_NAME")

        if not recipient_name:
            raise ValueError(
                "DATABRICKS_RECIPIENT_NAME environment variable is required"
            )

        return cls(
            recipient_name=recipient_name,
            log_level=os.getenv("LOG_LEVEL", "INFO")
        )

    def to_dict(self) -> dict:
        """Convert config to dictionary."""
        return {
            "recipient_name": self.recipient_name,
            "log_level": self.log_level
        }
