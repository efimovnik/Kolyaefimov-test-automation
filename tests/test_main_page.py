import pytest
from playwright.sync_api import expect
from pages.main_page import MainPage
from utils.test_data_loader import load_test_data


@pytest.mark.parametrize("data", load_test_data("test_data/main_page.json"))
def test_main_page(page, data):
    page = MainPage(page)
    page.fill_form(data["name"], data["email"], data["message"], data["request_type"])
    page.submit_form()
    expect(page.success_message).to_have_text("Спасибо! Ваш запрос уже получен.Я свяжусь с вами по указанному email в течение 3 дней или ранее, если я смогу что-то предложить в ответ.")