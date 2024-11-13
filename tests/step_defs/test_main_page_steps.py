from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright, expect, Page
from pages.main_page import MainPage
from pytest_bdd.parsers import parse

scenarios("../features/main_page.feature")

@given(parse('I open the main page'))
def step_open_main_page(login):
    pass

@when(parse('I fill the form with name "{name}", email "{email}", message "{message}", and request type "{request_type}"'))
def step_fill_form(login: MainPage, name, email, message, request_type):
    main_page = MainPage(login)
    if name:
        main_page.fill_form(name=name, email=email, message=message, request_type=request_type)
    else:
        # Only fill other fields if name is empty
        main_page.fill_form(name="", email=email, message=message, request_type=request_type)

@when(parse('I submit the form'))
def step_submit_form(login: MainPage):
    main_page = MainPage(login)
    main_page.submit_form()

@then(parse('I should see the success message "{message}"'))
def step_verify_success_message(login: MainPage, message):
    main_page = MainPage(login)
    expect(main_page.success_message).to_have_text(message)
