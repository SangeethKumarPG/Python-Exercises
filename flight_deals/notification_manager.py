from email.mime.text import MIMEText
import requests
import smtplib
import flight_data
import datetime

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.chat_id = "510122498"
        self.bot_token = ""
        self.username = ""
        self.password = ""
        #self.google_flight_url = 'https://www.google.com/travel/flights?q=Flights%20to%20SFO%20from%20HNL%20on%202022-09-13%20through%202022-09-17'



    def format_date(self,time_string):
        dt = time_string.split(" ")[0]
        day = int(dt.split("/")[0])
        month = int(dt.split("/")[1])
        year =int(dt.split("/")[2])
        return datetime.date(year=year,day=day, month=month)


    def send_message(self,bot_message):
        rm_index = bot_message.index('booking')
        bot_message = bot_message[:rm_index]
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.chat_id + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)
        response.raise_for_status()
        print(response.status_code)


    def create_message_body(self,discounted_flights):
        message_list = []
        booking_url = self.generate_url(discounted_flights)
        discounted_flights_keys = list(discounted_flights.keys())
        for key in discounted_flights_keys:
            message_content = f"Low price Alert₹₹₹!!!"
            price = round(discounted_flights[key].get('price'))
            depart_city = discounted_flights[key].get('departure_city')
            depart_city_code = discounted_flights[key].get('depature_city_code')
            arrival_city = discounted_flights[key].get('arrival_city')
            arrival_city_code = discounted_flights[key].get('arrival_city_code')
            arrival_time = discounted_flights[key].get('arrival_time')
            departure_time = discounted_flights[key].get('departure_time')
            if discounted_flights[key].get('intermediary_stop') != None:
                stop_over_city = discounted_flights[key].get('intermediary_stop')
                message_content += f"Only ₹{price} from {depart_city}-{depart_city_code} to {arrival_city}-{arrival_city_code}, via {stop_over_city} , from {arrival_time} to {departure_time}"
                message_content+= f"\n booking link : {booking_url[key]}"
            else:
                message_content += f"Only ₹{price} from {depart_city}-{depart_city_code} to {arrival_city}-{arrival_city_code}, from {arrival_time} to {departure_time}"
                message_content+= f"\n booking link : {booking_url[key]}"
            message_list.append(message_content)
            # self.send_message(message_content)
            message_content=""
        return message_list


    def send_discount_message(self,discounted_flights):
        message_content_list = self.create_message_body(discounted_flights) 
        for message_content in message_content_list:
            self.send_message(message_content)
        
    def generate_url(self, discounted_flights):
        discounted_flights_keys = list(discounted_flights.keys())
        url_dict = {}
        for key in discounted_flights_keys:
            arrival_time = self.format_date(discounted_flights[key].get('arrival_time')).strftime('%Y-%m-%d')
            departure_time = self.format_date(discounted_flights[key].get('departure_time')).strftime('%Y-%m-%d')
            arrival_city_code = discounted_flights[key].get('arrival_city_code')
            depart_city_code = discounted_flights[key].get('depature_city_code')
            google_flight_url = f"https://www.google.com/travel/flights?q=Flights%20to%20{arrival_city_code}%20from%20{depart_city_code}%20on%20{departure_time}%20through%20{arrival_time}"
            url_dict[key] = google_flight_url
            
        return url_dict

    
    def send_email(self, discounted_flights, email_list):
        message_content_list = self.create_message_body(discounted_flights) 
        for user in email_list:
            for message_content in message_content_list:
                with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                    connection.starttls()
                    connection.login(user=self.username, password=self.password)
                    updated_message_content = message_content.replace('₹','Rs')
                    connection.sendmail(from_addr=self.username, to_addrs=user,msg=f"Subject:New Low Price Flight \n\n{updated_message_content}")
                
        