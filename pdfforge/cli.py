#!/usr/bin/env python3
"""Interactive and non-interactive CLI for PDFForge.

Usage:
  pdfforge                       # Interactive shell
  pdfforge convert file.pdf ...  # Non-interactive command
  pdfforge --help                # Show help
"""

import argparse
import shlex
import sys
from pathlib import Path
from typing import List, Optional

from pdfforge.services.pdf_service import PDFService
from pdfforge.core.logger import ConsoleLogger

from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TimeElapsedColumn,
)
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich import box


# ============================================================
# Console
# ============================================================

console = Console()


# ============================================================
# Custom Logger - suppresses DEBUG messages
# ============================================================

class CliLogger(ConsoleLogger):
    """Logger that does NOT print DEBUG messages."""
    
    def debug(self, message: str) -> None:
        """Override to suppress DEBUG messages."""
        pass  # Do nothing


logger = CliLogger()


# ============================================================
# Clean Shell Operators
# ============================================================

def clean_shell_operators(args: List[str]) -> List[str]:
    """
    Remove shell operators like &, |, ;, &&, ||, >, <, etc.
    from the argument list.

    This allows users to accidentally type 'convert & file.pdf'
    and still have it work correctly.
    """
    # List of common shell operators to filter out
    operators = {
        '&', '|', ';', '&&', '||', '>', '<', '>>', '<<', '|&', ';&', ';;',
    }
    
    cleaned = []
    for arg in args:
        if arg not in operators and not arg.startswith('&') and not arg.startswith('|'):
            cleaned.append(arg)
    
    return cleaned


# ============================================================
# PDFForge ASCII Logo
# ============================================================

PDFFORGE_LOGO = r"""
██████╗  ██████╗ ███████╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██████╔╝██║   ██║█████╗  █████╗  ██║   ██║██████╔╝██║  ███╗█████╗
██╔═══╝ ██║   ██║██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝
██║     ╚██████╔╝███████╗██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═╝      ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
"""


# ============================================================
# Header
# ============================================================

def print_header() -> None:
    """Display the PDFForge application header."""

    logo = Text(
        PDFFORGE_LOGO,
        style="bold white",
        justify="center",
        no_wrap=True,
    )

    header = Panel(
        logo,
        title="[bold cyan]PDFForge[/]",
        title_align="center",
        subtitle="[bold cyan]Python PDF Toolkit[/]",
        subtitle_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        padding=(1, 2),
        expand=False,
    )

    console.print(header)
    console.print()


# ============================================================
# Welcome
# ============================================================

def show_welcome() -> None:
    """Show welcome message."""

    console.print(
        "[bold green]📚 Welcome to PDFForge Interactive Shell![/]"
    )

    console.print(
        "[dim]Type a command or 'help' for available commands. "
        "Type 'exit' or 'quit' to leave.[/]"
    )

    console.print()


# ============================================================
# Help
# ============================================================

def show_help() -> None:
    """Display help in interactive shell."""

    table = Table(
        title="[bold cyan]📚 Available Commands[/]",
        box=box.ROUNDED,
        header_style="bold blue",
        border_style="cyan",
    )

    table.add_column(
        "Command",
        style="cyan",
        no_wrap=True,
    )

    table.add_column(
        "Description",
        style="white",
    )

    table.add_column(
        "Example",
        style="yellow",
    )

    table.add_row(
        "convert",
        "Convert PDF to images",
        "convert document.pdf --zoom 2.0",
    )

    table.add_row(
        "convert (with spaces)",
        "Path with spaces, no quotes needed",
        "convert D:/My Docs/report.pdf",
    )

    table.add_row(
        "convert (page selection)",
        "Select pages: all, single, or range",
        "convert document.pdf --pages 5-10",
    )

    table.add_row(
        "convert (output dir)",
        "Custom output directory",
        "convert document.pdf --output-dir my_images",
    )

    table.add_row(
        "merge",
        "Merge PDFs (coming soon)",
        "merge file1.pdf file2.pdf --output merged.pdf",
    )

    table.add_row(
        "help",
        "Show this help message",
        "help",
    )

    table.add_row(
        "exit / quit",
        "Exit the interactive shell",
        "exit",
    )

    console.print(table)
    console.print()

    examples = Panel(
        "[bold]Quick Examples:[/]\n"
        "  [cyan]convert document.pdf --zoom 2.5 --format png[/]\n"
        "  [cyan]convert document.pdf --pages 5[/]              # Single page\n"
        "  [cyan]convert document.pdf --pages 20-46[/]          # Range\n"
        "  [cyan]convert document.pdf --pages 1,3,5-10,20[/]    # Mixed\n"
        "  [cyan]convert document.pdf --output-dir my_images[/] # Custom output dir\n"
        "  [cyan]convert \"My Report.pdf\" --format jpg[/]\n"
        "  [cyan]merge chapter1.pdf chapter2.pdf --output full_book.pdf[/]\n"
        "  [cyan]help[/]\n"
        "  [cyan]exit[/]",
        title="[bold yellow]💡 Examples[/]",
        border_style="yellow",
        box=box.ROUNDED,
    )

    console.print(examples)


