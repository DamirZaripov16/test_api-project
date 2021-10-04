import pytest

from fixtures.common_models import AuthenticateUserInvalidResponse
from fixtures.constants import ResponseText
from fixtures.store_item.model import AddStoreItem


class TestUpdateStoreItem:
    def test_update_store_item(self, app, user_info):
        """
        1. Try to update store item
        2. Check that status code is 200
        3. Check response
        """
        data = AddStoreItem.random()
        res = app.store_item.update_store_item(
            data.name, data=data, header=user_info.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.name == data.name

    def test_update_store_item_wo_auth_header(self, app, user_info):
        """
        1. Try to update store item wo auth header
        2. Check that status code is 401
        3. Check response
        """
        data = AddStoreItem.random()
        res = app.store_item.update_store_item(
            name=data.name,
            data=data,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    @pytest.mark.xfail
    @pytest.mark.parametrize("field", ["price", "store_id"])
    def test_update_store_item_wo_data(self, app, user_info, field):
        """
        1. Try to update store item wo data
        2. Check that status code is 400
        3. Check response
        """
        data = AddStoreItem.random()
        setattr(data, field, None)
        res = app.store_item.update_store_item(
            name=data.name,
            data=data,
            header=user_info.header,
            type_response=None,
        )
        assert res.status_code == 400, "Check status code"

    @pytest.mark.xfail
    def test_update_store_item_with_invalid_name(self, app, store, invalid_name=5):
        """
        1. Try to update store with nameItem = 5
        2. Check that status code is 400
        3. Check response
        """
        data = AddStoreItem.random()
        res = app.store_item.update_store_item(
            name=invalid_name,
            data=data,
            header=store.header,
            type_response=None,
        )
        assert res.status_code == 400, "Check status code"
