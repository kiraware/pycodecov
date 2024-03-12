from dataclasses import dataclass

from .report import BaseReportFile, ReportFile
from .total import ReportTotal

__all__ = [
    "CommitCoverage",
    "CommitCoverageReport",
    "CommitCoverageTotal",
]


@dataclass(slots=True)
class CommitCoverage:
    """
    A schema used to store info about commit coverage.

    Attributes:
        totals: totals coverage report information.
        commit_file_url: Codecov URL to see file coverage on commit.
    """

    totals: ReportTotal
    commit_file_url: str


@dataclass(slots=True)
class CommitCoverageReport(CommitCoverage):
    """
    A schema used to store info about commit coverage report.

    Attributes:
        files: file specific commit coverage totals.
    """

    files: list[ReportFile]


@dataclass(slots=True)
class CommitCoverageTotal(CommitCoverage):
    """
    A schema used to store info about commit coverage report.

    Attributes:
        files: file specific commit coverage totals.
    """

    files: list[BaseReportFile]
