import pytest
from playwright.sync_api import expect
from pages.main_page import MainPage

@pytest.mark.parametrize("name, email, message, request_type", [
    ("Personal", "personal@test.com", "Personal test message", "Личный"),
    ("", "commercial@commercial.com", "commercial message", "Коммерческий")])
def test_main_page(page, name, email, message, request_type):
    page = MainPage(page)
    page.fill_form(name=name, email=email, message=message, request_type=request_type)
    page.submit_form()
    expect(page.success_message).to_have_text("Спасибо! Ваш запрос уже получен.Я свяжусь с вами по указанному email в течение 3 дней или ранее, если я смогу что-то предложить в ответ.")