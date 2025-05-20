from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    SEARCH_INPUT = ("xpath", "//input[@id='small-searchterms']")
    DROPDOWN = ("xpath", "//ul[@id='ui-id-1']")
    CART = ("xpath", "//span[text()='Shopping cart']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1) # явное ожидание 10 сек и раз в секунду драйвер
                                                                       # будет опрашивать страницу

    def open(self):
        """Метод для открытия страниц"""
        self.driver.get(self.PAGE_URL) # PAGE_URL будет прописан для каждой страницы индивидуально и будет подтягиваться
                                       # после запуска драйвера

    def is_opened(self):
        """Проверка, что страница открылась"""
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def search_product(self, product_name):
        """Поиск товара на странице"""
        search_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(product_name)
        dropdown = self.wait.until(EC.presence_of_element_located(self.DROPDOWN))
        self.wait.until(EC.visibility_of(dropdown), "Выпадающее окно не отображается")
        dropdown_item = ("xpath", f"//li/a[text()='{product_name}']")
        self.wait.until(EC.presence_of_element_located(dropdown_item),
                        f"Отсутствует {product_name} в выпадающем окне").click()

    def go_to_cart(self):
        """Переход в корзину"""
        self.wait.until(EC.element_to_be_clickable(self.CART)).click()
