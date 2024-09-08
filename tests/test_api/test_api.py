from aiohttp import ClientSession

from pycodecov.api.api import API


async def test_api():
    async with API("CODECOV_API_TOKEN") as api:
        assert api._token == "CODECOV_API_TOKEN"
        assert isinstance(api._session, ClientSession)
        assert str(api._session._base_url) == "https://api.codecov.io"
        assert api._session.headers == {
            "Accept": "application/json",
            "Authorization": "Bearer CODECOV_API_TOKEN",
        }


async def test_api_without_token():
    async with API() as api:
        assert api._token is None
        assert isinstance(api._session, ClientSession)
        assert str(api._session._base_url) == "https://api.codecov.io"
        assert api._session.headers == {"Accept": "application/json"}
