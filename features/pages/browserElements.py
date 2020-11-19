from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class BrowserElement(BasePage):
    NAME = (By.NAME, 'fld_username')
    EMAIL = (By.NAME, "fld_email")

    def __init__(self, driver):
        super().__init__(driver)

    def search_item(self, name, email):
        self.find_element(*self.NAME).send_keys(name)
        self.find_element(*self.EMAIL).send_keys(email)
