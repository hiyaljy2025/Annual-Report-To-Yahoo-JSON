from dataclasses import dataclass, field


@dataclass
class FinancialLine:
    """
    Represents one row in a financial statement.
    """

    label: str

    note: str | None = None

    values: list[str] = field(default_factory=list)
