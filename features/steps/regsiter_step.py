from behave import given, when, then

from features.support.models.register import RegisterBody, RegisterResponse


@given("I have a valid registration body")
def step_impl(context):
    context.register_body = RegisterBody.random()

@when("I send a register request")
def step_impl(context):
    context.response = context.api_client.register(
        body=context.register_body
    )