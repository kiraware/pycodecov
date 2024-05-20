from typing import Any

from ..enums import Service
from ..schemas import GitAuthor, Owner, User

__all__ = [
    "parse_git_author_data",
    "parse_owner_data",
    "parse_user_data",
]


def parse_git_author_data(data: dict[str, Any]) -> GitAuthor:
    """
    Parse git author data.

    Args:
        data: git author json data.

    Returns:
        A `GitAuthor` schema.

    Examples:
    >>> data = {
    ...     "id": 123,
    ...     "username": "string",
    ...     "name": "string",
    ...     "email": "string",
    ... }
    >>> git_author = parse_git_author_data(data)
    >>> git_author
    GitAuthor(id=123, username='string', name='string', email='string')
    """
    id = data.get("id")
    username = data.get("username")
    name = data.get("name")
    email = data.get("email")

    return GitAuthor(id, username, name, email)


def parse_owner_data(data: dict[str, Any]) -> Owner:
    """
    Parse owner data.

    Args:
        data: owner json data.

    Returns:
        An `Owner` schema.

    Examples:
    >>> data = {
    ...     "service": "github",
    ...     "username": "string",
    ...     "name": "string",
    ... }
    >>> owner = parse_owner_data(data)
    >>> owner
    Owner(service=<Service.GITHUB: 'github'>, username='string', name='string')
    """
    service = data.get("service")
    username = data.get("username")
    name = data.get("name")

    return Owner(Service(service), username, name)


def parse_user_data(data: dict[str, Any]) -> User:
    """
    Parse user data.

    Args:
        data: user json data.

    Returns:
        A `User` schema.

    Examples:
    >>> data = {
    ...     "service": "github",
    ...     "username": "string",
    ...     "name": "string",
    ...     "activated": True,
    ...     "is_admin": True,
    ...     "email": "string",
    ... }
    >>> user = parse_user_data(data)
    >>> user
    User(service=<Service.GITHUB: 'github'>, username='string', name='string', activated=True, is_admin=True, email='string')
    """  # noqa: E501
    owner = parse_owner_data(data)

    service = owner.service
    username = owner.username
    name = owner.name

    activated = data.get("activated")
    is_admin = data.get("is_admin")
    email = data.get("email")

    return User(service, username, name, activated, is_admin, email)
