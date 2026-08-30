# PDFForge

> A professional, open-source Python toolkit for working with PDF files.

PDFForge is a modular Python PDF toolkit designed to make common PDF operations simple, reliable, and easy to extend.

The project follows clean software architecture principles, including **Clean Code**, **SOLID principles**, modular design, dependency injection, and design patterns.

---

##  Current Features

| Feature | Status |
|---|---|
| PDF → Images | ✅ Available |
| Interactive CLI | ✅ Available |
| Non-interactive CLI | ✅ Available |
| Paths containing spaces without quotes | ✅ Available |
| Colored terminal output | ✅ Available |
| Progress indicators | ✅ Available |
| Graceful `Ctrl+C` handling | ✅ Available |
| Merge PDFs | 🚧 Planned |
| Split PDFs | 🚧 Planned |
| Extract Text | 🚧 Planned |
| Encrypt / Decrypt PDFs | 🚧 Planned |
| Rotate Pages | 🚧 Planned |
| Compress PDFs | 🚧 Planned |
| Add Watermarks | 🚧 Planned |

More PDF operations will be added as the project evolves.

---

##  Project Goals

PDFForge aims to become a complete and extensible PDF toolkit for Python developers and everyday users.

The main goals of the project are:

- Provide a clean and maintainable PDF processing architecture.
- Make PDF operations accessible through a simple CLI.
- Support both interactive and non-interactive usage.
- Keep individual PDF operations modular and independent.
- Make the project easy for other developers to extend.
- Follow modern Python development practices.
- Provide a foundation for future PDF processing features.

---

##  Design Philosophy

PDFForge is designed around several important principles.

### Modular

Each PDF operation is separated into its own logical component.

### Extensible

New operations can be added without unnecessarily changing existing functionality.

### Testable

The architecture is designed to make individual components easier to test.

### Maintainable

The project follows clean-code principles and attempts to keep responsibilities separated.

### User-Friendly

The CLI provides colored output, tables, panels, progress indicators, and an interactive shell powered by `Rich`.

---

#  Installation

Clone the repository:

```bash
git clone https://github.com/roy-twsl/PDFForge.git
```

Enter the project directory:

