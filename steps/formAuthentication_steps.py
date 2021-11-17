from behave import step


@step("Page title is Login Page")
def step_impl(context):
    expected_page_title = "Login Page"
    displayed_page_title = context.page.get_page_title()
    assert displayed_page_title == expected_page_title, \
        f"Displayed page title: {displayed_page_title} is not equal expected page title: {expected_page_title}"


@step("User logs in")
def step_impl(context):
    context.page.input_username()
    context.page.input_password()
    context.page.click_login()


@step("Successful log in message pop up")
def step_impl(context):
    expected_msg = "You logged into a secure area!"
    actual_msg = context.page.check_login_message()
    assert actual_msg == expected_msg, \
        f"Displayed message: {actual_msg} is not equal expected message: {expected_msg}"


@step("User logs out")
def step_impl(context):
    context.page.click_logout()


@step("Successful log out message pop up")
def step_impl(context):
    expected_msg = "You logged out of the secure area!"
    actual_msg = context.page.check_logout_message()
    assert actual_msg == expected_msg, \
        f"Displayed message: {actual_msg} is not equal expected message: {expected_msg}"


@step("User logs in with invalid credentials")
def step_impl(context):
    for row in context.table:
        context.page.input_username(row['Username'])
        context.page.input_password(row['Password'])
        context.page.click_login()


@step("Invalid credentials message pop up")
def step_impl(context):
    expected_msg = "Your password is invalid!"
    expected_msg1 = "Your username is invalid!"
    actual_msg = context.page.check_invalid_message()
    if expected_msg not in actual_msg and expected_msg1 not in actual_msg:
        raise AssertionError(f"{actual_msg} is not equal {expected_msg} or {expected_msg1}")