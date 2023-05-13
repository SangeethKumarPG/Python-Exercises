from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/sangeethkumarpg/Desktop/Development/Python/chromedriver"

amazon_product_url = "https://www.amazon.in/Redragon-K617-Keyboard-Mechanical-Supported/dp/B09BVCVTBC/ref=sr_1_3?crid=2T90GA13RFLJC&keywords=mechanical%2Bkeyboards&nav_sdd=aps&qid=1682554605&refinements=p_36%3A1318504031&rnid=1318502031&s=computers&sprefix=mechanical&sr=1-3&th=1"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(amazon_product_url)
price = driver.find_element(By.CSS_SELECTOR,"#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole")
# print(price.get_attribute("class"))
print(price.tag_name)
print(price.text)
driver.quit()