from dataclasses import dataclass
from datetime import datetime

from .commit import CommitDetail

__all__ = [
    "Branch",
    "BranchDetail",
]


@dataclass(slots=True)
class Branch:
    """
    A schema used to store info about branch.

    Attributes:
        name: branch name.
        updatestamp: last time the branch was updated.
    """

    name: str
    updatestamp: datetime


@dataclass(slots=True)
class BranchDetail(Branch):
    """
    A schema used to store info about branch detail.

    Attributes:
        head_commit: branch's current head commit.
    """

    head_commit: CommitDetail
