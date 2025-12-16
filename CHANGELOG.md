# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Additional SAP BDC SDK feature integrations
- Enhanced error handling and logging
- Performance optimizations
- Integration tutorials and examples

## [0.1.0] - 2025-12-16

### Added
- Initial release of SAP BDC MCP Server
- Support for 5 core SAP BDC operations:
  - `create_or_update_share` - Create/update data shares with ORD metadata
  - `create_or_update_share_csn` - Configure shares using CSN schema
  - `publish_data_product` - Publish data products
  - `delete_share` - Delete and withdraw shares
  - `generate_csn_template` - Auto-generate CSN templates
- MCP protocol implementation using stdio transport
- Configuration management via environment variables
- Databricks integration support
- Delta Sharing protocol support
- Comprehensive test suite
- Documentation and examples
- GitHub Actions CI/CD workflows
- MIT License

### Technical Details
- Python 3.9+ support
- Compatible with SAP BDC Connect SDK 1.1.6+
- MCP SDK integration
- Type hints throughout codebase
- Async/await support for MCP operations

### Known Limitations
- Requires Databricks environment with dbutils
- Recipient configuration needed for Delta Sharing
- Limited to SAP BDC Connect SDK exposed functionality

---

## Release Notes Template

### [Version] - YYYY-MM-DD

#### Added
- New features

#### Changed
- Changes in existing functionality

#### Deprecated
- Soon-to-be removed features

#### Removed
- Removed features

#### Fixed
- Bug fixes

#### Security
- Security improvements

---

[Unreleased]: https://github.com/MarioDeFelipe/sap-bdc-mcp-server/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/MarioDeFelipe/sap-bdc-mcp-server/releases/tag/v0.1.0
