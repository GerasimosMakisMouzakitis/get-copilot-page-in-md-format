# Copilot Instructions for get-copilot-page-in-md-format

## Project Overview
Single-file Python CLI tool that fetches web pages and converts them to markdown format using BeautifulSoup, html2text, and Playwright for JavaScript rendering. The script intelligently detects JavaScript-heavy SPAs and automatically retries with browser automation.

## Core Workflow Pattern
The script follows a linear pipeline: **validate URL → fetch HTML → detect SPA → retry with browser if needed → extract title → convert to markdown → save file**. Each function handles one step and returns None/False on failure to enable early exit via `sys.exit(1)`.

## Key Implementation Details

### SPA Detection & Browser Automation
- `is_spa_page()` detects JavaScript-rendered pages by checking text content length (<200 chars) and empty `<div id="app">` or `<div id="root">` containers
- `fetch_with_browser()` uses Playwright's Chromium to render JavaScript, waits for `networkidle` + 2s buffer
- Script gracefully degrades if Playwright not installed—warns user but continues with available content

### Content Extraction Strategy
- `extract_title()` tries 3 fallback sources: `<title>`, `<h1>`, then `<meta property="og:title">`
- `convert_to_markdown()` searches for content in order: `<main>`, `<article>`, divs with class containing "content/main", then falls back to `<body>`
- Navigation, scripts, styles, headers, and footers are removed via `soup.decompose()`

### HTML2Text Configuration
```python
h.body_width = 0  # No text wrapping - preserves original line structure
h.ignore_links = False  # Keep all links
h.skip_internal_links = False  # Include anchor links
```

### Filename Sanitization
`sanitize_filename()` removes filesystem-unsafe chars (`<>:"/\|?*`), replaces whitespace with underscores, truncates to 200 chars. Auto-appends `.md` extension if missing.

## Development Workflow

**Setup:**
```bash
pip install -r requirements.txt
playwright install chromium
```

**Testing changes:**
```bash
python src/get_copilot_page.py <test-url> -o test_output.md

# Or use symlink for backwards compatibility
python get_copilot_page.py <test-url> -o test_output.md
```

**Testing SPA detection:**
```bash
# Test with JavaScript-rendered page (should auto-detect and use browser)
python src/get_copilot_page.py https://copilot.microsoft.com/shares/pages/xyz
```

**Dependencies:** requests (HTTP), beautifulsoup4 (parsing), html2text (conversion), playwright (optional, for JS-rendered pages). Script checks imports and exits with helpful message if missing.

## Project-Specific Conventions

- **Error handling:** Print user-friendly messages, then `sys.exit(1)`. No exceptions bubble to user.
- **User-Agent:** Hardcoded Mozilla string in `fetch_page_content()` to avoid bot blocks
- **Timeout:** 30-second request timeout prevents hanging
- **Shebang:** `#!/usr/bin/env python3` enables direct execution (`chmod +x get_copilot_page.py`)

## File Structure
```
src/
├── __init__.py              # Package initialization
└── get_copilot_page.py      # Main script (all logic in one file)

docs/
├── USAGE.md                 # Extended usage examples
└── SUMMARY.md               # Project summary

tests/                       # Test directory (for future tests)
backup/                      # Version backups with timestamps
.github/
└── copilot-instructions.md  # This file

Root files:
├── setup.py                 # Package configuration
├── requirements.txt         # 4 dependencies with minimum versions
├── LICENSE                  # MIT License
├── MANIFEST.in              # Package manifest
└── README.md                # Main documentation
```

## When Modifying

- Test with various page structures (pages with/without `<main>`, different title locations)
- Ensure filename sanitization handles edge cases (very long titles, special Unicode)
- Maintain backward compatibility—this is a simple tool users rely on as-is
