import discord
import random
import typing
from discord.ext import commands
from main import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

commandss = ['bot_info', 'news']

@bot.command()
async def info(ctx):
    await ctx.send(f'Доступные команды: {commandss}')

@bot.command()
async def bot_info(ctx):
    await ctx.send(f'Данный бот умеет выводить новости на тему глобального потепления')

@bot.command()
async def news(ctx):
    pars_info = pars()
    for news, links, imgs, date in pars_info.items():
        await ctx.send(news, links, imgs, date)

















bot.run('token')












