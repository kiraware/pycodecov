# Codecov API

There is one API available for codecov named get_service_owners.

## get_service_owners

get_service_owners is used to get a paginated list of owners
to which the currently authenticated user has access. Read
[get_service_owners reference](../reference/api.md#pycodecov.api.Codecov.get_service_owners)
for more details.

!!! example

    ```python
    import asyncio
    import os

    from pycodecov import Codecov
    from pycodecov.enums import Service

    CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]

    async def main():
        async with Codecov(CODECOV_API_TOKEN) as codecov:
            service_owners = await codecov.get_service_owners(Service.GITHUB)
            print(service_owners)


    asyncio.run(main())
    ```

    Output:

    ```console
    PaginatedListApi(count=2, next=None, previous=None, results=[Owner(service=<Service.GITHUB: 'github'>, username='jazzband', name='jazzband'), Owner(service=<Service.GITHUB: 'github'>, username='kiraware', name=None)], total_pages=1)
    ```
