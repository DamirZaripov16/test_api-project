import logging

import pytest

from fixtures.app import StoreApp
from fixtures.authentication.model import (
    AuthenticationUserResponse,
    AuthenticationUserType,
)
from fixtures.register.model import RegisterUser, RegisterUserResponse

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return StoreApp(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    ),


@pytest.fixture
def authenticate_user(app):
    data = RegisterUser.random()
    res_register = app.register.register(data=data, type_response=RegisterUserResponse)
    res_authenticate = app.authenticate.authenticate(
        data=data, type_response=AuthenticationUserResponse
    )
    token = res_authenticate.data.access_token
    header = {"Authorization": f"JWT {token}"}
    user_uuid = res_register.data.uuid
    return AuthenticationUserType(header, user_uuid)
