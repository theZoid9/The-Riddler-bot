import discord
from discord.ext import commands
import random


# Create instance of bot.
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Map of riddles to answers
riddles = {
    "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": "An echo.",
    "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?": "A pencil."
}

# To keep track of the last riddle asked per channel
last_riddle = {}

# 1st command

@bot.command(name='riddle')
async def tell_riddle(ctx):
    riddle, answer = random.choice(list(riddles.items()))
    last_riddle[ctx.channel.id] = riddle
    await ctx.send(riddle)

@bot.command(name='answer')
async def give_answer(ctx):
    if ctx.channel.id in last_riddle:
        await ctx.send(riddles[last_riddle[ctx.channel.id]])
    else:
        await ctx.send("I haven't told a riddle in this channel yet!")

bot.run('discord token')
