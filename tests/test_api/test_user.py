import os
from unittest.mock import patch

import pytest

from pycodecov import Codecov, schemas
from pycodecov.api import User
from pycodecov.api.user import parse_user_api
from pycodecov.enums import Service
from pycodecov.exceptions import CodecovError

CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]


async def test_user_get_detail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "jazzband", "name": "jazzband"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "service": "github",
                        "username": "kiraware",
                        "name": None,
                        "activated": True,
                        "is_admin": False,
                        "email": "test@email.com",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users()
            user = users[0]

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "service": "github",
                "username": "kiraware",
                "name": None,
                "activated": False,
                "is_admin": True,
                "email": "test@email.com",
            }

            user_detail = await user.get_detail()

            mocked.assert_called_with("/api/v2/github/jazzband/users/kiraware")

            assert isinstance(user_detail, schemas.User)
            assert user_detail.service == Service.GITHUB
            assert user_detail.username == "kiraware"
            assert user_detail.name is None
            assert not user_detail.activated
            assert user_detail.is_admin
            assert user_detail.email == "test@email.com"


async def test_direct_user_get_detail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with User(
            Service.GITHUB, "jazzband", "kiraware", token=CODECOV_API_TOKEN
        ) as user:
            assert isinstance(user, User)
            assert user.service == Service.GITHUB
            assert user.owner_username == "jazzband"
            assert user.username == "kiraware"
            assert user.name is None
            assert user.activated is None
            assert user.is_admin is None
            assert user.email is None

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "service": "github",
                "username": "kiraware",
                "name": None,
                "activated": False,
                "is_admin": True,
                "email": "test@email.com",
            }

            user_detail = await user.get_detail()

            mocked.assert_called_with("/api/v2/github/jazzband/users/kiraware")

            assert isinstance(user_detail, schemas.User)
            assert user_detail.service == Service.GITHUB
            assert user_detail.username == "kiraware"
            assert user_detail.name is None
            assert not user_detail.activated
            assert user_detail.is_admin
            assert user_detail.email == "test@email.com"


async def test_user_get_detail_fail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "jazzband", "name": "jazzband"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "service": "github",
                        "username": "kiraware",
                        "name": None,
                        "activated": True,
                        "is_admin": False,
                        "email": "test@email.com",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users()
            user = users[0]

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "error": "msg"
            }
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(CodecovError, match="{'error': 'msg'}"):
                await user.get_detail()

            mocked.assert_called_with("/api/v2/github/jazzband/users/kiraware")


async def test_direct_user_get_detail_fail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with User(
            Service.GITHUB, "jazzband", "kiraware", token=CODECOV_API_TOKEN
        ) as user:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "error": "msg"
            }
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(CodecovError, match="{'error': 'msg'}"):
                await user.get_detail()

            mocked.assert_called_with("/api/v2/github/jazzband/users/kiraware")


async def test_parse_user_api():
    user = schemas.User(Service.GITHUB, "kiraware", None, True, False, "test@email.com")
    user_api = parse_user_api(user, owner_username="jazzband")

    assert isinstance(user_api, User)
    assert user_api.service == Service.GITHUB
    assert user_api.owner_username == "jazzband"
    assert user_api.username == "kiraware"
    assert user_api.name is None
    assert user_api.activated
    assert not user_api.is_admin
    assert user_api.email == "test@email.com"
