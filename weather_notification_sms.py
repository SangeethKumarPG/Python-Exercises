import requests


# import os

# os.getenv("key")

#export key using export KEY=value
MY_LAT = 10.783060,
MY_LONG = 76.007988

test_lat = 30.733299
test_lon = 79.066902
parameters = {
    
    "lat" : test_lat,
    "lon" : test_lon,
    "units" : "metric",
    "exclude" :"current,minutely,daily" ,
    "appid" : "d3f37269fcf467441dba03d672e5c493"
}

bot_token =""
chat_id = "510122498"

def send_message(bot_message):
    global chat_id, bot_token
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    response.raise_for_status()
    print(response.status_code)


one_call_api_url = "https://api.openweathermap.org/data/2.8/onecall?"
weather_api_url = "https://api.openweathermap.org/data/2.5/weather?"
response = requests.get(url=one_call_api_url, params=parameters)
response.raise_for_status()
json_data = response.json()


hourly_weather_list = json_data.get("hourly")
result = ["rain" for item in hourly_weather_list if item["weather"][0]["id"] < 700]

if "rain" in result:
    send_message("It will rain, Bring an umbrella☔️")












