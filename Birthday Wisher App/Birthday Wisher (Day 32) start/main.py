import smtplib

my_email = "liv125461@gmail.com"
password = "abc123"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="vxntcy@gmail.com", msg="Subject: Hello\n\nHello")
connection.close()