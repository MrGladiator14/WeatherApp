import requests
import os
from datetime import datetime 

location = input("Enter the city name : ")
api_link = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=8e1c8de1e3ff923e010a81287937bdad")
complete_api_link = api_link.json()

temp_city = ((complete_api_link['main']['temp']) - 273.15)
weather_desc = (complete_api_link['weather'][0]['description'])
hmdt = (complete_api_link['main']['humidity'])

date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")
print(f"Weather stats for > {location} | {date_time}")
print("Current Temperature  : {:.2f} deg C".format(temp_city))
print("Current Weather Description : ", weather_desc)
print("Current Humidity  : ", hmdt, '%')
