from selenium import webdriver
from pages.home_page import HomePage
from pages.abTesting_page import AbTesting
from pages.addRemoveElem_page import AddRemoveTesting
from pages.formAuthentication_page import FormAuthentication
from pages.dropdown_page import Dropdown
from pages.js_alerts_page import JavaScriptAlerts
from pages.horizontal_slider_page import HorizontalSlider


def get_starting_page(driver: webdriver.Remote, base_url: str) -> webdriver:
    driver.get(base_url)
    return HomePage(driver)
