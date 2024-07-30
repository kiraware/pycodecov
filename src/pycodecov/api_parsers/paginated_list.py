from typing import Any

from ..api import PaginatedList, PaginatedListApi
from ..types import ApiParser, TApi

__all__ = ["parse_paginated_list_api"]


def parse_paginated_list_api(
    paginated_list: PaginatedList,
    api_parser: ApiParser,
    payload: dict[str, Any],
) -> PaginatedListApi[TApi]:
    """
    Turn paginated list results into it's API form.

    Args:
        paginated_list: a paginated list.
        api_parser: function that turn paginated list results into it's API form.

    Returns:
        A `PaginatedListApi`.

    Examples:
    >>> from pycodecov.api import PaginatedList
    >>> from pycodecov.api_parsers import parse_owner_api
    >>> from pycodecov.parsers import parse_owner_data
    >>> data = {
    ...     "count": 123,
    ...     "next": "http://api.codecov.io/api/v2/github/?page=4",
    ...     "previous": "http://api.codecov.io/api/v2/github/?page=2",
    ...     "results": [
    ...         {"service": "github", "username": "string", "name": "string"},
    ...     ],
    ...     "total_pages": 7,
    ... }
    >>> paginated_list_data = parse_paginated_list_data(data, parse_owner_data)
    >>> paginated_list = PaginatedList(
    ...     paginated_list_data.count,
    ...     paginated_list_data.results,
    ...     paginated_list_data.total_pages,
    ...     parse_owner_data,
    ...     paginated_list_data.next,
    ...     paginated_list_data.previous,
    >>> )
    >>> paginated_list_api = parse_paginated_list_api(paginated_list, parse_owner_api)
    >>> paginated_list_api
    PaginatedList(...)
    """
    results = [
        api_parser(result, paginated_list._token, paginated_list._session, **payload)
        for result in paginated_list
    ]

    return PaginatedListApi(
        paginated_list.count,
        results,
        paginated_list.total_pages,
        paginated_list.parser,
        api_parser,
        payload,
        paginated_list.next,
        paginated_list.previous,
        paginated_list._token,
        paginated_list._session,
    )
