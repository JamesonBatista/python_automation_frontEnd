from behave import *

from features.pages.browserElements import BrowserElement


@given(u'for acessado pagina de teste "{url}"')
def step_impl(context, url):
    global page
    page = BrowserElement(context.driver)
    page.open(url)


@when(u'fizer validacoes')
def step_impl(context):
    page.search_item("Jam Batista", "jam@jam.com")


@then(u'teremos resultados')
def step_impl(context):
    pass
