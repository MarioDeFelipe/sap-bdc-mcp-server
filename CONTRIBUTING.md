# Contributing to SAP BDC MCP Server

Thank you for your interest in contributing to the SAP BDC MCP Server project!

## Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

4. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Running Tests

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=sap_bdc_mcp --cov-report=html
```

Run specific tests:

```bash
pytest tests/test_server.py::test_list_tools
```

## Code Style

This project follows Python best practices:

- Use type hints where appropriate
- Follow PEP 8 style guidelines
- Write docstrings for all public functions and classes
- Keep functions focused and single-purpose

## Adding New Tools

To add a new tool to the MCP server:

1. Add the tool definition in `list_tools()` in [server.py](src/sap_bdc_mcp/server.py)
2. Implement the tool handler in `call_tool()` in [server.py](src/sap_bdc_mcp/server.py)
3. Add tests in [tests/test_server.py](tests/test_server.py)
4. Update the README with documentation for the new tool
5. Add usage examples in [examples/example_usage.py](examples/example_usage.py)

## Testing Your Changes

Before submitting a pull request:

1. Run all tests: `pytest`
2. Check code formatting
3. Test the MCP server manually with an MCP client
4. Update documentation as needed

## Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Run tests to ensure everything passes
5. Commit with clear, descriptive messages
6. Push to your fork
7. Submit a pull request

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include tests for new functionality
- Update documentation as needed
- Ensure all tests pass

## Questions?

If you have questions or need help, please open an issue on the repository.

Thank you for contributing!
