import configuration
import behave
from behave import runner

from parsers import register_type_parsers

register_type_parsers()


def before_all(context: runner.Context) -> None:  # czemu korzystasz tutaj z typowania context: runner.Context
    context.base_url = behave.use_fixture(configuration.base_url, context)
    # co oznacza typowanie None ? ze funckaj nie zwraca zanej wartosci ?


def before_scenario(context: runner.Context, scenario) -> None:
    context.driver = behave.use_fixture(configuration.driver, context)
    # ten argument scenario nie jest tu potrzebny ?


def after_scenario(context: runner.Context, scenario) -> None:
    context.driver.close()
