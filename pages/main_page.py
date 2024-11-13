from playwright.sync_api import Page, Response
import pytest
import allure

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.name = page.get_by_label("Имя")
        self.email = page.get_by_label("Email(required)")
        self.message = page.get_by_placeholder("Чем я могу вам помочь?")
        self.request_type = page.get_by_label("Тип запроса")
        self.submit_button = page.get_by_role("button", name="Отправить")
        self.success_message = page.locator(".form-submission-text")
        self.submission_error_forbidden = page.locator("//p[contains(@class,'form-field-error') and contains(text(),'Forbidden')]")
        self.submission_error = page.locator("//p[contains(@class,'form-field-error') and starts-with(text(),'Form submission failed.')]")
        self.submission_response = None

    def fill_form(self, name: str, email: str, message: str, request_type: str = None):
        self.name.fill(name)
        self.email.fill(email)
        self.message.fill(message)
        if request_type:
            self.request_type.select_option(request_type)

    def submit_form(self):
        with self.page.expect_response("https://www.kolyaefimov.com/api/form/SaveFormSubmission") as response_info:
            self.submit_button.click()  # submit the form
        self.submission_response = response_info.value
        allure.attach(self.submission_response.text(), name="Submission Response", attachment_type=allure.attachment_type.TEXT)
