from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.XPATH, "//input[@type ='submit']").click()

alert = driver.switch_to.alert
alert.accept()
