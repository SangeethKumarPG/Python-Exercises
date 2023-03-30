import requests
# import json
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# news_api_top_headlines_url = "https://newsapi.org/v2/top-headlines?"
# news_api_top_headlines_params= {
#     "q" : "tesla",
#     "country" : "us",
#     "category" : "business",
#     "apiKey" : "6dbed163a27a4a3999ba2854ad99d7d5"

# }
news_api_url= "https://newsapi.org/v2/everything?"
news_api_params = {
    "q" : "tesla",
    "from" : "",
    "sources" : "business-insider",
    "sortBy" : "publishedAt",
    "apiKey" : "6dbed163a27a4a3999ba2854ad99d7d5",
    "language" : "en",
    "page" : 1
}

stock_api_key = "XT27T0IZY9TBW887"
stock_api_url = 'https://www.alphavantage.co/query?'
stock_api_params = {
    "function" :"TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK,
    "apikey" : stock_api_key
}

def get_news():
    news_api_params["from"] = closing_dates[1]
    news_api_response = requests.get(url=news_api_url, params=news_api_params)
    article_list = news_api_response.json().get("articles")
    top_3_articles = article_list[:3]
    news_list = []
    for item in top_3_articles:
        news_dict = dict()
        news_dict["headline"] = html.unescape(item.get("title"))
        news_dict["brief"] = html.unescape(item.get("description"))
        news_list.append(news_dict)
    return news_list


chat_id = "510122498"
bot_token = "5643470724:AAGJ5pcrmYIEI6zW4EwrWyGvHmyDySiKAbo"
def send_message(bot_message):
    global chat_id, bot_token
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    response.raise_for_status()


stock_api_response = requests.get(url=stock_api_url, params=stock_api_params)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

json_stock_data = stock_api_response.json()
daily_prices_data = json_stock_data.get("Time Series (Daily)")
closing_dates = [key for key in daily_prices_data.keys()]

yesterdays_price = float(daily_prices_data.get(closing_dates[0]).get("4. close"))
day_before_yesterdays_price = float(daily_prices_data.get(closing_dates[1]).get("4. close"))

change_in_price = yesterdays_price - day_before_yesterdays_price
percentage_change_in_price = (change_in_price/yesterdays_price) * 100

print(f"Yesterday : {yesterdays_price}, day before yesterday : {day_before_yesterdays_price}")
print(f"Change in price : {percentage_change_in_price}")

if percentage_change_in_price >= 2.00 or percentage_change_in_price <= -2.00:
    top_news = get_news()
    if percentage_change_in_price >=2.00:
        message_content = f"{STOCK}:🔺{round(abs(percentage_change_in_price),2)}%\n"
    else:
        message_content = f"{STOCK}:🔻{round(abs(percentage_change_in_price),2)}%\n"
    for news_item in top_news:
        message_content+= f"Headline:{news_item['headline']}\n Brief:{news_item['brief']}\n\n\n"
    send_message(message_content)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

