#Traditional way of reading csv file

# with open("weather_data_pandas/weather_data.csv") as file:
#     weather_data = file.readlines()

# print(f"The weather data : {weather_data}")

#Using csv library to read file 

# import csv

# with open("weather_data_pandas/weather_data.csv") as file:
#     data = csv.reader(file)
#     temprature = []
#     for row in data:
#         if row[1] != 'temp':
#             temprature.append(int(row[1]))
#     print(temprature)
#     for row in data:
#         print(row)

import pandas 

data = pandas.read_csv("weather_data_pandas/weather_data.csv")
print(data["temp"])

#Converting dataframe to dictionary
data_to_dict = data.to_dict()
print(f"Data as dictionary : {data_to_dict}")

#converting series to list

temp_list = data["temp"].to_list()
print(f"Temprature series as a list : {temp_list}")

#calculating mean(average) traditionally with list
avg_temp = sum(temp_list) / len(temp_list)

print(f"Average temprature = {avg_temp}")

#calculating mean(average) of series using mean() function

mean_of_temp = data["temp"].mean()

print(f"Mean of the tempratures  = {mean_of_temp}")

#calculating maximum value using pandas series max function

max_temp = data["temp"].max()
print(f"Maximum temprature is : {max_temp}")

#accessing columns directly as attributes

print(data.condition)

#filtering out data by rows

print(f"Weather condition of monday = \n {data[data.day == 'Monday']}")

#filtering the row with maximum temprature

print(f"Weather condtion of the day with maximum temprature : \n {data[data.temp == data.temp.max()]}")

print(f"Weather condition of tuesday : {data[data.day == 'Tuesday'].temp[1]}")

#Mondays temprature to farenheight

print(f"Mondays temprature to farenheight : {data[data.day == 'Monday'].temp[0] * (9/5) + 32}")

# Alternatively 
print(f"Mondays temprature to farenheight : {int(data[data.day == 'Monday'].temp) * (9/5) + 32}")

#Creating a new dataframe from dictionary

student_score = {
    "name" : ["Jake", "John", "Sam"],
    "mark" : [50, 67, 80]
}
data_frame = pandas.DataFrame(student_score)
print(f"Data frame : \n {data_frame}")
#Converting the created data frame to csv file

data_frame.to_csv("weather_data_pandas/new_csv_data.csv")