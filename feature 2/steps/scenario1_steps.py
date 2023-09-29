from behave import *

@given("Rush time")
def step_given(context):
    if context.hour >8 and context.hour <10:
        context.hour = "rush hour"
    if context.hour >16 and context.hour <18:
        context.hour = "rush hour"

@when("daytime between hours between 7 am-8 am and daytime between hours between 4 pm-5 pm")
def step_when(context):
    if context.hour > 7 and context.hour < 8:
        pass

@then("Price will increase")
def step_then(context):
    hour = context.hour
    if hour == "rush hour":
        assert True
    else:
        assert False