```bash
cd PDFForge
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

For development, install the project in editable mode:

```bash
pip install -e .
```

---

#  Usage

PDFForge supports two primary CLI modes:

1. Interactive mode
2. Non-interactive mode

---

## 1. Interactive Mode

Run PDFForge without any arguments:

```bash
pdfforge
```

This starts the PDFForge Interactive Shell.

The shell provides a professional terminal interface with:

- Colored output
- Command tables
- Progress indicators
- Interactive commands
- Error handling
- Graceful interruption

Example:

```text
╔══════════════════════════════════════════════════════════╗
║                       PDFForge                           ║
║                                                          ║
║                  Python PDF Toolkit                      ║
╚══════════════════════════════════════════════════════════╝
```

After starting the shell, commands can be entered directly:

```text
pdfforge> help
```

Convert a PDF:

```text
pdfforge> convert document.pdf --zoom 2.0
```

Convert a PDF using JPG:

```text
pdfforge> convert document.pdf --zoom 2.0 --format jpg
```

Exit the interactive shell:

```text
pdfforge> exit
```

You can also use:

```text
pdfforge> quit
```

or press:

```text
Ctrl+C
```

---

#  Converting PDF Files to Images

PDFForge currently supports converting PDF pages into image files.

Basic usage:

```bash
pdfforge convert document.pdf
```

Specify the zoom level:

```bash
pdfforge convert document.pdf --zoom 2.5
```

Specify the output format:

```bash
pdfforge convert document.pdf --format jpg
```

Both `png` and `jpg` are currently supported.

Example:

```bash
pdfforge convert document.pdf --zoom 2.5 --format png
```

---

#  Paths Containing Spaces

PDFForge supports paths containing spaces without requiring quotation marks.

For example:

```bash
pdfforge convert D:/My Documents/Annual Report.pdf
```

The same functionality is available inside the interactive shell:

```text
pdfforge> convert D:/My Documents/Annual Report.pdf
```

Quoting paths is also supported:

```bash
pdfforge convert "D:/My Documents/Annual Report.pdf"
```

---

#  Non-Interactive Mode

PDFForge can also be used directly from the command line without entering the interactive shell.

Example:

```bash
pdfforge convert document.pdf
```

With custom zoom:

```bash
pdfforge convert document.pdf --zoom 2.0
```

With a different image format:

```bash
pdfforge convert document.pdf --format jpg
```

This mode is useful for scripts, automation, and command-line workflows.

---

#  Help

To display the main help information:

```bash
pdfforge --help
```

Inside the interactive shell:

```text
pdfforge> help
```

The interactive help system displays the available commands, descriptions, and examples.

---

#  Interrupting Operations

PDFForge is designed to handle user interruption gracefully.

Pressing:

```text
Ctrl+C
```

during an interactive session exits the shell cleanly.

If `Ctrl+C` is pressed during a PDF conversion, the conversion is interrupted and the application handles the interruption without producing an unhandled traceback.

---

#  Project Structure

The project is organized into separate layers and components to keep responsibilities isolated.

A simplified structure looks like this:

```text
PDFForge/
│
├── pdfforge/
│   ├── core/
│   ├── services/
│   ├── operations/
│   └── cli.py
│
├── tests/
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
└── pyproject.toml
```

The exact structure may evolve as new PDF operations are added.

---

#  Adding a New PDF Operation

PDFForge is designed to make adding new PDF operations straightforward.

A typical workflow is:

1. Create the new operation inside the appropriate package.
2. Implement the required operation interface.
3. Keep the operation focused on a single responsibility.
4. Register the operation in the appropriate service layer.
5. Add the corresponding CLI command.
6. Support both interactive and non-interactive usage when appropriate.
7. Add tests for the new functionality.
8. Update the documentation.

The goal is to keep new functionality isolated rather than creating unnecessary dependencies between existing components.

---

#  Contributing

Contributions are welcome.

You can contribute by:

- Reporting bugs
- Suggesting new PDF operations
- Improving existing functionality
- Adding tests
- Improving documentation
- Fixing bugs
- Improving CLI usability
- Adding new features

Before making significant changes, please read:

```text
CONTRIBUTING.md
```

---

#  Development Workflow

A typical contribution workflow is:

```bash
git checkout -b feature/my-feature
```

Make your changes, test them, and commit:

```bash
git add .
git commit -m "Add my feature"
```

Push your branch:

```bash
git push -u origin feature/my-feature
```

Then open a Pull Request on GitHub.

For larger changes, please describe what was changed and why.

---

#  Code Quality

When contributing to PDFForge, try to follow these principles:

- Follow PEP 8.
- Use meaningful names.
- Use type hints where appropriate.
- Keep functions small and focused.
- Follow the Single Responsibility Principle.
- Avoid unnecessary duplication.
- Add docstrings to public classes and methods.
- Keep business logic separate from CLI presentation.
- Use the existing architecture instead of introducing unnecessary alternatives.
- Handle errors gracefully.
- Add or update tests when changing functionality.

For CLI-related changes, use the existing `Rich`-based presentation style instead of introducing a different terminal UI framework.

---

#  Testing

Before submitting a Pull Request, contributors should verify that their changes do not break existing functionality.

At minimum, test:

- PDF conversion
- Interactive shell startup
- `help`
- `convert`
- Paths containing spaces
- `Ctrl+C` handling
- Invalid commands
- Invalid input files
- Non-interactive CLI usage

If tests are added or modified, make sure they pass before opening the Pull Request.

---

#  Roadmap

The long-term goal of PDFForge is to provide a complete PDF toolkit.

Planned operations include:

- PDF merging
- PDF splitting
- Text extraction
- PDF encryption
- PDF decryption
- Page rotation
- PDF compression
- Watermarks
- Metadata management
- Additional PDF transformations
- Improved automation support

The roadmap may change as the project develops.

---

#  Contact

**Maintainer:** Roy

**GitHub:** [@roy-twsl](https://github.com/roy-twsl)

**Repository:** [github.com/roy-twsl/PDFForge](https://github.com/roy-twsl/PDFForge)

For bugs, feature requests, and technical discussions, please use the GitHub repository's issue and discussion features.

---

#  License

PDFForge is released under the **GNU General Public License v3.0**.

You are free to:

- Use the software
- Study the source code
- Modify the software
- Distribute copies
- Distribute modified versions

However, when distributing the software or derivative works, the conditions of the GNU GPL v3.0 must be respected.

The original copyright and attribution must not be removed.

See the [`LICENSE`](LICENSE) file for the complete license text.

---

#  Acknowledgements

PDFForge is built with the help of the Python open-source ecosystem.

Special thanks to the projects and communities that make modern PDF processing possible.

---

#  About PDFForge

PDFForge is an open-source project created with the goal of building a powerful, maintainable, and extensible PDF toolkit for Python.

The project is continuously evolving, and new PDF operations and improvements will be introduced over time.

**Built with Python. Built for PDFs. Built for developers.**

---

Copyright © 2026 Roy

Licensed under the GNU General Public License v3.0.
