from annual_report_parser.config_loader import ConfigLoader
from annual_report_parser.models.financial_statement import FinancialStatement


class FinancialStatementExtractor:
    """
    Locate the financial statement pages within an annual report.
    """

    def __init__(self):
        loader = ConfigLoader()
        self.keywords = loader.load("statement_keywords.json")

    def contains_keyword(self, text: str, keywords: list[str]) -> bool:
        """
        Return True if any keyword exists in the text.
        """
        text = text.lower()

        for keyword in keywords:
            if keyword.lower() in text:
                return True

        return False

    def extract(self, document):

        income = []
        balance = []
        cash = []

        for page in document.pages:

            text = page.lower()

            if self.contains_keyword(
                text,
                self.keywords["income_statement"],
            ):
                income.append(page)

            elif self.contains_keyword(
                text,
                self.keywords["balance_sheet"],
            ):
                balance.append(page)

            elif self.contains_keyword(
                text,
                self.keywords["cash_flow"],
            ):
                cash.append(page)

        return FinancialStatement(
            income_statement=income,
            balance_sheet=balance,
            cash_flow=cash,
        )