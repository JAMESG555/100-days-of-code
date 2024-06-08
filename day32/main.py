import pandas
import datetime as dt
import random
import smtplib
from config import my_email, password
##################### Hard Starting Project ######################
today = dt.datetime.now()
today_day = today.day
today_month = today.month
pd_bd = pandas.read_csv("birthdays.csv")
birthdays_dict = pd_bd.to_dict()

def find_name_by_month_day(month, day):
    for i in range(len(birthdays_dict['month'])):
        if birthdays_dict['month'][i] == month and birthdays_dict['day'][i] == day:
            return i
    return None

def create_letter(name):
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as data:
        contents = data.read()
        contents = contents.replace("[NAME]", name)
    return contents

def send_email(i):
        letter = create_letter(birthdays_dict['name'][i])
        with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=my_email, password=password)
             connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict['email'][i], msg=f"Subject:Happy Birthday!\n\n{letter}")

if find_name_by_month_day(today_month, today_day):
    send_email(find_name_by_month_day(today_month, today_day))



