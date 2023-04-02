import discord
import random

color= 0xB200FF

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