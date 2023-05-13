from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

def send_email_alert(price,product,url):
    my_email = ""
    password = ""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg=f"Subject:Price Drop Alert on Product\n\n Dear User,\n{product} you are looking for is available for{price}\n click to buy : {url}"
                            )
        



amazon_product_url = "https://www.amazon.in/Redragon-K617-Keyboard-Mechanical-Supported/dp/B09BVCVTBC/ref=sr_1_3?crid=2T90GA13RFLJC&keywords=mechanical%2Bkeyboards&nav_sdd=aps&qid=1682554605&refinements=p_36%3A1318504031&rnid=1318502031&s=computers&sprefix=mechanical&sr=1-3&th=1"
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language":"en-GB,en;q=0.7"
}
response = requests.get(url=amazon_product_url, headers=headers)

with open("WebScraping/amazon_price_tracker/dump.html","w") as dump:
    dump.write(response.text)

soup = BeautifulSoup(response.text,"lxml")    


base_price = 2800.0
current_price = soup.select_one(selector="#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole")

price_now = float(current_price.getText().replace(',',''))



if price_now < base_price:
    send_email_alert(price_now,soup.title.getText(),amazon_product_url)

