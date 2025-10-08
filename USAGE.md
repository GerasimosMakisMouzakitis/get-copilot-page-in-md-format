# Usage Guide

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
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
2. **Extracts** the page title and main content
3. **Converts** HTML to clean markdown format
4. **Removes** unnecessary elements (scripts, styles, navigation)
5. **Preserves** links, images, formatting, lists, and structure
6. **Adds** a header with the page title and source URL
7. **Saves** to a `.md` file

## Output Format

The generated markdown file includes:

```markdown
# Page Title

**Source:** https://original-url.com

---

[Converted page content in markdown format]
```

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
- Maximum filename length is 200 characters
