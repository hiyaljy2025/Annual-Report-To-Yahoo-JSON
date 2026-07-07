from dataclasses import dataclass


@dataclass
class Page:
    """
    Represents a single page in a PDF document.
    """

    number: int
    text: str