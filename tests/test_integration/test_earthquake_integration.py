from pycodecov import Codecov


async def test_when_request_latest_earthquake_then_pass_without_error():
    async with Codecov() as pycodecov:
        await pycodecov.earthquake.get_latest_earthquake()


async def test_when_request_latest_earthquake_shakemap_then_pass_without_error():
    async with Codecov() as pycodecov:
        latest_earthquake = await pycodecov.earthquake.get_latest_earthquake()
        await latest_earthquake.shakemap.get_content()


async def test_when_request_strong_earthquake_then_pass_without_error():
    async with Codecov() as pycodecov:
        list(await pycodecov.earthquake.get_strong_earthquake())


async def test_when_request_felt_earthquake_then_pass_without_error():
    async with Codecov() as pycodecov:
        list(await pycodecov.earthquake.get_felt_earthquake())
