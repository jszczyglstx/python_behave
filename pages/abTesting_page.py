from selenium.webdriver.common.by import By
from pages.base import BasePage


class AbTesting(BasePage):

    class Locators:
        PAGE_TITLE = By.XPATH, "//h3"

    def get_page_title(self) -> str:
        return self.get_element(self.Locators.PAGE_TITLE).text
