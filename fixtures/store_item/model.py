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
            name=fake.word().lower(),
            price=fake.random_digit(),
            store_id=fake.random_digit(),
        )


@attr.s
class StoreItemResponse:
    name: str = attr.ib()
    price: int = attr.ib()
    itemID: int = attr.ib()


@attr.s
class GetAllStoreItemResponse:
    items: List[str] = attr.ib()
