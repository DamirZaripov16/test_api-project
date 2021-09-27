from fixtures.authentication.model import AuthenticationUser
from fixtures.common_models import AuthenticateUserInvalidResponse
from fixtures.constants import ResponseText


class TestAuthUser:
    def test_authenticate_user_with_valid_data(self, app, register_user):
        """
        1. Try to auth user with valid data
        2. Check that status code is 201
        3. Check response
        """
        res = app.authenticate.authenticate(data=register_user.user)
        assert res.status_code == 200, "Check status code"

    def test_authenticate_user_with_random_data(self, app):
        """
        1. Try to auth user with empty random data
        2. Check that status code is 401
        3. Check response
        """
        data = AuthenticationUser.random()
        res = app.authenticate.authenticate(
            data=data, type_response=AuthenticateUserInvalidResponse
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION
        assert res.data.status_code == 401
