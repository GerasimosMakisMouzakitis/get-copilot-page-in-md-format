# get-copilot-page-in-md-format

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/GerasimosMakisMouzakitis/get-copilot-page-in-md-format?style=social)](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format)

> **Convert any webpage to clean markdown in seconds—even JavaScript-heavy SPAs. Drop it in your project, run one command, and you're done. No complex setup, no configuration files, just instant results.** 🚀

A Python tool to download web pages and save them in markdown format with **automatic JavaScript rendering support**.

**Version:** 2.0  
**Author:** Gerasimos Makis Mouzakitis  
**Created:** October 8, 2025 (UTC)  
**Last Updated:** October 8, 2025 (UTC)  
**In cooperation with:** GitHub Codespaces, GitHub Copilot Chat, and Claude Sonnet 3.5 Chat Agent

> 💡 **New to the project?** Check out [VIRAL-STRATEGY.md](docs/VIRAL-STRATEGY.md) to learn how to help this project grow!

## 🎯 Quick Start (3 Steps)

```bash
# 1. Download (or clone)
curl -O https://raw.githubusercontent.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/main/src/get_copilot_page.py

# 2. Install dependencies (one-time)
pip install requests beautifulsoup4 html2text playwright && playwright install chromium

# 3. Run!
python get_copilot_page.py https://example.com
```

That's it! No complex setup, no configuration files. See [PORTABLE-USAGE.md](docs/PORTABLE-USAGE.md) for more integration options.

## Features

- 🚀 **100% Portable** - Single file, drop it anywhere and run
- 📥 Download any public web page using its URL
- ⚡ **Automatic JavaScript rendering** for single-page applications (SPAs)
- 📝 Automatically converts HTML content to clean markdown
- 🎯 Preserves page structure, links, and formatting
- 🏷️ Auto-generates filename from page title or use custom output name
- 🔗 Includes source URL in the output for reference
- 🤖 Smart detection of JavaScript-heavy pages with automatic retry
- 🔌 Easy to integrate into any project or workflow

## Installation

### Option 1: Install from source (recommended)
```bash
# Clone repository
git clone https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format.git
cd get-copilot-page-in-md-format

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser (for JavaScript-rendered pages)
playwright install chromium
```

### Option 2: Install as package
```bash
# Install from local directory
pip install -e .

# Install Playwright browser
playwright install chromium
```

## Usage

### Basic Usage

Download a page (filename auto-generated from page title):
```bash
python src/get_copilot_page.py <URL>

# Or use the symlink for backwards compatibility
python get_copilot_page.py <URL>
```

### Custom Output Filename

Specify a custom output filename:
```bash
python src/get_copilot_page.py <URL> -o my_page.md
```

### Examples

```bash
# Download with auto-generated filename
python src/get_copilot_page.py https://example.com/page

# Download with custom filename
python src/get_copilot_page.py https://example.com/page -o tutorial.md

# Works with JavaScript-rendered pages (SPAs)
python src/get_copilot_page.py https://copilot.microsoft.com/shares/pages/xyz -o copilot_share.md
```

### Command-Line Options

- `url` (required): The URL of the Copilot public page to download
- `-o, --output`: Optional custom output filename (default: auto-generated from page title)
- `-h, --help`: Show help message

## Requirements

- Python 3.6 or higher
- requests
- beautifulsoup4
- html2text
- playwright (optional but recommended for JavaScript-rendered pages)

## Important: What This Tool Can and Cannot Download

### ✅ Works With:
- Public web pages (blogs, documentation, articles)
- Static HTML pages
- JavaScript-rendered pages (React, Vue, Angular apps)
- Most news sites and content pages
- GitHub Pages, Medium articles, Wikipedia
- Public documentation sites

### ❌ Cannot Download:
- **Login-protected pages** - Pages that require you to sign in
- **Paywalled content** - Content behind subscription walls
- **Anti-bot protected sites** - Sites that actively block automated tools
- **Complex web applications** - Banking sites, dashboards with heavy security
- **Some dynamically loaded content** - Content that requires specific user interactions

**If the tool cannot download a page, it will show you a clear error message explaining why.**

## Output Format

The generated markdown file includes:
- Page title as the main heading
- Source URL for reference
- Full page content converted to markdown format
- Preserved formatting, links, and structure

## Project Structure

```
get-copilot-page-in-md-format/
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   └── get_copilot_page.py      # Main script
│
├── docs/                         # Documentation
│   ├── USAGE.md                 # Extended usage guide
│   ├── SUMMARY.md               # Project summary
│   ├── PORTABLE-USAGE.md        # Integration guide
│   ├── VIRAL-STRATEGY.md        # Growth strategy
│   └── REORGANIZATION.md        # Reorganization history
│
├── tests/                        # Test files (for future tests)
│   └── README.md                # Test documentation
│
├── backup/                       # Version backups
│   ├── README.md                # Backup documentation
│   └── *.zip                    # Timestamped backups
│
├── .github/                      # GitHub configuration
│   └── copilot-instructions.md  # AI agent instructions
│
├── Root files:
│   ├── README.md                # Main documentation (you are here)
│   ├── LICENSE                  # MIT License
│   ├── ATTRIBUTION.md           # Attribution & credit guidelines
│   ├── CHANGELOG.md             # Version history
│   ├── setup.py                 # Package configuration
│   ├── requirements.txt         # Python dependencies
│   ├── MANIFEST.in              # Package manifest
│   └── get_copilot_page.py     # Symlink → src/ (backwards compatibility)
```

## Version History

### Version 2.0 (October 8, 2025)
- ✨ Added Playwright browser automation for JavaScript-rendered pages
- 🔍 Automatic SPA (Single Page Application) detection
- 🔄 Smart retry mechanism with browser rendering
- 📚 Enhanced documentation
- 🎯 Graceful degradation when Playwright not installed

### Version 1.0 (Initial)
- Basic HTML to Markdown conversion
- Static page fetching

## Author & Credits

**Author:** Gerasimos Makis Mouzakitis  
**Collaboration:** Developed in cooperation with GitHub Codespaces, GitHub Copilot Chat, and Claude Sonnet 3.5 Chat Agent

### Using This Project?

**Please provide attribution!** See [ATTRIBUTION.md](ATTRIBUTION.md) for guidelines.

Quick attribution example:
```markdown
Powered by [get-copilot-page-in-md-format](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format) 
by Gerasimos Makis Mouzakitis
```

## License

**MIT License** - Free for commercial and non-commercial use with attribution.

See [LICENSE](LICENSE) for full terms. See [ATTRIBUTION.md](ATTRIBUTION.md) for usage guidelines.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before getting started.

- 🐛 [Report a Bug](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/issues/new?template=bug_report.md)
- 💡 [Request a Feature](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/issues/new?template=feature_request.md)
- 📚 [Improve Documentation](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/issues/new?template=documentation.md)
- 🔒 [Report Security Issue](SECURITY.md)

## Community

- **Code of Conduct:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- **Security Policy:** [SECURITY.md](SECURITY.md)
- **Release Notes:** [RELEASE_NOTES.md](RELEASE_NOTES.md)