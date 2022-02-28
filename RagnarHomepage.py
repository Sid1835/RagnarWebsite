# Create a test with selenium that opens https://www.runragnar.com/
# Scroll the footer and verify that this page has “© 2022 ExpressVPN. All rights reserved.”

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=options)
    browser.implicitly_wait(5)

    browser.get("https://www.runragnar.com/")
    print(browser.page_source)

    test_string = "2022 Races Now Open"

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    header = browser.find_element(By.CLASS_NAME, "column-heading")
    print(header.text)

    if test_string == header.text:
        print("OK!")
    else:
      print(f"ERROR!!!! '{test_string}' not the same as '{header.text}'")

    browser.quit()
