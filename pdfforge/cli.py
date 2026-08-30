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
    # Use nargs="*" to accept path parts separately (handles paths with spaces)
    convert_parser.add_argument(
        "input_parts",
        nargs="*",
        help="Path to the input PDF file (supports spaces without quotes)"
    )
    convert_parser.add_argument(
        "--zoom",
        type=float,
        default=2.0,
        help="Zoom factor for image quality (higher = better quality)"
    )
    convert_parser.add_argument(
        "--format",
        choices=["png", "jpg"],
        default="png",
        help="Output image format"
    )

    # Subcommand: merge (placeholder for future implementation)
    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs into one")
    merge_parser.add_argument("inputs", nargs="+", help="List of PDF files to merge")
    merge_parser.add_argument("--output", required=True, help="Output merged PDF file path")

    # Parse command-line arguments
    args = parser.parse_args()

    # Initialize logger and service
    logger = ConsoleLogger()
    service = PDFService(logger=logger)

    try:
        if args.command == "convert":
            # Reconstruct the full path from individual parts
            # This allows users to omit quotes even if the path contains spaces
            if not args.input_parts:
                logger.error("No input file specified.")
                sys.exit(1)

            # If the user used quotes, the entire path is a single element
            if len(args.input_parts) == 1:
                raw_path = args.input_parts[0]
            else:
                # Otherwise, join all parts with spaces to reconstruct the full path
                raw_path = " ".join(args.input_parts)

            # Convert to absolute Path object
            pdf_path = Path(raw_path).resolve()

            # Execute the conversion
            result = service.convert_to_images(
                pdf_path=pdf_path,
                zoom=args.zoom,
                output_format=args.format,
            )

            logger.info(f"Successfully generated {len(result)} images.")
            for img_path in result:
                print(f"  - {img_path}")

        elif args.command == "merge":
            # Placeholder: merge functionality is not yet implemented
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