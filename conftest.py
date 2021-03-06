import logging

import pytest

from fixtures.app import StoreApp
from fixtures.common_models import UserStore
from fixtures.payment.model import AddPayment
from fixtures.register.model import RegisterUser
from fixtures.store.model import Store
from fixtures.store_item.model import AddStoreItem
from fixtures.user_balance.model import AddUserBalance
from fixtures.user_info.model import AddUserInfo

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return StoreApp(url)


@pytest.fixture
def register_user(app) -> UserStore:
    """
    Register new user
    """
    data = RegisterUser.random()
    res = app.register.register(data=data)
    data = UserStore(user=data, user_uuid=res.data.uuid)
    return data


@pytest.fixture
def authenticate_user(app, register_user) -> UserStore:
    """
    Login user
    """
    res = app.authenticate.authenticate(data=register_user.user)
    token = res.data.access_token
    header = {"Authorization": f"JWT {token}"}
    data = UserStore(**register_user.to_dict())
    data.header = header
    return data


@pytest.fixture
def user_info(app, authenticate_user) -> UserStore:
    """
    Add user info
    """
    data = AddUserInfo.random()
    app.user_info.add_user_info(
        uuid=authenticate_user.user_uuid, data=data, header=authenticate_user.header
    )
    data_user = UserStore(**authenticate_user.to_dict())
    data_user.user_info = data
    return data_user


@pytest.fixture
def store(app, user_info) -> UserStore:
    """
    Add store
    """
    data = Store.random()
    app.store.add_store(data.name, header=user_info.header)
    data_store = UserStore(**user_info.to_dict())
    data_store.store = data.name
    return data_store


@pytest.fixture
def store_item(app, store) -> UserStore:
    """
    Add store item
    """
    data = AddStoreItem.random()
    app.store_item.add_store_item(data.name, data=data, header=store.header)
    data_store_item = UserStore(**store.to_dict())
    data_store_item.store_item = data.name
    return data_store_item


@pytest.fixture
def user_balance(app, store_item) -> UserStore:
    """
    Add user balance
    """
    data = AddUserBalance.random()
    app.user_balance.add_user_balance(
        uuid=store_item.user_uuid, data=data, header=store_item.header
    )
    data_user_balance = UserStore(**store_item.to_dict())
    data_user_balance.user_balance = data
    return data_user_balance


@pytest.fixture
def pay(app, user_balance) -> UserStore:
    """
    Add payment
    """
    data = AddPayment.random()
    app.payment.add_payment(
        uid=user_balance.user_uuid, data=data, header=user_balance.header
    )
    data_pay = UserStore(**user_balance.to_dict())
    data_pay.pay = data
    return data_pay


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    ),
