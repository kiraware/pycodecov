from typing import Any

from aiohttp import ClientSession

from .. import schemas
from ..api import Owner, User
from ..types import CodecovApiToken

__all__ = [
    "parse_owner_api",
    "parse_user_api",
]


def parse_owner_api(
    schema: schemas.Owner,
    token: CodecovApiToken | None = None,
    session: ClientSession | None = None,
    **kwargs: Any,
) -> Owner:
    """
    Turn Owner schema into Owner API.

    Args:
        schema: owner data.
        token: Codecov API Token.
        session: client session.

    Returns:
        An `Owner` API.

    Examples:
    >>> from pycodecov.parsers import parse_owner_data
    >>> data = {
    ...     "service": "github",
    ...     "username": "string",
    ...     "name": "string",
    ... }
    >>> owner = parse_owner_data(data)
    >>> owner_api = parse_owner_api(owner)
    >>> owner_api
    Owner(service=<Service.GITHUB: 'github'>, username='string', name='string')
    """
    return Owner(schema.service, schema.username, schema.name, token, session)


def parse_user_api(
    schema: schemas.User,
    token: CodecovApiToken | None = None,
    session: ClientSession | None = None,
    **kwargs: Any,
) -> User:
    """
    Turn User schema into User API.

    Args:
        schema: user data.
        token: Codecov API Token.
        session: client session.

    Returns:
        An `User` API.

    Examples:
    >>> from pycodecov.parsers import parse_user_data
    >>> data = {
    ...     "service": "github",
    ...     "username": "string",
    ...     "name": "string",
    ...     "activated": True,
    ...     "is_admin": True,
    ...     "email": "string",
    ... }
    >>> user = parse_user_data(data)
    >>> user_api = parse_user_api(user)
    >>> user_api
    User(service=<Service.GITHUB: 'github'>, username='string', name='string', activated=True, is_admin=True, email='string')
    """  # noqa: E501
    return User(
        schema.service,
        kwargs["owner_username"],
        schema.username,
        schema.name,
        schema.activated,
        schema.is_admin,
        schema.email,
        token,
        session,
    )
