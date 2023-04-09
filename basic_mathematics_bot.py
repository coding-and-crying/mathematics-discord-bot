import discord
from decouple import config
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.command()
async def add(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)


@bot.command()
async def subtract(ctx, num1: int, num2: int):
    await ctx.send(num1 - num2)


@bot.command()
async def multiply(ctx, num1: int, num2: int):
    await ctx.send(num1 * num2)


@bot.command()
async def divide(ctx, num1: int, num2: int):
    await ctx.send(num1 / num2)


bot.run(config('BOT_TOKEN'))
