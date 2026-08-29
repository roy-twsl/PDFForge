"""Placeholder for text extraction operation."""

from pdfforge.core.interfaces import IOperation


class TextExtractor(IOperation):
    """Extract text from a PDF (not yet implemented)."""

    def execute(self, **kwargs) -> str:
        raise NotImplementedError("Text extraction is not yet implemented.")