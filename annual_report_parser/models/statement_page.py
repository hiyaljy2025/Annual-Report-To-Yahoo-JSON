from dataclasses import dataclass

from annual_report_parser.models.page import Page


@dataclass
class StatementPage:
    """
    Represents a page that has been identified
    as a financial statement.
    """

    statement_type: str

    page: Page