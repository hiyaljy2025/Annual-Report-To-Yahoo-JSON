from annual_report_parser.models.financial_line import FinancialLine
from annual_report_parser.models.financial_table import FinancialTable
from annual_report_parser.models.statement_page import StatementPage


class FinancialTableParser:
    """
    Converts a StatementPage into a FinancialTable.
    """

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

            table.lines.append(
                FinancialLine(
                    label=line,
                    values=[],
                )
            )

        return table