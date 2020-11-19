from environment import Environment


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def open(self, url):
        environment = Environment().page_url
        url = url
        self.driver.get(environment + url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
