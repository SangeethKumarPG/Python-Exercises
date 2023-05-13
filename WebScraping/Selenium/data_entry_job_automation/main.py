from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import requests
import time
import json

GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdHRby7SQYuH8nAZeGo7YQntsfzm1UFE2MCXpTw-IHK3yOb3w/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.59954412562571%2C%22east%22%3A-122.31630285365306%2C%22south%22%3A37.68429375815747%2C%22north%22%3A37.8314103088676%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

class ScrapeZillow():
    def __init__(self):
        header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Accept-Language":"en-GB,en;q=0.7"
        }
        response = requests.get(url=ZILLOW_LINK,headers=header)
        # print(response.content)
        self.soup = BeautifulSoup(response.content,'html.parser')

    
    def find_listing(self):
        top_listings = []
        data = json.loads(self.soup.select_one('script[data-zrr-shared-data-key]').contents[0]
                          .strip('!<>-'))
        # with open('json_dump.json','w') as json_data:
        #     json_data.write(json.dumps(data,indent=4))
        property_list = data.get('cat1').get('searchResults').get('listResults')
        base_url = "https://www.zillow.com"
        for item in property_list:
            item_dict = dict()
            if 'https' not in item.get('detailUrl'):
                item_dict['property_link'] = base_url + item.get('detailUrl')
            else:
                item_dict['property_link'] = item.get('detailUrl')
            item_dict['address'] = item.get('address')
            if item.get('units') == None:
                item_dict['price'] = item.get('price').replace('$','').replace('+','').replace('/mo','')
            else:
                item_dict['price'] = item.get('units')[0].get('price').replace('$','').replace('+','').replace('/mo','')
            top_listings.append(item_dict)
        return top_listings


class SubmitResponse():
    def __init__(self):
        self.chrome_driver_path = "/Users/sangeethkumarpg/Desktop/Development/Python/chromedriver"
        self.options = webdriver.ChromeOptions()
        self.service = ChromeService(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def submit_response(self,listings):
        self.driver.get(GOOGLE_FORM_LINK)
        for item in listings:
            time.sleep(3)
            address = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
            time.sleep(1)
            address.send_keys(item.get("address"))
            time.sleep(1)
            price = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(1)
            price.send_keys(item.get("price"))
            time.sleep(1)
            link = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
            link.send_keys(item.get("property_link"))
            time.sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()




zill = ScrapeZillow()
top_listings = zill.find_listing()
# print(top_listings)
google_sheet = SubmitResponse()
google_sheet.submit_response(top_listings)
        





