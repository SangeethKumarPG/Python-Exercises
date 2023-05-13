from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/sangeethkumarpg/Desktop/Development/Python/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service,options=options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# parent_div = driver.find_element(By.CSS_SELECTOR,"#articlecount>a:nth-child(1)")
# print(parent_div.text)
# parent_div.click()
# history_element = driver.find_element(By.LINK_TEXT,"View history")
# history_element.click()
# search = driver.find_element(By.NAME,"search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
first_name = driver.find_element(By.NAME,"username")
password = driver.find_element(By.NAME,"password")
submit_button = driver.find_element(By.CSS_SELECTOR,"#HTMLFormElements > table > tbody > tr:nth-child(9) > td > input:nth-child(2)")
first_name.send_keys("Name")
first_name.send_keys("Password")
submit_button.click()
# driver.quit()