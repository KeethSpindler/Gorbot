import os
import requests
from discord.ext import commands
from dotenv import load_dotenv
from funcs.Bartender import Drink
from funcs.Pin import Pin
from util.Request import Request
from util.Sanitizer import DrinkJsonSanitizer
from util.Formatter import DrinkFormatter
from util.Embedder import DrinkEmbedder, PinEmbedder

load_dotenv()
TOKEN = os.getenv('TOKEN')
request = Request(requests)

bot = commands.Bot(command_prefix='.')

'''
@author: Keeth S.
@desc: Returns a random drink embedded from the Drink object's  embed method
@retunrs: async message back to channel
'''
@bot.command()
async def drink(ctx):
    try:
        drink_json = request.get_drink_json()
        drink = Drink(drink_json, DrinkJsonSanitizer, DrinkFormatter, DrinkEmbedder)
        await ctx.send(embed = drink.embed)
    except Exception as ex:
        print(ex)
        await ctx.send('Sorry, a server-side error occured')

@bot.command()
async def cocktail(ctx):
    await drink(ctx)

'''
@author: Keeth S.
@desc: Sends a embed to the Pin channel when a user reply's to a message with .pin
@retunrs: async message back to channel confirming message was pinned
'''
@bot.command()
async def pin(ctx):
    try:
        if not ctx.message.reference:
            await ctx.message.channel.send('You have to reply .pin to the message you want pinned.')
            return
        reply = await ctx.message.channel.fetch_message(ctx.message.reference.message_id)
        pin = Pin(reply, PinEmbedder)
        pin_channel = bot.get_channel(791029579737071616)
        await pin_channel.send(embed=pin.embed)
        await ctx.message.channel.send('You got it, message pinned.')
    except Exception as ex:
        print(ex)
        await ctx.send('Sorry, a server-side error occured')

@bot.event
async def on_ready():
    print(f'{bot.user} is online.')

bot.run(TOKEN)