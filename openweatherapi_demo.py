import requests
import json
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
one_call_api_url = "https://api.openweathermap.org/data/2.8/onecall?"
weather_api_url = "https://api.openweathermap.org/data/2.5/weather?"
response = requests.get(url=one_call_api_url, params=parameters)
response.raise_for_status()
# print(response.status_code)
json_data = response.json()
# json_formatted_data = json.dumps(json_data, indent=4)

# with open("dummy.json", "w") as file:
#     file.write(json_formatted_data)

hourly_weather_list = json_data.get("hourly")
result = ["rain" for item in hourly_weather_list if item["weather"][0]["id"] < 700]
# print(result)

if "rain" in result:
    print("Bring an umbrella")



# json_formatted_data = json.dumps(result, indent=4)

# with open("dummy.json", "w") as file:
#     file.write(json_formatted_data)



