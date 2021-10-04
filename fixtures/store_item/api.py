from requests import Response

from fixtures.store_item.model import StoreItemResponse, AddStoreItem
from fixtures.validator import Validator
from common.deco import logging as log


class StoreItem(Validator):
    def __init__(self, app):
        self.app = app

    POST_STORE_ITEM = "/item/{}"
    PUT_STORE_ITEM = "/item/{}"
    GET_STORE_ITEM = "/item/{}"

    @log("Add store item")
    def add_store_item(
        self,
        name: str,
        data: AddStoreItem,
        header=None,
        type_response=StoreItemResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItem/storeItemAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_STORE_ITEM.format(name)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Update store item")
    def update_store_item(
        self,
        name: str,
        data: AddStoreItem,
        header=None,
        type_response=StoreItemResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItem/storeItemUpdate # noqa
        """
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.PUT_STORE_ITEM.format(name)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get store item")
    def get_store_item(
        self, name: str, header=None, type_response=StoreItemResponse
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItem/storeItemGet # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_STORE_ITEM.format(name)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
