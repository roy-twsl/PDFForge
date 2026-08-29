"""
PDFForge – A modular, extensible PDF toolkit.

This package provides a clean facade (PDFService) for all PDF operations.
"""

from pdfforge.services.pdf_service import PDFService
from pdfforge.core.exceptions import (
    PdfConversionError,
    PdfFileNotFoundError,
    PdfReadError,
    ImageSaveError,
)

__version__ = "0.1.0"
__all__ = [
    "PDFService",
    "PdfConversionError",
    "PdfFileNotFoundError",
    "PdfReadError",
    "ImageSaveError",
]