import fitz

from annual_report_parser.models.document import Document
from annual_report_parser.models.report import ReportMetadata


class PDFReader:

    def read(self, pdf_path: str) -> Document:

        document = fitz.open(pdf_path)

        metadata = document.metadata

        pages = []

        for page in document:

            text = page.get_text()

            pages.append(text)

        report = ReportMetadata(
            file_name=pdf_path.split("\\")[-1],
            page_count=document.page_count,
            title=metadata.get("title"),
            author=metadata.get("author"),0
            creator=metadata.get("creator"),
            producer=metadata.get("producer"),
        )

        full_text = "\n".join(pages)

        document.close()

        return Document(
            metadata=report,
            pages=pages,
            full_text=full_text,
        )
