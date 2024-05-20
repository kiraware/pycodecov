from .. import schemas
from ..enums import Service
from ..exceptions import CodecovError
from ..parsers import parse_owner_data, parse_paginated_list_data, parse_user_data
from .api import API
from .paginated_list import PaginatedList

__all__ = ["User"]


class User(API):
    """
    User API Wrapper from Codecov API.
    """

    async def get_service_owners(
        self, service: Service, page: int | None = None, page_size: int | None = None
    ) -> PaginatedList[schemas.Owner]:
        """
        Get a paginated list of owners to which the currently authenticated user has
        access.

        Args:
            service: git hosting service provider.
            page: a page number within the paginated result set.
            page_size: number of results to return per page.

        Returns:
            Paginated list of `Owner`.

        Examples:
            >>> import asyncio
            >>> import os
            >>> from pycodecov import Codecov
            >>> from pycodecov.enums import Service
            >>> async def main():
            ...     async with Codecov(os.environ["CODECOV_API_TOKEN"]) as codecov:
            ...         service_owners = await codecov.users.get_service_owners(
            ...             Service.GITHUB
            ...         )
            ...         print(service_owners)
            >>> asyncio.run(main())
            PaginatedList(...)
        """
        params = {}
        optional_params = {
            "page": page,
            "page_size": page_size,
        }

        params.update({k: v for k, v in optional_params.items() if v is not None})

        async with self._session.get(
            f"{self.api_url}/{service}", params=params
        ) as response:
            data = await response.json()

            if response.ok:
                paginated_list = parse_paginated_list_data(data, parse_owner_data)

                return PaginatedList(
                    paginated_list.count,
                    paginated_list.results,
                    paginated_list.total_pages,
                    parse_owner_data,
                    self._token,
                    self._session,
                    paginated_list.next,
                    paginated_list.previous,
                )

            raise CodecovError(data)

    async def get_owner_detail(
        self, service: Service, owner_username: str
    ) -> schemas.Owner:
        """
        Get a single owner by name.

        Args:
            service: git hosting service provider.
            owner_username: username from service provider.

        Returns:
            An `Owner`.

        Examples:
            >>> import asyncio
            >>> from pycodecov import Codecov
            >>> from pycodecov.enums import Service
            >>> async def main():
            ...     async with Codecov() as codecov:
            ...         owner = await codecov.users.get_owner_detail(
            ...             Service.GITHUB, "jazzband"
            ...         )
            ...         print(owner)
            >>> asyncio.run(main())
            Owner(service=<Service.GITHUB: 'github'>, username='jazzband', name='jazzband')
        """  # noqa: E501
        async with self._session.get(
            f"{self.api_url}/{service}/{owner_username}"
        ) as response:
            data = await response.json()

            if response.ok:
                return parse_owner_data(data)

            raise CodecovError(data)

    async def get_user_list(
        self,
        service: Service,
        owner_username: str,
        activated: bool | None = None,
        is_admin: bool | None = None,
        page: int | None = None,
        page_size: int | None = None,
        search: str | None = None,
    ) -> PaginatedList[schemas.User]:
        """
        Get a paginated list of users for the specified owner (org).

        Args:
            service: git hosting service provider.
            owner_username: username from service provider.
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
            ...         users = await codecov.users.get_user_list(
            ...             Service.GITHUB, "jazzband"
            ...         )
            ...         print(users)
            >>> asyncio.run(main())
            PaginatedList(...)
        """
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
            f"{self.api_url}/{service}/{owner_username}/users/", params=params
        ) as response:
            data = await response.json()

            if response.ok:
                paginated_list = parse_paginated_list_data(data, parse_user_data)

                return PaginatedList(
                    paginated_list.count,
                    paginated_list.results,
                    paginated_list.total_pages,
                    parse_user_data,
                    self._token,
                    self._session,
                    paginated_list.next,
                    paginated_list.previous,
                )

            raise CodecovError(data)
