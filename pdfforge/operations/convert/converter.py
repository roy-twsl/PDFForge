"""Core converter that turns PDF pages into images using PyMuPDF."""

from pathlib import Path
from typing import List, Optional, Callable, Union
import fitz  # PyMuPDF

from pdfforge.core.interfaces import IOperation, ILogger, IFileNamingStrategy, IImageSaver
from pdfforge.core.exceptions import PdfReadError, ImageSaveError
from pdfforge.core.file_utils import validate_pdf_path
from pdfforge.core.logger import ConsoleLogger
from pdfforge.operations.convert.naming import SequentialFileNamingStrategy
from pdfforge.operations.convert.saver import LocalImageSaver


class PdfToImageConverter(IOperation):
    """
    Operation that converts selected pages of a PDF to image files.

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
        progress_callback: Optional[Callable[[int, int], None]] = None,
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
            progress_callback: Optional callback function(current_page, total_pages).
        """
        self.naming_strategy = naming_strategy or SequentialFileNamingStrategy()
        self.image_saver = image_saver or LocalImageSaver()
        self.logger = logger or ConsoleLogger()
        self.zoom = zoom
        self.image_format = image_format.lower()
        self.output_dir_name = output_dir_name
        self.progress_callback = progress_callback

    def execute(
        self,
        pdf_path: Path,
        pages: Optional[Union[int, str, List[int], range]] = None,
        **kwargs
    ) -> List[Path]:
        """
        Convert selected pages of a PDF to images.

        Args:
            pdf_path: Path to the input PDF file.
            pages: Page selection. Can be:
                - None: all pages (default)
                - int: single page number (1-based)
                - str: "1,3,5-10" or "1-5" or "1,3-5,10"
                - List[int]: list of page numbers
                - range: range of page numbers
            **kwargs: Additional parameters (ignored).

        Returns:
            List[Path]: Paths to the generated images.

        Raises:
            PdfFileNotFoundError: If the PDF file does not exist.
            PdfReadError: If the PDF cannot be opened.
            ImageSaveError: If saving an image fails.
            ValueError: If page selection is invalid.
        """
        pdf_path = Path(pdf_path)
        validate_pdf_path(pdf_path)

        # Prepare output directory
        output_dir = pdf_path.parent / self.output_dir_name
        output_dir.mkdir(parents=True, exist_ok=True)

        # Open PDF
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            raise PdfReadError(f"Could not open PDF '{pdf_path}': {e}")

        total_pages = len(doc)

        # Parse page selection
        page_numbers = self._parse_pages(pages, total_pages)

        if not page_numbers:
            self.logger.warning("No pages to convert.")
            doc.close()
            return []

        self.logger.info(
            f"Converting {len(page_numbers)} pages from '{pdf_path.name}' "
            f"(total: {total_pages} pages)"
        )
        saved_files = []

        # Process each selected page
        for idx, page_num in enumerate(page_numbers):
            try:
                # Convert 1-based to 0-based index
                page = doc[page_num - 1]
                mat = fitz.Matrix(self.zoom, self.zoom)
                pix = page.get_pixmap(matrix=mat)

                # Build filename and path
                filename = self.naming_strategy.get_filename(
                    page_number=page_num,
                    total_pages=total_pages,
                    extension=self.image_format,
                )
                file_path = output_dir / filename

                # Save the image
                self.image_saver.save(pix.tobytes(), file_path)
                saved_files.append(file_path)

                # Call progress callback if provided
                if self.progress_callback:
                    self.progress_callback(idx + 1, len(page_numbers))

            except Exception as e:
                self.logger.error(f"Failed to convert page {page_num}: {e}")

        doc.close()
        self.logger.info(
            f"Completed. {len(saved_files)} images saved in '{output_dir}'"
        )
        return saved_files

    def _parse_pages(
        self,
        pages: Optional[Union[int, str, List[int], range]],
        total_pages: int
    ) -> List[int]:
        """
        Parse page selection into a list of page numbers (1-based).

        Args:
            pages: Page selection input.
            total_pages: Total number of pages in the PDF.

        Returns:
            List[int]: List of page numbers (1-based).

        Raises:
            ValueError: If page selection is invalid.
        """
        if pages is None:
            # All pages
            return list(range(1, total_pages + 1))

        if isinstance(pages, int):
            # Single page
            if 1 <= pages <= total_pages:
                return [pages]
            raise ValueError(f"Page {pages} is out of range (1-{total_pages})")

        if isinstance(pages, range):
            # Range object
            return list(pages)

        if isinstance(pages, list):
            # List of integers
            for p in pages:
                if not isinstance(p, int) or not (1 <= p <= total_pages):
                    raise ValueError(f"Page {p} is out of range (1-{total_pages})")
            return sorted(set(pages))

        if isinstance(pages, str):
            # String like "1,3,5-10" or "1-5" or "1,3-5,10"
            return self._parse_pages_string(pages, total_pages)

        raise ValueError(f"Invalid pages type: {type(pages)}")

    def _parse_pages_string(self, pages_str: str, total_pages: int) -> List[int]:
        """
        Parse a string like "1,3,5-10" into a list of page numbers.

        Args:
            pages_str: String with page numbers and ranges.
            total_pages: Total number of pages in the PDF.

        Returns:
            List[int]: List of page numbers (1-based).

        Raises:
            ValueError: If the string format is invalid.
        """
        pages = []
        parts = pages_str.split(',')

        for part in parts:
            part = part.strip()
            if not part:
                continue

            if '-' in part:
                # Range like "5-10"
                try:
                    start, end = part.split('-')
                    start = int(start.strip())
                    end = int(end.strip())

                    if start < 1 or end > total_pages or start > end:
                        raise ValueError(
                            f"Invalid range {start}-{end}. "
                            f"Must be between 1 and {total_pages}"
                        )
                    pages.extend(range(start, end + 1))
                except ValueError as e:
                    raise ValueError(f"Invalid range format: '{part}'. {e}")
            else:
                # Single page like "5"
                try:
                    page = int(part)
                    if page < 1 or page > total_pages:
                        raise ValueError(
                            f"Page {page} is out of range (1-{total_pages})"
                        )
                    pages.append(page)
                except ValueError:
                    raise ValueError(f"Invalid page number: '{part}'")

        # Remove duplicates and sort
        return sorted(set(pages))