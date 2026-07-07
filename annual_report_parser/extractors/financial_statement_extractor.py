from annual_report_parser.config_loader import ConfigLoader
from annual_report_parser.models.financial_statement import FinancialStatement
from annual_report_parser.models.statement_page import StatementPage


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
    
    def get_page_header(self, text: str, lines: int = 10) -> str:
        """
        Return only the first few lines of a page.

        Financial statement titles almost always appear
        near the top of the page.

        """

        return "\n".join(
        text.splitlines()[:lines]
        ).lower()

    def extract(self, document):

        income = []
        balance = []
        cash = []

        for page in document.pages:

            
            text = page.text
            header = self.get_page_header(text)

            if self.contains_keyword(
                header,
                self.keywords["income_statement"],
            ):
              
                title = header.splitlines()[0]

                print(
                    f"Found Income Statement"
                    f"on page {page.number}: {title}"
                )

                income.append(
                    StatementPage(
                        statement_type="income_statement",
                        page=page,
                    )
                )

            elif self.contains_keyword(
                header,
                self.keywords["balance_sheet"],
            ):
                title = header.splitlines()[0]

                print( 
                     f"Found Balance Sheet "
                     f"on page {page.number}: {title}"
                )
                
                balance.append(
                    StatementPage(
                        statement_type="balance_sheet",
                        page=page,
                    )
                )

            elif self.contains_keyword(
                header,
                self.keywords["cash_flow"],
            ):
               
                title = header.splitlines()[0]

                print(
                     f"Found Cash Flow Statement"
                     f"on page {page.number}: {title}"
)
                cash.append(
                    StatementPage(
                        statement_type="cash_flow",
                        page=page,
                    )
                )

        return FinancialStatement(
            income_statement=income,
            balance_sheet=balance,
            cash_flow=cash,
        )