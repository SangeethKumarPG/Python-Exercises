from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "/Users/sangeethkumarpg/Desktop/Development/Python/chromedriver"
url = "http://orteil.dashnet.org/experiments/cookie/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=options,service=service)
driver.get(url)

cookie = driver.find_element(By.XPATH,'//*[@id="cookie"]')
children_list = []
def update_children():
    money = driver.find_element(By.ID,"money")
    current_balance = money.text.replace(',','')
    if int(current_balance) >= 7000:
        if int(current_balance) >= 123456789:
             driver.find_element(By.ID,"buyTime machine").click()
        elif int(current_balance) >= 1000000:
             driver.find_element(By.ID,"buyPortal").click()
        elif int(current_balance) >= 50000:
             driver.find_element(By.ID,"buyAlchemy lab").click()
        else:
             driver.find_element(By.ID,"buyShipment").click()
    else:
        if int(current_balance) >= 2000:
             driver.find_element(By.ID,"buyMine").click()
        elif int(current_balance) >=500:
             driver.find_element(By.ID,"buyFactory").click()
        elif int(current_balance) >= 100:
             driver.find_element(By.ID,"buyGrandma").click()
        elif int(current_balance) >= 15:
             driver.find_element(By.ID,"buyCursor").click()
    return


time_out_start = time.time()
timout = 5
main_timer = time.time()
main_timeout = 300
try:
    while time.time()< main_timer + main_timeout:
        
        if time.time() < time_out_start+timout:
            cookie.click()
        else:
            update_children()
            time_out_start = time.time()
except KeyboardInterrupt:
    pass
print(driver.find_element(By.ID,"cps").text)

driver.quit()