import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_default_timeout(3000)
    yield page
    page.close()

@pytest.fixture(scope="function")
def login(page):
    page.goto("https://www.kolyaefimov.com/")
    yield page