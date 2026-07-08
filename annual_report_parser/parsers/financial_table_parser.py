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

    def should_keep_line(
        self,
        label: str,
        values: list[str],
    ) -> bool:
        """
        Decide whether a parsed line is a genuine
        financial row.
        """

        if not label:
            return False

        if not values:
            return False

        label = label.lower().strip()

        ignore = {
            "fy2025",
            "fy2024",
            "fy2023",
            "change",
            "%",
            "s$'000",
            "s$",
            "page",
        }

        if label in ignore:
            return False

        # Ignore report titles
        if "annual report" in label:
            return False

        # Ignore page references
        if "page" in label:
            return False

        # Ignore addresses
        if "industrial park" in label:
            return False

        # Ignore very short labels
        if len(label) < 4:
            return False

        return True

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
            print("---------------------------")
            print(f"Label : {label}")
            print(f"Values: {values}")

            if self.should_keep_line(label, values):

                table.lines.append(
                    FinancialLine(
                        label=label,
                        values=values,
                    )
                )

        return table
