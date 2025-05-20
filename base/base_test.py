import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.books_page import BooksPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage


# делаем аннотацию типов внутри класса BaseTest
class BaseTest:

    data: Data
    login_page: LoginPage
    main_page: MainPage
    books_page: BooksPage
    product_page: ProductPage
    cart_page: CartPage

    # создаем фикстуру
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver # для использования в тестах драйвера
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.books_page = BooksPage(driver)
        request.cls.product_page = ProductPage(driver)
        request.cls.cart_page = CartPage(driver)
