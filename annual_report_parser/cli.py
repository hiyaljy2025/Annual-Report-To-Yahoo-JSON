print("cli.py is running")
import typer
from rich import print

from annual_report_parser.pdf_reader import PDFReader

app = typer.Typer(
    help="Annual Report → Yahoo Finance JSON Converter"
)


@app.command()
def version():
    """Show application version."""
    print("[bold green]Annual Report To Yahoo JSON[/bold green]")
    print("Version: 0.1.0")


@app.command()
def inspect(pdf: str):
    """Inspect a PDF annual report."""

    reader = PDFReader()

    report = reader.read(pdf)

    print()
    print("=" * 50)
    print("[bold cyan]Annual Report Inspector[/bold cyan]")
    print("=" * 50)

    print(f"PDF File : {report.file_name}")
    print(f"Pages    : {report.page_count}")
    print(f"Title    : {report.title}")
    print(f"Author   : {report.author}")
    print(f"Creator  : {report.creator}")
    print(f"Producer : {report.producer}")


if __name__ == "__main__":
    app()