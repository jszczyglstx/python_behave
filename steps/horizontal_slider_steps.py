from behave import step


@step("User moves Horizontal slider to the end")
def step_impl(context):
    context.page.move_slider_to_the_end()


@step("User moves Horizontal slider to the beginning")
def step_impl(context):
    context.page.move_slider_to_the_beginning()