from requests import Response

from fixtures.payment.model import AddPayment, PaymentResponse
from fixtures.validator import Validator
from common.deco import logging as log


class Payment(Validator):
    def __init__(self, app):
        self.app = app

    POST_PAYMENT = "/pay/{}"

    @log("Add payment")
    def add_payment(
        self,
        uuid: int,
        data: AddPayment,
        header=None,
        type_response=PaymentResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/pay/payAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_PAYMENT.format(uuid)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)
