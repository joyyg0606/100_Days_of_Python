import smtplib

my_email = "example@gmail.com"
password = "abc1234"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="2example@gmail.com", msg="Subject: Hello\n\nHello")
connection.close()