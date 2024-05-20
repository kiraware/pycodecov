from unittest.mock import MagicMock

import pytest

from pycodecov.exceptions import CodecovValidationError
from pycodecov.parsers import parse_forecast_element


def test_parse_element_with_invalid_attribute():
    element = MagicMock()
    element.get.return_value = None

    with pytest.raises(
        CodecovValidationError, match="domain attribute in forecast tag not found"
    ):
        parse_forecast_element(element)
