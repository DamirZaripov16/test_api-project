import random

from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class AddUserBalance(BaseClass):
    balance: float = attr.ib(default=None)

    @staticmethod
    def random():
        return AddUserBalance(
            balance=random.randint(10, 20),
        )


@attr.s
class UserBalanceResponse:
    message = attr.ib(default=None, validator=attr.validators.instance_of(str))
    balance = attr.ib(default=None, validator=attr.validators.instance_of(float))


@attr.s
class GetUserBalanceResponse:
    message = attr.ib(default=None, validator=attr.validators.instance_of(str))
    balance = attr.ib(default=None, validator=attr.validators.instance_of(float))
