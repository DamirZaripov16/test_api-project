from fixtures.common_models import AuthenticateUserInvalidResponse, MessageResponse
from fixtures.constants import ResponseText
from fixtures.store.model import Store


class TestGetStore:
    def test_get_store(self, app, store):
        """
        1. Try to get store
        2. Check that status code is 201
        3. Check response
        """
        res = app.store.get_store(store.store, header=store.header)
        assert res.status_code == 200, "Check status code"
        assert res.data.name == store.store

    def test_get_store_wo_auth_header(self, app, user_info):
        """
        1. Try to get store wo auth header
        2. Check that status code is 401
        3. Check response
        """
        data = Store.random()
        res = app.store.get_store(
            name=data.name,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    def test_get_store_with_non_existing_name(self, app, user_info):
        """
        1. Try to double add with same data
        2. Check that status code is 404
        3. Check response
        """
        data = Store("Non-existing store")
        res = app.store.get_store(
            data.name, header=user_info.header, type_response=MessageResponse
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_STORE_NOT_FOUND
