from aiohttp import ClientSession

from .api import API
from .branch import Branch
from .repo import Repo
from .user import User

__all__ = ["Codecov"]


class Codecov(API):
    """
    Base Codecov API wrapper.
    """

    def __init__(
        self,
        token: str | None = None,
        session: ClientSession | None = None,
    ) -> None:
        API.__init__(self, token, session)

        self.branches = Branch(self._token, self._session)
        self.repos = Repo(self._token, self._session)
        self.users = User(self._token, self._session)
