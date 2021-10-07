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
    access_token = attr.ib(default=None, validator=attr.validators.instance_of(str))
