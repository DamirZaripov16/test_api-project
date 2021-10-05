import random

import pytest

from fixtures.common_models import AuthenticateUserInvalidResponse, MessageResponse
from fixtures.constants import ResponseText
from fixtures.store_item.model import AddStoreItem


class TestAddStoreItem:
    def test_add_store_item(self, app, store):
        """
        1. Try to add store item
        2. Check that status code is 201
        3. Check response
        """
        data = AddStoreItem.random()
        res = app.store_item.add_store_item(data.name, data=data, header=store.header)
        assert res.status_code == 201, "Check status code"
        assert res.data.name == data.name

    def test_add_store_item_wo_auth_header(self, app, store):
        """
        1. Try to add store item wo auth header
        2. Check that status code is 401
        3. Check response
        """
        data = AddStoreItem.random()
        res = app.store_item.add_store_item(
            name=data.name,
            data=data,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    def test_add_the_same_store_item(self, app, store):
        """
        1. Try to add the same store item
        2. Check that status code is 400
        3. Check response
        """
        data = AddStoreItem.random()
        res = app.store_item.add_store_item(
            name=data.name,
            data=data,
            header=store.header,
        )
        assert res.status_code == 201, "Check status code"
        res_2 = app.store_item.add_store_item(
            name=data.name,
            data=data,
            header=store.header,
            type_response=MessageResponse,
        )
        assert res_2.status_code == 400, "Check status code"
        assert res_2.data.message == ResponseText.MESSAGE_STORE_ITEM_EXISTS.format(
            data.name
        )

    @pytest.mark.xfail
    @pytest.mark.parametrize("field", ["price", "store_id"])
    def test_add_store_item_wo_data(self, app, store, field):
        """
        1. Try to add store item wo data
        2. Check that status code is 400
        3. Check response
        """
        data = AddStoreItem.random()
        setattr(data, field, None)
        res = app.store_item.add_store_item(
            name=data.name,
            data=data,
            header=store.header,
            type_response=None,
        )
        assert res.status_code == 400, "Check status code"

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        "name", [random.randint(1, 1000), "---", "\xbdR6\x10\x7f", True]
    )
    def test_add_store_item_with_invalid_name(self, app, store, name):
        """
        1. Try to add store item with invalid nameItem
        2. Check that status code is 400
        3. Check response
        """
        data = AddStoreItem.random()
        res = app.store_item.add_store_item(
            name=name,
            data=data,
            header=store.header,
            type_response=None,
        )
        assert res.status_code == 400, "Check status code"
