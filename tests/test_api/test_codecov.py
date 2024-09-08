import os
from unittest.mock import patch

from pycodecov import Codecov
from pycodecov.api import Owner
from pycodecov.enums import Service

CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]


async def test_get_service_owner():
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

            mocked.assert_called_once_with("/api/v2/github", params={})

            assert len(service_owners) == 1
            assert service_owners.count == 1
            assert service_owners.next is None
            assert service_owners.previous is None
            assert service_owners.total_pages == 1
            assert isinstance(service_owners[0], Owner)
            assert service_owners[0].service == Service.GITHUB
            assert service_owners[0].username == "string"
            assert service_owners[0].name == "string"


async def test_get_service_owner_with_params():
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

            service_owners = await codecov.get_service_owners(
                Service.GITHUB, page=1, page_size=1
            )

            mocked.assert_called_once_with(
                "/api/v2/github", params={"page": "1", "page_size": "1"}
            )

            assert len(service_owners) == 1
            assert service_owners.count == 1
            assert service_owners.next is None
            assert service_owners.previous is None
            assert service_owners.total_pages == 1
            assert isinstance(service_owners[0], Owner)
            assert service_owners[0].service == Service.GITHUB
            assert service_owners[0].username == "string"
            assert service_owners[0].name == "string"
