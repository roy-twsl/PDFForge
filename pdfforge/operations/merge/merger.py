"""Placeholder for PDF merge operation."""

from pathlib import Path
from typing import List
from pdfforge.core.interfaces import IOperation


class PdfMerger(IOperation):
    """Merge multiple PDFs into one (not yet implemented)."""

    def execute(self, **kwargs) -> Path:
        raise NotImplementedError("Merge operation is not yet implemented.")