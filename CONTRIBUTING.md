# Contributing to PDFForge

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
