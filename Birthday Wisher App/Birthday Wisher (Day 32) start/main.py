import smtplib

my_email = "helloareyouthereareyouokay@gmail.com"
password = "kdcsioymsdmfmyog"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="joyyg0606@gmail.com", msg="Subject: Hello\n\nidkrandom")
    connection.close()