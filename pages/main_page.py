class MainPage:
    def __init__(self, page):
        self.page = page
        self.name = page.get_by_label("Имя")