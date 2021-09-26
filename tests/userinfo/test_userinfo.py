from fixtures.userinfo.model import UserInfo


class TestUserInfo:
    def test_add_user_info(self, app, authenticate_user):
        """
        Steps.
            1. Try to login with valid data
            2. Check status code is 200
            3. Check response
        """
        data = UserInfo.random()
        res = app.userinfo.add_user_info(
            user_id=authenticate_user.uuid, data=data, header=authenticate_user.header
        )
        assert res.status_code == 200