# ============================================================
# Command Parser
# ============================================================

def parse_command_line(cmd_line: str) -> Optional[List[str]]:
    """Parse a command line respecting quotes."""

    try:
        return shlex.split(cmd_line)

    except ValueError as exc:
        console.print(
            f"[red]❌ Error parsing command:[/] {exc}"
        )

        return None


# ============================================================
# Convert Command
# ============================================================

def handle_convert_command(
    args: List[str],
    service: PDFService,
) -> bool:
    """Handle 'convert' command. Returns True on success."""

    # Clean shell operators from arguments
    args = clean_shell_operators(args)

    parser = argparse.ArgumentParser(
        prog="convert",
        description="Convert PDF pages to images",
        add_help=False,
    )

    parser.add_argument(
        "input_parts",
        nargs="*",
        help="Path to the PDF file (supports spaces without quotes)",
    )

    parser.add_argument(
        "--pages",
        type=str,
        default=None,
        help="Page selection: all (default), single (e.g., 5), "
             "range (e.g., 5-10), or list (e.g., 1,3,5-10)",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Output directory name. If not provided, auto-generates "
             "(images, images_1, images_2, ...)",
    )

    parser.add_argument(
        "--zoom",
        type=float,
        default=2.0,
        help="Zoom factor for image quality (default: 2.0)",
    )

    parser.add_argument(
        "--format",
        choices=["png", "jpg"],
        default="png",
        help="Output image format (default: png)",
    )

    try:
        parsed_args = parser.parse_args(args)

    except SystemExit:
        console.print(
            "[red]❌ Invalid arguments for 'convert' command.[/]"
        )

        console.print(
            "[yellow]💡 Usage: "
            "convert <pdf_file> "
            "[--pages PAGES] "
            "[--output-dir DIR] "
            "[--zoom ZOOM] "
            "[--format {png,jpg}][/]"
        )

        return False

    if not parsed_args.input_parts:
        console.print(
            "[red]❌ Error:[/] No input file specified."
        )

        console.print(
            "[yellow]💡 Usage: "
            "convert <pdf_file> "
            "[--pages PAGES] "
            "[--output-dir DIR] "
            "[--zoom ZOOM] "
            "[--format {png,jpg}][/]"
        )

        return False

    raw_path = (
        " ".join(parsed_args.input_parts)
        if len(parsed_args.input_parts) > 1
        else parsed_args.input_parts[0]
    )

    pdf_path = Path(raw_path).resolve()

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not pdf_path.exists():
        console.print(
            f"[red]❌ File not found:[/] {pdf_path}"
        )

        return False

    if not pdf_path.is_file():
        console.print(
            f"[red]❌ Input path is not a file:[/] {pdf_path}"
        )

        return False

    # --------------------------------------------------------
    # Parse pages
    # --------------------------------------------------------

    pages = parsed_args.pages
    if pages is not None and pages.lower() == "all":
        pages = None

    # --------------------------------------------------------
    # Parse output directory
    # --------------------------------------------------------

    output_dir_name = parsed_args.output_dir

    # Display info
    if pages is None:
        page_info = "[green]All pages[/]"
    else:
        page_info = f"[yellow]'{pages}'[/]"

    if output_dir_name is None:
        dir_info = "[green]Auto-generated (images, images_1, ...)[/]"
    else:
        dir_info = f"[yellow]'{output_dir_name}'[/]"

    # --------------------------------------------------------
    # Conversion information
    # --------------------------------------------------------

    console.print()

    console.print(
        f"[bold cyan]📄 Converting:[/] "
        f"[white]{pdf_path.name}[/]"
    )

    console.print(
        f"[dim]   Location: {pdf_path.parent}[/]"
    )

    console.print(
        f"[dim]   Pages: {page_info}[/]"
    )

    console.print(
        f"[dim]   Output Dir: {dir_info}[/]"
    )

    console.print(
        f"[dim]   Zoom: {parsed_args.zoom} | "
        f"Format: {parsed_args.format}[/]"
    )

    console.print()

    # --------------------------------------------------------
    # Conversion with Progress Callback
    # --------------------------------------------------------

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn(
                "[progress.description]{task.description}"
            ),
            BarColumn(),
            TextColumn(
                "[progress.percentage]{task.percentage:>3.0f}%"
            ),
            TimeElapsedColumn(),
            console=console,
            transient=False,
        ) as progress:

            task = progress.add_task(
                "[cyan]Converting pages...",
                total=100,
            )

            # Define callback to update progress
            def update_progress(current: int, total: int) -> None:
                if total > 0:
                    percent = (current / total) * 100
                    progress.update(
                        task,
                        completed=percent,
                        description=f"[cyan]Converting page {current} of {total}...",
                    )

            # Execute conversion with callback
            result = service.convert_to_images(
                pdf_path=pdf_path,
                zoom=parsed_args.zoom,
                output_format=parsed_args.format,
                pages=pages,
                output_dir_name=output_dir_name,
                progress_callback=update_progress,
            )

            # Ensure 100% completion
            progress.update(
                task,
                completed=100,
                description="[green]✓ Conversion complete![/]",
            )

        # ----------------------------------------------------
        # Success - Show limited output
        # ----------------------------------------------------

        console.print()
        console.print(
            f"[bold green]✅ Success![/] "
            f"Generated [cyan]{len(result)}[/] images."
        )

        if result:
            # Show output directory
            output_dir = result[0].parent
            console.print(f"[dim]   Output folder: {output_dir}[/]")

        console.print()

        # Show only first 5 files to avoid clutter
        if len(result) <= 5:
            for img_path in result:
                console.print(f"   [dim]• {img_path}[/]")
        else:
            for img_path in result[:5]:
                console.print(f"   [dim]• {img_path}[/]")
            console.print(f"   [dim]... and {len(result) - 5} more[/]")

        console.print()

        return True

    except KeyboardInterrupt:
        console.print(
            "\n[yellow]⚠️ Conversion interrupted by user.[/]"
        )

        return False

    except Exception as exc:
        console.print(
            f"[red]❌ Conversion failed:[/] {exc}"
        )

        return False


