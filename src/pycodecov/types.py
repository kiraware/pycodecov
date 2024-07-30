from typing import Any, Protocol, TypeVar

from aiohttp import ClientSession

__all__ = [
    "ApiParser",
    "CodecovApiToken",
    "CodecovUrl",
    "T",
    "TApi",
]


CodecovApiToken = str
CodecovUrl = str

T = TypeVar("T")
TApi = TypeVar("TApi")


class ApiParser(Protocol):
    def __call__(
        self,
        schema: Any,
        token: CodecovApiToken | None,
        session: ClientSession | None,
        **kwargs: Any,
    ) -> Any: ...
