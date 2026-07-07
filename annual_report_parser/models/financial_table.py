from dataclasses import dataclass, field

from annual_report_parser.models.financial_line import FinancialLine


@dataclass
class FinancialTable:
    """
    Represents a financial statement table.
    """

    statement_type: str

    page_number: int

    lines: list[FinancialLine] = field(default_factory=list)