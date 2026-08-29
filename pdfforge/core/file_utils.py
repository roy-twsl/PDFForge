"""File and path utility functions."""

from pathlib import Path
from pdfforge.core.exceptions import PdfFileNotFoundError


def validate_pdf_path(pdf_path: Path) -> None:
    """
    Check that the given path exists and is a valid PDF file.

    Args:
        pdf_path: Path object pointing to a PDF file.

    Raises:
        PdfFileNotFoundError: If the file does not exist.
    """
    if not pdf_path.exists():
        raise PdfFileNotFoundError(f"PDF file not found: {pdf_path}")
    # Optionally check file extension or magic bytes here.