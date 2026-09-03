# Contributing to PDFForge

Thank you for your interest in contributing to PDFForge.

PDFForge is an open-source Python PDF toolkit designed around modular architecture, clean code, maintainability, and extensibility.

Contributions of all kinds are welcome, including bug fixes, new PDF operations, tests, documentation improvements, and CLI improvements.

Please read this guide before submitting a Pull Request.

---

# Before You Start

Before contributing, please:

1. Read the project README.
2. Understand the existing project structure.
3. Check existing Issues and Pull Requests.
4. Avoid duplicating work that is already in progress.
5. For major changes, open an Issue first to discuss the proposed approach.

---

# Fork the Repository

Fork the PDFForge repository on GitHub:

```text
https://github.com/roy-twsl/PDFForge
```

Then clone your fork:

```bash
git clone https://github.com/YOUR-USERNAME/PDFForge.git
```

Enter the project directory:

```bash
cd PDFForge
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

For development:

```bash
pip install -e .
```

---

# Creating a Branch

Create a separate branch for your change.

For example:

```bash
git checkout -b feature/add-pdf-splitting
```

For bug fixes:

```bash
git checkout -b fix/cli-path-handling
```

For documentation changes:

```bash
git checkout -b docs/update-readme
```

Avoid making unrelated changes in the same branch.

---

# Code Guidelines

PDFForge follows clean and maintainable Python code practices.

## Keep Responsibilities Separate

Each component should have a clear responsibility.

Avoid putting business logic directly into the CLI when that logic belongs in a service or operation.

---

## Follow the Existing Architecture

Before introducing a new architectural pattern or framework, understand how the existing project is structured.

New functionality should integrate with the current architecture rather than creating a parallel implementation.

---

## Use Type Hints

Use type hints for function parameters and return values where practical.

Example:

```python
def convert_file(path: Path, zoom: float = 2.0) -> list[Path]:
    ...
```

---

## Use Meaningful Names

Prefer clear names:

```python
pdf_path
output_format
zoom_level
conversion_result
```

Avoid unclear names:

```python
x
tmp
data2
foo
```

---

## Keep Functions Focused

Functions should perform one clear task whenever possible.

Avoid creating very large functions that handle unrelated responsibilities.

---

## Use Docstrings

Public classes, functions, and methods should have useful docstrings.

Example:

```python
def convert_to_images(
    pdf_path: Path,
    zoom: float = 2.0,
    output_format: str = "png",
) -> list[Path]:
    """Convert PDF pages into image files."""
