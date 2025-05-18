from behave import then
from dataclasses import is_dataclass

@then("the response status code should be {expected_code:d}")
def step_status_code(context, expected_code):
    assert context.response.status_code == expected_code, (
        f"Expected status {expected_code}, got {context.response.status_code}"
    )


@then("the response should match {model_name} model")
def step_validate_response_model(context, model_name):
    model_cls = context.models[model_name]
    assert is_dataclass(model_cls), f"{model_name} is not a dataclass"
    model_cls(**context.response.json())
