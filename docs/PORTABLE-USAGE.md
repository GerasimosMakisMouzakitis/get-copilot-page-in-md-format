# Portable Usage Guide

## 🚀 Quick Start: Drop & Use

This tool is **100% portable** - just drop it into any folder and run!

## ⚠️ Important: What This Tool Can Download

### ✅ Works With:
- Public web pages (blogs, articles, documentation)
- Static HTML pages
- JavaScript-rendered pages (React, Vue, Angular)
- Most content sites (Wikipedia, Medium, GitHub Pages)

### ❌ Cannot Download:
- **Login-required pages** - Pages needing authentication
- **Paywalled content** - Content behind subscription walls
- **Anti-bot protected sites** - Sites blocking automated tools
- **Secure applications** - Banking sites, private dashboards
- **Interactive-only content** - Content requiring user clicks/actions

**The tool shows clear error messages when it cannot access a page.**

---

## Method 1: Single File Usage (Simplest)

### Step 1: Download
```bash
# Option A: Download just the main script
curl -O https://raw.githubusercontent.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/main/src/get_copilot_page.py

# Option B: Clone entire repo
git clone https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format.git
```

### Step 2: Install dependencies (one-time)
```bash
pip install requests beautifulsoup4 html2text playwright
playwright install chromium
```

### Step 3: Use from anywhere
```bash
# If you downloaded just the file
python get_copilot_page.py https://example.com

# If you cloned the repo
python src/get_copilot_page.py https://example.com

# Or use the symlink
python get_copilot_page.py https://example.com
```

---

## Method 2: Copy to Your Project

### For Your Application Folder:

```
your-app/
├── your_app.py
├── get_copilot_page.py    ← Copy this file here
└── requirements.txt
```

### Usage in your project:
```python
# your_app.py
import subprocess

# Call as subprocess
result = subprocess.run([
    'python', 'get_copilot_page.py', 
    'https://example.com',
    '-o', 'output.md'
])

# Or import directly
import sys
sys.path.append('.')
from get_copilot_page import fetch_page_content, convert_to_markdown

html = fetch_page_content('https://example.com')
title, markdown = convert_to_markdown(html, 'https://example.com')
```

---

## Method 3: Make it Globally Accessible

### Linux/Mac:
```bash
# Copy to user bin
cp src/get_copilot_page.py ~/.local/bin/get-copilot-page
chmod +x ~/.local/bin/get-copilot-page

# Now use from anywhere:
get-copilot-page https://example.com
```

### Windows:
```powershell
# Copy to a folder in PATH
copy src\get_copilot_page.py C:\Users\YourName\bin\get-copilot-page.py

# Use from anywhere:
python C:\Users\YourName\bin\get-copilot-page.py https://example.com
```

---

## Method 4: As Python Module

### Install in your project:
```bash
# From your project directory
pip install -e /path/to/get-copilot-page-in-md-format
```

### Use in your code:
```python
from src.get_copilot_page import (
    fetch_page_content,
    fetch_with_browser,
    is_spa_page,
    convert_to_markdown
)

# Fetch and convert
html = fetch_page_content('https://example.com')
if is_spa_page(html):
    html = fetch_with_browser('https://example.com')
    
title, markdown = convert_to_markdown(html, 'https://example.com')
print(markdown)
```

---

## Method 5: Docker Container (Ultimate Portability)

### Create Dockerfile:
```dockerfile
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install requests beautifulsoup4 html2text playwright
RUN playwright install --with-deps chromium

# Copy script
COPY src/get_copilot_page.py /app/
WORKDIR /app

ENTRYPOINT ["python", "get_copilot_page.py"]
```

### Build and use:
```bash
docker build -t get-copilot-page .
docker run -v $(pwd):/output get-copilot-page https://example.com -o /output/page.md
```

---

## Method 6: One-Liner (No Installation)

### Linux/Mac:
```bash
curl -s https://raw.githubusercontent.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/main/src/get_copilot_page.py | python - https://example.com
```

### With dependencies check:
```bash
pip install -q requests beautifulsoup4 html2text playwright 2>/dev/null && \
python -c "$(curl -s https://raw.githubusercontent.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/main/src/get_copilot_page.py)" https://example.com
```

---

## Integration Examples

### 1. Bash Script Integration
```bash
#!/bin/bash
# my-script.sh

# Download and convert page
python get_copilot_page.py "$1" -o output.md

# Do something with the markdown
cat output.md | grep "keyword"
```

