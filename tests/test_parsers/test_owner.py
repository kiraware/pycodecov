from pycodecov.enums import Service
from pycodecov.parsers import parse_owner_data
from pycodecov.schemas import Owner


def test_parse_owner_data():
    data = {
        "service": "github",
        "username": "string",
        "name": "string",
    }

    owner = parse_owner_data(data)

    assert isinstance(owner, Owner)
    assert owner.service == Service.GITHUB
    assert owner.username == "string"
    assert owner.name == "string"
