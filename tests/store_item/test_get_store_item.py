import pytest
from fixtures.common_models import AuthenticateUserInvalidResponse, MessageResponse
from fixtures.constants import ResponseText


class TestGetStoreItem:
    def test_get_store_item(self, app, store_item):
        """
        1. Try to get store item
        2. Check that status code is 201
        3. Check response
        """
        res = app.store_item.get_store_item(
            store_item.store_item, header=store_item.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.name == store_item.store_item

    def test_get_all_store_items(self, app, store_item):
        """
        1. Try to get all the store items
        2. Check that status code is 200
        3. Check response
        """
        res = app.store_item.get_all_store_items(
            header=store_item.header,
        )
        assert res.status_code == 200, "Check status code"
        assert res.data is not False

    @pytest.mark.xfail
    def test_get_all_store_items_wo_auth_header(self, app, store_item):
        """
        1. Try to get all the store items wo auth header
        2. Check that status code is 401
        3. Check response
        """
        res = app.store_item.get_all_store_items(
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    def test_store_item_info_wo_auth_header(self, app, store_item):
        """
        1. Try to get store item wo auth header
        2. Check that status code is 401
        3. Check response
        """
        res = app.store_item.get_store_item(
            store_item.store_item,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    def test_store_item_with_non_existing_item_name(
        self, app, store_item, non_existing_item_name=1000
    ):
        """
        1. Try to get store item with non-existing item name
        2. Check that status code is 404
        3. Check response
        """
        res = app.store_item.get_store_item(
            name=non_existing_item_name,
            header=store_item.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_STORE_ITEM_NOT_FOUND
