import requests
import datetime as dt

server_time = "UTC"
our_time = "Asia/kolkata"

parameters = {
    "lat" : 10.783060,
    "lng" : 76.007988,
    "formatted" : 0 
}
def convert_to_ist(time):
    hours = time.hour
    minutes = time.minute
    hours =  hours + 5 + (minutes + 30)//60
    minutes = (minutes + 30) % 60 
    return str(hours) + ":" + str(minutes)

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

# print(response.json())
data = response.json()
sunrise = data.get("results").get("sunrise")
sunset = data.get("results").get("sunset")
sunset_time_list = sunset.split("T")[1].split(":")
sunset_time = dt.time(hour = int(sunset_time_list[0]), minute=int(sunset_time_list[1]))
sunrise_time_list = sunrise.split("T")[1].split(":")
sunrise_time = dt.time(hour=int(sunrise_time_list[0]), minute=int(sunrise_time_list[1]))
ist_sunrise_time = convert_to_ist(sunrise_time)
ist_sunset_time = convert_to_ist(sunset_time)

print(f"Sunset time : {ist_sunset_time}")
print(f"Sunrise time : {ist_sunrise_time}")

# test_time = dt.time(hour=8, minute=46)
# print(f"Test time : {convert_to_ist(test_time)}")

current_time = str(dt.datetime.now())
# print(current_time.split(" "))

