# Usage Guide

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

2. **Run the script:**
   ```bash
   python get_copilot_page.py <URL>
   ```

## Examples

### Example 1: Download with auto-generated filename
```bash
python get_copilot_page.py https://github.copilot.example.com/page
```
This will create a file like `GitHub_Copilot_Page_Title.md`

### Example 2: Download with custom filename
```bash
python get_copilot_page.py https://github.copilot.example.com/page -o my_notes.md
```
This will create a file named `my_notes.md`

### Example 3: Make script executable (Linux/Mac)
```bash
chmod +x get_copilot_page.py
./get_copilot_page.py https://github.copilot.example.com/page
```

## What the Script Does

1. **Fetches** the HTML content from the provided URL
2. **Detects** if the page is JavaScript-rendered (SPA) and automatically retries with browser automation
3. **Extracts** the page title and main content
4. **Converts** HTML to clean markdown format
5. **Removes** unnecessary elements (scripts, styles, navigation)
6. **Preserves** links, images, formatting, lists, and structure
7. **Adds** a header with the page title and source URL
8. **Saves** to a `.md` file

## Output Format

The generated markdown file includes:

```markdown
# Page Title

**Source:** https://original-url.com

---

[Converted page content in markdown format]
```

## Important: Pages That May Not Work

This tool works with most public web pages, but some pages cannot be downloaded:

### ✅ Works With:
- **Public web pages** - Blogs, news articles, documentation
- **Static pages** - Regular HTML websites
- **JavaScript-heavy pages** - React, Vue, Angular applications (requires Playwright)
- **Most content sites** - Wikipedia, Medium, GitHub Pages

### ❌ Cannot Download:
- **Login-required pages** - Any page that needs you to sign in first
- **Paywalled content** - Articles or content behind a payment wall
- **Anti-bot sites** - Websites that block automated tools
- **Some secure applications** - Banking sites, private dashboards
- **Interactive-only content** - Content that only loads after specific user actions

**When a page cannot be downloaded, you will see a clear error message explaining the problem.**

## Troubleshooting

### Missing Dependencies
If you get an import error, install the required packages:
```bash
pip install -r requirements.txt
```

### Invalid URL
Make sure the URL includes the protocol (http:// or https://):
- ✅ Good: `https://example.com/page`
- ❌ Bad: `example.com/page`

### Page Cannot Be Downloaded
If you see an error like "Could not extract content", the page may:
- Require login credentials
- Be protected against automated access
- Need specific browser cookies or sessions
- Have anti-scraping measures enabled

**Try with a different public URL to confirm the tool is working correctly.**

### Network Issues
If you can't access the URL, check:
- Your internet connection
- The URL is publicly accessible
- No firewall is blocking the request

## Advanced Usage

### Using with Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the script
python get_copilot_page.py <URL>
```

### Batch Processing Multiple URLs

Create a file `urls.txt` with one URL per line, then:

```bash
while read url; do
  python get_copilot_page.py "$url"
done < urls.txt
```

## Tips

- The script automatically removes navigation, footer, and header elements
- Scripts and styles are stripped from the output
- Links and images are preserved in markdown format
- The filename is sanitized to be filesystem-safe
- JavaScript-rendered pages (SPAs) are automatically detected and handled with browser automation
- For best results with dynamic pages, ensure Playwright and Chromium are installed
- Maximum filename length is 200 characters
