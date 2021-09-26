from fixtures.authentication.api import Authenticate
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.userinfo.api import Userinfo


class StoreApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = Register(self)
        self.authenticate = Authenticate(self)
        self.userinfo = Userinfo(self)
