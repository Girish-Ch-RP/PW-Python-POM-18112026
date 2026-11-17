import pytest
from playwright.sync_api import expect, Playwright, Page

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.login_link=page.locator("#login2")
        self.username_input=page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.login_button = page.locator('button[onclick="logIn()"]')

    def login(self,username,password):
        self.login_link.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
