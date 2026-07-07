import fitz

from annual_report_parser.models.document import Document
from annual_report_parser.models.page import Page
from annual_report_parser.models.report import ReportMetadata


class PDFReader:

    def read(self, pdf_path: str) -> Document:

        pdf = fitz.open(pdf_path)

        metadata = pdf.metadata

        pages = []

        for page_number, page in enumerate(pdf, start=1):

            text = page.get_text()

            pages.append(
                Page(
                    number=page_number,
                    text=text,
                )
            )

        report = ReportMetadata(
            file_name=pdf_path.split("\\")[-1],
            page_count=pdf.page_count,
            title=metadata.get("title"),
            author=metadata.get("author"),
            creator=metadata.get("creator"),
            producer=metadata.get("producer"),
        )

        full_text = "\n".join(page.text for page in pages)

        pdf.close()

        return Document(
            metadata=report,
            pages=pages,
            full_text=full_text,
        )