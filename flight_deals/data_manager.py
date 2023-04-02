import requests
import flight_search
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_PUT_API_ENDPOINT ="https://api.sheety.co/45fb9d517a6e430d238aa49526695266/flightDeals/prices/"
        self.SHEETY_GET_API_ENDPOINT = "https://api.sheety.co/45fb9d517a6e430d238aa49526695266/flightDeals/prices"
        self.SHEETY_GET_API_ENDPOINT_FOR_USERDETAILS = "https://api.sheety.co/45fb9d517a6e430d238aa49526695266/flightDeals/users"
        self.request_header = {
            "Authorization": "Bearer This_is_my_top_secret_bearer_token"
        }
        self.sheet_data = None
        self.flight_search = flight_search.FlightSearch()

    def get_sheet_data(self):
        get_response = requests.get(self.SHEETY_GET_API_ENDPOINT, headers=self.request_header)
        self.sheet_data = get_response.json()
        return self.sheet_data


    def add_iata_code_to_sheets(self):
        end_point = self.SHEETY_PUT_API_ENDPOINT
        for item in self.sheet_data.get("prices"):
            id = item.get("id")
            end_point = f"{self.SHEETY_PUT_API_ENDPOINT}{int(id)}"
            iata_code = self.flight_search.search_flight(item.get("city"))
            request_body = {
                "price":{
                    "iataCode":iata_code
                }
            }
            put_data_response = requests.put(url=end_point, json=request_body, headers=self.request_header)
            id = 0


    def is_cheap(self,flight_details):
        price_list = self.sheet_data.get('prices')
        key_list = []
        for i in range(9):
            key_list.append(list(flight_details[i].keys())[0])
        simplified_flight_detail = {k:v for i in range(len(key_list)) for (k,v) in flight_details[i].items()}
        # print(f"Simplified flight details : {simplified_flight_detail}")
        simplified_sheet_data = {}
        for i in range(len(price_list)):
            k = price_list[i].get("iataCode")
            simplified_sheet_data[k] = {
                "city" : price_list[i].get('city'),
                "lowestPrice": price_list[i].get('lowestPrice'),
                "inr": price_list[i].get('inr'),
                "id": price_list[i].get('id')
            }
        discounts_available = {}
        for item in key_list:
            try:
                if simplified_flight_detail[item].get('price') < simplified_sheet_data[item].get('inr'):
                    discounts_available[item] = simplified_flight_detail[item]
            except TypeError:
                pass
        return discounts_available


    def get_user_emails(self):
        response_data = requests.get(url=self.SHEETY_GET_API_ENDPOINT_FOR_USERDETAILS, headers=self.request_header)
        # print(response_data.text)
        response_data_json = response_data.json()
        users_list = response_data_json.get("users")
        email_list = [user.get('email') for user in users_list]
        # print(email_list)
        return email_list

