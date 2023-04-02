import discord
import requests
import json
from weather import *
from discord.ext import commands
import messages

token = 'Token goes here'
api_key = 'Api Goes here'
client = discord.Client(intents=discord.Intents.all())
command_prefix = '!cat'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!cat'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix+" weather"):
        if len(message.content.replace("!cat weather", '')) >= 1:
            location = message.content.replace(command_prefix+" weather", '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = json.loads(requests.get(url).content)['main']
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))
                
                
    elif message.author != client.user and message.content.startswith(command_prefix+" aqi"):
        if len(message.content.replace("!cat AQI", '')) >= 1:
            location = message.content.replace(command_prefix+" aqi", '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = coord(json.loads(requests.get(url).content)['coord'])
                await message.channel.send(embed=aqi(data, location,api_key))
            except KeyError:
                await message.channel.send(embed=error_message(location))
    elif message.author != client.user and message.content.startswith(command_prefix+" ping"):
        x=int(round(client.latency, 1)*1000)
        await message.channel.send('returns meow! in '+str(x)+' ms')
    
    elif message.author != client.user and message.content.startswith(command_prefix+" gpt"):
        await message.channel.send(messages.gpt()[0])
        await message.channel.send(messages.gpt()[1])
        
        
    elif message.author != client.user and message.content.startswith(command_prefix+" hi"):
        embed = messages.intro()
        #setting footer
        #setting image
        embed.set_image(url="https://cdn.discordapp.com/attachments/875062233305055232/1092010566626844743/banner.png")
        #setting thumbnail
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/875062233305055232/1092022304625672252/image.png")
        #Setting timestamp
       #adding fields
        embed.add_field(name="Hi",value='About me',inline=False)
        embed.add_field(name="Help",value='I help with commands',inline=True)
        embed.add_field(name="Weather",value='I tell the weather',inline=True)
        embed.add_field(name="AQI",value='I tell the Air Quality Index',inline=True)
        embed.add_field(name="Plan my trip",value='I Plan your trip',inline=True)
        # sending the embed
        await message.channel.send(embed=embed)
    


client.run(token)


#added weater
# added hi
# added aqi

# added cat gpt