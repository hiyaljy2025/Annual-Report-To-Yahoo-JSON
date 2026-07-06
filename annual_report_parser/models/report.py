from pydantic import BaseModel
from typing import Optional


class ReportMetadata(BaseModel):
    file_name: str
    page_count: int

    title: Optional[str] = None
    author: Optional[str] = None
    creator: Optional[str] = None
    producer: Optional[str] = None