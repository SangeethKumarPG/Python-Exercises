from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PROMISED_UP = 100
PROMISED_DOWN = 10
TWITTER_USER_NAME = ""
TWITTER_PASSWORD = ""
chrome_driver_path = "/Users/sangeethkumarpg/Desktop/Development/Python/chromedriver"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"
class InternetSpeedTwitterBot():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)
        self.service = ChromeService(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(options=self.options,service=self.service)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a > span.start-text').click()
        time.sleep(65)
        download_speed = self.driver.find_element(By.CSS_SELECTOR,'#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span')
        self.down = download_speed.text
        upload_speed = self.driver.find_element(By.CSS_SELECTOR,'#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span')
        self.up = upload_speed.text
        self.driver.quit()
        self.driver1 = webdriver.Chrome(options=self.options,service=self.service)
        return [self.down,self.up]
    
    def tweet_at_provider(self):
        self.driver1.get(TWITTER_URL)
        time.sleep(3)
        login_email = self.driver1.find_element(By.CSS_SELECTOR,"#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
        login_email.send_keys(TWITTER_USER_NAME)
        time.sleep(2)
        self.driver1.find_element(By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div').click()
        time.sleep(5)
        login_password = self.driver1.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')  
        login_password.send_keys(TWITTER_PASSWORD)
        time.sleep(5)
        login_password.send_keys(Keys.ENTER)

        time.sleep(10)
        self.driver1.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
        time.sleep(4)


        text_box = self.driver1.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        text_box.send_keys(f"@keralavisionISP Getting low internet speed on Jio 5G, download speed:{self.down}, upload speed : {self.down}")
        time.sleep(3)
        self.driver1.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div[4]/div/span/span').click()
        time.sleep(2)
        self.driver1.quit()
