from dataclasses import dataclass
from typing import Generic

from ..types import CodecovUrl, T

__all__ = ["PaginatedList"]


# FIXME
# Update generic type syntax according to PEP 695 when mypy supports it.
@dataclass(slots=True)
class PaginatedList(Generic[T]):
    """
    A schema used to store info about paginated list.

    Attributes:
        count: total number of result elements.
        next: codecov uri for the next result page.
        previous: codecov uri for the previous result page.
        results: list of contained elements for the current page.
        total_pages: total result pages.
    """

    count: int
    next: CodecovUrl | None
    previous: CodecovUrl | None
    results: list[T]
    total_pages: int
