import fitz  # PyMuPDF

from annual_report_parser.models.report import ReportMetadata


class PDFReader:
    def read(self, pdf_path: str) -> ReportMetadata:
        document = fitz.open(pdf_path)

        metadata = document.metadata

        report = ReportMetadata(
            file_name=pdf_path.split("\\")[-1],
            page_count=document.page_count,
            title=metadata.get("title"),
            author=metadata.get("author"),
            creator=metadata.get("creator"),
            producer=metadata.get("producer"),
        )

        document.close()

        return report