```

---

# CLI Guidelines

PDFForge provides both an interactive and non-interactive CLI.

When modifying the CLI, make sure the change works correctly in the appropriate mode.

The project uses `Rich` for terminal presentation.

Use the existing style for:

- Tables
- Panels
- Progress indicators
- Colored messages
- Error messages
- Interactive prompts

Do not introduce another terminal UI framework unless there is a strong architectural reason.

---

# Interactive Shell

The interactive shell is started with:

```bash
pdfforge
```

When modifying the interactive shell, verify that the following still work:

```text
help
convert
exit
quit
```

The shell should also handle:

```text
Ctrl+C
```

gracefully.

When testing the shell, also verify:

- Drag & drop paths
- Paths containing spaces
- Quoted paths
- Shell operator characters such as `&`, `|`, and `;`
- Progress display
- Page selection
- Custom output directories

---

# File Paths

PDFForge supports paths containing spaces without requiring quotation marks.

For example:

```bash
pdfforge convert D:/My Documents/Annual Report.pdf
```

Changes to CLI argument parsing must not accidentally break this behavior.

Quoted paths should continue to work as well:

```bash
pdfforge convert "D:/My Documents/Annual Report.pdf"
```

Drag & drop input should also continue to work correctly.

---

# Page Selection

PDFForge supports selecting individual pages, page ranges, and combinations of both.

Examples:

```text
5
20-46
1,3,5-10,20
```

When modifying page selection, verify:

- Single pages work correctly.
- Page ranges work correctly.
- Multiple pages work correctly.
- Mixed page selections work correctly.
- Invalid page selections are handled clearly.
- Pages outside the available PDF range are handled correctly.
- Page selection works in both interactive and non-interactive modes.

---

# Output Directory Handling

PDFForge supports custom output directories through:

```bash
--output-dir
```

For example:

```bash
pdfforge convert document.pdf --output-dir my_output
```

The application also creates unique output directories when an automatically selected directory already exists.

Example:

```text
images/
images_1/
images_2/
```

When modifying output handling, verify that:

- Existing output is not unintentionally overwritten.
- Unique directory names are generated correctly.
- Custom output directories work correctly.
- Paths containing spaces work correctly.
- Page selection works correctly with custom output directories.

---

# Shell Operator Handling

The interactive shell must handle common shell operator characters that can appear in pasted or dragged paths.

Examples include:

```text
&
|
;
```

Changes to command parsing must not cause these characters to unexpectedly split or corrupt valid PDF paths.

Test this behavior using paths that contain spaces and drag & drop input.

---

# Real-time Progress

PDFForge displays real-time conversion progress.

The progress information may include:

- Current page
- Percentage completed
- Elapsed time
- Overall progress

When changing conversion or progress behavior, verify that:

- Progress starts correctly.
- Current page information is updated.
- Percentage completion is correct.
- Elapsed time is displayed.
- Progress reaches completion correctly.
- Errors do not leave the terminal in an unusable state.
- `Ctrl+C` interrupts the operation gracefully.

When many files are generated, PDFForge may limit the number of generated image paths displayed after conversion to keep terminal output readable.

---

# Error Handling

User-facing errors should be handled gracefully.

Avoid exposing unnecessary Python tracebacks to normal CLI users.

For example, a missing PDF should result in a clear message such as:

```text
File not found: document.pdf
```

rather than an unexplained application crash.

Expected error cases include:

- Missing files
- Invalid PDF files
- Invalid page selections
- Pages outside the available range
- Invalid output directories
- Conversion failures
- User interruption

---

# Ctrl+C Handling

When modifying conversion or interactive-shell behavior, test interruption handling.

The application should:

- Handle `Ctrl+C` without an unnecessary traceback.
- Stop the current operation when appropriate.
- Return to a safe state.
- Exit the interactive shell cleanly when `Ctrl+C` is used at the main prompt.

---

# Testing

Before opening a Pull Request, test the functionality you changed.

For CLI changes, test at least:

- Starting the application
- `--help`
- Interactive shell startup
- `help`
- `convert`
- Invalid commands
- Missing files
- Paths containing spaces
- Quoted paths
- Drag & drop paths
- Shell operator handling
- Page selection
- Custom output directories
- Automatic unique output directories
- Progress display
- `Ctrl+C` during interaction
- `Ctrl+C` during conversion
- Non-interactive commands

If you add a new PDF operation, add appropriate automated tests.

Run the test suite with:

```bash
pytest
```

When fixing a bug, preferably add a regression test that reproduces the problem before fixing it.

---

# Adding a New PDF Operation

When adding a new operation:

1. Create the operation in the appropriate package.
2. Follow the existing operation interface and architecture.
3. Keep the implementation focused.
4. Register the operation in the service layer.
5. Add the CLI command if required.
6. Support interactive mode when appropriate.
7. Support non-interactive mode when appropriate.
8. Add tests.
9. Update `README.md`.
10. Update any relevant documentation.

For example, a future PDF splitting feature should not require unrelated existing operations to be rewritten.

---

# Commit Messages

Write clear and meaningful commit messages.

Good:

```text
Add PDF splitting operation
```

```text
Fix CLI handling for paths with spaces
```

```text
Improve interactive shell Ctrl+C handling
```

Avoid vague messages:

```text
update
```

```text
fix
```

```text
changes
```

---

# Pull Requests

Before opening a Pull Request:

1. Make sure your branch contains only relevant changes.
2. Test the changes.
3. Review the modified files.
4. Write a clear Pull Request title.
5. Explain what was changed.
6. Explain why the change was necessary.
7. Mention any limitations or known issues.
8. Respond to reviewer feedback.

A Pull Request should be focused on one feature, bug fix, or related group of changes.

---

# Code Review

All contributions may be reviewed before being merged.

Reviewers may request changes related to:

- Correctness
- Code quality
- Architecture
- Maintainability
- Testing
- Documentation
- CLI usability
- Error handling

If changes are requested, update the branch and push the new commits to the same Pull Request.

---

# Documentation

When adding or changing a user-facing feature, update the documentation.

Documentation should explain:

- What the feature does.
- How to use it.
- Available options.
- Relevant examples.
- Any limitations.

Do not document functionality that does not actually exist yet as an available feature.

Planned features should be clearly marked as planned or under development.

---

# Reporting Bugs

When reporting a bug, provide as much useful information as possible.

Please include:

- A clear description of the problem.
- Steps to reproduce it.
- Expected behavior.
- Actual behavior.
- Operating system.
- Python version.
- PDFForge version or commit.
- Relevant error messages.

If the issue involves a specific PDF file, provide a safe sample PDF when possible.

Do not upload confidential or sensitive documents.

---

# Feature Requests

Feature requests are welcome.

When proposing a new feature, explain:

1. What the feature should do.
2. Why it would be useful.
3. How you expect users to interact with it.
4. Any relevant technical considerations.

For major architectural changes, discuss the idea before starting a large implementation.

---

# Security Issues

Please do not publicly disclose serious security vulnerabilities before they can be properly investigated.

For security-sensitive issues, contact the project maintainer privately when possible.

---

# License

By contributing to PDFForge, you agree that your contributions will be licensed under the same license as the project.

PDFForge is licensed under the:

**GNU General Public License v3.0 (GPL-3.0)**

See the `LICENSE` file for the complete license text.

---

# Project Maintainer

**Roy**

GitHub:

```text
https://github.com/roy-twsl
```

PDFForge repository:

```text
https://github.com/roy-twsl/PDFForge
```

---

# Thank You

Every contribution helps improve PDFForge.

Whether you are fixing a small bug, improving documentation, adding tests, or implementing a completely new PDF operation, your contribution is appreciated.

Thank you for helping build PDFForge.
