# Contributing to get-copilot-page-in-md-format

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 Ways to Contribute

- **Report bugs** - Found a bug? Open an issue with details
- **Suggest features** - Have an idea? Share it in an issue
- **Fix issues** - Pick an existing issue and submit a PR
- **Improve documentation** - Help make the docs clearer
- **Share the project** - Star ⭐ and share with others

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Clear title** - Summarize the issue
2. **Steps to reproduce** - How to trigger the bug
3. **Expected behavior** - What should happen
4. **Actual behavior** - What actually happens
5. **Environment** - OS, Python version, dependencies
6. **Error messages** - Full stack trace if applicable

### Example Bug Report

```markdown
**Title:** SPA detection fails for React apps with lazy loading

**Steps to reproduce:**
1. Run: `python src/get_copilot_page.py https://example.com/react-app`
2. Page uses React with lazy loading

**Expected:** Should detect SPA and use browser
**Actual:** Uses static fetch, returns empty content

**Environment:**
- OS: Ubuntu 22.04
- Python: 3.10.12
- Playwright: 1.40.0

**Error:** No error, but output file is nearly empty
```

## 💡 Suggesting Features

Feature requests are welcome! Please:

1. **Check existing issues** - Avoid duplicates
2. **Explain the use case** - Why is this needed?
3. **Provide examples** - Show how it would work
4. **Consider alternatives** - Are there workarounds?

## 🔧 Development Setup

### 1. Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/get-copilot-page-in-md-format.git
cd get-copilot-page-in-md-format
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## 📝 Coding Standards

### Style Guidelines

- Follow **PEP 8** Python style guide
- Use **4 spaces** for indentation (not tabs)
- **Maximum line length:** 100 characters
- Use **descriptive variable names**
- Add **docstrings** for functions
- Keep functions **focused and single-purpose**

### Example Function Style

```python
def extract_title(soup):
    """
    Extract page title from HTML using multiple fallback methods.
    
    Args:
        soup: BeautifulSoup object of the parsed HTML
        
    Returns:
        str: Extracted title or None if no title found
    """
    # Try <title> tag first
    title_tag = soup.find('title')
    if title_tag and title_tag.string:
        return title_tag.string.strip()
    
    # Fallback to <h1>
    h1_tag = soup.find('h1')
    if h1_tag:
        return h1_tag.get_text(strip=True)
    
    return None
```

### Testing Your Changes

```bash
# Test with various URLs
python src/get_copilot_page.py https://example.com -o test_output.md

# Test SPA detection
python src/get_copilot_page.py https://copilot.microsoft.com/shares/pages/xyz

# Test error handling
python src/get_copilot_page.py invalid-url
```

## 🚀 Submitting Pull Requests

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] All tests pass (if applicable)
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

### PR Guidelines

1. **Clear title** - Summarize the change
2. **Description** - Explain what and why
3. **Link issues** - Reference related issues
4. **Screenshots** - If UI/output changes
5. **Breaking changes** - Highlight if any

### Example PR Description

```markdown
## What

Add support for custom User-Agent strings

## Why

Some websites block the default User-Agent. This allows users to specify a custom one.

## How

- Added `--user-agent` CLI argument
- Updated `fetch_page_content()` to accept custom UA
- Added documentation to README.md

## Testing

Tested with:
- Default User-Agent (existing behavior)
- Custom User-Agent on sites that block bots
- Invalid User-Agent (error handling)

Closes #42
```

## 🔍 Code Review Process

1. **Automated checks** - GitHub Actions will run (if configured)
2. **Maintainer review** - Code will be reviewed for quality
3. **Feedback** - Changes may be requested
4. **Merge** - Once approved, PR will be merged

## 📜 Commit Message Guidelines

Use clear, descriptive commit messages:

```bash
# Good commit messages
git commit -m "Add custom User-Agent support"
git commit -m "Fix SPA detection for lazy-loaded React apps"
git commit -m "Update documentation for browser automation"

# Bad commit messages
git commit -m "fix bug"
git commit -m "update"
git commit -m "asdf"
```

### Commit Message Format

```
<type>: <short summary>

<optional detailed description>

<optional footer>
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code formatting (no logic change)
- `refactor:` Code restructuring (no behavior change)
- `test:` Adding/updating tests
- `chore:` Maintenance tasks

## 🤝 Community Guidelines

- **Be respectful** - Treat everyone with kindness
- **Be patient** - Maintainers are volunteers
- **Be constructive** - Offer solutions, not just criticism
- **Be inclusive** - Welcome contributors of all levels

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for our full community guidelines.

## 📞 Getting Help

- **Issues** - Open an issue for questions
- **Discussions** - Start a discussion for general topics
- **Email** - Contact the maintainer for private matters

## 🙏 Recognition

All contributors will be recognized in the project. Thank you for making this project better!

---

**Ready to contribute?** Pick an issue labeled `good-first-issue` or `help-wanted` to get started! 🚀
