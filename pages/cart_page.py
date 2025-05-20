from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    PAGE_URL = Links.CART_PAGE

    def check_product_name(self, product_name):
        """Проверяем, что в корзине есть товар с указанным именем"""
        name = ("xpath", f"//td/a[text()='{product_name}']")
        self.wait.until(EC.presence_of_element_located(name), f"В корзине отсутствует товар {product_name}")

    def check_product_price(self, product_price):
        """Проверяем, что в корзине есть товар с указанной ценой"""
        price = ("xpath", f"//span[@class='product-unit-price' and text()='{product_price}']")
        self.wait.until(EC.presence_of_element_located(price), f"В корзине отсутствует товар {product_price}")
