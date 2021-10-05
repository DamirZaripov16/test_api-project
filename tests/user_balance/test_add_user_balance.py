import pytest

from fixtures.common_models import AuthenticateUserInvalidResponse, MessageResponse
from fixtures.constants import ResponseText
from fixtures.user_balance.model import AddUserBalance


class TestAddUserBalance:
    def test_add_user_balance(self, app, store_item):
        """
        1. Try to add user balance
        2. Check that status code is 201
        3. Check response
        """
        data = AddUserBalance.random()
        res = app.user_balance.add_user_balance(
            uuid=store_item.user_uuid, data=data, header=store_item.header
        )
        assert res.status_code == 201, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_ADDED_USER_BALANCE.format(
            float(data.balance)
        )

    def test_add_user_balance_wo_auth_header(self, app, store_item):
        """
        1. Try to add user balance wo auth header
        2. Check that status code is 401
        3. Check response
        """
        data = AddUserBalance.random()
        res = app.user_balance.add_user_balance(
            uuid=store_item.user_uuid,
            data=data,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    @pytest.mark.xfail
    @pytest.mark.parametrize("field", ["balance"])
    def test_add_user_balance_with_empty_data(self, app, store_item, field):
        """
        1. Try to add user balance with empty data
        2. Check that status code is 400
        3. Check response
        """
        data = AddUserBalance.random()
        setattr(data, field, None)
        res = app.user_balance.add_user_balance(
            uuid=store_item.user_uuid,
            data=data,
            header=store_item.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 400, "Check status code"

    @pytest.mark.xfail
    @pytest.mark.parametrize("balance", ["123", -40, True])
    def test_add_user_balance_with_invalid_balance(self, app, store_item, balance):
        """
        1. Try to add user balance with invalid balance
        2. Check that status code is 400
        3. Check response
        """
        data = AddUserBalance.random()
        res = app.user_balance.add_user_balance(
            uuid=store_item.user_uuid,
            data=data,
            header=store_item.header,
            type_response=None,
        )
        assert res.status_code == 400, "Check status code"
