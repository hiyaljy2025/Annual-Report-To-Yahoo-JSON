print("cli.py is running")

import typer
from rich import print

from annual_report_parser.pdf_reader import PDFReader
from annual_report_parser.inspector import Inspector
from annual_report_parser.extractors.financial_statement_extractor import (
    FinancialStatementExtractor,
)

app = typer.Typer(
    help="Annual Report → Yahoo Finance JSON Converter"
)


@app.command()
def version():
    """Show application version."""
    print("[bold green]Annual Report To Yahoo JSON[/bold green]")
    print("Version: 0.3.0")


@app.command()
def inspect(pdf: str):
    """Inspect a PDF annual report."""

    reader = PDFReader()
    document = reader.read(pdf)

    inspector = Inspector()
    info = inspector.inspect(document)

    print()
    print("=" * 50)
    print("[bold cyan]Annual Report Inspector[/bold cyan]")
    print("=" * 50)
    print()

    print(f"PDF File : {document.metadata.file_name}")
    print(f"Pages    : {document.metadata.page_count}")
    print(f"Company  : {info['company']}")
    print(f"Year     : {info['year']}")


@app.command()
def extract(pdf: str):
    """Extract financial statement pages."""

    reader = PDFReader()
    document = reader.read(pdf)

    extractor = FinancialStatementExtractor()
    statements = extractor.extract(document)

    print()
    print("=" * 50)
    print("[bold cyan]Financial Statements[/bold cyan]")
    print("=" * 50)
    print()

    print(f"Income Statement Pages : {len(statements.income_statement)}")
    print(f"Balance Sheet Pages    : {len(statements.balance_sheet)}")
    print(f"Cash Flow Pages        : {len(statements.cash_flow)}")


if __name__ == "__main__":
    app()