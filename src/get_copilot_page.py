#!/usr/bin/env python3
"""
Script to download web pages and save them in markdown format.

Author: Gerasimos Makis Mouzakitis
In cooperation with: GitHub Codespaces, GitHub Copilot Chat, and Claude Sonnet 3.5 Chat Agent
Created: October 8, 2025 (UTC)
Last Updated: October 8, 2025 (UTC)
Version: 2.0 - Added JavaScript rendering support with Playwright
"""

import argparse
import sys
import re
from urllib.parse import urlparse
from pathlib import Path

__version__ = "2.0"
__author__ = "Gerasimos Makis Mouzakitis"
__created__ = "2025-10-08 UTC"
__updated__ = "2025-10-08 UTC"

try:
    import requests
    from bs4 import BeautifulSoup
    import html2text
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError as e:
    if "playwright" in str(e):
        PLAYWRIGHT_AVAILABLE = False
        import requests
        from bs4 import BeautifulSoup
        import html2text
    else:
        print("Error: Required packages not installed.")
        print("Please run: pip install -r requirements.txt")
        print("For JavaScript-rendered pages, also run: playwright install chromium")
        sys.exit(1)


def is_valid_url(url):
    """Validate if the provided string is a valid URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def sanitize_filename(title):
    """Convert title to a safe filename."""
    # Remove or replace characters that are unsafe for filenames
    filename = re.sub(r'[<>:"/\\|?*]', '', title)
    filename = re.sub(r'\s+', '_', filename)
    filename = filename.strip('._')
    return filename[:200] if filename else "copilot_page"


def fetch_page_content(url, use_browser=False):
    """Fetch the HTML content from the given URL."""
    if use_browser and PLAYWRIGHT_AVAILABLE:
        return fetch_with_browser(url)
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None


def fetch_with_browser(url):
    """Fetch page content using Playwright for JavaScript-rendered pages."""
    try:
        print("Using browser to render JavaScript content...")
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=30000)
            # Wait a bit for any dynamic content to load
            page.wait_for_timeout(2000)
            content = page.content()
            browser.close()
            return content
    except Exception as e:
        print(f"Error fetching with browser: {e}")
        print("Note: Make sure Playwright browsers are installed: playwright install chromium")
        return None


def is_spa_page(html_content):
    """Detect if a page is likely a JavaScript-rendered SPA with minimal content."""
    if not html_content:
        return False
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements for content check
    for script in soup(["script", "style", "noscript"]):
        script.decompose()
    
    # Get text content
    text_content = soup.get_text(strip=True)
    
    # If very little text content (less than 200 chars), likely an SPA
    if len(text_content) < 200:
        return True
    
    # Check for common SPA indicators
    if soup.find('div', id='app') or soup.find('div', id='root'):
        # If these divs are empty or nearly empty, it's likely an SPA
        app_div = soup.find('div', id='app') or soup.find('div', id='root')
        if app_div and len(app_div.get_text(strip=True)) < 100:
            return True
    
    return False


def extract_title(soup):
    """Extract the page title from the HTML."""
    # Try to find title in various common locations
    title = None
    
    # Try <title> tag first
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    
    # Try h1 tag
    if not title:
        h1 = soup.find('h1')
        if h1:
            title = h1.get_text().strip()
    
    # Try meta title
    if not title:
        meta_title = soup.find('meta', property='og:title')
        if meta_title and meta_title.get('content'):
            title = meta_title['content'].strip()
    
    return title or "Copilot Page"


def convert_to_markdown(html_content, url):
    """Convert HTML content to markdown format."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title
    title = extract_title(soup)
    
    # Remove script and style elements
    for script in soup(["script", "style", "nav", "footer", "header"]):
        script.decompose()
    
    # Get the main content
    # Try to find main content area
    main_content = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile('content|main', re.I)) or soup.body or soup
    
    # Convert to markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap text
    h.skip_internal_links = False
    
    markdown_content = h.handle(str(main_content))
    
    # Add header with source URL
    header = f"# {title}\n\n"
    header += f"**Source:** {url}\n\n"
    header += "---\n\n"
    
    return title, header + markdown_content


def save_markdown(content, filename, output_dir="downloads"):
    """
    Save markdown content to a file in the specified output directory.
    
    Args:
        content: Markdown content to save
        filename: Name of the output file
        output_dir: Directory to save the file (default: "downloads")
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create output directory if it doesn't exist
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Create full file path
        file_path = output_path / filename
        
        # Save the file
        file_path.write_text(content, encoding='utf-8')
        print(f"Successfully saved to: {file_path.absolute()}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False


def main():
    """Main function to handle command-line arguments and orchestrate the process."""
    parser = argparse.ArgumentParser(
        description=f'Download web pages in markdown format (v{__version__}).\n\n'
                    f'Author: {__author__}\n'
                    f'Created: {__created__}\n'
                    f'In cooperation with: GitHub Codespaces, GitHub Copilot Chat, and Claude Sonnet 3.5 Chat Agent',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python get_copilot_page.py https://example.com/page
  python get_copilot_page.py https://example.com/page -o custom_name.md
  python get_copilot_page.py https://example.com/page -d my_downloads/
  python get_copilot_page.py https://copilot.microsoft.com/shares/pages/xyz
  
Downloaded files are saved to the 'downloads/' folder by default.
        """
    )
    
    parser.add_argument('url', help='URL of the web page to download')
    parser.add_argument('-o', '--output', help='Output filename (default: auto-generated from page title)')
    parser.add_argument('-d', '--dir', '--output-dir', dest='output_dir', 
                        default='downloads',
                        help='Output directory for downloaded files (default: downloads/)')
    
    args = parser.parse_args()
    
    # Validate URL
    if not is_valid_url(args.url):
        print(f"Error: Invalid URL provided: {args.url}")
        sys.exit(1)
    
    print(f"Fetching page from: {args.url}")
    
    # Fetch the page content
    html_content = fetch_page_content(args.url)
    if not html_content:
        sys.exit(1)
    
    # Check if it's a JavaScript-rendered SPA
    if is_spa_page(html_content):
        print("Detected JavaScript-rendered page (SPA)...")
        if PLAYWRIGHT_AVAILABLE:
            print("Retrying with browser automation...")
            html_content = fetch_with_browser(args.url)
            if not html_content:
                sys.exit(1)
        else:
            print("\nWarning: This appears to be a JavaScript-rendered page.")
            print("Install Playwright for better support:")
            print("  pip install playwright")
            print("  playwright install chromium")
            print("\nAttempting to convert available content...\n")
    
    print("Converting to markdown...")
    
    # Convert to markdown
    title, markdown_content = convert_to_markdown(html_content, args.url)
    
    # Determine output filename
    if args.output:
        output_filename = args.output
    else:
        safe_title = sanitize_filename(title)
        output_filename = f"{safe_title}.md"
    
    # Ensure .md extension
    if not output_filename.endswith('.md'):
        output_filename += '.md'
    
    # Save to file
    if save_markdown(markdown_content, output_filename, args.output_dir):
        print(f"Page title: {title}")
        print("Conversion completed successfully!")
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
