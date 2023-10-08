import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("MAIL_PASS")
destination = os.getenv("DESTINATION")


def send_mail(origin_mail, password, destination_mail, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # make connection secure
        connection.login(user=origin_mail, password=password)
        connection.sendmail(
            from_addr=origin_mail,
            to_addrs=destination_mail,
            msg=f"subject:Quote for the day\n\n{message}"
        )


def get_quote():
    with open("quotes.txt") as f:
        messages = f.readlines()
    return random.choice(messages)


if __name__ == "__main__":
    message = get_quote()
    now = dt.datetime.now()
    if now.weekday() == 6:
        send_mail(origin_mail=my_email, password=password, destination_mail=destination, message=message)

