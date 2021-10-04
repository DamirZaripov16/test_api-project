from typing import List

from faker import Faker
import attr


fake = Faker()


@attr.s
class Store:
    name: str = attr.ib(default=None)

    @staticmethod
    def random():
        return Store(name=fake.word().lower())


@attr.s
class StoreResponse:
    name: str = attr.ib()
    uuid: int = attr.ib()
    items: List[str] = attr.ib()
