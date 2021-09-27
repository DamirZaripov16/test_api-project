from fixtures.authentication.api import Authenticate
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.user_info.api import UserInfo


class StoreApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = Register(self)
        self.authenticate = Authenticate(self)
        self.user_info = UserInfo(self)
