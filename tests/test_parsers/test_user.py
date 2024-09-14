from pycodecov.enums import Service
from pycodecov.parsers import parse_user_data
from pycodecov.schemas import User


def test_parse_user_data():
    data = {
        "service": "github",
        "username": "string",
        "name": "string",
        "activated": True,
        "is_admin": True,
        "email": "string",
    }

    user = parse_user_data(data)

    assert isinstance(user, User)
    assert user.service == Service.GITHUB
    assert user.username == "string"
    assert user.name == "string"
    assert user.activated
    assert user.is_admin
    assert user.name == "string"
