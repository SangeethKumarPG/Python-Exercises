import requests
import datetime
import flight_search


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.FLIGHT_PRICES_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search?"
        self.API_HEADER = {
            "apikey" : "I6T1BkeM5Lay5khuIchgS13fH5lejMhO"
        }
        self.details_list = []
        self.fs = flight_search.FlightSearch()
        self.intermediary_stop = False

    def format_time(self,time_string):
        dt = time_string.split("T")[0]
        tm = time_string.split("T")[1].split(":")
        day = int(dt.split("-")[2])
        month = int(dt.split("-")[1])
        year =int(dt.split("-")[0])
        hour = int(tm[0])
        minute = int(tm[1])
        return datetime.datetime(year=year,day=day, month=month, hour=hour, minute=minute)


    def get_flight_detail(self,sheet_data):
        locations = [city.get("iataCode") for city in sheet_data["prices"]]
        for location in locations:
            detail = self.get_detail(location)
            self.details_list.append(detail)
        return self.details_list



    def get_detail(self,location):
        details_search_response = self.fs.get_flight_data(location)
        if len(details_search_response.json().get('data')) <= 0:
            details_search_response = self.fs.get_flight_data(location=location, stopover=1)
        if len(details_search_response.json().get('data')) != 0 and len(details_search_response.json().get('data')[0].get('route')) > 1:
            self.intermediary_stop = True
        else:
            self.intermediary_stop = False
        try:
            # print(details_search_response.text)
            price = details_search_response.json().get('data')[0].get('price')
            departure_city = details_search_response.json().get('data')[0].get('cityFrom')
            departure_city_iata_code = details_search_response.json().get('data')[0].get('cityCodeFrom')
            arrival_city = details_search_response.json().get('data')[0].get('cityTo')
            arrival_city_iata_code = details_search_response.json().get('data')[0].get('cityCodeTo')
            arrival_time = details_search_response.json().get('data')[0].get('route')[0].get('local_arrival')
            departure_time = details_search_response.json().get('data')[0].get('route')[0].get('local_departure')
            if self.intermediary_stop :
                stop_over_city = details_search_response.json().get('data')[0].get('route')[0].get('cityTo')
        except IndexError:
            detail_dict = {location : {"details":"Not available"}}
        else:
            arrival_formatted_time = self.format_time(arrival_time).strftime("%d/%m/%Y %H:%M")
            departure_formatted_time = self.format_time(departure_time).strftime("%d/%m/%Y %H:%M")
            if not self.intermediary_stop:
                detail_dict = {location : {"price":price,
                                        "departure_city":departure_city,
                                        "depature_city_code" : departure_city_iata_code,
                                        "arrival_city" : arrival_city,
                                        "arrival_city_code" : arrival_city_iata_code,
                                        "arrival_time" : arrival_formatted_time,
                                        "departure_time" : departure_formatted_time                                   
                                        }}
            else:
                detail_dict = {location : {"price":price,
                                        "departure_city":departure_city,
                                        "depature_city_code" : departure_city_iata_code,
                                        "arrival_city" : arrival_city,
                                        "arrival_city_code" : arrival_city_iata_code,
                                        "arrival_time" : arrival_formatted_time,
                                        "departure_time" : departure_formatted_time,
                                        "intermediary_stop" : stop_over_city                                   
                                        }}

        return detail_dict
    
