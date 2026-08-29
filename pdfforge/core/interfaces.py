"""Core interfaces (abstractions) for the PDFForge framework."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional


class IOperation(ABC):
    """Interface for any PDF operation (convert, merge, split, etc.)."""

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Execute the operation with given parameters.

        Args:
            **kwargs: Operation-specific parameters (e.g., pdf_path, zoom).

        Returns:
            Any: Result of the operation (e.g., list of image paths).
        """
        pass


class ILogger(ABC):
    """Abstract logger interface for consistent logging across the project."""

    @abstractmethod
    def info(self, message: str) -> None:
        """Log an info-level message."""
        pass

    @abstractmethod
    def debug(self, message: str) -> None:
        """Log a debug-level message."""
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        """Log an error-level message."""
        pass


class IFileNamingStrategy(ABC):
    """Strategy for generating output filenames (e.g., page_001.png)."""

    @abstractmethod
    def get_filename(self, page_number: int, total_pages: int, extension: str) -> str:
        """
        Return the filename for a given page.

        Args:
            page_number: 1-based page index.
            total_pages: Total number of pages in the PDF.
            extension: File extension (e.g., 'png', 'jpg').

        Returns:
            str: The filename without path.
        """
        pass


class IImageSaver(ABC):
    """Strategy for saving image data to a destination."""

    @abstractmethod
    def save(self, image_data: bytes, file_path: Path) -> None:
        """
        Save image bytes to the given file path.

        Args:
            image_data: Raw image bytes (e.g., PNG or JPEG data).
            file_path: Target path (directory will be created if missing).
        """
        pass