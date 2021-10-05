from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class AddPayment(BaseClass):
    itemId: int = attr.ib(default=None)

    @staticmethod
    def random():
        return AddPayment(
            itemId=fake.random_digit(),
        )


@attr.s
class PaymentResponse:
    message: str = attr.ib()
    balance: float = attr.ib()
    name: str = attr.ib()
    price: int = attr.ib()
