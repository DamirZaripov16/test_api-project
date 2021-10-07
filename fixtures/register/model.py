from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class RegisterUser(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return RegisterUser(username=fake.email(), password=fake.password())


@attr.s
class RegisterUserResponse:
    message = attr.ib(default=None, validator=attr.validators.instance_of(str))
    uuid = attr.ib(default=None, validator=attr.validators.instance_of(int))
