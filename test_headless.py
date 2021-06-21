from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument('--incognito')
browser = "chrome"

if browser == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(10)
    driver.get("https://google.com")
    #driver.get_screenshot_as_file('google.png')
    print(driver.title)
    driver.find_element(By.XPATH('//input[@title = ["Search"]')).send_keys('hello')
    driver.back()

if browser == "firefox":
    driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
    driver.implicitly_wait(10)
    driver.get("https://google.com")
    print(driver.title)

