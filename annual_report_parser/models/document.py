from pydantic import BaseModel

from annual_report_parser.models.page import Page
from annual_report_parser.models.report import ReportMetadata


class Document(BaseModel):
    """
    Represents an annual report document.
    """

    metadata: ReportMetadata

    pages: list[Page]

    full_text: str