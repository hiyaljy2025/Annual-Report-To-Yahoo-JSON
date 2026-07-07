from dataclasses import dataclass


@dataclass
class FinancialLine:
    """
    Represents one row in a financial statement.
    """

    label: str

    values: list[str]