from unittest.mock import MagicMock

import pytest

from pycodecov.exceptions import CodecovValidationError
from pycodecov.parsers import parse_datetime_element


def test_parse_element_with_invalid_attribute():
    timerange = MagicMock()
    timerange.get.return_value = None

    element = MagicMock()
    element.__iter__.return_value = [timerange]
    with pytest.raises(
        CodecovValidationError, match="datetime attribute in timerange tag not found"
    ):
        for dt in parse_datetime_element(element):
            pass
