import os
from unittest.mock import patch

from pycodecov import Codecov, schemas
from pycodecov.api import Owner, User
from pycodecov.enums import Service

CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]


async def test_owner_get_detail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "string", "name": "string"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "string"
            assert service_owner.name == "string"

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "service": "github",
                "username": "string",
                "name": "string",
            }

            service_owner_detail = await service_owner.get_detail()

            mocked.assert_called_with("/api/v2/github/string")

            assert isinstance(service_owner_detail, schemas.Owner)
            assert service_owner_detail.service == Service.GITHUB
            assert service_owner_detail.username == "string"
            assert service_owner_detail.name == "string"


async def test_direct_owner_get_detail():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Owner(
            Service.GITHUB, "string", token=CODECOV_API_TOKEN
        ) as service_owner:
            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "string"
            assert service_owner.name is None

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "service": "github",
                "username": "string",
                "name": "string",
            }

            service_owner_detail = await service_owner.get_detail()

            mocked.assert_called_once_with("/api/v2/github/string")

            assert isinstance(service_owner_detail, schemas.Owner)
            assert service_owner_detail.service == Service.GITHUB
            assert service_owner_detail.username == "string"
            assert service_owner_detail.name == "string"


async def test_owner_get_users():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "string", "name": "string"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "string"
            assert service_owner.name == "string"

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "service": "github",
                        "username": "string",
                        "name": "string",
                        "activated": True,
                        "is_admin": False,
                        "email": "string",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users()

            mocked.assert_called_with("/api/v2/github/string/users", params={})

            assert len(users) == 1
            assert users.count == 1
            assert users.next is None
            assert users.previous is None
            assert users.total_pages == 1
            assert isinstance(users[0], User)
            assert users[0].service == Service.GITHUB
            assert users[0].username == "string"
            assert users[0].name == "string"
            assert users[0].activated
            assert not users[0].is_admin
            assert users[0].email == "string"


async def test_direct_owner_get_users():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Owner(
            Service.GITHUB, "string", token=CODECOV_API_TOKEN
        ) as service_owner:
            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "string"
            assert service_owner.name is None

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "service": "github",
                        "username": "string",
                        "name": "string",
                        "activated": True,
                        "is_admin": False,
                        "email": "string",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users()

            mocked.assert_called_with("/api/v2/github/string/users", params={})

            assert len(users) == 1
            assert users.count == 1
            assert users.next is None
            assert users.previous is None
            assert users.total_pages == 1
            assert isinstance(users[0], User)
            assert users[0].service == Service.GITHUB
            assert users[0].username == "string"
            assert users[0].name == "string"
            assert users[0].activated
            assert not users[0].is_admin
            assert users[0].email == "string"


async def test_owner_get_users_with_params():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"service": "github", "username": "string", "name": "string"},
                ],
                "total_pages": 1,
            }

            service_owners = await codecov.get_service_owners(Service.GITHUB)
            service_owner = service_owners[0]

            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "string"
            assert service_owner.name == "string"

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "service": "github",
                        "username": "string",
                        "name": "string",
                        "activated": True,
                        "is_admin": False,
                        "email": "string",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users(True, False, 1, 1, "string")

            mocked.assert_called_with(
                "/api/v2/github/string/users",
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
            assert users[0].username == "string"
            assert users[0].name == "string"
            assert users[0].activated
            assert not users[0].is_admin
            assert users[0].email == "string"


async def test_direct_owner_get_users_with_params():
    with patch("pycodecov.api.api.ClientSession.get") as mocked:
        async with Owner(
            Service.GITHUB, "string", token=CODECOV_API_TOKEN
        ) as service_owner:
            assert isinstance(service_owner, Owner)
            assert service_owner.service == Service.GITHUB
            assert service_owner.username == "string"
            assert service_owner.name is None

            mocked.return_value.__aenter__.return_value.json.return_value = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "service": "github",
                        "username": "string",
                        "name": "string",
                        "activated": True,
                        "is_admin": False,
                        "email": "string",
                    },
                ],
                "total_pages": 1,
            }

            users = await service_owner.get_users(True, False, 1, 1, "string")

            mocked.assert_called_with(
                "/api/v2/github/string/users",
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
            assert users[0].username == "string"
            assert users[0].name == "string"
            assert users[0].activated
            assert not users[0].is_admin
            assert users[0].email == "string"
