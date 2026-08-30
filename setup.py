"""Setup script for PDFForge package."""

from setuptools import setup, find_packages

setup(
    name="pdfforge",
    version="1.0.1",
    description="A comprehensive, extensible PDF toolkit in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Roy",
    author_email="your.email@example.com",
    url="https://github.com/roy_twsl/PDFForge",
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