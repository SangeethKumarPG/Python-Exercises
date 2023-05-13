from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/sangeethkumarpg/Desktop/Development/Python/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service=ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service,options=options)

webiste_url = "https://www.python.org/"
driver.get(webiste_url)
parent_element = driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
children_elements = parent_element.find_elements(By.TAG_NAME,"time")

time_list = [item.text for item in children_elements]
links_of_children = parent_element.find_elements(By.TAG_NAME,'a')
event_names = [item.text for item in links_of_children]
result_dict = dict()
for index,(k,v) in enumerate(zip(time_list,event_names)):
    event = {'time':k,'name':v}
    result_dict[index] = event

print(result_dict)




driver.quit()