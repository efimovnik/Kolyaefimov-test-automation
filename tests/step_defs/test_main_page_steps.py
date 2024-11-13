from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright, expect, Page
from pages.main_page import MainPage
from pytest_bdd.parsers import cfparse, re
import pytest

scenarios("../features/main_page.feature")


@pytest.fixture
def main_page(login: Page):
    # Create and return a shared MainPage instance
    return MainPage(login)

@given(cfparse('I open the main page'))
def step_open_main_page(login):
    pass

@when(re(r'I fill the form with name "(?P<name>.*?)", email "(?P<email>.*?)", message "(?P<message>.*?)", and request type "(?P<request_type>.*?)"'))
def step_fill_form(main_page: MainPage, name, email, message, request_type):
    main_page.fill_form(name=name, email=email, message=message, request_type=request_type)


@when(cfparse('I submit the form'))
def step_submit_form(main_page: MainPage):
    main_page.submit_form()

@then(cfparse('I should see the success message "{message}"'))
def step_verify_success_message(main_page: MainPage, message):
    expect(main_page.success_message).to_have_text(message)

@then(cfparse('I should see the validation message "{rejection_message}"'))
def step_verify_success_message(main_page: MainPage, rejection_message):
    if main_page.submission_error.is_visible():
        expect(main_page.submission_error).to_have_text(rejection_message)
    else: # 403 Forbidden
        expect(main_page.submission_error_forbidden).to_have_text("Forbidden")
    
@then(cfparse('I should see a "{status_code}" response for the form submission'))
def step_verify_success_message(main_page: MainPage, status_code):
    actual_status = main_page.submission_response.status
    assert actual_status == int(status_code), f"Expected status code {status_code}, but got {actual_status}"
    
