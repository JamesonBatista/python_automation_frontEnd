from time import sleep

from selenium.webdriver import Chrome


def before_all(context):
    context.driver = Chrome()
    context.driver.implicitly_wait(30)
    context.driver.set_page_load_timeout(30)
    context.driver.maximize_window()


def after_all(context):
    sleep(2)
    context.driver.close()
    context.driver.quit()
