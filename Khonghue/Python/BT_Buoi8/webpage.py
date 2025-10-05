class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_box = "#search"
        self.login_button = "#login"

    def search_product(self, item_name):
        self.page.fill(self.search_box, item_name)
        self.page.press(self.search_box, "Enter")

    def go_to_login(self):
        self.page.click(self.login_button)