### 2. Python Script Integration
```python
# my_script.py
import subprocess
import sys

def convert_url_to_markdown(url, output_file):
    """Convert URL to markdown using get_copilot_page.py"""
    result = subprocess.run([
        sys.executable, 
        'get_copilot_page.py',
        url,
        '-o', output_file
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✓ Converted: {url} → {output_file}")
        return True
    else:
        print(f"✗ Error: {result.stderr}")
        return False

# Usage
convert_url_to_markdown('https://example.com', 'page.md')
```

### 3. Node.js Integration
```javascript
// my-script.js
const { exec } = require('child_process');

function convertToMarkdown(url, outputFile) {
    return new Promise((resolve, reject) => {
        exec(`python get_copilot_page.py ${url} -o ${outputFile}`, 
            (error, stdout, stderr) => {
                if (error) {
                    reject(stderr);
                } else {
                    resolve(stdout);
                }
            }
        );
    });
}

// Usage
convertToMarkdown('https://example.com', 'page.md')
    .then(output => console.log('✓ Converted:', output))
    .catch(err => console.error('✗ Error:', err));
```

### 4. GitHub Actions Integration
```yaml
# .github/workflows/convert.yml
name: Convert Pages to Markdown

on: [push]

jobs:
  convert:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      
      - name: Install dependencies
        run: |
          pip install requests beautifulsoup4 html2text playwright
          playwright install chromium
      
      - name: Convert pages
        run: |
          python src/get_copilot_page.py https://example.com -o docs/page.md
```

---

## Minimal Requirements

### What you need:
- ✅ Python 3.6+
- ✅ 4 Python packages (requests, beautifulsoup4, html2text, playwright)
- ✅ Chromium browser (for JavaScript pages)
- ✅ Internet connection

### What you DON'T need:
- ❌ No complex setup
- ❌ No database
- ❌ No web server
- ❌ No configuration files
- ❌ No API keys

---

## Troubleshooting

### Issue: "Module not found"
```bash
# Solution: Install dependencies
pip install requests beautifulsoup4 html2text playwright
```

### Issue: "Playwright browser not found"
```bash
# Solution: Install Chromium
playwright install chromium
```

### Issue: "Permission denied"
```bash
# Solution: Make executable
chmod +x get_copilot_page.py
```

### Issue: Python not in PATH
```bash
# Solution: Use full path
/usr/bin/python3 get_copilot_page.py https://example.com
```

---

## Performance Tips

### 1. Skip browser for static pages
```bash
# Faster for static HTML pages
python get_copilot_page.py https://static-site.com -o output.md
```

### 2. Batch processing
```bash
# Convert multiple pages
for url in $(cat urls.txt); do
    python get_copilot_page.py "$url" -o "$(echo $url | md5).md"
done
```

### 3. Parallel processing
```bash
# Convert multiple pages in parallel
cat urls.txt | xargs -P 4 -I {} python get_copilot_page.py {} -o {}.md
```

---

## Portability Checklist

✅ **Single file** - `src/get_copilot_page.py` is self-contained  
✅ **No configuration** - Works out of the box  
✅ **Cross-platform** - Linux, Mac, Windows  
✅ **No root required** - User-level installation  
✅ **No external services** - All local processing  
✅ **Offline capable** - Once dependencies installed  
✅ **No database** - Stateless operation  
✅ **Standard libraries** - All from PyPI  

---

## Distribution Options

### For End Users:
1. **GitHub Release** - Download binary/script
2. **PyPI Package** - `pip install get-copilot-page`
3. **Docker Image** - `docker pull get-copilot-page`
4. **Snap Package** - `snap install get-copilot-page`

### For Developers:
1. **Git Clone** - Full source access
2. **Direct Download** - Single file
3. **Python Module** - Import in code
4. **API Wrapper** - Call from any language

---

## Quick Reference

```bash
# Basic usage
python get_copilot_page.py <URL>

# Custom output
python get_copilot_page.py <URL> -o output.md

# From Python code
python -c "from get_copilot_page import *; print(fetch_page_content('https://example.com'))"

# Help
python get_copilot_page.py --help
```

---

**Bottom line: It's a simple Python script. Drop it anywhere, install 4 packages, and run!** 🚀

No complex setup. No configuration. Just works.
