from dataclasses import dataclass

from ..enums import Coverage
from .commit import Commit, GitCommit
from .component import Component
from .flag import Flag
from .total import ReportTotal

__all__ = [
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
]


@dataclass(slots=True)
class LineNumberComparison:
    """
    A schema used to store info about line number comparison.

    Attributes:
        base: base line number.
        head: head line number.
    """

    base: int | None
    head: int | None


@dataclass(slots=True)
class LineCoverageComparison:
    """
    A schema used to store info about line coverage comparison.

    Attributes:
        base: base line coverage status.
        head: head line coverage status.
    """

    base: Coverage | None
    head: Coverage | None


@dataclass(slots=True)
class LineComparison:
    """
    A schema used to store info about line comparison.

    Attributes:
        value: text contained in the line.
        number: line number comparison.
        coverage: line coverage status comparison.
        is_diff: whether the line is in diff.
        added: whether the line was added.
        removed: whether the line was removed.
        sessions: sessions count.
    """

    value: str
    number: LineNumberComparison
    coverage: LineCoverageComparison
    is_diff: bool
    added: bool
    removed: bool
    sessions: int


@dataclass(slots=True)
class TotalComparison:
    """
    A schema used to store info about total comparison.

    Attributes:
        base: base totals coverage report information.
        head: head totals coverage report information.
        patch: patch totals coverage report information.
    """

    base: ReportTotal
    head: ReportTotal
    patch: ReportTotal | None


@dataclass(slots=True)
class FileNameComparison:
    """
    A schema used to store info about file name comparison.

    Attributes:
        base: base file name.
        head: head file name.
    """

    base: str | None
    head: str | None


@dataclass(slots=True)
class FileStatComparison:
    """
    A schema used to store info about file stat comparison.

    Attributes:
        added: added count.
        removed: removed count.
    """

    added: int
    removed: int


@dataclass(slots=True)
class FileChangeSummaryComparison:
    """
    A schema used to store info about file coverage change summary comparison.

    Attributes:
        hits: line coverage hits count summary.
        misses: line coverage misses count summary.
        partials: line coverage partials count summary.
    """

    hits: int | None
    misses: int | None
    partials: int | None


@dataclass(slots=True)
class FileComparison:
    """
    A schema used to store info about file comparison.

    Attributes:
        name: file name comparison.
        totals: totals file comparison.
        has_diff: whether the file has diff data.
        stats: file stat.
        change_summary: file coverage change summary.
        lines: lines comparison.
    """

    name: FileNameComparison
    totals: TotalComparison
    has_diff: bool
    stats: FileStatComparison | None
    change_summary: FileChangeSummaryComparison | None
    lines: list[LineComparison]


@dataclass(slots=True)
class DiffComparison:
    """
    A schema used to store info about diff comparison.

    Attributes:
        git_commits: list of git commit.
    """

    git_commits: list[GitCommit]


@dataclass(slots=True)
class CommitComparison:
    """
    A schema used to store info about commit comparison.

    Attributes:
        base_commit: base commit SHA.
        head_commit: head commit SHA.
        totals: total comparison.
        commit_uploads: list of commits.
        diff: diff comparison.
        files: list of files comparison.
        untracked: list of untracked files name.
        has_unmerged_base_commits: whether if any commits exist in the base reference
            but not in the head reference.
    """

    base_commit: str
    head_commit: str
    totals: TotalComparison
    commit_uploads: list[Commit]
    diff: DiffComparison
    files: list[FileComparison]
    untracked: list[str]
    has_unmerged_base_commits: bool


@dataclass(slots=True)
class ComponentComparison(Component):
    """
    A schema used to store info about component comparison.

    Attributes:
        base_report_totals: base totals coverage report information.
        head_report_totals: head totals coverage report information.
        diff_totals: diff totals coverage report information.
    """

    base_report_totals: ReportTotal
    head_report_totals: ReportTotal
    diff_totals: ReportTotal | None


@dataclass(slots=True)
class FlagComparison(Flag):
    """
    A schema used to store info about flag comparison.

    Attributes:
        base_report_totals: base totals coverage report information.
        head_report_totals: head totals coverage report information.
        diff_totals: diff totals coverage report information.
    """

    base_report_totals: ReportTotal
    head_report_totals: ReportTotal
    diff_totals: ReportTotal | None
