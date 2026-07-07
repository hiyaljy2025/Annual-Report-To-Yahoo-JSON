from dataclasses import dataclass

from annual_report_parser.models.page import Page


@dataclass
class FinancialStatement:

    income_statement: list[Page]

    balance_sheet: list[Page]

    cash_flow: list[Page]