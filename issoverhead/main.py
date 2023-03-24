import requests
import datetime as dt
import smtplib

MY_LAT = 10.783060 # Your latitude
MY_LONG = 76.007988 # Your longitude
iss_latitude = 0.0
iss_longitude = 0.0
ist_sunrise_time = 0
ist_sunset_time = 0

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def convert_to_ist(time):
    hours = time.hour
    minutes = time.minute
    hours =  hours + 5 + (minutes + 30)//60
    minutes = (minutes + 30) % 60 
    return str(hours) + ":" + str(minutes)

def is_iss_over_me(lat, lng):
    global MY_LAT, MY_LONG
    lat_proximity = lat <= MY_LAT + 5.0 and lat >= MY_LAT - 5.0
    lng_proximity = lng <= MY_LONG + 5.0 and lng >= MY_LONG - 5.0
    print(f"result : {lat_proximity}, {lng_proximity}")
    if lat_proximity and lng_proximity:
        return True
    return False

def send_email_notification():
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="sangeeth695@gmail.com", password="omkkonvlcfzdbnvo")
        connection.sendmail(from_addr="sangeeth695@gmail.com", to_addrs="pgsangeethkumar@gmail.com", msg="Subject:Look Up!!! ISS is near you!\n\n Dear Sangeeth, The ISS is above you")


def curret_iss_position():
    global iss_latitude, iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"Iss lat : {iss_latitude}")
    print(f"iss long : {iss_longitude}")



#Your position is within +5 or -5 degrees of the ISS position.
# print(is_iss_over_me(iss_latitude,iss_longitude))
# print(is_iss_over_me(iss_latitude,iss_longitude))



def get_sun_timing():
    global ist_sunrise_time, ist_sunset_time, parameters
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    sunrise = data.get("results").get("sunrise")
    sunset = data.get("results").get("sunset")
    sunset_time_list = sunset.split("T")[1].split(":")
    sunset_time = dt.time(hour = int(sunset_time_list[0]), minute=int(sunset_time_list[1]))
    sunrise_time_list = sunrise.split("T")[1].split(":")
    sunrise_time = dt.time(hour=int(sunrise_time_list[0]), minute=int(sunrise_time_list[1]))
    ist_sunrise_time = convert_to_ist(sunrise_time)
    ist_sunset_time = convert_to_ist(sunset_time)
    print(ist_sunrise_time)
    print(ist_sunset_time)


#If the ISS is close to my current position


# print(f"Is dark : {is_dark}\n is near proximity : {iss_is_near_proximity}")

def notify():
    global ist_sunset_time, ist_sunrise_time, iss_latitude, iss_longitude
    time_now = dt.datetime.now()
    get_sun_timing()
    curret_iss_position()
    print(f"iss lat : {iss_latitude}, iss long : {iss_longitude}")
    print(f"ist sunrise time {ist_sunrise_time}, ist sunset time : {ist_sunset_time}")
    iss_is_near_proximity = is_iss_over_me(iss_latitude,iss_longitude)
    current_hour = time_now.hour
    is_dark = current_hour < int(ist_sunrise_time.split(":")[0]) or current_hour > int(ist_sunset_time.split(":")[0])
    if is_dark and iss_is_near_proximity:
        print("It is dark")
        send_email_notification()

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



