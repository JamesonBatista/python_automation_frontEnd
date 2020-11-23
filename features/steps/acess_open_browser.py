from behave import *

from features.pages.browserElements import BrowserElement


@given(u'for acessado pagina de teste "{url}"')
def step_impl(context, url):
    global page
    page = BrowserElement(context.driver)
    page.open(url)


@when(u'fizer validacoes com "{name_user}" e email "{email_user}"')
def step_impl(context, name_user, email_user):
    page.search_item(name_user, email_user)


@then(u'teremos resultados')
def step_impl(context):
    pass
