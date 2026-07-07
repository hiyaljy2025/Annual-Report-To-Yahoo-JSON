from annual_report_parser.models.financial_statement import FinancialStatement


class FinancialStatementExtractor:
    def extract(self, document):

        income = []
        balance = []
        cash = []

        for page in document.pages:

            text = page.lower()

            if "income statement" in text:
                income.append(page)

            elif "financial position" in text:
                balance.append(page)

            elif "cash flow" in text:
                cash.append(page)

        return FinancialStatement(
            income_statement=income,
            balance_sheet=balance,
            cash_flow=cash,
        )