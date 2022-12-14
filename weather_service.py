# This file establishes a connection with weather API to fetch the weather information

import requests  # this package needs to be installed locally
import json


# reference API documentation: https://open-meteo.com/en/docs
# API = https://api.open-meteo.com/v1/forecast?latitude=60.3172&longitude=24.963301&current_weather=True&windspeed_unit=ms

def getWeatherDataByLatLon(lat, lon):
    url = 'https://api.open-meteo.com/v1/forecast?current_weather=True&windspeed_unit=ms&latitude=' + str(
        lat) + '&longitude=' + str(lon)
    response_API = requests.get(url)
    # print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    temp = parse_json['current_weather']['temperature']
    wind_speed = parse_json['current_weather']['windspeed']

    # https://www.jodc.go.jp/data_format/weather-code.html
    weather_code = parse_json['current_weather']['weathercode']
    return (temp, wind_speed, weather_code)


""" Only temp, wind speed and cloudiness were seleceted parameters
from the weather API as required by the game"""
