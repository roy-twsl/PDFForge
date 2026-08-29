"""Setup script for PDFForge package."""

from setuptools import setup, find_packages

setup(
    name="pdfforge",
    version="0.1.0",
    description="A comprehensive, extensible PDF toolkit in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/PDFForge",
    packages=find_packages(),
    install_requires=["PyMuPDF", "pypdf"],
    entry_points={
        "console_scripts": [
            "pdfforge = pdfforge.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)