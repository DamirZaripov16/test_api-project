import pytest

from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse
from fixtures.authentication.model import AuthenticationUser


class TestAuthenticationUser:
    def test_authenticate_user_with_valid_data(self, app):
        """
        Steps.
            1. Try to authenticate user with valid data
            2. Check status code is 200
            3. Check response
        """
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER
        res_authenticate = app.authenticate.authenticate(data=data, type_response=None)
        assert res_authenticate.status_code == 200

    def test_authenticate_user_with_unregistred_data(self, app):
        """
        Steps.
            1. Try to authenticate user with invalid data
            2. Check status code is 401
            3. Check response
        """
        data = AuthenticationUser.random()
        res = app.authenticate.authenticate(data=data)
        assert res.status_code == 401

    @pytest.mark.parametrize("field", ["username", "password"])
    def test_auth_empty_data(self, app, field):
        """
        Steps.
            1. Try to login user with empty data
            2. Check that status code is 401
            3. Check response
        """
        data = AuthenticationUser.random()
        setattr(data, field, None)
        res = app.authenticate.authenticate(data)
        assert res.status_code == 401
