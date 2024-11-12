from behave import given, when, then
from playwright.sync_api import sync_playwright, expect
from pages.main_page import MainPage

@given("I open the main page")
def step_open_main_page(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context.page = browser.new_page()
    context.page.goto("https://www.kolyaefimov.com/")
    context.main_page = MainPage(context.page)

@when('I fill the form with name "{name}", email "{email}", message "{message}", and request type "{request_type}"')
def step_fill_form(context, name, email, message, request_type):
    context.main_page.fill_form(name=name, email=email, message=message, request_type=request_type)

@when("I submit the form")
def step_submit_form(context):
    context.main_page.submit_form()

@then('I should see the success message "{message}"')
def step_verify_success_message(context, message):
    expect(context.main_page.success_message).to_have_text(message)
