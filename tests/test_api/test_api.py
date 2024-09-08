import os

from aiohttp import ClientSession

from pycodecov.api.api import API

CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]


async def test_api():
    async with API(CODECOV_API_TOKEN) as api:
        assert api._token == CODECOV_API_TOKEN
        assert isinstance(api._session, ClientSession)
        assert str(api._session._base_url) == "https://api.codecov.io"
        assert api._session.headers == {
            "Accept": "application/json",
            "Authorization": f"Bearer {CODECOV_API_TOKEN}",
        }


async def test_api_with_supplied_session():
    async with API(CODECOV_API_TOKEN, ClientSession("https://test.com")) as api:
        assert api._token == CODECOV_API_TOKEN
        assert isinstance(api._session, ClientSession)
        assert str(api._session._base_url) == "https://test.com"


async def test_api_without_token():
    async with API() as api:
        assert api._token is None
        assert isinstance(api._session, ClientSession)
        assert str(api._session._base_url) == "https://api.codecov.io"
        assert api._session.headers == {"Accept": "application/json"}
