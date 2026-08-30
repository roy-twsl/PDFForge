# Contributing to PDFForge

Thank you for your interest in contributing to PDFForge.

PDFForge is an open-source Python PDF toolkit designed around modular architecture, clean code, maintainability, and extensibility.

Contributions of all kinds are welcome, including bug fixes, new PDF operations, tests, documentation improvements, and CLI improvements.

---

#  Before You Start

Before contributing, please:

1. Read the project README.
2. Understand the existing project structure.
3. Check existing Issues and Pull Requests.
4. Avoid duplicating work that is already in progress.
5. For major changes, open an Issue first to discuss the proposed approach.

---

#  Fork the Repository

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

#  Creating a Branch

Create a separate branch for your change.

For example:

```bash
git checkout -b feature/add-pdf-splitting
```

For bug fixes:

```bash
git checkout -b fix/cli-path-handling
```

Avoid making unrelated changes in the same branch.

---

#  Code Guidelines

PDFForge follows clean and maintainable Python code practices.

## 1. Keep Responsibilities Separate

Each component should have a clear responsibility.

Avoid putting business logic directly into the CLI when that logic belongs in a service or operation.

---

## 2. Follow the Existing Architecture

Before introducing a new architectural pattern or framework, understand how the existing project is structured.

New functionality should integrate with the current architecture rather than creating a parallel implementation.

---

## 3. Use Type Hints

Use type hints for function parameters and return values where practical.

Example:

```python
def convert_file(path: Path, zoom: float = 2.0) -> list[Path]:
    ...
```

---

## 4. Use Meaningful Names

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

## 5. Keep Functions Focused

Functions should perform one clear task whenever possible.

Avoid creating very large functions that handle unrelated responsibilities.

---

## 6. Use Docstrings

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

#  CLI Guidelines

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

#  Interactive Shell

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

---

#  File Paths

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

---

#  Error Handling

User-facing errors should be handled gracefully.

Avoid exposing unnecessary Python tracebacks to normal CLI users.

For example, a missing PDF should result in a clear message such as:

```text
❌ File not found: document.pdf
```

rather than an unexplained application crash.

---

#  Ctrl+C Handling

When modifying conversion or interactive-shell behavior, test interruption handling.

The application should:

- Handle `Ctrl+C` without an unnecessary traceback.
- Stop the current operation when appropriate.
- Return to a safe state.
- Exit the interactive shell cleanly when `Ctrl+C` is used at the main prompt.

---

#  Testing

Before opening a Pull Request, test the functionality you changed.

For CLI changes, test at least:

- Starting the application.
- `--help`
- Interactive shell startup.
- `help`
- `convert`
- Invalid commands.
- Missing files.
- Paths containing spaces.
- Quoted paths.
- `Ctrl+C` during interaction.
- `Ctrl+C` during conversion.
- Non-interactive commands.

If you add a new PDF operation, add appropriate automated tests.

---

#  Adding a New PDF Operation

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

#  Commit Messages

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

#  Pull Requests

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

#  Code Review

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

#  Documentation

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

#  Reporting Bugs

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

#  Feature Requests

Feature requests are welcome.

When proposing a new feature, explain:

1. What the feature should do.
2. Why it would be useful.
3. How you expect users to interact with it.
4. Any relevant technical considerations.

For major architectural changes, discuss the idea before starting a large implementation.

---

#  Security Issues

Please do not publicly disclose serious security vulnerabilities before they can be properly investigated.

For security-sensitive issues, contact the project maintainer privately when possible.

---

#  License

By contributing to PDFForge, you agree that your contributions will be licensed under the same license as the project.

PDFForge is licensed under the:

**GNU General Public License v3.0 (GPL-3.0)**

See the `LICENSE` file for the complete license text.

---

# 👤 Project Maintainer

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

#  Thank You

Every contribution helps improve PDFForge.

Whether you are fixing a small bug, improving documentation, adding tests, or implementing a completely new PDF operation, your contribution is appreciated.

