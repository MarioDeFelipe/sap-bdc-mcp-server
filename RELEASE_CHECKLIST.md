# Release Checklist

This document outlines the steps for releasing the SAP BDC MCP Server.

## Pre-Release Validation (With Kiro)

- [ ] Databricks environment setup verified
- [ ] SAP BDC Connect SDK authentication working
- [ ] All 5 tools tested successfully:
  - [ ] create_or_update_share
  - [ ] create_or_update_share_csn
  - [ ] publish_data_product
  - [ ] delete_share
  - [ ] generate_csn_template
- [ ] Claude Desktop integration tested
- [ ] Error handling validated
- [ ] Documentation accuracy confirmed

## GitHub Publication

### Initial Repository Setup

- [ ] Create GitHub repository
- [ ] Update README.md with correct repository URLs
- [ ] Update CONTRIBUTING.md with repository-specific information
- [ ] Add repository description and topics

### First Commit

```bash
cd C:\Users\mariodefe\sap-bdc-mcp-server
git add .
git commit -m "Initial commit: SAP BDC MCP Server v0.1.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sap-bdc-mcp-server.git
git push -u origin main
```

### Repository Configuration

- [ ] Enable GitHub Issues
- [ ] Enable GitHub Discussions
- [ ] Create Wiki (optional)
- [ ] Add topics: `mcp`, `sap`, `databricks`, `claude`, `ai`, `mcp-server`, `delta-sharing`
- [ ] Configure branch protection rules for main branch
- [ ] Add repository description
- [ ] Set up repository social preview image (optional)

### GitHub Actions Setup

- [ ] Verify CI workflow runs successfully
- [ ] Set up CodeQL scanning
- [ ] Configure Dependabot (optional)

## PyPI Publication (After Validation)

### Preparation

- [ ] Verify version number in pyproject.toml
- [ ] Update CHANGELOG.md with release notes
- [ ] Ensure all tests pass
- [ ] Build package locally and test

### PyPI Account Setup

- [ ] Create PyPI account (if needed)
- [ ] Generate API token
- [ ] Add `PYPI_API_TOKEN` to GitHub Secrets

### Release Process

```bash
# Build the package
python -m build

# Test with TestPyPI first
twine upload --repository testpypi dist/*

# If successful, upload to PyPI
twine upload dist/*
```

- [ ] Create GitHub release with tag (e.g., v0.1.0)
- [ ] GitHub Actions will automatically publish to PyPI
- [ ] Verify package on PyPI
- [ ] Test installation from PyPI: `pip install sap-bdc-mcp-server`

## npm Publication (Future - After Python Package)

### Preparation

- [ ] Create package.json for npm
- [ ] Set up Node.js wrapper (if needed)
- [ ] Test npm package locally

### npm Account Setup

- [ ] Create npm account (if needed)
- [ ] Generate npm access token
- [ ] Add `NPM_TOKEN` to GitHub Secrets

### Release Process

- [ ] Update package.json version
- [ ] Test npm package locally
- [ ] Create GitHub release (will trigger automatic npm publish)
- [ ] Verify package on npm
- [ ] Test installation from npm

## Post-Release

- [ ] Announce release on relevant channels
- [ ] Update documentation
- [ ] Monitor issues and feedback
- [ ] Plan next iteration based on feedback

## Version Numbering

Follow Semantic Versioning (semver):
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

Current version: **0.1.0** (Initial Release)

## Emergency Rollback

If critical issues are discovered:

1. Yank the release from PyPI: `pip install yank <package>`
2. Create hotfix branch
3. Fix the issue
4. Release patch version
5. Communicate with users

## Notes

- Always test on TestPyPI before production PyPI
- Keep CHANGELOG.md updated
- Tag releases in Git
- Create GitHub releases with detailed notes
- Monitor CI/CD pipelines for failures
