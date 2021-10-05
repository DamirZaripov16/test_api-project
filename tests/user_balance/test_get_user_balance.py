from fixtures.common_models import AuthenticateUserInvalidResponse, MessageResponse
from fixtures.constants import ResponseText


class TestGetUserBalance:
    def test_get_user_balance(self, app, user_balance):
        """
        1. Try to get user balance
        2. Check that status code is 200
        3. Check response
        """
        res = app.user_balance.get_user_balance(
            uuid=user_balance.user_uuid, header=user_balance.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_USER_BALANCE_INFO.format(
            float(res.data.balance)
        )

    def test_get_user_balance_wo_auth_header(self, app, user_balance):
        """
        1. Try to get user balance wo auth header
        2. Check that status code is 401
        3. Check response
        """
        res = app.user_balance.get_user_balance(
            uuid=user_balance.user_uuid,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    def test_user_balance_with_non_existing_user(
        self, app, user_balance, non_existing_user=1000
    ):
        """
        1. Try to get user balance with non-existing user id
        2. Check that status code is 404
        3. Check response
        """
        res = app.user_balance.get_user_balance(
            uuid=non_existing_user,
            header=user_balance.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_USER_BALANCE_NOT_FOUND
