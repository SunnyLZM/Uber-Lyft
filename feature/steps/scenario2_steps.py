from behave import *


@given("Bad weather")
def step_given(context):
    context.weather = "bad"

@when("Temperature lower than 30︒F")
def step_when(context):
    context.temperature = 25

@then("Price will increase")
def step_then(context):
    weather = context.weather
    temperature = context.temperature
    if weather == "bad" and temperature < 30:
        assert True
    else:
        assert False