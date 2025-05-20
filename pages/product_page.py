from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def is_product_page(self, name):
        page = ("xpath", f"//div[@class='breadcrumb']//strong[contains(text(),'{name}')]")
        self.wait.until(EC.presence_of_element_located(page))
