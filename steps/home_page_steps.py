from behave import step


@step("Page title is page_title")
def step_impl(context):
    displayed_page_title = context.page.get_page_title()
    expected_page_title = "Some title"
    assert displayed_page_title == expected_page_title, \
        f"Displayed page title: {displayed_page_title} is not equal expected page title: {expected_page_title}"


@step("User click A/B Testing")
def step_impl(context):
    context.page.click_ab_testing()


@step("User clicks Add/Remove Elements")
def step_impl(context):
    context.page.click_add_remove_elem()


@step("User clicks Form Authentication")
def step_impl(context):
    context.page.click_form_authentication()


@step("User clicks Dropdown")
def step_impl(context):
    context.page.click_dropdown()


@step("User clicks JavaScript Alerts")
def step_impl(context):
    context.page.click_js_alerts()


@step("User clicks Horizontal slider")
def step_impl(context):
    context.page.click_horizontal_slider()
