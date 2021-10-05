from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class AddUserBalance(BaseClass):
    balance: int = attr.ib(default=None)

    @staticmethod
    def random():
        return AddUserBalance(
            balance=fake.random_digit(),
        )


@attr.s
class UserBalanceResponse:
    message: str = attr.ib()
    balance: int = attr.ib()