# ============================================================
# Merge Command
# ============================================================

def handle_merge_command(args: List[str]) -> bool:
    """Handle 'merge' command placeholder."""

    console.print()

    merge_panel = Panel(
        "[yellow]⚠️ Merge operation is not yet implemented.[/]\n\n"
        "[dim]This feature is planned for future releases.[/]\n\n"
        "[dim]Follow development at:[/]\n"
        "[cyan]https://github.com/roy-twsl/PDFForge[/]",
        title="[bold yellow]Merge PDFs[/]",
        border_style="yellow",
        box=box.ROUNDED,
    )

    console.print(merge_panel)
    console.print()

    return False


# ============================================================
# Non-Interactive Mode
# ============================================================

def run_non_interactive(args: List[str]) -> None:
    """Run a single command in non-interactive mode."""

    if not args:
        return

    # Clean shell operators
    args = clean_shell_operators(args)

    if not args:
        console.print("[red]❌ No command provided.[/]")
        sys.exit(1)

    cmd = args[0].lower()

    service = PDFService(
        logger=logger
    )

    if cmd == "convert":
        handle_convert_command(
            args[1:],
            service,
        )

    elif cmd == "merge":
        handle_merge_command(
            args[1:]
        )

    else:
        console.print(
            f"[red]❌ Unknown command:[/] '{cmd}'"
        )

        console.print(
            "[yellow]💡 Run 'pdfforge --help' "
            "for available commands.[/]"
        )

        sys.exit(1)


