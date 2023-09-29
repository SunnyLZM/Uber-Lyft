from behave import *

@given("Bad weather")
def step_given(context):
    context.weather = "bad"

@when("Humidity above 70% ")
def step_when(context):
    context.humidity = 80

@then("Price will increase")
def step_then(context):
    weather = context.weather
    humidity = context.humidity
    if weather == "bad" and humidity < 30:
        assert True
    else:
        assert False


