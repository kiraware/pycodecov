# User

There are two API available for User named Owner API and User API.

## Owner API

There are two API available for Owner API named get_detail and get_users.

### get_detail

get_detail is used to get a single owner by name. Read
[get_detail reference](../reference/api.md#pycodecov.api.Owner.get_detail)
for more details.

!!! example

    === "Facade"

        ```python
        import asyncio
        import os

        from pycodecov import Codecov
        from pycodecov.enums import Service

        CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]

        async def main():
            async with Codecov(CODECOV_API_TOKEN) as codecov:
                service_owners = await codecov.get_service_owners(Service.GITHUB)
                for service_owner in service_owners:
                    print(await service_owner.get_detail())


        asyncio.run(main())
        ```

        Output

        ```console
        Owner(service=<Service.GITHUB: 'github'>, username='jazzband', name='jazzband')
        Owner(service=<Service.GITHUB: 'github'>, username='kiraware', name=None)
        ```

    === "Non Facade"

        ```python
        import asyncio
        import os

        from pycodecov.api import Owner
        from pycodecov.enums import Service

        CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]

        async def main():
            async with Owner(Service.GITHUB, "jazzband", token=CODECOV_API_TOKEN) as service_owner:
                print(await service_owner.get_detail())


        asyncio.run(main())
        ```

        Output:

        ```console
        Owner(service=<Service.GITHUB: 'github'>, username='jazzband', name='jazzband')
        ```

### get_users

get_users is used to get a paginated list of users for the
specified owner (org).
[get_users reference](../reference/api.md#pycodecov.api.Owner.get_users)
for more details.

!!! example

    === "Facade"

        ```python
        import asyncio
        import os

        from pycodecov import Codecov
        from pycodecov.enums import Service

        CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]

        async def main():
            async with Codecov(CODECOV_API_TOKEN) as codecov:
                service_owners = await codecov.get_service_owners(Service.GITHUB)
                for service_owner in service_owners:
                    print(await service_owner.get_users())


        asyncio.run(main())
        ```

        Output

        ```console
        PaginatedListApi(count=467, next='/api/v2/github/jazzband/users?page=2', previous=None, results=[User(service=<Service.GITHUB: 'github'>, username='andersk', name='Anders Kaseorg', activated=False, is_admin=False, email='a******@mit.edu'), User(service=<Service.GITHUB: 'github'>, username='PiDelport', name='Pi Delport', activated=False, is_admin=False, email='p********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='RazerM', name='Frazer McLean', activated=False, is_admin=False, email='f*****@frazermclean.co.uk'), User(service=<Service.GITHUB: 'github'>, username='mariocesar', name='Mario César', activated=False, is_admin=False, email='m*************@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='albertyw', name='Albert Wang', activated=False, is_admin=False, email='g**@albertyw.com'), User(service=<Service.GITHUB: 'github'>, username='asfaltboy', name='Pavel Savchenko', activated=False, is_admin=False, email='p**************@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='mozillazg', name='Huang Huang', activated=False, is_admin=False, email='m***********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='tysonclugg', name='Tyson Clugg', activated=False, is_admin=False, email='t****@clugg.net'), User(service=<Service.GITHUB: 'github'>, username='sergei-maertens', name='Sergei Maertens', activated=False, is_admin=False, email='s*****@maykinmedia.nl'), User(service=<Service.GITHUB: 'github'>, username='hzlmn', name='Oleh Kuchuk', activated=False, is_admin=False, email='k**********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='jibaku', name=None, activated=False, is_admin=False, email=None), User(service=<Service.GITHUB: 'github'>, username='tony', name='Tony Narlock', activated=False, is_admin=False, email='t***@git-pull.com'), User(service=<Service.GITHUB: 'github'>, username='saxix', name='Stefano Apostolico', activated=True, is_admin=False, email='s***********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='jpadilla', name='José Padilla', activated=False, is_admin=False, email='h****@jpadilla.com'), User(service=<Service.GITHUB: 'github'>, username='jaraco', name='Jason R. Coombs', activated=False, is_admin=False, email='j*****@jaraco.com'), User(service=<Service.GITHUB: 'github'>, username='agconti', name='Andrew Conti', activated=False, is_admin=False, email='a*************@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='alex', name='Alex Gaynor', activated=False, is_admin=False, email='a**********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='mvantellingen', name='Michael van Tellingen', activated=False, is_admin=False, email='m******************@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='neithere', name='Andy Mikhailenko', activated=False, is_admin=False, email='n*******@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='pydanny', name='Daniel Feldroy', activated=False, is_admin=False, email='d*****@feldroy.com')], total_pages=24)
        PaginatedListApi(count=1, next=None, previous=None, results=[User(service=<Service.GITHUB: 'github'>, username='kiraware', name=None, activated=True, is_admin=False, email='k********@gmail.com')], total_pages=1)
        ```

    === "Non Facade"

        ```python
        import asyncio
        import os

        from pycodecov.api import Owner
        from pycodecov.enums import Service

        CODECOV_API_TOKEN = os.environ["CODECOV_API_TOKEN"]

        async def main():
            async with Owner(Service.GITHUB, "jazzband", token=CODECOV_API_TOKEN) as service_owner:
                print(await service_owner.get_users())


        asyncio.run(main())
        ```

        Output:

        ```console
        PaginatedListApi(count=467, next='/api/v2/github/jazzband/users?page=2', previous=None, results=[User(service=<Service.GITHUB: 'github'>, username='andersk', name='Anders Kaseorg', activated=False, is_admin=False, email='a******@mit.edu'), User(service=<Service.GITHUB: 'github'>, username='PiDelport', name='Pi Delport', activated=False, is_admin=False, email='p********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='RazerM', name='Frazer McLean', activated=False, is_admin=False, email='f*****@frazermclean.co.uk'), User(service=<Service.GITHUB: 'github'>, username='mariocesar', name='Mario César', activated=False, is_admin=False, email='m*************@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='albertyw', name='Albert Wang', activated=False, is_admin=False, email='g**@albertyw.com'), User(service=<Service.GITHUB: 'github'>, username='asfaltboy', name='Pavel Savchenko', activated=False, is_admin=False, email='p**************@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='mozillazg', name='Huang Huang', activated=False, is_admin=False, email='m***********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='tysonclugg', name='Tyson Clugg', activated=False, is_admin=False, email='t****@clugg.net'), User(service=<Service.GITHUB: 'github'>, username='sergei-maertens', name='Sergei Maertens', activated=False, is_admin=False, email='s*****@maykinmedia.nl'), User(service=<Service.GITHUB: 'github'>, username='hzlmn', name='Oleh Kuchuk', activated=False, is_admin=False, email='k**********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='jibaku', name=None, activated=False, is_admin=False, email=None), User(service=<Service.GITHUB: 'github'>, username='tony', name='Tony Narlock', activated=False, is_admin=False, email='t***@git-pull.com'), User(service=<Service.GITHUB: 'github'>, username='saxix', name='Stefano Apostolico', activated=True, is_admin=False, email='s***********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='jpadilla', name='José Padilla', activated=False, is_admin=False, email='h****@jpadilla.com'), User(service=<Service.GITHUB: 'github'>, username='jaraco', name='Jason R. Coombs', activated=False, is_admin=False, email='j*****@jaraco.com'), User(service=<Service.GITHUB: 'github'>, username='agconti', name='Andrew Conti', activated=False, is_admin=False, email='a*************@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='alex', name='Alex Gaynor', activated=False, is_admin=False, email='a**********@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='mvantellingen', name='Michael van Tellingen', activated=False, is_admin=False, email='m******************@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='neithere', name='Andy Mikhailenko', activated=False, is_admin=False, email='n*******@gmail.com'), User(service=<Service.GITHUB: 'github'>, username='pydanny', name='Daniel Feldroy', activated=False, is_admin=False, email='d*****@feldroy.com')], total_pages=24)
        ```

## User API

There is one API available for User API named get_detail.

### get_detail

get_detail is used to get a single owner by name. Read
[get_detail reference](../reference/api.md#pycodecov.api.User.get_detail)
for more details.

!!! example

    === "Facade"

        ```python
        import asyncio
        import os

        from pycodecov import Codecov
        from pycodecov.enums import Service


        async def main():
            async with Codecov(os.environ["CODECOV_API_TOKEN"]) as codecov:
                service_owners = await codecov.get_service_owners(Service.GITHUB)
                for service_owner in service_owners:
                    users = await service_owner.get_users()
                    for user in users:
                        print(await user.get_detail())


        asyncio.run(main())
        ```

        Output

        ```console
        User(service=<Service.GITHUB: 'github'>, username='andersk', name='Anders Kaseorg', activated=False, is_admin=False, email='a******@mit.edu')
        User(service=<Service.GITHUB: 'github'>, username='PiDelport', name='Pi Delport', activated=False, is_admin=False, email='p********@gmail.com')
        User(service=<Service.GITHUB: 'github'>, username='RazerM', name='Frazer McLean', activated=False, is_admin=False, email='f*****@frazermclean.co.uk')
        ...
        ```

    === "Non Facade"

        ```python
        import asyncio
        import os

        from pycodecov.api import User
        from pycodecov.enums import Service


        async def main():
            async with User(
                Service.GITHUB, "jazzband", "kiraware", token=os.environ["CODECOV_API_TOKEN"]
            ) as user:
                print(await user.get_detail())


        asyncio.run(main())
        ```

        Output:

        ```console
        User(service=<Service.GITHUB: 'github'>, username='kiraware', name=None, activated=False, is_admin=False, email='k********@gmail.com')
        ```
