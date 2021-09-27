from requests import Response

from fixtures.authentication.model import AuthenticationUser, AuthenticationUserResponse
from fixtures.validator import Validator
from common.deco import logging as log


class Authenticate(Validator):
    def __init__(self, app):
        self.app = app

    POST_AUTHENTICATION = "/auth"

    @log("User Authentication")
    def authenticate(
        self, data: AuthenticationUser, type_response=AuthenticationUserResponse
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth/authUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_AUTHENTICATION}",
            json=data.to_dict(),
        )
        return self.structure(response, type_response=type_response)
