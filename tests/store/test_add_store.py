from fixtures.common_models import AuthenticateUserInvalidResponse, MessageResponse
from fixtures.constants import ResponseText
from fixtures.store.model import Store


class TestAddStore:
    def test_add_store(self, app, user_info):
        """
        1. Try to add store
        2. Check that status code is 201
        3. Check response
        """
        data = Store.random()
        res = app.store.add_store(data.name, header=user_info.header)
        assert res.status_code == 201, "Check status code"
        assert res.data.name == data.name

    def test_add_store_wo_auth_header(self, app, user_info):
        """
        1. Try to add store wo auth header
        2. Check that status code is 401
        3. Check response
        """
        data = Store.random()
        res = app.store.add_store(
            name=data.name,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    def test_add_the_same_store(self, app, user_info):
        """
        1. Try to add store with the same data
        2. Check that status code is 400
        3. Check response
        """
        data = Store.random()
        res = app.store.add_store(data.name, header=user_info.header)
        assert res.status_code == 201, "Check status code"
        res_2 = app.store.add_store(
            data.name, header=user_info.header, type_response=MessageResponse
        )
        assert res_2.status_code == 400, "Check status code"
        assert res_2.data.message == ResponseText.MESSAGE_STORE_EXISTS.format(data.name)
