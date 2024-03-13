from dataclasses import dataclass
from datetime import datetime

from ..enums import Language
from .total import CommitTotal
from .user import Owner

__all__ = [
    "Repo",
    "RepoConfig",
]


@dataclass(slots=True)
class Repo:
    """
    A schema used to store info about repository.

    Attributes:
        name: repository name.
        private: whether private or public repository.
        updatestamp: last time the repository was updated.
        author: repository owner.
        language: primary programming language used.
        branch: default branch name.
        active: whether the repository has received a coverage upload.
        activated: whether the repository has been manually deactivated.
        totals: recent commit totals on the default branch.
    """

    name: str
    private: bool
    updatestamp: datetime | None
    author: Owner
    language: Language | None
    branch: str
    active: bool | None
    activated: bool | None
    totals: CommitTotal | None


@dataclass(slots=True)
class RepoConfig:
    """
    A schema used to store info about repository config.

    Attributes:
        upload_token: token used for uploading coverage reports for repository.
        graph_token: token used for repository graphs.
    """

    upload_token: str
    graph_token: str
