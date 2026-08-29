"""Strategies for saving image data to different destinations."""

from pathlib import Path
from pdfforge.core.interfaces import IImageSaver
from pdfforge.core.exceptions import ImageSaveError


class LocalImageSaver(IImageSaver):
    """
    Saves image bytes to the local filesystem.

    Creates parent directories if they don't exist.
    """

    def save(self, image_data: bytes, file_path: Path) -> None:
        """
        Write image bytes to the given file path.

        Args:
            image_data: Raw image bytes (PNG, JPEG, etc.).
            file_path: Target path.

        Raises:
            ImageSaveError: If writing fails (permissions, disk full, etc.).
        """
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "wb") as f:
                f.write(image_data)
        except OSError as e:
            raise ImageSaveError(f"Failed to save image to {file_path}: {e}")