from dataclasses import dataclass

@dataclass
class FinancialStatement:

    income_statement: list[str]

    balance_sheet: list[str]

    cash_flow: list[str]