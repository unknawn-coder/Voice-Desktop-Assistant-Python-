import datetime as dt
import requests
from config import api_key_weather
api_key = api_key_weather
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY ="Brampton"

def kelvin_to_celsius_fahrenheit(kelvin):
  celsius = kelvin - 273.15
  fahrenheit = celsius * (9/5) + 32
  return celsius,fahrenheit


url = BASE_URL + "q=" + CITY + "&appid=" + api_key  
response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius , temp_fahrenheit =kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
#print(response)
'''print(f"the temperature is {temp_celsius:.2f} degree celsius in {CITY} today")
print(f"Feels like {feels_like_celsius:.2f} degree celsius ")
print(f"wind speed in {CITY} today is {wind_speed:.2f} meters per second")
print(f"Humididty is {humidity:.2f}% ")
print(f"Today {description} can be seen")
print(f"Sun rises in {CITY} at {sunrise_time} local time")
print(f"Sun set in {CITY} at {sunset_time} local time")'''