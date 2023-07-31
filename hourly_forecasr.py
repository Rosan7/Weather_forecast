from datetime import timezone
import datetime
import time
import requests
import json

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
response_API = requests.get(url)
data = response_API.text
json_data = json.loads(data)
list_dates = json_data['list']


def get_info(date, time, parameter):
    date_provided = f"{date}, {time}"
    date_format = datetime.datetime.strptime(date_provided, "%m/%d/%Y, %H:%M:%S")
    utc_time = date_format.replace(tzinfo=timezone.utc)
    unix_time = int(utc_time.timestamp())
    for dates in list_dates:
        if dates['dt'] == unix_time:
            if parameter == "speed":
                return dates['wind'][parameter]
            else:
                return dates['main'][parameter]


running = True
print('This is a Weather forecasting Application.You have four options')
print('Enter 1 to Get Predicted Temparature')
print('Enter 2 to Get Wind Speed')
print("Enter 3 to Get Pressure")
print("Enter 0 to Exit the Application")
while running:
    option = int(input("Enter your choice : "))
    if option == 1:
        date = input("Enter a date in between 27/03/2019 and 31/03/2019 in mm/dd/yyyy : ")
        time = input("Enter a time in between from 27/03/2019 18:00:00 hrs to 31/03/2019 17:00:00 hrs based on the "
                     "date provided in hh:00:00 format : ")

        print(get_info(date, time, "temp"))

    elif option == 2:
        date = input("Enter a date in between 27/03/2019 and 31/03/2019 in mm/dd/yyyy : ")
        time = input("Enter a time in between from 27/03/2019 18:00:00 hrs to 31/03/2019 17:00:00 hrs based on the "
                     "date provided in hh:00:00 format : ")
        print(get_info(date, time, "speed"))
    elif option == 3:
        date = input("Enter a date in between 27/03/2019 and 31/03/2019 in mm/dd/yyyy : ")
        time = input("Enter a time in between from 27/03/2019 18:00:00 hrs to 31/03/2019 17:00:00 hrs based on the "
                     "date provided in hh:00:00 format : ")
        print(get_info(date, time, "pressure"))

    elif option == 0:
        print("Have a great day!!!")
        running = False
    else:
        print("Wrong Choice . Enter your choice again!!!!")
        print()
