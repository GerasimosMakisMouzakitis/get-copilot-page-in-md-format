# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1] - 2025-10-08

### Added
- **Comprehensive legal disclaimer** (DISCLAIMER.md) - 6000+ word legal protection document
- **Disclaimer display on script execution** - Shows legal notice every time the tool runs
- **Dedicated downloads folder** - All files now saved to `downloads/` directory by default
- **Custom output directory option** - New `-d/--dir/--output-dir` flag for flexible file organization
- **Automatic directory creation** - Creates output directories if they don't exist
- **Updated documentation** - All docs now include limitations and legal warnings

### Changed
- Default save location changed from current directory to `downloads/` folder
- README.md now includes prominent disclaimer warnings
- Enhanced .gitignore to exclude downloads folder and allow DISCLAIMER.md

### Security
- Added comprehensive legal protection against misuse
- Clear terms of acceptable and prohibited use
- User liability and responsibility clearly defined
- Compliance guidelines for copyright, ToS, and privacy laws

## [2.0] - 2025-10-08

### Added
- **Playwright browser automation** for JavaScript-rendered pages
- **Automatic SPA detection** - identifies JavaScript-heavy pages
- **Smart retry mechanism** - automatically retries with browser when SPA detected
- **Graceful degradation** - warns user if Playwright not installed but continues
- **Project reorganization** - Standard Python package structure
  - `src/` directory for source code
  - `docs/` directory for documentation
  - `tests/` directory for future tests
  - `setup.py` for package installation
  - `LICENSE` file (MIT)
  - Proper `.gitignore` with Python best practices
- **Version metadata** - Author, creation date, last updated timestamp
- **Backup system** - Timestamped ZIP backups with UTC timestamps
- Enhanced documentation in README.md and USAGE.md

### Changed
- Reorganized file structure to follow Python packaging standards
- Updated documentation to reflect new directory structure
- Improved error messages and user guidance
- Enhanced `.gitignore` with comprehensive Python exclusions

### Fixed
- JavaScript-rendered pages now properly captured
- Empty content issue with SPA pages resolved

## [1.0] - Initial Release

### Added
- Basic HTML to Markdown conversion
- Static page fetching with requests
- BeautifulSoup HTML parsing
- html2text Markdown conversion
- Title extraction with multiple fallback sources
- Content area detection (main, article, divs)
- Filename sanitization
- Command-line interface with argparse
- Custom output filename option
- Auto-generated filenames from page titles

---

**Author:** Gerasimos Makis Mouzakitis  
**In cooperation with:** GitHub Codespaces, GitHub Copilot Chat, and Claude Sonnet 3.5 Chat Agent
