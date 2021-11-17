from selenium.webdriver.common.by import By
from pages.base import BasePage


class HorizontalSlider(BasePage):

    class Locators:
        SLIDER = By.XPATH, "//input"

    def move_slider_to_the_end(self):
        for i in range(10):
            self.move_slider_to_right(self.Locators.SLIDER)

    def move_slider_to_the_beginning(self):
        for i in range(10):
            self.move_slider_to_left(self.Locators.SLIDER)
