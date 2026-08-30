"""High-level facade for all PDF operations."""

from pathlib import Path
from typing import List, Optional, Callable  # 👈 اضافه شد
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
        output_dir_name: str = "images",
        progress_callback: Optional[Callable[[int, int], None]] = None,  # 👈 اضافه شد
    ) -> List[Path]:
        """
        Convert all pages of a PDF to images.

        Args:
            pdf_path: Path to the input PDF file.
            zoom: Zoom factor (higher = better quality, larger files).
            output_format: Image format ('png' or 'jpg').
            output_dir_name: Name of the output directory (created alongside the PDF).
            progress_callback: Optional callback function(current_page, total_pages).  # 👈 اضافه شد

        Returns:
            List[Path]: List of paths to generated image files.

        Raises:
            PdfFileNotFoundError: If the PDF file does not exist.
            PdfReadError: If the PDF cannot be opened.
            ImageSaveError: If image saving fails.
        """
        converter = PdfToImageConverter(
            naming_strategy=self.naming_strategy,
            image_saver=self.image_saver,
            logger=self.logger,
            zoom=zoom,
            image_format=output_format,
            output_dir_name=output_dir_name,
            progress_callback=progress_callback,  # 👈 ارسال شد
        )
        return converter.execute(pdf_path=pdf_path)

    # Future operations will be added here:
    # def merge_pdfs(self, inputs: List[Path], output: Path) -> Path: ...
    # def split_pdf(self, pdf_path: Path, pages: List[int]) -> List[Path]: ...
    # def extract_text(self, pdf_path: Path) -> str: ...