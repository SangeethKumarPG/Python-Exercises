#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_data
import notification_manager

dm = data_manager.DataManager()

sheet_data = dm.get_sheet_data()

fd = flight_data.FlightData()



flight_details = fd.get_flight_detail(sheet_data=sheet_data)
discounted_flights = dm.is_cheap(flight_details)

nm = notification_manager.NotificationManager()
nm.send_discount_message(discounted_flights=discounted_flights)
mailing_list = dm.get_user_emails()
nm.send_email(discounted_flights, mailing_list)

