from typing import List

from faker import Faker
import attr


fake = Faker()


@attr.s
class Store:
    name: str = attr.ib(default=None)

    @staticmethod
    def random():
        return Store(name=fake.email().lower())


@attr.s
class StoreResponse:
    name = attr.ib(default=None, validator=attr.validators.instance_of(str))
    uuid = attr.ib(default=None, validator=attr.validators.instance_of(int))
    items = attr.ib(default=None, validator=attr.validators.instance_of(List))
