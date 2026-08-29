"""Core converter that turns PDF pages into images using PyMuPDF."""

from pathlib import Path
from typing import List, Optional
import fitz  # PyMuPDF

from pdfforge.core.interfaces import IOperation, ILogger, IFileNamingStrategy, IImageSaver
from pdfforge.core.exceptions import PdfReadError, ImageSaveError
from pdfforge.core.file_utils import validate_pdf_path
from pdfforge.core.logger import ConsoleLogger
from pdfforge.operations.convert.naming import SequentialFileNamingStrategy
from pdfforge.operations.convert.saver import LocalImageSaver


class PdfToImageConverter(IOperation):
    """
    Operation that converts every page of a PDF to an image file.

    This class follows the Strategy pattern for naming and saving,
    and uses dependency injection for all its collaborators.
    """

    def __init__(
        self,
        naming_strategy: Optional[IFileNamingStrategy] = None,
        image_saver: Optional[IImageSaver] = None,
        logger: Optional[ILogger] = None,
        zoom: float = 2.0,
        image_format: str = "png",
        output_dir_name: str = "images",
    ):
        """
        Initialize the converter with strategies and settings.

        Args:
            naming_strategy: How to name output image files.
            image_saver: How to save image data (local, cloud, etc.).
            logger: Logger for progress and error messages.
            zoom: Scaling factor (e.g., 2.0 = 2x resolution).
            image_format: 'png' or 'jpg'.
            output_dir_name: Subdirectory name relative to PDF's parent.
        """
        self.naming_strategy = naming_strategy or SequentialFileNamingStrategy()
        self.image_saver = image_saver or LocalImageSaver()
        self.logger = logger or ConsoleLogger()
        self.zoom = zoom
        self.image_format = image_format.lower()
        self.output_dir_name = output_dir_name

    def execute(self, pdf_path: Path, **kwargs) -> List[Path]:
        """
        Convert a PDF to images.

        Args:
            pdf_path: Path to the input PDF file.
            **kwargs: Additional parameters (ignored, but kept for interface compatibility).

        Returns:
            List[Path]: Paths to the generated images.

        Raises:
            PdfFileNotFoundError: If the PDF file does not exist.
            PdfReadError: If the PDF cannot be opened.
            ImageSaveError: If saving an image fails.
        """
        pdf_path = Path(pdf_path)
        validate_pdf_path(pdf_path)  # raises if not found

        # Prepare output directory
        output_dir = pdf_path.parent / self.output_dir_name
        output_dir.mkdir(parents=True, exist_ok=True)

        # Open PDF
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            raise PdfReadError(f"Could not open PDF '{pdf_path}': {e}")

        total_pages = len(doc)
        self.logger.info(f"Converting {total_pages} pages from '{pdf_path.name}'")
        saved_files = []

        # Process each page
        for page_num in range(total_pages):
            try:
                page = doc[page_num]
                # Render page with zoom
                mat = fitz.Matrix(self.zoom, self.zoom)
                pix = page.get_pixmap(matrix=mat)

                # Build filename and path
                filename = self.naming_strategy.get_filename(
                    page_number=page_num + 1,
                    total_pages=total_pages,
                    extension=self.image_format,
                )
                file_path = output_dir / filename

                # Save the image via the injected saver
                self.image_saver.save(pix.tobytes(), file_path)
                saved_files.append(file_path)
                self.logger.debug(f"Saved page {page_num+1} → {filename}")

            except Exception as e:
                self.logger.error(f"Failed to convert page {page_num+1}: {e}")
                # Continue with the next page; we don't stop the whole process.
                # Optionally, you could re-raise here if you want to fail fast.

        doc.close()
        self.logger.info(f"Completed. {len(saved_files)} images saved in '{output_dir}'")
        return saved_files