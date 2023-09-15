import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://172.16.3.234/CZCRM/")
driver.maximize_window()


driver.find_element(By.NAME,"username").send_keys("admin@test.com")
driver.find_element(By.NAME,"password").send_keys("Pass@1")
driver.find_element(By.NAME,"loginUser").click()

if driver.title=="Ticketing CRM":
  driver.find_element(By.NAME,"login_existing_agent").click()

driver.find_element(By.LINK_TEXT,"Masters").click()


time.sleep(10)









