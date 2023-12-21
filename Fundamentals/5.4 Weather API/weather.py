from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv('WEATHERAPI_API_KEY')

city_to_search = input("Where do you want to know the weather for?\n")

url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_to_search}&aqi=no'
response = requests.get(url)
weather_json = response.json()

weather_unit = 'c'
temp = weather_json.get('current').get(f'temp_{weather_unit}')
description = weather_json.get('current').get('condition').get('text')
location = weather_json.get('location').get('name')

print(weather_json)
print(f'The weather in {location} is {temp} deg. {weather_unit.upper()} and and {description}')