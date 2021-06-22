import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_m1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewAdminModule')


def test_m2():
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get('https://google.com')