from dataclasses import dataclass

from annual_report_parser.models.statement_page import StatementPage


@dataclass
class FinancialStatement:

    income_statement: list[StatementPage]

    balance_sheet: list[StatementPage]

    cash_flow: list[StatementPage]