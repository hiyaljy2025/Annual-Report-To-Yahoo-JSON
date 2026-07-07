import re

from annual_report_parser.models.financial_line import FinancialLine
from annual_report_parser.models.financial_table import FinancialTable
from annual_report_parser.models.statement_page import StatementPage


class FinancialTableParser:
    """
    Converts a StatementPage into a FinancialTable.
    """

    def is_number(self, token: str) -> bool:
        """
        Returns True if the token looks like a financial number.
        """

        pattern = r"^\(?[\d,]+(\.\d+)?\)?$"

        return re.match(pattern, token) is not None

    def parse(self, statement_page: StatementPage) -> FinancialTable:

        table = FinancialTable(
            statement_type=statement_page.statement_type,
            page_number=statement_page.page.number,
        )

        lines = statement_page.page.text.splitlines()

        for line in lines:

            line = line.strip()

            if not line:
                continue

            tokens = line.split()

            values = []

            while tokens and self.is_number(tokens[-1]):
                values.insert(0, tokens.pop())

            label = " ".join(tokens)

            table.lines.append(
                FinancialLine(
                    label=label,
                    values=values,
                )
            )

        return table