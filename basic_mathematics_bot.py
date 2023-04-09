import discord
from decouple import config
from discord.ext import commands
from typing import Union

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.command()
async def easteregg(ctx):
    await ctx.send("The most powerful enemy is yourself, that's the price of being aware of your own existence.")


@bot.command()
async def add(ctx, num1: Union[int, float], num2: Union[int, float]):
    await ctx.send(num1 + num2)


@bot.command()
async def subtract(ctx, num1: Union[int, float], num2: Union[int, float]):
    await ctx.send(num1 - num2)


@bot.command()
async def multiply(ctx, num1: Union[int, float], num2: Union[int, float]):
    await ctx.send(num1 * num2)


@bot.command()
async def divide(ctx, num1: Union[int, float], num2: Union[int, float]):
    await ctx.send(num1 / num2)


bot.run(config('BOT_TOKEN'))
