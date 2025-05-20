from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE # вызов из класса Links атрибута LOGIN_PAGE

    EMAIL_FIELD = ("xpath", "//input[@id='Email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='Password']")
    SUBMIT_BUTTON = ("xpath", "//input[@value='Log in']")

    def enter_login(self, login):
        """Ввод логина в поле авторизации."""
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(login)

    def enter_password(self, password):
        """Ввод пароля в поле авторизации."""
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_submit_button(self):
        """Нажатие кнопки Log in под полем авторизации."""
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def auth(self, login, password):
        """Авторизация через один метод."""
        self.open()
        self.enter_login(login)
        self.enter_password(password)
        self.click_submit_button()

