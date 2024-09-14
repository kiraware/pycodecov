# Codecov API

There is one API available for Codecov API named get_service_owners.

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

    If you want to use pagination, you can pass `page` and `page_size` parameters
    to get_service_owners.

    ```python
    ...
    service_owners = await codecov.get_service_owners(Service.GITHUB, 1, 1)
    ...
    ```

    Output:

    ```console
    PaginatedListApi(count=2, next='/api/v2/github/?page=2&page_size=1', previous=None, results=[Owner(service=<Service.GITHUB: 'github'>, username='jazzband', name='jazzband')], total_pages=2)
    ```
