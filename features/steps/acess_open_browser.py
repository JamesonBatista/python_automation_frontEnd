from behave import *

from features.pages.browserElements import BrowserElement


@given(u'for acessado pagina de teste "{url}"')
def step_impl(context, url):
    global page
    page = BrowserElement(context.driver)
    page.open(url)


@when(u'fizer validacoes com "{nameUser}" e email "{emailUser}"')
def step_impl(context, nameUser, emailUser):
    page.search_item(nameUser, emailUser)


@then(u'teremos resultados')
def step_impl(context):
    pass