Thank you for helping build PDFForge.# Contributing to PDFForge

Thank you for your interest in contributing to PDFForge.

PDFForge is an open-source project, and contributions of all kinds are welcome. You can contribute code, tests, documentation, bug reports, feature ideas, architectural improvements, or code reviews.

Please read this guide before submitting a Pull Request.

---

## Code of Conduct

Please be respectful and constructive when interacting with other contributors.

Technical disagreements are normal in open-source development, but discussions should remain professional and focused on improving the project.

---

## Ways to Contribute

There are many ways to contribute to PDFForge:

* Report bugs
* Suggest features
* Improve documentation
* Add tests
* Fix existing issues
* Implement new PDF operations
* Improve performance
* Improve error handling
* Improve the CLI
* Improve the project architecture
* Review Pull Requests

You do not need to be an expert to contribute.

---

## Before You Start

Before working on a new feature or bug fix:

1. Check the existing Issues.
2. Search for related Pull Requests.
3. Make sure the change has not already been implemented.
4. For significant changes, open an Issue first to discuss the proposed approach.

This helps prevent duplicated work and keeps the project direction consistent.

---

## Fork the Repository

If you are not a direct collaborator, start by creating a fork of the repository.

Repository:

```text
https://github.com/roy-twsl/PDFForge
```

After creating your fork, clone it locally:

```bash
git clone https://github.com/YOUR_USERNAME/PDFForge.git
```

Then enter the project directory:

```bash
cd PDFForge
```

---

## Create a Branch

Do not make changes directly on the `main` branch.

Create a separate branch for your work.

For a new feature:

```bash
git checkout -b feature/your-feature-name
```

For a bug fix:

```bash
git checkout -b fix/your-bug-name
```

For documentation:

```bash
git checkout -b docs/your-documentation-change
```

Use a short and descriptive branch name.

---

## Set Up the Development Environment

Install the project dependencies:

```bash
pip install -r requirements.txt
```

For development, install PDFForge in editable mode:

```bash
pip install -e .
```

---

## Coding Guidelines

Please follow these guidelines when contributing code.

### Python Style

Follow standard Python conventions and generally follow PEP 8.

Use clear and descriptive names.

Good:

```python
def convert_pdf_to_images(pdf_path):
    ...
```

Avoid:

```python
def do_it(x):
    ...
```

---

### Type Hints

Use type hints for function and method parameters and return values whenever practical.

Example:

```python
def convert_pdf(pdf_path: Path, zoom: float = 2.0) -> list[Path]:
    ...
```

---

### Docstrings

Public classes, functions, and methods should have useful docstrings.

Document:

* What the component does
* Important parameters
* Return values
* Exceptions when relevant

---

### Single Responsibility

Keep classes and functions focused on one responsibility.

Avoid creating large classes that perform unrelated tasks.

---

### Reuse Existing Abstractions

Before creating a new abstraction, check whether an existing interface or component can be reused.

For example:

```text
IOperation
ILogger
IFileNamingStrategy
IImageSaver
```

When appropriate, extend the existing architecture instead of bypassing it.

---

## Adding a New PDF Operation

When implementing a new operation:

1. Create the appropriate operation package.
2. Implement the operation.
3. Follow the `IOperation` interface where appropriate.
4. Add custom exceptions if necessary.
5. Add the operation to `PDFService` if it is part of the public API.
6. Add CLI support if appropriate.
7. Add tests.
8. Update the README.
9. Update examples when useful.

For example:

```text
pdfforge/
└── operations/
    └── merge/
        ├── __init__.py
        └── merger.py
```

---

## Testing

All new functionality should include appropriate tests.

Run the test suite with:

```bash
pytest
```

If your contribution changes existing behavior, make sure the existing tests still pass.

When fixing a bug, preferably add a regression test that reproduces the problem before fixing it.

---

## Pull Request Process

Before opening a Pull Request:

