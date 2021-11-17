from behave import step


@step("Page title is Dropdown")
def step_impl(context):
    expected_page_title = "Dropdown List"
    displayed_page_title = context.page.get_page_title()
    assert displayed_page_title == expected_page_title, \
        f"Displayed page title: {displayed_page_title} is not equal expected page title: {expected_page_title}"


@step("User clicks at Dropdown list")
def step_impl(context):
    context.page.pick_option_1()