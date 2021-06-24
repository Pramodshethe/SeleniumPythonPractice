import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome","edge"], scope= "class")
def init_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("init_driver")
class M1test:
    pass


class Test_Google(M1test):
    def test_google(self):
        self.driver.get("https://google.com")
