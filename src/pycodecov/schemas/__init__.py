"""
Module to store common schema classes used by pycodecov.
"""

from .branch import Branch, BranchDetail
from .commit import BaseCommit, Commit, CommitDetail, GitCommit
from .comparison import (
    CommitComparison,
    ComponentComparison,
    DiffComparison,
    FileChangeSummaryComparison,
    FileComparison,
    FileNameComparison,
    FileStatComparison,
    FlagComparison,
    LineComparison,
    LineCoverageComparison,
    LineNumberComparison,
    TotalComparison,
)
from .component import Component
from .coverage import CommitCoverage, CommitCoverageReport, CommitCoverageTotal
from .coverage_trend import CoverageTrend
from .flag import Flag
from .line import Line
from .paginated_list import PaginatedList
from .pull import Pull
from .repo import Repo, RepoConfig
from .report import BaseReportFile, Report, ReportFile
from .total import BaseTotal, CommitTotal, ReportTotal
from .user import GitAuthor, Owner, User

__all__ = [
    "Branch",
    "BranchDetail",
    "BaseCommit",
    "Commit",
    "CommitDetail",
    "GitCommit",
    "CommitComparison",
    "ComponentComparison",
    "DiffComparison",
    "FileChangeSummaryComparison",
    "FileComparison",
    "FileNameComparison",
    "FileStatComparison",
    "FlagComparison",
    "LineComparison",
    "LineCoverageComparison",
    "LineNumberComparison",
    "TotalComparison",
    "Component",
    "CommitCoverage",
    "CommitCoverageReport",
    "CommitCoverageTotal",
    "CoverageTrend",
    "Flag",
    "Line",
    "PaginatedList",
    "Pull",
    "Repo",
    "RepoConfig",
    "BaseReportFile",
    "Report",
    "ReportFile",
    "BaseTotal",
    "CommitTotal",
    "ReportTotal",
    "GitAuthor",
    "Owner",
    "User",
]
