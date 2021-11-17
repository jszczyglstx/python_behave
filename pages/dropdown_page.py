from selenium.webdriver.common.by import By

from pages.base import BasePage


class Dropdown(BasePage):

    class Locators:

        DROPDOWN_PAGE_TITLE = By.XPATH, "//h3"
        DROPDOWN_LIST = By.ID, "dropdown"
        CHECK_IF_OPTION_SELECTED = By.XPATH, "//option[@selected='selected'][text()='Option 1']"

    class DropdownOptions:

        OPTION_1 = "1"

    def get_page_title(self):
        return self.get_element(self.Locators.DROPDOWN_PAGE_TITLE).text

    def pick_option_1(self):
        self.select_from_dropdown_by_value(self.Locators.DROPDOWN_LIST, self.DropdownOptions.OPTION_1)

