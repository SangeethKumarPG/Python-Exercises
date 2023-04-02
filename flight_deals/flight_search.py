import requests
import datetime
import time
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_HEADER = {
            "apikey" : "I6T1BkeM5Lay5khuIchgS13fH5lejMhO"
        }
        self.FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/locations/query?"
        self.FLIGHT_LOCATION_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search?"

    def search_flight(self, location):
        parameters = {
            "term":location,
            "locale" : "en-US",
            "location_types": "airport",
            "limit" : 1,
            "active_only" : True
        }
        fligh_search_response = requests.get(url=self.FLIGHT_SEARCH_ENDPOINT,params=parameters, headers=self.API_HEADER)
        return fligh_search_response.json().get("locations")[0].get("code")


    def get_flight_data(self,location,stopover=0):
        todays_date = datetime.datetime.now()
        time_delta = datetime.timedelta(days=180)
        end_date = todays_date + time_delta
        requset_params = {
            "fly_from" : "BOM",
            "fly_to" : "",
            "date_from" : todays_date.strftime("%d/%m/%Y"),
            "date_to" : end_date.strftime("%d/%m/%Y"),
            "adults" : 1,
            "children" : 0,
            "infants" : 0,
            "adult_hold_bag" : 1,
            "adult_hand_bag" :1,
            "curr" : "INR",
            "limit" : 10,
            "max_stopovers" : stopover
        }
        requset_params["fly_to"] = location
        details_search_response = requests.get(url=self.FLIGHT_LOCATION_SEARCH_ENDPOINT, headers = self.API_HEADER, params=requset_params)
        return details_search_response
