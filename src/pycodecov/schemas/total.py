from dataclasses import dataclass

__all__ = [
    "BaseTotal",
    "CommitTotal",
    "ReportTotal",
]


@dataclass(slots=True)
class BaseTotal:
    """
    A schema used to store info about base totals coverage information.

    Attributes:
        files: files count.
        lines: lines count.
        hits: hits count.
        misses: misses count.
        partials: partials count.
        coverage: coverage count.
        branches: branches count.
        methods: methods count.
    """

    files: int
    lines: int
    hits: int
    misses: int
    partials: int
    coverage: float
    branches: int
    methods: int


@dataclass(slots=True)
class CommitTotal(BaseTotal):
    """
    A schema used to store info about totals coverage commit information.

    Attributes:
        sessions: sessions count.
        complexity: complexity count.
        complexity_total: complexity_total count.
        complexity_ratio: complexity_ratio count.
    """

    sessions: int
    complexity: float
    complexity_total: float
    complexity_ratio: float


@dataclass(slots=True)
class ReportTotal(BaseTotal):
    """
    A schema used to store info about totals coverage report information.

    Attributes:
        messages: messages count.
        sessions: sessions count.
        complexity: complexity count.
        complexity_total: complexity_total count.
        complexity_ratio: complexity_ratio count.
        diff: diff report.
    """

    messages: int
    sessions: int
    complexity: float
    complexity_total: float
    complexity_ratio: float
    diff: int | list[int | str | None]
