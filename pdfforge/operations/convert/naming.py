"""Strategies for generating output image filenames."""

from pdfforge.core.interfaces import IFileNamingStrategy


class SequentialFileNamingStrategy(IFileNamingStrategy):
    """
    Default naming: page_001.png, page_002.png, etc.

    Attributes:
        prefix: String prefix before the page number.
        zero_padding: Number of digits for zero-padding (e.g., 3 → 001).
    """

    def __init__(self, prefix: str = "page", zero_padding: int = 3):
        self.prefix = prefix
        self.zero_padding = zero_padding

    def get_filename(self, page_number: int, total_pages: int, extension: str) -> str:
        """
        Generate a zero-padded filename.

        Args:
            page_number: 1-based page index.
            total_pages: (unused here, kept for interface consistency).
            extension: File extension (e.g., 'png').

        Returns:
            str: e.g., 'page_001.png'
        """
        return f"{self.prefix}_{page_number:0{self.zero_padding}d}.{extension}"