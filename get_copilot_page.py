#!/usr/bin/env python3
"""
Script to download GitHub Copilot public pages and save them in markdown format.
"""

import argparse
import sys
import re
from urllib.parse import urlparse
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
    import html2text
except ImportError:
    print("Error: Required packages not installed.")
    print("Please run: pip install -r requirements.txt")
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


def fetch_page_content(url):
    """Fetch the HTML content from the given URL."""
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


def save_markdown(content, filename):
    """Save markdown content to a file."""
    try:
        output_path = Path(filename)
        output_path.write_text(content, encoding='utf-8')
        print(f"Successfully saved to: {output_path.absolute()}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False


def main():
    """Main function to handle command-line arguments and orchestrate the process."""
    parser = argparse.ArgumentParser(
        description='Download GitHub Copilot public pages in markdown format.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python get_copilot_page.py https://example.com/copilot-page
  python get_copilot_page.py https://example.com/copilot-page -o custom_name.md
        """
    )
    
    parser.add_argument('url', help='URL of the Copilot public page to download')
    parser.add_argument('-o', '--output', help='Output filename (default: auto-generated from page title)')
    
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
    if save_markdown(markdown_content, output_filename):
        print(f"Page title: {title}")
        print("Conversion completed successfully!")
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
