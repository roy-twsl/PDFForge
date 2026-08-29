"""Custom exceptions for PDFForge operations."""


class PdfConversionError(Exception):
    """Base exception for all PDF conversion/processing errors."""
    pass


class PdfFileNotFoundError(PdfConversionError):
    """Raised when the specified PDF file does not exist."""
    pass


class PdfReadError(PdfConversionError):
    """Raised when the PDF cannot be opened or read."""
    pass


class ImageSaveError(PdfConversionError):
    """Raised when an image cannot be saved to disk."""
    pass


class UnsupportedFormatError(PdfConversionError):
    """Raised when an unsupported output format is requested."""
    pass