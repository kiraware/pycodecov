from aiohttp import ClientSession

from .. import schemas
from ..enums import Service
from ..exceptions import CodecovError
from ..parsers import parse_user_data
from ..types import CodecovApiToken
from .api import API

__all__ = ["User"]


class User(API, schemas.User):
    """
    User API Wrapper from Codecov API.
    """

    def __init__(
        self,
        service: Service,
        owner_username: str | None = None,
        username: str | None = None,
        name: str | None = None,
        activated: bool | None = None,
        is_admin: bool | None = None,
        email: str | None = None,
        token: CodecovApiToken | None = None,
        session: ClientSession | None = None,
    ) -> None:
        API.__init__(self, token, session)
        schemas.User.__init__(self, service, username, name, activated, is_admin, email)

        self.owner_username = owner_username

    async def get_detail(self) -> schemas.User:
        """
        Get a user for the specified owner_username or ownerid.

        Returns:
            A `User`.

        Examples:
            >>> import asyncio
            >>> import os
            >>> from pycodecov import Codecov
            >>> from pycodecov.enums import Service
            >>> async def main():
            ...     async with Codecov(os.environ["CODECOV_API_TOKEN"]) as codecov:
            ...         service_owners = await codecov.get_service_owners(Service.GITHUB)
            ...         for owner in service_owners:
            ...             users = await owner.get_users()
            ...             for user in users:
            ...                 print(user)
            >>> asyncio.run(main())
            User(...)
            ...
        """  # noqa: E501
        async with self._session.get(
            f"{self.api_url}/{self.service}/{self.owner_username}/users/{self.username}"
        ) as response:
            data = await response.json()

            if response.ok:
                return parse_user_data(data)

            raise CodecovError(data)
