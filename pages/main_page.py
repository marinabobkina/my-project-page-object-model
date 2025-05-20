import pytest
from selenium.common.exceptions import TimeoutException
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = Links.MAIN_PAGE

    MY_ACCOUNT_NAME = ("xpath", "//a[text()='m123456@mail.ru']")
    MENU_ITEM = ("xpath", "//ul[@class='top-menu']//a[contains(text(), 'Books')] ")

    def check_my_account(self):
        """Проверяем, что название аккаунта присутствует на главной странице"""
        try:
            self.wait.until(EC.presence_of_element_located(self.MY_ACCOUNT_NAME))
            return True
        except TimeoutException:
            pytest.fail("Элемент MY_ACCOUNT_NAME не был найден в течение заданного времени ожидания")
            return False
        # альтернативный метод без конструкции try - except
        # self.wait.until(EC.presence_of_element_located(self.MY_ACCOUNT_NAME),
        # "Элемент MY_ACCOUNT_NAME не был найден в течение заданного времени ожидания")

    def choice_menu_item(self, menu_item_name):
        """Кликаем по указанному названию пункта меню"""
        locator = ("xpath", f"//ul[@class='top-menu']//a[contains(text(), '{menu_item_name}')] ")
        self.wait.until(EC.element_to_be_clickable(locator)).click()
