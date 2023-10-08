import csv
import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("MAIL_PASS")

now = dt.datetime.now()

def birthday_list():
    birthday_list = []
    with open("birthdays.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            birthday_list.append(row)
    return birthday_list

def read_and_prep_message(name):
    with open(f"letter_templates/letter_{random.randint(1, 4)}.txt") as file:
        message = file.read()
        return message.replace("[NAME]", name)

def send_mail(origin_mail, password, destination_mail, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # make connection secure
        connection.login(user=origin_mail, password=password)
        connection.sendmail(
            from_addr=origin_mail,
            to_addrs=destination_mail,
            msg=f"subject:Happy Birthday\n\n{message}"
        )

list = birthday_list()
for line in list:
    if int(line["month"]) == now.month and int(line["day"]) == now.day:
        message = read_and_prep_message(line["name"])
        destination_mail = line["email"]
        send_mail(my_email, password, destination_mail, message)
