import pytest
from playwright.sync_api import expect
from pages.main_page import MainPage


def test_main_page(set_up):
    page = MainPage(set_up)
    expect(page.name).to_have_text("")