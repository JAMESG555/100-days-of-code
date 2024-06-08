# import smtplib
# from config import my_email, password
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="james_G5@hotmail.com", msg="Subject:Hello\n\nTest123")
#     # connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year

print(type(year))
print(type(now))

if year == 2024:
    print(True)
else:
    print(False)
