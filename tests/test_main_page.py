from playwright.sync_api import expect
from pages.main_page import MainPage


def test_main_page(page):
    page = MainPage(page)
    page.fill_form(
        name="Test", 
        email="test@test.com",
        message="Test message",
        request_type="Личный",
        )
    page.submit_form()
    expect(page.success_message).to_have_text("Спасибо! Ваш запрос уже получен.Я свяжусь с вами по указанному email в течение 3 дней или ранее, если я смогу что-то предложить в ответ.")