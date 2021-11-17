from selenium.webdriver.common.by import By

from pages.base import BasePage


class JavaScriptAlerts(BasePage):

    class Locators:
        JS_ALERT = By.XPATH, "//button[text()='Click for JS Alert']"
        JS_CONFIRM = By.XPATH, "//button[text()='Click for JS Confirm']"
        JS_PROMPT = By.XPATH, "//button[text()='Click for JS Prompt']"
        PAGE_TITLE = By.XPATH, "//h3"
        RESULT = By.XPATH, "//h4[contains(text(), 'Result')]/following-sibling::p"

    def click_js_alert_button(self) -> None:
        self.get_element(self.Locators.JS_ALERT).click()

    def click_js_confirm_button(self) -> None:
        self.get_element(self.Locators.JS_CONFIRM).click()

    def click_js_prompt_button(self) -> None:
        self.get_element(self.Locators.JS_PROMPT).click()

    def get_page_title(self) -> str:
        return self.get_element(self.Locators.PAGE_TITLE).text

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_result(self) -> str:
        return self.get_element(self.Locators.RESULT).text

