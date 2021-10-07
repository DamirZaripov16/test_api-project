from typing import List

from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class AddStoreItem(BaseClass):
    name: str = attr.ib(default=None)
    price: str = attr.ib(default=None)
    store_id: int = attr.ib(default=None)

    @staticmethod
    def random():
        return AddStoreItem(
            name=fake.email().lower(),
            price=fake.random_digit(),
            store_id=fake.random_digit(),
        )


@attr.s
class StoreItemResponse:
    name = attr.ib(default=None, validator=attr.validators.instance_of(str))
    price = attr.ib(default=None, validator=attr.validators.instance_of(float))
    itemID = attr.ib(default=None, validator=attr.validators.instance_of(int))


@attr.s
class GetAllStoreItemResponse:
    items = attr.ib(default=None, validator=attr.validators.instance_of(List))
