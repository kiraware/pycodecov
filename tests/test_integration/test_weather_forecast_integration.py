import pytest

from pycodecov import Codecov
from pycodecov.enums import Province, Type


@pytest.mark.parametrize("province", Province)
async def test_given_provinces_when_request_weather_forecast_then_pass_without_error(
    province,
):
    async with Codecov() as pycodecov:
        weather_forecast_data = await pycodecov.weather_forecast.get_weather_forecast(
            province
        )
        for area, weather in weather_forecast_data.weathers.items():
            if area.type == Type.LAND:
                list(weather)
