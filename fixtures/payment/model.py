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
    message = attr.ib(default=None, validator=attr.validators.instance_of(str))
    balance = attr.ib(default=None, validator=attr.validators.instance_of(float))
    name = attr.ib(default=None, validator=attr.validators.instance_of(str))
    price = attr.ib(default=None, validator=attr.validators.instance_of(float))
