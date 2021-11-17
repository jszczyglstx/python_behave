from selenium.webdriver.common.by import By
from pages.base import BasePage


class AddRemoveTesting(BasePage):

    class Locators:
        PAGE_TITLE = By.XPATH, "//h3"
        ADD_ELEM_BUTTON = By.XPATH, "//button[text()='Add Element']"
        DELETE_BUTTON = By.XPATH, "//button[text()='Delete']"

    def get_page_title(self) -> str:
        return self.get_element(self.Locators.PAGE_TITLE).text

    def click_add_element_button(self) -> None:
        self.click(self.Locators.ADD_ELEM_BUTTON)

    def get_delete_button(self) -> bool:
        return self.check_if_visible(self.Locators.DELETE_BUTTON)

    def click_delete_button(self) -> None:
        self.click(self.Locators.DELETE_BUTTON)

    def check_if_delete_button_available(self) -> bool:
        return self.check_invisibility_of_element(self.Locators.DELETE_BUTTON)
