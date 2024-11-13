import pytest
from playwright.sync_api import expect
from pages.main_page import MainPage
from utils.test_data_loader import load_test_data


@pytest.mark.parametrize("data", load_test_data("test_data/main_page_negative.json"))
def test_main_page_negative(login, data):
    page = MainPage(login)
    page.fill_form(data["name"], data["email"], data["message"], data["request_type"])
    page.submit_form()
    expect(page.submission_error).to_have_text(data["rejection_message"])