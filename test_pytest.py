import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.mark.m2
def test_m1():
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewAdminModule')


@pytest.mark.m1
def test_m2():
    driver.get('https://google.com')


@pytest.mark.m2
def test_m3():
    driver.get('https://yahoo.com')