"""Command-line interface for PDFForge."""

import argparse
import sys
from pathlib import Path
from pdfforge.services.pdf_service import PDFService
from pdfforge.core.logger import ConsoleLogger


def main():
    """Entry point for the `pdfforge` CLI command."""
    parser = argparse.ArgumentParser(
        description="PDFForge – master your PDF files."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: convert
    convert_parser = subparsers.add_parser("convert", help="Convert PDF to images")
    convert_parser.add_argument("input", type=str, help="Path to the input PDF file")
    convert_parser.add_argument("--zoom", type=float, default=2.0, help="Zoom factor for image quality")
    convert_parser.add_argument("--format", choices=["png", "jpg"], default="png", help="Output image format")

    # Subcommand: merge (placeholder)
    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs into one")
    merge_parser.add_argument("inputs", nargs="+", help="List of PDF files to merge")
    merge_parser.add_argument("--output", required=True, help="Output merged PDF file path")

    # Parse arguments
    args = parser.parse_args()

    # Create service with a console logger
    logger = ConsoleLogger()
    service = PDFService(logger=logger)

    try:
        if args.command == "convert":
            result = service.convert_to_images(
                pdf_path=Path(args.input),
                zoom=args.zoom,
                output_format=args.format,
            )
            logger.info(f"Successfully generated {len(result)} images.")
            for img_path in result:
                print(f"  - {img_path}")

        elif args.command == "merge":
            # This is a placeholder – we'll implement merge later
            logger.error("Merge operation is not yet implemented.")
            sys.exit(1)

        else:
            logger.error(f"Unknown command: {args.command}")
            sys.exit(1)

    except Exception as e:
        logger.error(f"Command failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()