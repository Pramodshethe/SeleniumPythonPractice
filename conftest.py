import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = driver
    request.cls.driver.implicitly_wait(10)
    yield
    driver.close()