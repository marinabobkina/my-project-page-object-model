import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver(request):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-features=PasswordLeakDetection")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver # создаем объект драйвера внутри тестовых классов == прописать драйвер в init класса
    yield driver
    driver.quit()