# ============================================================
# Interactive Shell
# ============================================================

def interactive_shell() -> None:
    """Run the interactive PDFForge shell."""

    print_header()
    show_welcome()
    show_help()

    service = PDFService(
        logger=logger
    )

    while True:
        try:
            cmd_line = Prompt.ask(
                "[bold cyan]PDFForge[/]"
            )

            if not cmd_line or cmd_line.strip() == "":
                continue

            parts = parse_command_line(
                cmd_line.strip()
            )

            if parts is None:
                continue

            if not parts:
                continue

            # Clean shell operators
            parts = clean_shell_operators(parts)

            if not parts:
                continue

            command = parts[0].lower()

            # ------------------------------------------------
            # Exit
            # ------------------------------------------------

            if command in [
                "exit",
                "quit",
                "q",
            ]:
                console.print(
                    "[yellow]👋 Goodbye![/]"
                )

                break

            # ------------------------------------------------
            # Help
            # ------------------------------------------------

            if command in [
                "help",
                "?",
            ]:
                show_help()
                continue

            # ------------------------------------------------
            # Convert
            # ------------------------------------------------

            if command == "convert":
                handle_convert_command(
                    parts[1:],
                    service,
                )

                continue

            # ------------------------------------------------
            # Merge
            # ------------------------------------------------

            if command == "merge":
                handle_merge_command(
                    parts[1:]
                )

                continue

            # ------------------------------------------------
            # Unknown command
            # ------------------------------------------------

            console.print(
                f"[red]❌ Unknown command:[/] '{command}'"
            )

            console.print(
                "[yellow]💡 Type 'help' "
                "for available commands.[/]"
            )

        except KeyboardInterrupt:
            console.print(
                "\n[yellow]👋 Goodbye![/]"
            )

            break

        except EOFError:
            console.print(
                "\n[yellow]👋 Goodbye![/]"
            )

            break

        except Exception as exc:
            console.print(
                f"[red]❌ Unexpected error:[/] {exc}"
            )


# ============================================================
# Main
# ============================================================

def main() -> None:
    """Entry point."""

    # --------------------------------------------------------
    # Interactive mode
    # --------------------------------------------------------

    if len(sys.argv) == 1:
        interactive_shell()
        return

    # --------------------------------------------------------
    # Help
    # --------------------------------------------------------

    if sys.argv[1] in [
        "-h",
        "--help",
    ]:
        print_header()

        console.print(
            "[bold cyan]PDFForge[/] "
            "[dim]- Python PDF Toolkit[/]"
        )

        console.print()

        console.print(
            "[bold]Usage:[/]"
        )

        console.print(
            "  [cyan]pdfforge[/] "
            "                     # Interactive shell"
        )

        console.print(
            "  [cyan]pdfforge convert <file>[/] "
            "    # Convert PDF to images"
        )

        console.print(
            "  [cyan]pdfforge convert <file> --pages PAGES[/] "
            "  # Select pages"
        )

        console.print(
            "  [cyan]pdfforge convert <file> --output-dir DIR[/] "
            "  # Custom output directory"
        )

        console.print(
            "  [cyan]pdfforge merge ...[/] "
            "              # Merge PDFs (coming soon)"
        )

        console.print(
            "  [cyan]pdfforge --help[/] "
            "               # Show this help"
        )

        console.print()

        return

    # --------------------------------------------------------
    # Non-interactive command
    # --------------------------------------------------------

    run_non_interactive(
        sys.argv[1:]
    )


# ============================================================
# Script Entry Point
# ============================================================

if __name__ == "__main__":
    main()