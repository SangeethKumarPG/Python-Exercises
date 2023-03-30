import requests
import datetime as dt
#--------------------- Keys fot nutritionx ---------------------#
APP_ID= '2d8b5677'
API_KEY='118c24f438e258231d70363bed14d6f4'
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
api_request_header = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "Content-Type" :"application/json"
}

post_request_body = {
    "query" : input("Enter your effort as a string : "),
    "gender" : "male",
    "weight_kg" : 72.5,
    "height_cm" : 169.00,
    "age" : 23
}

response = requests.post(url=API_ENDPOINT, json=post_request_body, headers=api_request_header)
# print(response.text)

nutritionx_response_json = response.json()
excercises = nutritionx_response_json.get("exercises")


#----------- Sheety for google sheets ----------------------------------#
sheety_post_end_point = "https://api.sheety.co/45fb9d517a6e430d238aa49526695266/myWorkouts/workouts"
sheety_request_header = {
    "Authorization" : "Bearer This_is_my_really_long_secret_token_for_authorization"
}
for excercise in excercises:
    sheety_request_body = {
        "workout" : {
            "date":dt.datetime.now().strftime("%d/%m/%Y"),
            "time":dt.datetime.now().strftime("%H:%M:%S"),
            "exercise":excercise.get("user_input").title(),
            "duration":excercise.get("duration_min"),
            "calories" : excercise.get("nf_calories")
        }
    }
    sheety_response = requests.post(url=sheety_post_end_point, json=sheety_request_body, headers=sheety_request_header)
    print(sheety_response.text)


