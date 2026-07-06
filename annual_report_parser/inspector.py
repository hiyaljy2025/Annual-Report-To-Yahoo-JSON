import re

from annual_report_parser.models.document import Document


class Inspector:

    def inspect(self, document: Document):

        first_pages = "\n".join(document.pages[:5])

        company = None

        year = None

        company_match = re.search(
            r"AIMS APAC REIT",
            first_pages,
            re.IGNORECASE,
        )

        if company_match:

            company = company_match.group(0)

        year_match = re.search(
            r"20\d\d",
            first_pages,
        )

        if year_match:

            year = int(year_match.group(0))

        return {
            "company": company,
            "year": year,
        }