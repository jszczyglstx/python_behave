from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def check_invisibility_of_element(self, locator, wait_seconds=3) -> bool:
        return WebDriverWait(self.driver, wait_seconds).until(EC.invisibility_of_element_located(locator))

    def get_element(self, locator, wait_seconds=3):
        return WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located(locator))

    def click(self, locator, wait_seconds=3) -> None:
        WebDriverWait(self.driver, wait_seconds).until(EC.element_to_be_clickable(locator)).click()

    def check_if_visible(self, locator, wait_seconds=3) -> bool:
        return WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located(locator)).is_displayed()

    def input_value(self, locator, input_value, wait_seconds=3) -> None:
        WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located(locator)).send_keys(input_value)

    def select_from_dropdown_by_value(self, locator, value, wait_seconds=3) -> None:
        select = Select(WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located(locator)))
        select.select_by_value(value)

    def force_click(self, locator) -> None:
        self.driver.execute_script("arguments[0].click();", locator)

    def move_slider_to_right(self, locator, wait_seconds=3) -> None:
        WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located(locator)).send_keys(Keys.RIGHT)

    def move_slider_to_left(self, locator, wait_seconds=3) -> None:
        WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located(locator)).send_keys(Keys.LEFT)
