from pydantic import BaseModel

from annual_report_parser.models.report import ReportMetadata


class Document(BaseModel):
    metadata: ReportMetadata

    pages: list[str]

    full_text: str