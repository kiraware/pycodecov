from dataclasses import dataclass
from datetime import datetime

from ..enums import CommitState
from .report import Report
from .total import CommitTotal
from .user import GitAuthor, Owner

__all__ = [
    "BaseCommit",
    "Commit",
    "CommitDetail",
    "GitCommit",
]


@dataclass(slots=True)
class BaseCommit:
    """
    A schema used to store info about base commit.

    Attributes:
        commitid: commit SHA.
        message: commit message.
        timestamp: timestamp when commit was made.
    """

    commitid: str
    message: str | None
    timestamp: datetime


@dataclass(slots=True)
class Commit(BaseCommit):
    """
    A schema used to store info about commit.

    Attributes:
        ci_passed: whether the CI process passed for this commit.
        author: commit author.
        branch: branch name on which this commit currently lives.
        totals: commit totals coverage information.
        state: codecov processing state for this commit.
        parent: commit SHA of first ancestor commit with coverage.
    """

    ci_passed: bool | None
    author: Owner | None
    branch: str | None
    totals: CommitTotal | None
    state: CommitState | None
    parent: str | None


@dataclass(slots=True)
class CommitDetail(Commit):
    """
    A schema used to store info about commit detail.

    Attributes:
        report: coverage report.
    """

    report: Report


@dataclass(slots=True)
class GitCommit(BaseCommit):
    """
    A schema used to store info about git commit.

    Attributes:
        author: commit author.
    """

    author: GitAuthor
