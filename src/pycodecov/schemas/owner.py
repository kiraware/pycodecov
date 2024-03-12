from dataclasses import dataclass

from ..enums import Service

__all__ = [
    "GitAuthor",
    "Owner",
]


@dataclass(slots=True)
class GitAuthor:
    """
    A schema used to store info about git author.

    Attributes:
        id: git author id.
        username: username of the git author.
        name: name of the git author.
        email: name of the git author.
    """

    id: int
    username: str | None
    name: str
    email: str


@dataclass(slots=True)
class Owner:
    """
    A schema used to store info about owner.

    Attributes:
        service: Git hosting service provider of the owner.
        username: username of the owner.
        name: name of the owner.
    """

    service: Service
    username: str | None
    name: str | None
