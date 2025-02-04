from playwright.sync_api import sync_playwright
from pages.saucedemo_login import SauceDemoLogin
import time


class TestSauceDemoLogin:

    def test_valid_user_login(self):

        with sync_playwright() as p:
            chrome = p.chromium.launch(headless=False)
            page = chrome.new_page()
            page.goto(SauceDemoLogin.login_url)
            page.wait_for_selector("text=Swag Labs", timeout=10000)
            assert page.title() == "Swag Labs"
            # send username
            SauceDemoLogin().send_username(page=page, username="standard_user")
            # send password
            SauceDemoLogin().send_password(page=page, password="secret_sauce")
            # login
            SauceDemoLogin().login(page=page)
            page.wait_for_selector('span[data-test="title"]')

