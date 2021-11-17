from behave import step


@step("Page title is A/B Test Control")
def step_impl(context):
    expected_page_title = "A/B Test Variation 1"
    displayed_page_title = context.page.get_page_title()
    assert displayed_page_title == expected_page_title, \
        f"Displayed page title: {displayed_page_title} is not equal expected page title: {expected_page_title}"
