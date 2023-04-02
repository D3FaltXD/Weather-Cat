import discord
import requests
import json
from weather import *
from discord.ext import commands
import messages

color = 0xB200FF
key_features = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature',
    'pressure': 'Air Pressure',
    'humidity': 'Humidity',
}
key_AQI = {
    "co":"Carbon Monoxide",
    "no":"Nitrogen Oxide",
    "no2":"Nitrogen Dioxide",
    "o3":"Ozone",
    "so2":"Sulphur Dioxide",
    "pm2_5":"PM 2.5",
    "pm10":"PM 10",
    "nh3":"Ammonia"
}


def coord(data):
    lon=data['lon']
    lat=data['lat']
    return [lat,lon]

def aqi(data,location,api_key):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={data[0]}&lon={data[1]}&appid={api_key}'
    data = json.loads(requests.get(url).content)['list']
    print(data,"\n\n\n\n\n\n")
    AQI=data[0]["main"]["aqi"]
    print(AQI)
    if(AQI==1):
        AQI="Good"
    elif(AQI==2):
        AQI="Fair"
    elif(AQI==3):
        AQI="Moderate"
    elif(AQI==4):
        AQI="Poor"
    else:
        AQI="Very Poor"
    location = location.title()
    message = discord.Embed(
        title=f'Weather in {location}',
        color=color
    )
    message.add_field(
        name="AQI",
        value=AQI,
        inline=False
    )
    for key in data[0]["components"]:
        print(key)
        message.add_field(
            name=key_AQI[key],
            value=str(data[0]["components"][key]),
            inline=True
        )
    message.set_thumbnail(url="https://media.discordapp.net/attachments/875062233305055232/1092055658880315433/image.png")
    return message



def weather_message(data, location):
    location = location.title()
    message = discord.Embed(
        title=f'Weather in {location}',
        color=color
    )
    for key in data:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline=True
        )
    message.set_thumbnail(url="https://media.discordapp.net/attachments/875062233305055232/1092055658880315433/image.png")
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}',
        color=color
    )