from typing import Any, Callable

from aiohttp import ClientSession

from .. import schemas
from ..exceptions import CodecovError
from ..parsers import parse_paginated_list_data
from ..types import CodecovUrl, T
from .api import API

__all__ = ["PaginatedList"]


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
        token: str | None = None,
        session: ClientSession | None = None,
        next: CodecovUrl | None = None,
        previous: CodecovUrl | None = None,
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
                        self._token,
                        self._session,
                        paginated_list.next,
                        paginated_list.previous,
                    )

                raise CodecovError(data)

        return None

    async def get_next(self) -> "PaginatedList[T] | None":
        return await self._get_next_or_previous(self.next)

    async def get_previous(self) -> "PaginatedList[T] | None":
        return await self._get_next_or_previous(self.previous)
