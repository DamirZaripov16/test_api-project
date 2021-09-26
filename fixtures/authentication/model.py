from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class AuthenticationUser(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return AuthenticationUser(username=fake.email(), password=fake.password())


@attr.s
class AuthenticationUserResponse:
    access_token: str = attr.ib()


@attr.s
class AuthenticationUserType:
    header: dict = attr.ib()
    uuid: int = attr.ib()
