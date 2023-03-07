import pandas

data = pandas.read_csv("squirrel_census_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

grey = data[data.PrimaryFurColor == 'Gray'].count()[0]
red = data[data.PrimaryFurColor == 'Cinnamon'].count()[0]
black = data[data.PrimaryFurColor == 'Black'].count()[0]
report = [
    {"Fur Color" : "grey" , "count" : grey},
    {"Fur Color" : "red" , "count" : red},
    {"Fur Color" : "black" , "count" : black}

]

census_data_frame = pandas.DataFrame(report)
print(census_data_frame)

census_data_frame.to_csv("squirrel_census_pandas/report.csv")
