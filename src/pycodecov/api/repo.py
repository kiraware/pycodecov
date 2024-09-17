from datetime import datetime
from typing import Any

from aiohttp import ClientSession

from .. import schemas
from ..enums import Language, Service
from ..exceptions import CodecovError
from ..parsers import parse_repo_data
from ..types import CodecovApiToken
from .api import API
from .owner import Owner

__all__ = [
    "Repo",
    "parse_repo_api",
]


class Repo(API, schemas.Repo):
    """
    Repo API Wrapper from Codecov API.
    """

    def __init__(
        self,
        service: Service,
        owner_username: str,
        user_username_or_ownerid: str,
        name: str,
        private: bool,
        updatestamp: datetime | None,
        author: Owner,
        language: Language | None,
        branch: str,
        active: bool | None,
        activated: bool | None,
        totals: schemas.CommitTotal | None,
        token: CodecovApiToken | None = None,
        session: ClientSession | None = None,
    ) -> None:
        API.__init__(self, token, session)
        schemas.Repo.__init__(
            self,
            name,
            private,
            updatestamp,
            author,
            language,
            branch,
            active,
            activated,
            totals,
        )

        self.service = service
        self.owner_username = owner_username
        self.user_username_or_ownerid = user_username_or_ownerid

    async def get_detail(
        self, service: Service, owner_username: str, repo_name: str
    ) -> schemas.Repo:
        """
        Get a single repository by name.

        Args:
            service: git hosting service provider.
            owner_username: username from service provider.
            repo_name: repository name.

        Returns:
            A `Repo`.

        Examples:
            >>> import asyncio
            >>> import os
            >>> from pycodecov import Codecov
            >>> async def main():
            ...     async with Codecov(os.environ["CODECOV_API_TOKEN"]) as codecov:
            ...         repo = await codecov.repos.get_repo_detail(
            ...             Service.GITHUB, "jazzband", "django-silk"
            ...         )
            ...         print(repo)
            >>> asyncio.run(main())
            Repo(...)
        """
        async with self._session.get(
            f"{self.api_url}/{service}/{owner_username}/repos/{repo_name}/"
        ) as response:
            data = await response.json()

            if response.ok:
                return parse_repo_data(data)

            raise CodecovError(data)

    async def get_repo_config(
        self,
        service: Service,
        owner_username: str,
        repo_name: str,
    ) -> schemas.RepoConfig:
        """
        Returns a repository config by name.

        Args:
            service: git hosting service provider.
            owner_username: username from service provider.
            repo_name: repository name.

        Returns:
            A `RepoConfig`.

        Examples:
            >>> import asyncio
            >>> import os
            >>> from pycodecov import Codecov
            >>> from pycodecov.enums import Service
            >>> async def main():
            ...     async with Codecov(os.environ["CODECOV_API_TOKEN"]) as codecov:
            ...         repo_config = await codecov.repos.get_repo_config(
            ...             Service.GITHUB, "jazzband", "django-silk"
            ...         )
            ...         print(repo_config)
            >>> asyncio.run(main())
            RepoConfig(...)
        """
        async with self._session.get(
            f"{self.api_url}/{service}/{owner_username}/repos/{repo_name}/config/"
        ) as response:
            data = await response.json()

            if response.ok:
                return parse_repo_config_data(data)

            raise CodecovError(data)


def parse_repo_api(
    schema: schemas.Repo,
    token: CodecovApiToken | None = None,
    session: ClientSession | None = None,
    **kwargs: Any,
) -> User:
    """
    Turn User schema into Repo API.

    Args:
        schema: repo data.
        token: Codecov API Token.
        session: client session.

    Returns:
        A `Repo` API.

    Examples:
    >>> import asyncio
    >>> async def main():
    ...     data = {
    ...         "service": "github",
    ...         "username": "string",
    ...         "name": "string",
    ...         "activated": True,
    ...         "is_admin": True,
    ...         "email": "string",
    ...     }
    ...     userrepo(data)
    ...     user_api = parse_repo_api(user, owner_username="string")
    ...     print(user_api)
    >>> asyncio.run(main())
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
