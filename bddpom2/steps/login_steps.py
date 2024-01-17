from behave import *


@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I enter an unregistered email')
def step_impl(context):
    context.login_page.set_email("tmta@itfactory.ro")


@when('I enter a password')
def step_impl(context):
    context.login_page.set_password("alabalaportocala")


@when('I click the Login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I should see "No customer account found" message')
def step_impl(context):
    assert context.login_page.is_main_error_message_displayed(), "The error message is not displayed"
    assert "No customer account found" in context.login_page.get_main_error_message_text(), "The error message does not contain the expected text"


@when('I enter "{email}" in the email input')
def step_impl(context, email):
    context.login_page.set_email(email)


@when('I enter "{password}" in the password input')
def step_impl(context, password):
    context.login_page.set_password(password)


@then('I should see "{message}" error message')
def step_impl(context, message):
    assert context.login_page.is_email_error_message_displayed(), "The email error message is not displayed"
    assert message in context.login_page.get_email_error_message_text(), f"The email error message does not contain '{message}'"


@when('I defocus from the email input')
def step_impl(context):
    context.login_page.defocus_email_input()

@then('The URL of the page is "{url}"')
def step_impl(context, url):
    assert context.login_page.is_url_correct(url), f"Error, page url is not {url}"