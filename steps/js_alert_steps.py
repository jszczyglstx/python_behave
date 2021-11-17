from behave import step


@step("Page title is JavaScript Alerts")
def step_impl(context):
    displayed_value = context.page.get_page_title()
    expected_value = "JavaScript Alerts"
    assert displayed_value == expected_value, \
        f"Displayed value: '{displayed_value}' is not equal to Expected value: '{expected_value}'"


@step("User clicks JS Alert")
def step_impl(context):
    context.page.click_js_alert_button()


@step("User accepts popup")
def step_impl(context):
    context.page.accept_alert()
    displayed_result = context.page.get_result()
    expected_result = "You successfully clicked an alert"
    assert displayed_result == expected_result, \
        f"{displayed_result} is not equal {expected_result}"


@step("User clicks JS Confirm")
def step_impl(context):
    context.page.click_js_confirm_button()


@step("User accept JS Confirm")
def step_impl(context):
    context.page.accept_alert()
    displayed_result = context.page.get_result()
    expected_result = "You clicked: Ok"
    assert displayed_result == expected_result, \
        f"{displayed_result} is not equal {expected_result}"


@step("User dismiss JS Confirm")
def step_impl(context):
    context.page.dismiss_alert()
    displayed_result = context.page.get_result()
    expected_result = "You clicked: Cancel"
    assert displayed_result == expected_result, \
        f"{displayed_result} is not equal {expected_result}"