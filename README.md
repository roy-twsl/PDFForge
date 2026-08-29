# PDFForge

> A modular and extensible Python toolkit for working with PDF files.

PDFForge is a Python-based PDF toolkit designed to provide a clean, maintainable, and extensible architecture for common PDF operations.

The project is built with a focus on **clean code, separation of concerns, SOLID principles, dependency injection, and reusable design patterns**, making it easier to add new PDF operations without unnecessarily changing the existing architecture.

---

## Features

PDFForge is actively under development.

### Currently Available

* PDF to image conversion
* PNG and JPEG output
* Configurable image quality
* Configurable output filenames
* Extensible image-saving strategies
* Console logging
* Custom exception handling
* Command-line interface

### Planned

* PDF merging
* PDF splitting
* Text extraction
* PDF encryption and decryption
* Page rotation
* PDF compression
* Watermarking
* Metadata management
* Additional PDF utilities

> Features marked as planned may change as the project evolves.

---

## Architecture

PDFForge is organized into separate layers to keep the codebase maintainable and extensible.

```text
PDFForge/
│
├── pdfforge/
│   ├── core/
│   │   ├── exceptions.py
│   │   ├── file_utils.py
│   │   ├── interfaces.py
│   │   └── logger.py
│   │
│   ├── operations/
│   │   ├── convert/
│   │   ├── merge/
│   │   ├── split/
│   │   └── extract_text/
│   │
│   ├── services/
│   │   └── pdf_service.py
│   │
│   ├── cli.py
│   └── __init__.py
│
├── examples/
├── tests/
│
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
├── pyproject.toml
└── setup.py
```

The architecture separates:

* **Core abstractions** — interfaces, exceptions, logging, and utilities
* **Operations** — individual PDF operations
* **Services** — high-level APIs for interacting with PDFForge
* **CLI** — command-line access
* **Tests** — automated testing
* **Examples** — practical usage examples

---

## Installation

### Clone the repository

```bash
git clone https://github.com/roy-twsl/PDFForge.git
```

```bash
cd PDFForge
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install PDFForge in editable mode

```bash
pip install -e .
```

---

## Requirements

* Python 3.8 or newer
* PyMuPDF
* pypdf
* pytest for development and testing

---

## Quick Start

### Convert a PDF to images

```python
from pathlib import Path
from pdfforge.services.pdf_service import PDFService

service = PDFService()

images = service.convert_to_images(
    pdf_path=Path("document.pdf"),
    zoom=2.0,
    output_format="png",
)

for image in images:
    print(image)
```

The generated images will be stored in the configured output directory.

---

## Command Line Usage

PDFForge also provides a command-line interface.

### Convert a PDF

```bash
pdfforge convert document.pdf
```

### Set image quality

```bash
pdfforge convert document.pdf --zoom 2.5
```

### Generate JPEG images

```bash
pdfforge convert document.pdf --format jpg
```

Additional commands will be introduced as more PDF operations are implemented.

---

## Design Principles

PDFForge follows several software engineering principles.

### Modularity

Each PDF operation is isolated from other operations so that functionality can be developed independently.

### Extensibility

New operations can be added without significantly modifying existing components.

### Separation of Concerns

Responsibilities are divided between core components, operations, services, and the command-line interface.

### Dependency Injection

Components such as loggers, naming strategies, and image savers can be replaced without modifying the core operation.

### Strategy Pattern

Several behaviors are implemented through interchangeable strategies, making the system easier to customize.

### Testability

The architecture is designed to make individual components easier to test independently.

---

## Adding a New Operation

A new PDF operation should generally:

1. Be placed inside the appropriate directory under `pdfforge/operations/`.
2. Implement the `IOperation` interface when appropriate.
3. Keep its responsibilities focused.
4. Use dependency injection where useful.
5. Provide appropriate error handling.
6. Include automated tests.
7. Be exposed through `PDFService` when it is intended to be part of the public API.
8. Include CLI support when appropriate.
9. Update the documentation.

---

## Testing

Run the test suite with:

```bash
pytest
```

Before submitting a Pull Request, make sure the existing tests pass and add tests for new functionality whenever appropriate.

---

## Contributing

Contributions are welcome.

You can contribute by:

* Reporting bugs
* Suggesting new features
* Improving documentation
* Improving tests
* Fixing bugs
* Implementing new PDF operations
* Improving the architecture
* Reviewing Pull Requests

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a contribution.

---

## Development Workflow

A typical contribution workflow is:

```text
Fork
  ↓
Clone
  ↓
Create a branch
  ↓
Make changes
  ↓
Run tests
  ↓
Commit
  ↓
Push
  ↓
Open Pull Request
  ↓
Code Review
  ↓
Merge
```

Please keep Pull Requests focused and avoid combining unrelated changes into a single contribution.

---

## Project Status

PDFForge is an evolving open-source project.

The current implementation focuses on establishing a clean foundation for a larger PDF processing toolkit.

APIs and project structure may change as the project develops.

---

## License

PDFForge is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

This means you are free to:

* Use the software
* Study the source code
* Modify the software
* Copy the software
* Share the software
* Distribute modified versions

When distributing the software or derivative works, the terms of the GPLv3 must be followed, including applicable requirements to preserve the license and provide corresponding source code.

See the [LICENSE](LICENSE) file for the complete license text.

---

## Copyright

Copyright © 2026 Roy / PDFForge Contributors

The source code remains protected by copyright. The GPLv3 license grants users specific freedoms while preserving the copyright and licensing conditions of the project.

---

## Acknowledgements

PDFForge uses and builds upon excellent open-source projects, including:

* [PyMuPDF](https://pymupdf.readthedocs.io/)
* [pypdf](https://pypdf.readthedocs.io/)

Thanks to the maintainers and contributors of these projects and to the broader open-source community.

---

## Repository

**GitHub:**
https://github.com/roy-twsl/PDFForge

---

## Contact

For bugs, feature requests, discussions, and contributions, please use the GitHub repository's issue and discussion features.

---

**PDFForge — Build, process, and master your PDFs with Python.**
