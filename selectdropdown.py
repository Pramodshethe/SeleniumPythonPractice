from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewAdminModule')
driver.find_element(By.XPATH, '//input[@id = "txtUsername"]').send_keys('admin')
driver.find_element(By.XPATH, '//input[@id = "txtPassword"]').send_keys('admin123')
driver.find_element(By.XPATH, "//input[@id = 'btnLogin']").click()

drop = driver.find_element(By.XPATH, '//select[@id = "searchSystemUser_userType"]')
select = Select(drop)
select.select_by_visible_text('Admin')