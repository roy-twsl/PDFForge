"""Default logger implementation that prints to console."""

from pdfforge.core.interfaces import ILogger


class ConsoleLogger(ILogger):
    """Simple logger that writes messages to stdout/stderr."""

    def info(self, message: str) -> None:
        print(f"[INFO] {message}")

    def debug(self, message: str) -> None:
        print(f"[DEBUG] {message}")

    def error(self, message: str) -> None:
        print(f"[ERROR] {message}")