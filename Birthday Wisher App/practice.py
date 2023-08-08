import random
import smtplib

#my_email = "helloareyouthereareyouokay@gmail.com"
#password = "kdcsioymsdmfmyog"

#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection = smtplib.SMTP("smtp.gmail.com")
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email, to_addrs="joyyg0606@gmail.com", msg="Subject: Hello\n\nidkrandom")
#    connection.close()

import datetime as dt
from sqlite3 import connect

#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#print(now)

#date_of_birth = dt.datetime(year=2006, month=7, day=14, hour=2)

MY_EMAIL = "helloareyouthereareyouokay@gmail.com"
MY_PASS = "kdcsioymsdmfmyog"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("Birthday Wisher App\Birthday Wisher (Day 32) start\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}")