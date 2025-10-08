"""
Setup configuration for get-copilot-page-in-md-format package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="get-copilot-page-in-md-format",
    version="2.0",
    author="Gerasimos Makis Mouzakitis",
    author_email="",
    description="Download web pages and save them in markdown format with JavaScript rendering support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: Markdown",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "html2text>=2020.1.16",
        "playwright>=1.40.0",
    ],
    entry_points={
        "console_scripts": [
            "get-copilot-page=src.get_copilot_page:main",
        ],
    },
    keywords="markdown html converter web scraping playwright javascript spa",
    project_urls={
        "Bug Reports": "https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format/issues",
        "Source": "https://github.com/GerasimosMakisMouzakitis/get-copilot-page-in-md-format",
    },
)
