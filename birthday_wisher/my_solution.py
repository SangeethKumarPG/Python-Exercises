import pandas
import datetime as dt
import random
import smtplib
##################### Extra Hard Starting Project ######################

FROM_ADDR = "sangeeth695@gmail.com"
#Replace with App password of google account
PASSWORD = ""
data_frame = pandas.read_csv("birthday_wisher/birthdays.csv")

#-------------------------- Test Data -----------------------------------#
# test_list = ["Sangeeth" , "pgsangeethkumar@gmail.com", 1999, 3, 24]
# # test_list = ["Rahul", "rahul123@gmail.com", 1998, 3, 24]
# data_frame = data_frame.drop([1], axis=0)
# data_frame.loc[len(data_frame)] = test_list
# test_list = ["Rahul", "rahul123@gmail.com", 1998, 3, 25]
# data_frame.loc[len(data_frame)] = test_list
# print(data_frame)
#------------------------------------------------------------------------#
# 1. Update the birthdays.csv
data_frame.to_csv('birthday_wisher/birthdays.csv', index=False)
birthday_dict = data_frame.to_dict(orient="records")
# print(birthday_dict)

# 2. Check if today matches a birthday in the birthdays.csv
current_date = dt.datetime.now()
current_day = current_date.day
current_month = current_date.month

todays_birthday = []

todays_birthday = [{"name" : item["name"], "email" : item["email"]} 
                   for item in birthday_dict if int(item['day']) == current_day and 
                    int(item['month']) == current_month ]
print(f"len of todays_birthdat : {len(todays_birthday)}")
if len(todays_birthday) <= 0:
    print("No birthdays today")
else:
    print(f"Todays birthday : {todays_birthday}")
    for person in todays_birthday:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
        random_letter = random.choice(letters)
        letter_content = []
        with open(f"birthday_wisher/letter_templates/{random_letter}") as letter:
            letter_content = letter.readlines()

        # print(f"Letter contents : {letter_content}")
        letter_string = "".join(letter_content)
        # print(f"Leter content is string : {letter_string}")
        name = person.get('name')
        email = person.get('email') 
        letter_string = letter_string.replace('[NAME]',name)
        letter_string = letter_string.replace('Angela','Sangeeth')
        # print(f"changed name : {letter_string}")

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=FROM_ADDR, password=PASSWORD)
            connection.sendmail(from_addr=FROM_ADDR, to_addrs=email ,msg=f"Subject:Happy Birthday!!!\n\n{letter_string}")
