from fixtures.authentication.api import Authenticate
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.store.api import Store
from fixtures.store_item.api import StoreItem
from fixtures.user_balance.api import UserBalance
from fixtures.user_info.api import UserInfo


class StoreApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = Register(self)
        self.authenticate = Authenticate(self)
        self.user_info = UserInfo(self)
        self.store = Store(self)
        self.store_item = StoreItem(self)
        self.user_balance = UserBalance(self)
