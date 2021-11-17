import configuration
import behave
from behave import runner

from parsers import register_type_parsers

register_type_parsers()


def before_all(context: runner.Context) -> None:
    context.base_url = behave.use_fixture(configuration.base_url, context)


def before_scenario(context: runner.Context, scenario) -> None:
    context.driver = behave.use_fixture(configuration.driver, context)


def after_scenario(context: runner.Context, scenario) -> None:
    context.driver.close()
