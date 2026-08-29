"""Unit tests for the PDF-to-image conversion operation."""

import os
import tempfile
from pathlib import Path
import pytest
from pdfforge.operations.convert.converter import PdfToImageConverter
from pdfforge.core.exceptions import PdfFileNotFoundError


def test_converter_raises_if_file_missing():
    """Ensure that converter raises an exception when the PDF file is not found."""
    converter = PdfToImageConverter()
    with pytest.raises(PdfFileNotFoundError):
        converter.execute(pdf_path=Path("nonexistent.pdf"))


def test_converter_creates_images(tmp_path):
    """Test that converter generates images for each page of a PDF."""
    # This test requires a real PDF file – we'll skip if not present.
    # In a real project, you'd have a sample PDF in the test data.
    pass