import behave
from behave import runner
from selenium import webdriver


@behave.fixture()
def driver(context: runner.Context) -> webdriver.remote:
    driver_class = _get_driver_class(context)
    if driver_class == "chrome":
        chrome_options = webdriver.ChromeOptions()
        driver_instance = webdriver.Chrome(chrome_options=chrome_options)
        driver_instance.set_window_size(1920, 1080)
        return driver_instance


@behave.fixture()
def _get_driver_class(context: runner.Context) -> str:
    return _get_argument_value(context, "driver", required=True)


@behave.fixture()
def base_url(context: runner.Context) -> str:
    return _get_argument_value(context, "base_url", required=True)


def _get_argument_value(context: runner.Context, key: str, required: bool = False) -> str:
    argument_value = context.config.userdata.get(key)
    return argument_value
