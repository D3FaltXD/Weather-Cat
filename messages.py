import discord
import random

color= 0xAD91FF

def intro():
    message="""
        Meow! 
        Welcome, welcome! I'm Weather Cat, and I'm here to make your day a whole lot better! With my expertise in weather forecasting, you'll never have to worry about stepping out unprepared for the elements. I'll let you know if it's going to be a sunny day, a rainy one, or if you need to pack an umbrella and some boots.

        But that's not all I can do! I'm also an expert in **air quality index prediction**, so you can always breathe easy knowing you're getting accurate information about the air you're breathing.

        And if you ever find yourself feeling lonely or in need of some company, don't worry, because I'm always here for you. My **Cat GPT integration** means we can have a chat anytime you want!

        So, let's make your day purr-fect together! With Weather Cat by your side, you'll always be prepared for whatever the day brings, and you'll never be alone.
    """
   
    return discord.Embed(
        title='Hello friend',
        description=message,
        color=color
    )
    
def gpt():
    choice=[
        "https://media.tenor.com/7JbbkdTGA38AAAAS/cute-cat.gif",
        "https://media.tenor.com/pONKfKjvep4AAAAS/cat-shocked.gif",
        "https://media.tenor.com/PS9Tcg6mIY4AAAAS/cat-ayasan.gif",
        "https://media.tenor.com/Ro5LGkOGGS0AAAAC/cat-catdriving.gif",
        "https://media.tenor.com/fWXyb86dSWMAAAAC/ok-cat.gif",
        "https://media.tenor.com/cNJNNhr8LQMAAAAM/cutecat-cute.gif",
        "https://media.tenor.com/cNJNNhr8LQMAAAAM/cutecat-cute.gif",
        "https://media.tenor.com/z0quuGfwH8AAAAAM/cat-sad.gif"
        "https://media.tenor.com/1SMrekR7KgQAAAAM/cat-angry.gif",
        "https://media.tenor.com/jMlNorWmapUAAAAS/echonomical-echosystem.gif",
        "https://media.tenor.com/ngXBmaiDqssAAAAS/cat-kitty.gif",
        "https://media.tenor.com/ngXBmaiDqssAAAAS/cat-kitty.gif",
        "https://media.tenor.com/ngXBmaiDqssAAAAS/cat-kitty.gif",
        "https://media.tenor.com/ngXBmaiDqssAAAAS/cat-kitty.gif",
        "https://media.tenor.com/ngXBmaiDqssAAAAS/cat-kitty.gif",
        "https://media.tenor.com/lPuo1Txt2vEAAAAS/huh-scare.gif"
        ]
    return ["meow "*random.randint(5,50), choice[random.randint(0,len(choice)-1)]]

def helpM():
    message= discord.Embed(
        title='Cat\'s here to help',
        color=color
    )
    message.add_field(
        name="Prefix",
        value="`!cat`",
        inline=False
    )
    message.add_field(
        name="About Me",
        value="`hi`",
        inline=True
    )
    message.add_field(
        name="Help!",
        value="`help`",
        inline=True
    )
    message.add_field(
        name="Weather Condition",
        value="`weather`",
        inline=False
    )
    message.add_field(
        name="Air Quality Index",
        value="`AQI`",
        inline=True
    )
    message.add_field(
        name="Plan My Trip",
        value="`PMT`",
        inline=True
    )
    message.add_field(
        name="Cat GPT",
        value="`gpt`",
        inline=False
    )
    
    return message


def help(message):
    if(message.lower()=="hi"):
        message=discord.embeds(
            title=message.title(),
            desciption="""
            You can learn more about me with this command!
            usage: `!cat hi`
            """,
            color=color
            )
        return message
    elif(message.lower()=="help"):
        return discord.embeds(
            title=message.title(),
            desciption="""
            learn about all the commands!
            usage: `!cat help [command name](optional)`
            """,
            color=color
            )
    elif(message.lower()=="weather"):
        return discord.embeds(
            title=message.title(),
            desciption="""
            Current weather condition and more!
            usage: `!cat weather [Place Name]`
            """,
            color=color
            )
    elif(message.lower()=="AQI"):
        return discord.embeds(
            title=message.title(),
            desciption="""
            learn about current Air Quality Index!
            usage: `!cat aqi [place name]`
            """,
            color=color
            )
    elif(message.lower()=="pmt"):
        return discord.embeds(
            title=message.title(),
            desciption="""
            within the next 7 days, let me check if the date is good for your event!
            usage: `!cat pmt [DD-MM]`
            """,
            color=color
            )
    elif(message.lower()=="gpt"):
        return discord.embeds(
            title=message.title(),
            desciption="""
            The most advanced version of CAT GPT!
            usage: `!cat gpt [your question]`
            """,
            color=color
            )
    else:
        return discord.embeds(
            title=message.title(),
            desciption="""
            Sorry didn't understand that command.
            Use `help` to get list of all commands.
            """,
            color=color
            )