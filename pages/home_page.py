from selenium.webdriver.common.by import By
from pages.base import BasePage


class HomePage(BasePage):

    class Locators:
        HOME_PAGE_TITLE = By.XPATH, "//h3"
        AB_TESTING_LINK = By.XPATH, "//a[text()='A/B Testing']"
        ADD_REMOVE_ELEM = By.XPATH, "//a[text()='Add/Remove Elements']"
        FORM_AUTHENTICATION = By.XPATH, "//a[text()='Form Authentication']"
        DROPDOWN = By.XPATH, "//a[text()='Dropdown']"
        JS_ALERTS = By.XPATH, "//a[text()='JavaScript Alerts']"
        HORIZONTAL_SLIDER = By.XPATH, "//a[text()='Horizontal Slider']"

    def get_page_title(self) -> str:
        return self.get_element(self.Locators.HOME_PAGE_TITLE).text

    def click_ab_testing(self) -> None:
        self.click(self.Locators.AB_TESTING_LINK)

    def click_add_remove_elem(self) -> None:
        self.click(self.Locators.ADD_REMOVE_ELEM)

    def click_form_authentication(self) -> None:
        self.click(self.Locators.FORM_AUTHENTICATION)

    def click_dropdown(self) -> None:
        self.click(self.Locators.DROPDOWN)

    def click_js_alerts(self) -> None:
        self.click(self.Locators.JS_ALERTS)

    def click_horizontal_slider(self) -> None:
        self.click(self.Locators.HORIZONTAL_SLIDER)
