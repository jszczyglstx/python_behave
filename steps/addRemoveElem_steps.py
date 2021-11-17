from behave import step


@step("Page title is Add/Remove Elements")
def step_impl(context):
    expected_page_title = "Add/Remove Elements"
    displayed_page_title = context.page.get_page_title()
    assert displayed_page_title == expected_page_title, \
        f"Displayed page title: {displayed_page_title} is not equal expected page title: {expected_page_title}"


@step("User clicks Add Element button")
def step_impl(context):
    context.page.click_add_element_button()


@step("User verifies if Delete button appeared")
def step_impl(context):
    delete = context.page.get_delete_button()
    if delete is True:
        pass
    else:
        raise AssertionError("Delete button is not visible")


@step("User clicks Delete Element button")
def step_impl(context):
    context.page.click_delete_button()


@step("User verifies if Delete button disappeared")
def step_impl(context):
    verify_delete = context.page.check_if_delete_button_available()
    if verify_delete is True:
        pass
    else:
        raise AssertionError("Delete button is visible")