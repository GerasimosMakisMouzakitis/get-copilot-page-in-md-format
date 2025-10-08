# get-copilot-page-in-md-format

A simple Python tool to download GitHub Copilot public pages and save them in markdown format.

## Features

- Download any public Copilot page using its URL
- Automatically converts HTML content to clean markdown
- Preserves page structure, links, and formatting
- Auto-generates filename from page title or use custom output name
- Includes source URL in the output for reference

## Installation

1. Clone this repository:
```bash
git clone https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format.git
cd get-copilot-page-in-md-format
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Download a Copilot public page (filename auto-generated from page title):
```bash
python get_copilot_page.py <URL>
```

### Custom Output Filename

Specify a custom output filename:
```bash
python get_copilot_page.py <URL> -o my_page.md
```

### Examples

```bash
# Download with auto-generated filename
python get_copilot_page.py https://example.com/copilot-page

# Download with custom filename
python get_copilot_page.py https://example.com/copilot-page -o copilot_tutorial.md
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

## Output Format

The generated markdown file includes:
- Page title as the main heading
- Source URL for reference
- Full page content converted to markdown format
- Preserved formatting, links, and structure

## License

MIT License

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.