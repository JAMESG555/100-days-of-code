import requests
import datetime
import smtplib
from config import my_email, password, dest_email

MY_LAT = -33.914589
MY_LONG = 151.241714

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now().hour
    if sunset <= time_now < sunrise:
        return True
    else:
        return False

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=dest_email, msg="Subject: ISS Overhead\n\nLook Up!")

# Uncomment this block to run the program continuously and check every minute
while True:
    if datetime.datetime.now().second == 0:
        if is_night() and is_overhead():
            send_email()