1. Make sure your branch contains only related changes.
2. Run the test suite.
3. Review your own changes.
4. Make sure there are no unnecessary files.
5. Make sure documentation is updated when necessary.
6. Use clear commit messages.
7. Push your branch to your fork.
8. Open a Pull Request against the `main` branch.

---

## Commit Messages

Write concise and descriptive commit messages.

Good examples:

```text
Add PDF merge operation
```

```text
Fix PDF-to-image output naming
```

```text
Add tests for image conversion
```

```text
Improve PDFService error handling
```

Avoid vague messages such as:

```text
update
```

```text
changes
```

```text
fix stuff
```

---

## Pull Request Guidelines

A good Pull Request should:

* Have a clear title.
* Explain what was changed.
* Explain why the change was needed.
* Include tests when appropriate.
* Include documentation changes when necessary.
* Keep unrelated changes out of the PR.
* Be reasonably small and focused.

A useful Pull Request description can follow this structure:

```markdown
## Summary

Describe the change.

## Motivation

Explain why the change was necessary.

## Changes

- Change 1
- Change 2
- Change 3

## Testing

Explain how the changes were tested.
```

---

## Code Review

All Pull Requests may be reviewed before merging.

Reviewers may request:

* Code changes
* Additional tests
* Documentation updates
* Better naming
* Architectural improvements
* Clarification of implementation details

Please treat review comments as part of the development process.

When changes are requested, update your branch and push the new commits to the same Pull Request.

---

## Reporting Bugs

When reporting a bug, provide as much useful information as possible.

A good bug report should include:

* A clear title
* Python version
* Operating system
* PDFForge version or commit
* Steps to reproduce
* Expected behavior
* Actual behavior
* Error message or traceback
* Minimal example when possible

Example:

```markdown
## Bug Description

PDFForge fails to convert a specific PDF to PNG.

## Environment

- Python: 3.12
- OS: Windows 11
- PDFForge: 0.1.0

## Steps to Reproduce

1. Run the following command:
   `pdfforge convert example.pdf`
2. Observe the error.

## Expected Behavior

The PDF should be converted into PNG images.

## Actual Behavior

The conversion fails with an exception.
```

---

## Feature Requests

Feature requests are welcome.

When proposing a feature, explain:

* What problem it solves
* Why it would be useful
* How you expect it to work
* Whether you would be willing to implement it

For larger architectural changes, please discuss the idea in an Issue before starting implementation.

---

## Documentation Contributions

Documentation improvements are welcome.

You can help by:

* Fixing unclear explanations
* Adding examples
* Correcting spelling or grammar
* Improving installation instructions
* Documenting APIs
* Adding tutorials
* Improving troubleshooting information

Documentation should remain clear and accessible to developers with different levels of experience.

---

## Dependencies

Avoid adding new dependencies unless they provide significant value.

When introducing a dependency:

1. Explain why it is needed.
2. Consider whether the functionality can reasonably be implemented using the standard library or existing dependencies.
3. Check its license compatibility with PDFForge.
4. Update the appropriate dependency files.

---

## Backward Compatibility

When modifying public APIs, consider backward compatibility.

If a breaking change is necessary:

* Clearly document it.
* Explain why it is necessary.
* Update relevant examples.
* Update tests.
* Mention it in the Pull Request.

---

## License

By contributing to PDFForge, you agree that your contribution will be licensed under the same **GNU General Public License v3.0** that applies to the project, provided that you have the legal right to submit the contribution under those terms.

Please make sure that you have the right to contribute any code, documentation, or other material that you submit.

---

## Questions

If you are unsure about anything:

1. Check the README.
2. Search existing Issues and Pull Requests.
3. Open a new Issue if the question has not already been answered.

---

## Thank You

Every contribution helps improve PDFForge.

Whether you submit a small documentation fix, report a bug, add a test, implement a new operation, or review someone else's code, your contribution is appreciated.

Thank you for helping make PDFForge better.
