class SauceDemoLogin:

    login_url = "https://www.saucedemo.com/"
    user_name_id = "user-name"
    password_id = "password"
    login_button_id = "login-button"

    def send_username(self, page, username):
        page.locator(f"#{self.user_name_id}").fill(username)

    def send_password(self, page, password):
        page.locator(f"#{self.password_id}").fill(password)

    def login(self, page):
        page.locator(f"#{self.login_button_id}").click()