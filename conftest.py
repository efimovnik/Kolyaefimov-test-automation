import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def set_up():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.kolyaefimov.com/")
        page.set_default_timeout(3000)
        yield page