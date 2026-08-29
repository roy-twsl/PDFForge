"""Basic usage examples for PDFForge."""

from pdfforge.services import PDFService


def main():
    """Demonstrate converting a PDF to images using PDFService."""
    service = PDFService()

    # Convert a PDF to PNG images with custom zoom
    result = service.convert_to_images(
        pdf_path="sample.pdf",
        zoom=2.5,
        output_format="png",
    )
    print(f"Generated {len(result)} images.")


if __name__ == "__main__":
    main()