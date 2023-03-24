import smtplib


my_email = "sangeeth695@gmail.com"
#password should be generated from App passwords page of google account
my_password = ""
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(
#     from_addr=my_email, to_addrs="pgsangeethkumar@gmail.com", 
#     msg="Subject:Test Email \n\nThis is a new test email body"
# )
# connection.close()

#Alternatively
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email, to_addrs="pgsangeethkumar@gmail.com", 
        msg="Subject: <NNTO>Test Email \n\nThis is a new test email body"
    )

