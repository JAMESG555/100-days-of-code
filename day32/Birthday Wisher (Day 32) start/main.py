import datetime as dt
import random
import smtplib
from config import my_email, password
now = dt.datetime.now()

def send_email():
    if get_day():
        with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=my_email, password=password)
             connection.sendmail(from_addr=my_email, to_addrs="james_G5@hotmail.com", msg=f"Subject:Monday Motivational Quote\n\n{get_quote()}")


def get_day():
    if now.weekday() == 0:
        return True
    else:
        return False

def get_quote():
    with open("quotes.txt", "r") as data:
        quote_list = data.readlines()
    return quote_list[random.randint(0, len(quote_list)-1)]

send_email()