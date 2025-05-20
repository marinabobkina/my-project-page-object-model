from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import random


class BooksPage(BasePage):

    PAGE_URL = Links.BOOKS_PAGE

    BUTTON_ADD_TO_CART = ("xpath", "//input[@value='Add to cart']")
    CONFIRM_MESSAGE = ("xpath", "//p[contains(text(), 'The product has been added')]")

    def choice_product_to_cart(self):
        """Выбор случайным образом продукта на странице с сохранением его названия и цены"""

        # случайным образом выбираем порядковый номер элемента, у которого есть кнопка Add to cart
        numbers = [1, 3, 5]
        number = random.choice(numbers)

        # находим название выбранного продукта и сохраняем его в переменную
        chosen_name = ("xpath", f"(//h2/a)[{number}]")
        text_name = self.wait.until(EC.presence_of_element_located(chosen_name)).text

        # находим цену выбранного продукта и сохраняем ее в переменную
        price = ("xpath", f"(//span[contains(@class,'actual-price')])[{number}]")
        value_price = self.wait.until(EC.presence_of_element_located(price)).text

        # кликаем кнопку добавления в корзину для выбранного товара
        button_add_to_cart = ("xpath", f"(//div[@class='product-item'])[{number}]//input[@value='Add to cart']")
        self.wait.until(EC.element_to_be_clickable(button_add_to_cart)).click()

        message = ("xpath", "//p[contains(text(), 'The product has been added')]")
        self.wait.until(EC.presence_of_element_located(message))
        self.wait.until(EC.invisibility_of_element(message))

        return text_name, value_price
