from unittest.mock import MagicMock

import pytest

from pycodecov.exceptions import CodecovValidationError
from pycodecov.parsers import parse_issue_element


def test_parse_element_with_invalid_attribute():
    element = MagicMock()
    element.find.return_value = None

    with pytest.raises(
        CodecovValidationError, match="timestamp tag in issue tag not found"
    ):
        parse_issue_element(element)


def test_parse_element_with_invalid_humidity_text():
    timestamp = MagicMock()
    timestamp.text = None

    element = MagicMock()
    element.find.return_value = timestamp
    with pytest.raises(
        CodecovValidationError, match="timestamp tag in issue tag has no text"
    ):
        parse_issue_element(element)
