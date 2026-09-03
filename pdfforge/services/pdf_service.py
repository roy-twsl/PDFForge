"""High-level facade for all PDF operations."""

from pathlib import Path
from typing import List, Optional, Callable, Union
from pdfforge.core.interfaces import ILogger, IFileNamingStrategy, IImageSaver
from pdfforge.core.logger import ConsoleLogger
from pdfforge.operations.convert.converter import PdfToImageConverter
from pdfforge.operations.convert.naming import SequentialFileNamingStrategy
from pdfforge.operations.convert.saver import LocalImageSaver


class PDFService:
    """
    Facade that provides a simple, unified interface for all PDF operations.

    Users interact with this class instead of instantiating individual operations.
    """

    def __init__(
        self,
        logger: Optional[ILogger] = None,
        naming_strategy: Optional[IFileNamingStrategy] = None,
        image_saver: Optional[IImageSaver] = None,
    ):
        """
        Initialize the PDF service with optional dependencies.

        Args:
            logger: Logger implementation (default: ConsoleLogger).
            naming_strategy: Strategy for naming output images (default: Sequential).
            image_saver: Strategy for saving images (default: LocalImageSaver).
        """
        self.logger = logger or ConsoleLogger()
        self.naming_strategy = naming_strategy or SequentialFileNamingStrategy()
        self.image_saver = image_saver or LocalImageSaver()

    def convert_to_images(
        self,
        pdf_path: Path,
        zoom: float = 2.0,
        output_format: str = "png",
        output_dir_name: Optional[str] = None,  # 👈 تغییر: None به معنی خودکار
        pages: Optional[Union[int, str, List[int], range]] = None,
        progress_callback: Optional[Callable[[int, int], None]] = None,
    ) -> List[Path]:
        """
        Convert selected pages of a PDF to images.

        Args:
            pdf_path: Path to the input PDF file.
            zoom: Zoom factor (higher = better quality, larger files).
            output_format: Image format ('png' or 'jpg').
            output_dir_name: Name of the output directory.
                - If None: auto-generate (images, images_1, images_2, ...)
                - If string: use exact name
            pages: Page selection. Can be:
                - None: all pages (default)
                - int: single page number (1-based)
                - str: "1,3,5-10" or "1-5" or "1,3-5,10"
                - List[int]: list of page numbers
                - range: range of page numbers
            progress_callback: Optional callback function(current_page, total_pages).

        Returns:
            List[Path]: List of paths to generated image files.

        Raises:
            PdfFileNotFoundError: If the PDF file does not exist.
            PdfReadError: If the PDF cannot be opened.
            ImageSaveError: If image saving fails.
            ValueError: If page selection is invalid.
        """
        # Auto-generate output directory name if not provided
        if output_dir_name is None:
            output_dir_name = self._get_unique_dir_name(pdf_path.parent)
            self.logger.info(f"Using output directory: '{output_dir_name}'")

        converter = PdfToImageConverter(
            naming_strategy=self.naming_strategy,
            image_saver=self.image_saver,
            logger=self.logger,
            zoom=zoom,
            image_format=output_format,
            output_dir_name=output_dir_name,
            progress_callback=progress_callback,
        )
        return converter.execute(pdf_path=pdf_path, pages=pages)

    def _get_unique_dir_name(self, base_path: Path) -> str:
        """
        Generate a unique directory name like 'images', 'images_1', 'images_2', etc.

        Args:
            base_path: The parent directory where the output folder will be created.

        Returns:
            str: A unique directory name that does not exist yet.
        """
        base_name = "images"
        target = base_path / base_name

        if not target.exists():
            return base_name

        counter = 1
        while True:
            new_name = f"{base_name}_{counter}"
            target = base_path / new_name
            if not target.exists():
                return new_name
            counter += 1

    # Future operations will be added here:
    # def merge_pdfs(self, inputs: List[Path], output: Path) -> Path: ...
    # def split_pdf(self, pdf_path: Path, pages: List[int]) -> List[Path]: ...
    # def extract_text(self, pdf_path: Path) -> str: ...