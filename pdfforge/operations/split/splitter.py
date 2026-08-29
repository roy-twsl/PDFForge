"""Placeholder for PDF split operation."""

from pathlib import Path
from typing import List
from pdfforge.core.interfaces import IOperation


class PdfSplitter(IOperation):
    """Split a PDF into multiple files (not yet implemented)."""

    def execute(self, **kwargs) -> List[Path]:
        raise NotImplementedError("Split operation is not yet implemented.")