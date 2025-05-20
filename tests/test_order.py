from base.base_test import BaseTest


class TestOrder(BaseTest):
    def test_success_authentification(self):
        """Проверка успешной авторизации."""

        # открыть страницу авторизации
        self.login_page.open()

        # ввести логин
        self.login_page.enter_login(self.data.LOGIN)

        # ввести пароль
        self.login_page.enter_password(self.data.PASSWORD)

        # нажать кнопку Log in
        self.login_page.click_submit_button()

        # проверить, что открылась главная страница
        self.main_page.is_opened()

        # проверить, что название аккаунта отображается на главной странице
        self.main_page.check_my_account()

    def test_success_product_search(self):
        """Проверка успешного поиска продукта."""

        # открыть главную страницу
        self.main_page.open()

        # проверить, что открылась главная страница
        self.main_page.is_opened()

        # ввести в поле поиска искомое слово (в данном случае "Fiction") и выбрать его в выпадающем окне
        self.main_page.search_product("Fiction")

        # проверить, что открылась страница нужного товара (в данном случае "Fiction")
        self.product_page.is_product_page("Fiction")

    def test_cart_add(self, driver):
        """Проверка успешного добавления продукта в корзину."""

        # открыть главную страницу
        self.main_page.open()

        # кликнуть указанный пункт меню
        self.main_page.choice_menu_item("Books")

        # проверить, что открылась страница, соответствующая Books
        self.books_page.is_opened()

        # добавление случайного продукта в корзину, сохранение его названия и цены
        product_name, product_price = self.books_page.choice_product_to_cart()

        # перейти в корзину
        self.books_page.go_to_cart()

        # проверить, что открылась страница корзины
        self.cart_page.is_opened()

        # проверить, что название и цена товара в корзине соответствуют выбранному товару
        self.cart_page.check_product_name(product_name)
        self.cart_page.check_product_price(product_price)
