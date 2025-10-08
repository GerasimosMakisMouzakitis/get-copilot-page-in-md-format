# Release Notes - Version 2.0

**Release Date:** October 8, 2025  
**Type:** Major Release

---

## 🎉 What's New in v2.0

This major release brings JavaScript rendering support, professional project structure, and enhanced documentation for both users and contributors.

### 🚀 Major Features

#### 1. **JavaScript Rendering with Playwright** 🌐
Finally! Full support for JavaScript-heavy websites and Single Page Applications (SPAs).

- **Automatic SPA Detection** - The tool now intelligently detects when a page requires JavaScript
- **Browser Automation** - Uses Playwright's Chromium engine to render dynamic content
- **Smart Retry** - Automatically retries with browser when SPA detected
- **Graceful Degradation** - Works without Playwright installed (with warning)

**Before v2.0:** ❌ JavaScript-rendered pages returned empty content  
**After v2.0:** ✅ Fully captures React, Vue, Angular, and other SPA frameworks

```bash
# Now works perfectly with SPAs
python src/get_copilot_page.py https://copilot.microsoft.com/shares/pages/xyz
```

#### 2. **Professional Project Structure** 📁
Reorganized to follow Python packaging best practices.

```
get-copilot-page-in-md-format/
├── src/                  # Source code
│   └── get_copilot_page.py
├── docs/                 # Documentation
│   ├── USAGE.md
│   ├── SUMMARY.md
│   └── PORTABLE-USAGE.md
├── tests/                # Future tests
├── setup.py              # Package installer
├── requirements.txt      # Dependencies
├── LICENSE               # MIT License
└── README.md             # Main docs
```

#### 3. **Enhanced Documentation** 📚
Comprehensive guides for every use case:

- **README.md** - Quick start with badges and examples
- **USAGE.md** - Detailed usage scenarios
- **CONTRIBUTING.md** - Contribution guidelines (new!)
- **CODE_OF_CONDUCT.md** - Community standards (new!)
- **SECURITY.md** - Security policy (new!)
- **ATTRIBUTION.md** - Usage and credit guidelines

---

## 🔧 Improvements

### Better Content Extraction
- Enhanced title extraction with multiple fallback methods
- Smarter content detection (tries `<main>`, `<article>`, content divs, then `<body>`)
- Improved filename sanitization for cross-platform compatibility

### User Experience
- Clearer error messages with actionable guidance
- Progress indicators for browser automation
- Better handling of edge cases (timeouts, SSL errors, etc.)

### Code Quality
- Added version metadata and timestamps
- Improved function documentation
- Better error handling throughout

---

## 📦 Installation & Setup

### Fresh Install

```bash
# Clone the repository
git clone https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format.git
cd get-copilot-page-in-md-format

# Install dependencies
pip install -r requirements.txt

# Optional: Install Playwright for JavaScript support
playwright install chromium

# Run the tool
python src/get_copilot_page.py https://example.com
```

### Upgrade from v1.0

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Install Playwright (new in v2.0)
playwright install chromium
```

**⚠️ Breaking Changes:** File location changed from root to `src/` directory
- **Old:** `python get_copilot_page.py ...`
- **New:** `python src/get_copilot_page.py ...`
- **Symlink available:** `get_copilot_page.py` → `src/get_copilot_page.py` (for compatibility)

---

## 📋 Full Changelog

### Added ✨
- Playwright browser automation for JavaScript-rendered pages
- Automatic SPA detection mechanism
- Smart retry with browser when static fetch fails
- Professional project structure with `src/`, `docs/`, `tests/` directories
- `setup.py` for package installation
- `LICENSE` file (MIT)
- `CONTRIBUTING.md` with contribution guidelines
- `CODE_OF_CONDUCT.md` with community standards
- `SECURITY.md` with security policy
- GitHub issue templates (bug, feature, docs)
- Pull request template
- Version metadata in source code
- Timestamp tracking (creation date, last updated)
- Backup system with timestamped archives
- Enhanced `.gitignore` with Python best practices

### Changed 🔄
- Moved source code to `src/` directory
- Moved documentation to `docs/` directory
- Reorganized file structure to follow packaging standards
- Updated all documentation to reflect new structure
- Improved error messages with better guidance
- Enhanced README with badges and clearer examples

### Fixed 🐛
- JavaScript-rendered pages now properly captured
- Empty content issue with SPA pages resolved
- Cross-platform filename compatibility improved
- Edge case handling for various page structures

---

## 🎯 Use Cases

### Perfect For:

✅ **Web Scraping** - Convert any webpage to markdown  
✅ **Documentation** - Save web docs for offline reading  
✅ **Archiving** - Preserve web content in portable format  
✅ **Content Migration** - Move content between platforms  
✅ **Research** - Save articles in clean, readable format  
✅ **SPA Support** - Works with React, Vue, Angular apps  

### Important Limitations

**This tool works with most public web pages, but cannot download:**
- Login-required pages (authentication needed)
- Paywalled content (subscription walls)
- Anti-bot protected sites (blocks automated tools)
- Secure web applications (banking, private dashboards)
- Content requiring user interaction (clicks, scrolling)

**The tool will show a clear error message when it cannot access a page.**

### Example Commands

```bash
# Static pages (fast)
python src/get_copilot_page.py https://example.com

# JavaScript-rendered SPAs (automatic detection)
python src/get_copilot_page.py https://copilot.microsoft.com/shares/xyz

# Custom output filename
python src/get_copilot_page.py https://docs.python.org -o python_docs.md

# Works with various sites
python src/get_copilot_page.py https://github.com/user/repo
python src/get_copilot_page.py https://stackoverflow.com/questions/12345
python src/get_copilot_page.py https://medium.com/@user/article
```

---

## 🔒 Security

This release includes a comprehensive security policy:

- Path traversal protection
- Input sanitization
- Safe filename generation
- Responsible disclosure guidelines

See [SECURITY.md](SECURITY.md) for details.

---

## 🤝 Contributing

We welcome contributions! This release includes:

- Detailed contribution guidelines
- Code style standards
- PR/issue templates
- Community code of conduct

See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## 🐛 Known Issues

None at this time. Please [report issues](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/issues) if you encounter any problems.

---

## 🙏 Acknowledgments

Thank you to everyone who uses this tool and provides feedback!

Special recognition for:
- Community members who requested JavaScript support
- Early testers of v2.0 beta features
- Contributors to documentation improvements

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/issues)
- **Discussions:** [GitHub Discussions](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/discussions)
- **Documentation:** [docs/](docs/)

---

## 🔮 Future Roadmap

Looking ahead to v2.1 and beyond:

- [ ] Add authentication support (cookies, headers)
- [ ] Batch processing for multiple URLs
- [ ] Custom content selectors
- [ ] Output format options (PDF, HTML)
- [ ] Configuration file support
- [ ] Plugin system for custom processors

Want to contribute? Check out [issues labeled `good-first-issue`](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)!

---

## 📜 License

MIT License - Free for commercial and non-commercial use with attribution.

See [LICENSE](LICENSE) and [ATTRIBUTION.md](ATTRIBUTION.md) for details.

---

**Enjoy v2.0! 🚀**

If you find this tool useful, please:
- ⭐ Star the repository
- 🐦 Share on social media
- 🤝 Contribute improvements
- 💬 Spread the word

**Download:** [v2.0 Release](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/releases/tag/v2.0)
