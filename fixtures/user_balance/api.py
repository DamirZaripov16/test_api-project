from requests import Response

from fixtures.user_balance.model import (
    AddUserBalance,
    UserBalanceResponse,
    GetUserBalanceResponse,
)
from fixtures.validator import Validator
from common.deco import logging as log


class UserBalance(Validator):
    def __init__(self, app):
        self.app = app

    POST_USER_BALANCE = "/balance/{}"
    GET_USER_BALANCE = "/balance/{}"

    @log("Add user balance")
    def add_user_balance(
        self,
        uuid: int,
        data: AddUserBalance,
        header=None,
        type_response=UserBalanceResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userBalance/userBalanceAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USER_BALANCE.format(uuid)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get user balance")
    def get_user_balance(
        self,
        uuid: int,
        header=None,
        type_response=GetUserBalanceResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userBalance/userBalanceGet # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_USER_BALANCE.format(uuid)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
