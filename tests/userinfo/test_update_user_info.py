import pytest

from fixtures.common_models import AuthenticateUserInvalidResponse, MessageResponse
from fixtures.constants import ResponseText
from fixtures.user_info.model import AddUserInfo


class TestUserInfo:
    def test_update_user_info(self, app, user_info):
        """
        1. Try to update user info
        2. Check that status code is 200
        3. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            uuid=user_info.user_uuid, data=data, header=user_info.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_UPDATE_USER_INFO

    def test_update_user_info_wo_authentication_header(self, app, user_info):
        """
        1. Try to update user info wo auth header
        2. Check that status code is 401
        3. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            uuid=user_info.user_uuid,
            data=data,
            header=None,
            type_response=AuthenticateUserInvalidResponse,
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT
        assert res.data.status_code == 401, "Check status code"

    def test_update_user_with_non_existing_user_id(
        self, app, user_info, non_existing_user=1000
    ):
        """
        1. Try to update user info with none exist user id
        2. Check that status code is 404
        3. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            uuid=non_existing_user,
            data=data,
            header=user_info.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_INFO_NOT_FOUND_DOT

    def test_update_userinfo_wo_header(self, app, user_info):
        """
        Steps.
            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Check that status code is 200
            5. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            uuid=user_info.user_uuid,
            data=data,
            header=None,
            type_response=AuthenticateUserInvalidResponse
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_ERROR
        assert res.data.error == ResponseText.ERROR_AUTHENTICATION_TEXT

    def test_update_userinfo_w_invalid_header(self, app, user_info):
        """
        Steps.
            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Check that status code is 200
            5. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            uuid=user_info.user_uuid,
            data=data,
            header={"Authorization": "JWT 895241"},
            type_response=AuthenticateUserInvalidResponse
        )
        assert res.status_code == 401
        assert res.data.description == ResponseText.DESCRIPTION_AUTHENTICATION_SEGMENTS_ERROR
        assert res.data.error == ResponseText.DESCRIPTION_AUTHENTICATION_INVALID_TOKEN_ERROR

    @pytest.mark.parametrize("uuid", ["invalid_id", "!!!", -35, True])
    def test_update_invalid_id_userinfo(self, app, user_info, uuid):
        """
        Steps.
            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Check that status code is 200
            5. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            uuid=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 404
