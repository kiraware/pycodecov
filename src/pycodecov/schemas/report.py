from dataclasses import dataclass

from .line import Line
from .total import ReportTotal

__all__ = [
    "BaseReportFile",
    "Report",
    "ReportFile",
]


@dataclass(slots=True)
class BaseReportFile:
    """
    A schema used to store info about base report file.

    Attributes:
        name: file path.
        totals: coverage totals.
    """

    name: str
    totals: ReportTotal


@dataclass(slots=True)
class ReportFile(BaseReportFile):
    """
    A schema used to store info about report file.

    Attributes:
        line_coverage: line-by-line coverage values.
    """

    line_coverage: list[Line]


@dataclass(slots=True)
class Report:
    """
    A schema used to store info about report.

    Attributes:
        totals: coverage totals.
        files: file specific coverage totals.
    """

    totals: ReportTotal
    files: list[ReportFile]
