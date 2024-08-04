from aiohttp import ClientSession

from .. import schemas
from ..api_parsers import parse_paginated_list_api, parse_user_api
from ..enums import Service
from ..exceptions import CodecovError
from ..parsers import parse_owner_data, parse_paginated_list_data, parse_user_data
from ..types import CodecovApiToken
from .api import API
from .paginated_list import PaginatedList, PaginatedListApi

__all__ = [
    "Owner",
    "User",
]


class Owner(API, schemas.Owner):
    """
    Owner API Wrapper from Codecov API.
    """

    def __init__(
        self,
        service: Service,
        username: str | None = None,
        name: str | None = None,
        token: CodecovApiToken | None = None,
        session: ClientSession | None = None,
    ) -> None:
        API.__init__(self, token, session)
        schemas.Owner.__init__(self, service, username, name)

    async def get_detail(self) -> schemas.Owner:
        """
        Get a single owner by name.

        Returns:
            An `Owner`.

        Examples:
            >>> import asyncio
            >>> from pycodecov import Codecov
            >>> from pycodecov.enums import Service
            >>> async def main():
            ...     async with Codecov() as codecov:
            ...         service_owners = await codecov.get_service_owners(Service.GITHUB)
            ...         for owner in service_owners:
            ...             print(await owner.get_detail())
            >>> asyncio.run(main())
            Owner(service=<Service.GITHUB: 'github'>, username='jazzband', name='jazzband')
        """  # noqa: E501
        async with self._session.get(
            f"{self.api_url}/{self.service}/{self.username}"
        ) as response:
            data = await response.json()

            if response.ok:
                return parse_owner_data(data)

            raise CodecovError(data)

    async def get_users(
        self,
        activated: bool | None = None,
        is_admin: bool | None = None,
        page: int | None = None,
        page_size: int | None = None,
        search: str | None = None,
    ) -> "PaginatedListApi[User]":
        """
        Get a paginated list of users for the specified owner (org).

        Args:
            activated: whether the user has been manually deactivated.
            is_admin: whether the user is admin.
            page: a page number within the paginated result set.
            page_size: number of results to return per page.
            search: a search term.

        Returns:
            Paginated list of `User`.

        Examples:
            >>> import asyncio
            >>> import os
            >>> from pycodecov import Codecov
            >>> from pycodecov.enums import Service
            >>> async def main():
            ...     async with Codecov(os.environ["CODECOV_API_TOKEN"]) as codecov:
            ...         service_owners = await codecov.get_service_owners(Service.GITHUB)
            ...         for owner in service_owners:
            ...             print(await owner.get_users())
            >>> asyncio.run(main())
            PaginatedList(...)
        """  # noqa: E501
        params = {}
        optional_params = {
            "activated": activated,
            "is_admin": is_admin,
            "page": page,
            "page_size": page_size,
            "search": search,
        }

        params.update({k: v for k, v in optional_params.items() if v is not None})

        async with self._session.get(
            f"{self.api_url}/{self.service}/{self.username}/users/", params=params
        ) as response:
            data = await response.json()

            if response.ok:
                paginated_list_data = parse_paginated_list_data(data, parse_user_data)
                paginated_list = PaginatedList(
                    paginated_list_data.count,
                    paginated_list_data.results,
                    paginated_list_data.total_pages,
                    parse_user_data,
                    paginated_list_data.next,
                    paginated_list_data.previous,
                    self._token,
                    self._session,
                )

                return parse_paginated_list_api(
                    paginated_list,
                    parse_user_api,
                    owner_username=self.username,
                )

            raise CodecovError(data)


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
