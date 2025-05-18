from features.support.api_client import ApiClient
from features.support.logger import setup_logger
from features.support.models.register import RegisterResponse


def before_all(context):
    context.logger = setup_logger()
    context.models = {
        "RegisterResponse": RegisterResponse,
    }
    context.api_client = ApiClient("http://localhost:56733")