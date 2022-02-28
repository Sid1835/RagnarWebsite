# Create a test with selenium that opens https://www.runragnar.com/
# Scroll the footer and verify that this page has “© 2022 ExpressVPN. All rights reserved.”

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
from selenium import webdriver

email = "siddhesh.d@testriq.com"
password = "Sid*141#"

url = "https://www.runragnar.com/auth/login"

driver = webdriver.chrome("C:\\Users\\siddh\\Desktop\\Auto\\chromedriver_win32\\chromedriver.exe")

driver.get(url)

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("rg_btn").click()


print("logged in success")

  #  browser.quit()
