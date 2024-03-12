from dataclasses import dataclass

from .owner import Owner

__all__ = ["User"]


@dataclass(slots=True)
class User(Owner):
    """
    A schema used to store info about user.

    Attributes:
        activated: whether the user has been manually deactivated.
        is_admin: whether the user is an admin.
        email: email of the user.
    """

    activated: bool
    is_admin: bool
    email: str | None
