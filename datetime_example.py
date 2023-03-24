import datetime as dt

current_time = dt.datetime.now()
# print(current_time)
print(current_time.year)
print(current_time.day)
print(current_time.weekday())

#To create a new date

new_date = dt.datetime(year=1999, day=2, month=11)

print(new_date)