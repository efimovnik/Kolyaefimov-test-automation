from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright, expect, Page
from pages.main_page import MainPage
from pytest_bdd.parsers import parse, cfparse, re

scenarios("../features/main_page.feature")

@given(cfparse('I open the main page'))
def step_open_main_page(login):
    pass

@when(re(r'I fill the form with name "(?P<name>.*?)", email "(?P<email>.*?)", message "(?P<message>.*?)", and request type "(?P<request_type>.*?)"'))
def step_fill_form(login: MainPage, name, email, message, request_type):
    main_page = MainPage(login)
    main_page.fill_form(name=name, email=email, message=message, request_type=request_type)


@when(cfparse('I submit the form'))
def step_submit_form(login: MainPage):
    main_page = MainPage(login)
    main_page.submit_form()

@then(cfparse('I should see the success message "{message}"'))
def step_verify_success_message(login: MainPage, message):
    main_page = MainPage(login)
    expect(main_page.success_message).to_have_text(message)

@then(cfparse('I should see the validation message "{rejection_message}"'))
def step_verify_success_message(login: MainPage, rejection_message):
    main_page = MainPage(login)
    main_page.submit_form()
    expect(main_page.submission_error).to_have_text(rejection_message)