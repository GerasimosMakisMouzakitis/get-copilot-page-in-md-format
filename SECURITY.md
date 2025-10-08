# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

We take the security of `get-copilot-page-in-md-format` seriously. If you discover a security vulnerability, please follow these steps:

### 1. **Do Not** Open a Public Issue

Please do not report security vulnerabilities through public GitHub issues. This helps prevent exploitation while we work on a fix.

### 2. Report Privately

Report the vulnerability by:

- **Opening a GitHub Security Advisory** (preferred)
  - Go to the [Security tab](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/security)
  - Click "Report a vulnerability"
  
- **Or email the maintainer** with details about the vulnerability

### 3. Include These Details

Please include as much of the following information as possible:

- **Type of vulnerability** (e.g., XSS, code injection, path traversal)
- **Affected component** (e.g., file sanitization, URL handling, browser automation)
- **Step-by-step reproduction** - How to trigger the vulnerability
- **Impact assessment** - What could an attacker do?
- **Suggested fix** (if you have one)
- **Proof of concept** (if applicable)

### Example Security Report

```markdown
**Type:** Path Traversal Vulnerability

**Component:** Filename sanitization in sanitize_filename()

**Reproduction:**
1. Run: python src/get_copilot_page.py https://malicious-site.com
2. Site returns title containing: "../../../etc/passwd"
3. File is saved outside intended directory

**Impact:** 
Attacker could overwrite arbitrary files on the user's system

**Suggested Fix:**
Use os.path.basename() after sanitization to prevent directory traversal

**Proof of Concept:**
See attached script: poc_path_traversal.py
```

## Response Timeline

- **Initial Response:** Within 48 hours
- **Confirmation & Assessment:** Within 5 business days
- **Fix Development:** Varies by severity
- **Patch Release:** As soon as fix is tested and verified

## Security Considerations

### What We Protect Against

- **Code injection** - Malicious code execution through user input
- **Path traversal** - File system access outside intended directories
- **XSS in output** - Cross-site scripting in generated markdown
- **Command injection** - Shell command injection through URLs
- **Dependency vulnerabilities** - Known CVEs in dependencies

### Known Limitations

This tool fetches and processes web content. Users should be aware:

#### 1. **Not All Pages Can Be Downloaded**

The tool works with most public web pages, but **cannot download**:
- **Login-required pages** - Pages that need authentication
- **Paywalled content** - Content behind subscription walls
- **Anti-bot protected sites** - Sites that block automated tools
- **Secure web applications** - Banking sites, private dashboards
- **Content requiring user interaction** - Pages that need clicks, scrolling, or form submission

**The tool will show a clear error message when it cannot access a page.**

#### 2. **Fetching Untrusted URLs**

The tool fetches arbitrary web pages:
- Use caution with untrusted or suspicious URLs
- Downloaded content is saved to your local filesystem
- Malicious sites could return harmful content
   
#### 3. **Playwright Browser Automation**

When JavaScript rendering is enabled, the tool executes JavaScript from web pages:
- Only use with trusted URLs
- The browser runs in a sandboxed environment, but still processes remote code
- Malicious JavaScript could potentially exploit browser vulnerabilities
   
#### 4. **Markdown Output Security**

Generated markdown may contain potentially unsafe content:
- Always review the output before using it in production
- Sanitize content before rendering in web applications
- Links in the output point to external sites (could be malicious)

### Safe Usage Guidelines

✅ **Safe:**
```bash
# Trusted, well-known sites
python src/get_copilot_page.py https://docs.python.org/

# With output verification
python src/get_copilot_page.py https://example.com -o output.md
cat output.md  # Review before using
```

⚠️ **Use with caution:**
```bash
# Unknown/untrusted sites
python src/get_copilot_page.py https://random-site.example/

# User-provided URLs in scripts
python src/get_copilot_page.py "$USER_URL"
```

🚫 **Avoid:**
```bash
# Running with elevated privileges
sudo python src/get_copilot_page.py ...

# Batch processing untrusted URLs without review
for url in untrusted_urls.txt; do
  python src/get_copilot_page.py "$url"
done
```

## Security Updates

Security patches will be released as:

1. **Critical vulnerabilities** - Emergency patch release
2. **High severity** - Patch within 7 days
3. **Medium/Low severity** - Included in next regular release

Users will be notified via:
- GitHub Security Advisories
- Release notes (CHANGELOG.md)
- README.md notice (for critical issues)

## Dependency Security

We monitor dependencies for known vulnerabilities:

- **requests** - HTTP library
- **beautifulsoup4** - HTML parsing
- **html2text** - Markdown conversion
- **playwright** - Browser automation (optional)

To check for vulnerable dependencies:

```bash
pip install safety
safety check -r requirements.txt
```

## Disclosure Policy

When a security issue is resolved:

1. **Fix is merged** to main branch
2. **New version is released** with security patch
3. **Security advisory is published** with details
4. **Credit given** to reporter (if desired)

We follow **responsible disclosure** principles:
- 90-day disclosure timeline
- Public disclosure only after fix is available
- Credit to security researchers

## Bug Bounty

We currently do not offer a bug bounty program. However, security researchers who responsibly disclose vulnerabilities will be:

- **Credited** in release notes
- **Thanked** publicly (if desired)
- **Listed** in a future SECURITY_CREDITS.md file

## Questions?

For security questions or concerns, please:
- Open a [Security Advisory](https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/security)
- Contact the maintainer directly

---

**Last Updated:** October 8, 2025
