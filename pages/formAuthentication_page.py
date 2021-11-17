from selenium.webdriver.common.by import By
from pages.base import BasePage


class FormAuthentication(BasePage):

    class Locators:
        PAGE_TITLE = By.XPATH, "//h2"
        USERNAME_FIELD = By.ID, "username"
        PASSWORD_FIELD = By.ID, "password"
        LOGIN_BUTTON = By.XPATH, "//i[contains(text(), 'Login')]"
        LOG_IN_MESSAGE = By.XPATH, "//div[@class='flash success']"
        LOG_OUT_BUTTON = By.XPATH, "//i[contains(text(), 'Logout')]"
        LOG_OUT_MESSAGE = By.XPATH, "//div[@class='flash success']"
        INVALID_MESSAGE = By.XPATH, "//div[@class='flash error']"

    class Credentials:
        username = "tomsmith"
        password = "SuperSecretPassword!"

    def get_page_title(self) -> str:
        return self.get_element(self.Locators.PAGE_TITLE).text

    def input_username(self, username=Credentials.username) -> None:
        self.input_value(self.Locators.USERNAME_FIELD, username)

    def input_password(self, password=Credentials.password) -> None:
        self.input_value(self.Locators.PASSWORD_FIELD, password)

    def click_login(self) -> None:
        self.click(self.Locators.LOGIN_BUTTON)

    def check_login_message(self) -> str:
        return self.get_element(self.Locators.LOG_IN_MESSAGE).text[:30]

    def click_logout(self) -> None:
        self.click(self.Locators.LOG_OUT_BUTTON)

    def check_logout_message(self) -> str:
        return self.get_element(self.Locators.LOG_OUT_MESSAGE).text[:34]

    def check_invalid_message(self) -> str:
        return self.get_element(self.Locators.INVALID_MESSAGE).text

