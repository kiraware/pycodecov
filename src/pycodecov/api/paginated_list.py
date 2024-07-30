from typing import Any, Callable

from aiohttp import ClientSession

from .. import schemas
from ..api_parsers import parse_paginated_list_api
from ..exceptions import CodecovError
from ..parsers import parse_paginated_list_data
from ..types import ApiParser, CodecovApiToken, CodecovUrl, T, TApi
from .api import API

__all__ = [
    "PaginatedList",
    "PaginatedListApi",
]


class PaginatedList(API, schemas.PaginatedList[T]):
    """
    Paginated list API Wrapper from Codecov API.
    """

    def __init__(
        self,
        count: int,
        results: list[T],
        total_pages: int,
        parser: Callable[[dict[str, Any]], T],
        next: CodecovUrl | None = None,
        previous: CodecovUrl | None = None,
        token: CodecovApiToken | None = None,
        session: ClientSession | None = None,
    ) -> None:
        API.__init__(self, token, session)
        schemas.PaginatedList.__init__(
            self, count, next, previous, results, total_pages
        )
        self.parser = parser

    async def _get_next_or_previous(
        self, next_or_previous: str | None
    ) -> "PaginatedList[T] | None":
        if next_or_previous is not None:
            async with self._session.get(next_or_previous) as response:
                data = await response.json()

                if response.ok:
                    paginated_list = parse_paginated_list_data(data, self.parser)

                    return PaginatedList(
                        paginated_list.count,
                        paginated_list.results,
                        paginated_list.total_pages,
                        self.parser,
                        paginated_list.next,
                        paginated_list.previous,
                        self._token,
                        self._session,
                    )

                raise CodecovError(data)

        return None

    async def get_next(self) -> "PaginatedList[T] | None":
        return await self._get_next_or_previous(self.next)

    async def get_previous(self) -> "PaginatedList[T] | None":
        return await self._get_next_or_previous(self.previous)


class PaginatedListApi(API, schemas.PaginatedList[TApi]):
    """
    Paginated list API Wrapper from Codecov API.
    """

    def __init__(
        self,
        count: int,
        results: list[TApi],
        total_pages: int,
        parser: Callable[[dict[str, Any]], T],
        api_parser: ApiParser,
        payload: dict[str, Any],
        next: CodecovUrl | None = None,
        previous: CodecovUrl | None = None,
        token: CodecovApiToken | None = None,
        session: ClientSession | None = None,
    ) -> None:
        API.__init__(self, token, session)
        schemas.PaginatedList.__init__(
            self, count, next, previous, results, total_pages
        )
        self.parser = parser
        self.api_parser = api_parser
        self.payload = payload

    async def _get_next_or_previous(
        self, next_or_previous: str | None
    ) -> "PaginatedListApi[TApi] | None":
        if next_or_previous is not None:
            async with self._session.get(next_or_previous) as response:
                data = await response.json()

                if response.ok:
                    paginated_list_data = parse_paginated_list_data(data, self.parser)

                    paginated_list = PaginatedList(
                        paginated_list_data.count,
                        paginated_list_data.results,
                        paginated_list_data.total_pages,
                        self.parser,
                        paginated_list_data.next,
                        paginated_list_data.previous,
                        self._token,
                        self._session,
                    )

                    return parse_paginated_list_api(
                        paginated_list, self.api_parser, **self.payload
                    )

                raise CodecovError(data)

        return None

    async def get_next(self) -> "PaginatedListApi[TApi] | None":
        return await self._get_next_or_previous(self.next)

    async def get_previous(self) -> "PaginatedListApi[TApi] | None":
        return await self._get_next_or_previous(self.previous)
