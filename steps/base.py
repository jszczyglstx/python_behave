from behave import step, given, runner
from pages import get_starting_page


@step('The user is redirected to the "{page_type:PageType}"')
def step_impl(context: runner.Context, page_type) -> None:
    context.page = page_type(context.driver)


@given("User is on the webpage")
def step_impl(context):
    context.page = get_starting_page(context.driver, context.base_url)
