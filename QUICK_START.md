# Quick Start - SAP BDC MCP Server

## For Mario: Publish to GitHub (Do This Now!)

### Step 1: Create GitHub Repository (2 minutes)

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `sap-bdc-mcp-server`
   - **Description**: `MCP server for SAP Business Data Cloud - enables AI assistants to manage data shares and Delta Sharing operations`
   - **Visibility**: **Public** ✅
   - **DO NOT** check any initialization options (no README, no .gitignore, no license)
3. Click "Create repository"

### Step 2: Push Your Code (1 minute)

Copy and run these commands (replace `YOUR_USERNAME` with your GitHub username):

```bash
cd C:\Users\mariodefe\sap-bdc-mcp-server
git remote add origin https://github.com/YOUR_USERNAME/sap-bdc-mcp-server.git
git push -u origin main
```

If it asks for authentication:
- Use your GitHub username
- Use a Personal Access Token (PAT) as password, not your GitHub password
- Or use: `gh auth login` if you have GitHub CLI

### Step 3: Configure Repository (3 minutes)

Once pushed, on GitHub:

1. **Add Topics** (click gear icon next to About):
   ```
   mcp, mcp-server, sap, sap-bdc, databricks, delta-sharing, claude, anthropic, ai, python
   ```

2. **Enable Features** (Settings tab):
   - ✅ Issues
   - ✅ Discussions
   - ✅ Projects (optional)

3. **Set Up Security** (Settings → Code security):
   - ✅ Dependabot alerts
   - ✅ Dependabot security updates

### Step 4: Update Documentation (2 minutes)

In your local copy, find and replace:
- **Find**: `YOUR_USERNAME`
- **Replace**: Your actual GitHub username

**Files to update:**
- [README.md](README.md) (3 occurrences)
- [CHANGELOG.md](CHANGELOG.md) (3 occurrences)

Then commit and push:
```bash
git add .
git commit -m "Update repository URLs"
git push
```

### Done! Ready for Kiro! ✅

Send Kiro:
1. Your repository URL: `https://github.com/YOUR_USERNAME/sap-bdc-mcp-server`
2. Point them to: [VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)

---

## For Kiro: Validation Testing (Do This After Mario Publishes)

### Step 1: Clone and Install (5 minutes)

```bash
# Clone the repository
git clone https://github.com/MarioDeFelipe/sap-bdc-mcp-server.git
cd sap-bdc-mcp-server

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install
pip install -e ".[dev]"
```

### Step 2: Configure (2 minutes)

```bash
# Copy environment template
copy .env.example .env

# Edit .env file and set your Databricks recipient name:
# DATABRICKS_RECIPIENT_NAME=your_actual_recipient_name
```

### Step 3: Run Tests (1 minute)

```bash
pytest -v
```

Expected: All tests should pass ✅

### Step 4: Test with Claude Desktop (10 minutes)

1. Find Claude config file:
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`

2. Add this configuration (update paths):
```json
{
  "mcpServers": {
    "sap-bdc": {
      "command": "C:\\full\\path\\to\\venv\\Scripts\\python.exe",
      "args": ["-m", "sap_bdc_mcp.server"],
      "env": {
        "DATABRICKS_RECIPIENT_NAME": "your_recipient_name"
      }
    }
  }
}
```

3. Restart Claude Desktop

4. In Claude, ask: "What SAP BDC tools are available?"

Expected: Should see 5 tools listed ✅

### Step 5: Full Validation (20 minutes)

Follow the complete guide: [VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)

Test all 5 tools:
1. ✅ create_or_update_share
2. ✅ create_or_update_share_csn
3. ✅ publish_data_product
4. ✅ delete_share
5. ✅ generate_csn_template

### Step 6: Report Results

Create an issue on GitHub with:
- ✅ What worked
- ⚠️ What didn't work (if anything)
- 📝 Any suggestions
- 👍 Approval for publication (if all good)

---

## After Validation: PyPI Publication (Mario)

### Prerequisites (One-time setup)

1. Create PyPI account: https://pypi.org/account/register/
2. Generate API token: https://pypi.org/manage/account/token/
3. Add token to GitHub:
   - Go to: `Settings → Secrets → Actions`
   - Add secret: `PYPI_API_TOKEN`
   - Paste your PyPI token

### Publish to PyPI

Once Kiro approves:

```bash
# 1. Update version if needed (in pyproject.toml)
# 2. Update CHANGELOG.md with release date

# 3. Commit changes
git add .
git commit -m "Prepare v0.1.0 release"
git push

# 4. Create GitHub Release
# Go to: https://github.com/YOUR_USERNAME/sap-bdc-mcp-server/releases/new
# - Tag: v0.1.0
# - Title: SAP BDC MCP Server v0.1.0
# - Description: See release notes in GITHUB_PUBLICATION_GUIDE.md
# - Click "Publish release"

# 5. GitHub Actions will automatically build and publish to PyPI!
```

Verify on PyPI: https://pypi.org/project/sap-bdc-mcp-server/

### Test Installation

```bash
pip install sap-bdc-mcp-server
```

---

## After PyPI: npm Publication (Future)

1. Create package.json
2. Decide on implementation approach
3. Set up npm account and token
4. Publish to npm registry

Details TBD after PyPI is stable.

---

## Timeline

| Phase | Owner | Duration | Status |
|-------|-------|----------|--------|
| Create GitHub Repo | Mario | 10 min | 🔄 Ready to start |
| Validation Testing | Kiro | 1-2 hours | ⏳ Waiting |
| Fix Issues (if any) | Mario | TBD | ⏳ If needed |
| PyPI Publication | Mario | 15 min | ⏳ After validation |
| npm Publication | Mario | TBD | ⏳ Future |

---

## Quick Reference URLs

### Live URLs:
- **Repository**: https://github.com/MarioDeFelipe/sap-bdc-mcp-server
- **Issues**: https://github.com/MarioDeFelipe/sap-bdc-mcp-server/issues
- **PyPI**: `https://pypi.org/project/sap-bdc-mcp-server/` (after release)

### Documentation
- Full docs: [README.md](README.md)
- Validation guide: [VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)
- Publication guide: [GITHUB_PUBLICATION_GUIDE.md](GITHUB_PUBLICATION_GUIDE.md)
- Project summary: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

---

## Need Help?

### For Mario:
- GitHub creation: https://docs.github.com/en/get-started/quickstart/create-a-repo
- PyPI upload: https://packaging.python.org/tutorials/packaging-projects/

### For Kiro:
- Follow [VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)
- Report issues on GitHub
- Contact Mario if stuck

---

## Success Checklist

### Mario's Tasks
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Configure repository settings
- [ ] Add topics/tags
- [ ] Share with Kiro
- [ ] Wait for validation
- [ ] Fix any issues reported
- [ ] Publish to PyPI
- [ ] Plan npm package

### Kiro's Tasks
- [ ] Clone repository
- [ ] Install dependencies
- [ ] Configure environment
- [ ] Run tests
- [ ] Test with Claude Desktop
- [ ] Validate all 5 tools
- [ ] Test in Databricks
- [ ] Report results
- [ ] Approve or request fixes

---

**Current Status**: 🚀 Ready for GitHub Publication!

**Next Action**: Mario creates GitHub repository and pushes code.

**Then**: Kiro validates and approves for PyPI.

Let's ship it! 🎉
