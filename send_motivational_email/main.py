import datetime as dt
import smtplib
import random


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
my_email = "sangeeth695@gmail.com"
my_password = "omkkonvlcfzdbnvo"
with open("send_motivational_email/quotes.txt") as quotes:
    list_of_quotes = quotes.readlines()


# print(list_of_quotes)
current_day = dt.datetime.now()
todays_quote = random.choice(list_of_quotes)
current_weekday = current_day.weekday()
if current_weekday == 3:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        message = f"Subject:Daily motivation {weekdays[current_weekday]}\n\n{todays_quote}"
        connection.sendmail(from_addr=my_email, to_addrs="pgsangeethkumar@gmail.com", msg=message)

