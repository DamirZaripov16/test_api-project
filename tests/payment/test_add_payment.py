import pytest

from fixtures.common_models import AuthenticateUserInvalidResponse, MessageResponse
from fixtures.constants import ResponseText
from fixtures.payment.model import AddPayment


class TestAddPayment:
    def test_add_payment(self, app, user_balance):
        """
        1. Try to add payment
        2. Check that status code is 200
        3. Check response
        """
        data = AddPayment.random()
        res = app.payment.add_payment(
            uuid=user_balance.user_uuid, data=data, header=user_balance.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_PAYMENT_ADDED

    def test_add_payment_wo_auth_header(self, app, user_balance):
        """
        1. Try to add payment wo auth header
        2. Check that status code is 401
        3. Check response
        """
        data = AddPayment.random()
        res = app.user_balance.add_user_balance(
            uuid=user_balance.user_uuid,
            data=data,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    @pytest.mark.parametrize("field", ["itemId"])
    def test_add_user_balance_with_empty_data(self, app, user_balance, field):
        """
        1. Try to add payment with empty data
        2. Check that status code is 400
        3. Check response
        """
        data = AddPayment.random()
        setattr(data, field, None)
        res = app.user_balance.add_user_balance(
            uuid=user_balance.user_uuid,
            data=data,
            header=user_balance.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 400, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_PAYMENT_BLANK_ITEM_ID_ADDED

    @pytest.mark.xfail
    @pytest.mark.parametrize("field", ["itemId"])
    def test_add_user_balance_with_invalid_item_id(self, app, user_balance, field):
        """
        1. Try to add payment with invalid itemId
        2. Check that status code is 400
        3. Check response
        """
        data = AddPayment.random()
        setattr(data, field, "123")
        setattr(data, field, -40)
        setattr(data, field, True)
        res = app.user_balance.add_user_balance(
            uuid=user_balance.user_uuid,
            data=data,
            header=user_balance.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 400, "Check status code"
