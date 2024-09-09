import os
from unittest.mock import patch

import pytest

from pycodecov import Codecov, schemas
from pycodecov.api import Owner, User
from pycodecov.api.owner import parse_owner_api
from pycodecov.enums import Service
from pycodecov.exceptions import CodecovError

CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]


async def test_owner_get_detail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "jazzband", "name": "test"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "jazzband"
            assert service_owner.name == "test"

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "service": "github",
                "username": "jazzband",
                "name": "test",
            }

            service_owner_detail = await service_owner.get_detail()

            mocked.assert_called_with("/api/v2/github/jazzband")

            assert isinstance(service_owner_detail, schemas.Owner)
            assert service_owner_detail.service == Service.GITHUB
            assert service_owner_detail.username == "jazzband"
            assert service_owner_detail.name == "test"


async def test_direct_owner_get_detail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Owner(
            Service.GITHUB, "jazzband", token=CODECOV_API_TOKEN
        ) as service_owner:
            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "jazzband"
            assert service_owner.name is None

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "service": "github",
                "username": "jazzband",
                "name": "test",
            }

            service_owner_detail = await service_owner.get_detail()

            mocked.assert_called_once_with("/api/v2/github/jazzband")

            assert isinstance(service_owner_detail, schemas.Owner)
            assert service_owner_detail.service == Service.GITHUB
            assert service_owner_detail.username == "jazzband"
            assert service_owner_detail.name == "test"


async def test_owner_get_detail_fail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "jazzband", "name": "test"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "error": "msg"
            }
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(CodecovError, match="{'error': 'msg'}"):
                await service_owner.get_detail()

            mocked.assert_called_with("/api/v2/github/jazzband")


async def test_direct_owner_get_detail_fail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Owner(Service.GITHUB, "jazzband", token=CODECOV_API_TOKEN) as owner:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "error": "msg"
            }
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(CodecovError, match="{'error': 'msg'}"):
                await owner.get_detail()

            mocked.assert_called_once_with("/api/v2/github/jazzband")


async def test_owner_get_users():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "jazzband", "name": "test"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "jazzband"
            assert service_owner.name == "test"

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
                        "email": "test@email",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users()

            mocked.assert_called_with("/api/v2/github/jazzband/users", params={})

            assert len(users) == 1
            assert users.count == 1
            assert users.next is None
            assert users.previous is None
            assert users.total_pages == 1
            assert isinstance(users[0], User)
            assert users[0].service == Service.GITHUB
            assert users[0].username == "kiraware"
            assert users[0].name is None
            assert users[0].activated
            assert not users[0].is_admin
            assert users[0].email == "test@email"


async def test_direct_owner_get_users():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Owner(
            Service.GITHUB, "jazzband", token=CODECOV_API_TOKEN
        ) as service_owner:
            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "jazzband"
            assert service_owner.name is None

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
                        "email": "test@email",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users()

            mocked.assert_called_with("/api/v2/github/jazzband/users", params={})

            assert len(users) == 1
            assert users.count == 1
            assert users.next is None
            assert users.previous is None
            assert users.total_pages == 1
            assert isinstance(users[0], User)
            assert users[0].service == Service.GITHUB
            assert users[0].username == "kiraware"
            assert users[0].name is None
            assert users[0].activated
            assert not users[0].is_admin
            assert users[0].email == "test@email"


async def test_owner_get_users_with_params():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "jazzband", "name": "test"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "jazzband"
            assert service_owner.name == "test"

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
                        "email": "test@email",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users(True, False, 1, 1, "string")

            mocked.assert_called_with(
                "/api/v2/github/jazzband/users",
                params={
                    "activated": "true",
                    "is_admin": "false",
                    "page": "1",
                    "page_size": "1",
                    "search": "string",
                },
            )

            assert len(users) == 1
            assert users.count == 1
            assert users.next is None
            assert users.previous is None
            assert users.total_pages == 1
            assert isinstance(users[0], User)
            assert users[0].service == Service.GITHUB
            assert users[0].username == "kiraware"
            assert users[0].name is None
            assert users[0].activated
            assert not users[0].is_admin
            assert users[0].email == "test@email"


async def test_direct_owner_get_users_with_params():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Owner(
            Service.GITHUB, "jazzband", token=CODECOV_API_TOKEN
        ) as service_owner:
            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "jazzband"
            assert service_owner.name is None

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
                        "email": "test@email",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users(True, False, 1, 1, "string")

            mocked.assert_called_with(
                "/api/v2/github/jazzband/users",
                params={
                    "activated": "true",
                    "is_admin": "false",
                    "page": "1",
                    "page_size": "1",
                    "search": "string",
                },
            )

            assert len(users) == 1
            assert users.count == 1
            assert users.next is None
            assert users.previous is None
            assert users.total_pages == 1
            assert isinstance(users[0], User)
            assert users[0].service == Service.GITHUB
            assert users[0].username == "kiraware"
            assert users[0].name is None
            assert users[0].activated
            assert not users[0].is_admin
            assert users[0].email == "test@email"


async def test_owner_get_users_fail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "jazzband", "name": "test"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "error": "msg"
            }
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(CodecovError, match="{'error': 'msg'}"):
                await service_owner.get_users()

            mocked.assert_called_with("/api/v2/github/jazzband/users", params={})


async def test_direct_owner_get_users_fail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Owner(
            Service.GITHUB, "jazzband", token=CODECOV_API_TOKEN
        ) as service_owner:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "error": "msg"
            }
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(CodecovError, match="{'error': 'msg'}"):
                await service_owner.get_users()

            mocked.assert_called_with("/api/v2/github/jazzband/users", params={})


async def test_parse_owner_api():
    owner = schemas.Owner(Service.GITHUB, "kiraware", None)
    owner_api = parse_owner_api(owner)

    assert isinstance(owner_api, Owner)
    assert owner_api.service == Service.GITHUB
    assert owner_api.username == "kiraware"
    assert owner_api.name is None
