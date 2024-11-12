from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.name = page.get_by_label("Имя")
        self.email = page.get_by_label("Email(required)")
        self.message = page.get_by_placeholder("Чем я могу вам помочь?")
        self.request_type = page.get_by_label("Тип запроса")
        self.submit_button = page.get_by_role("button", name="Отправить")
        self.success_message = page.locator(".form-submission-text")

    def fill_form(self, name: str, email: str, message: str, request_type: str = None):
        self.name.fill(name)
        self.email.fill(email)
        self.message.fill(message)
        if request_type:
            self.request_type.select_option(request_type)

    def submit_form(self):
        self.submit_button.click()