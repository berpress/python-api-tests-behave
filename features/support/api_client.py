import requests
from requests import Response

from features.support.logs import logging as log
from features.support.models.auth import AuthBody
from features.support.models.register import RegisterBody


class ApiClient:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    _POST_REGISTER = "/register"
    _POST_AUTH = "/auth"

    @log("Try to register new user")
    def register(self, body: RegisterBody) -> Response:
        return self.session.post(url=f"{self.url}{self._POST_REGISTER}", json=body.__dict__)

    @log("Try to auth registered user")
    def auth(self, body: AuthBody) -> Response:
        return self.session.post(url=f"{self.url}{self._POST_AUTH}", json=body.__dict__)