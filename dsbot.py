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
    news = list(pars_info['news'])
    links = list(pars_info['links'])
    imgs = list(pars_info['imgs'])
    date = list(pars_info['date'])
    for i in range(10):
        await ctx.send(news[i])
        await ctx.send(links[i])
        await ctx.send(imgs[i])
        await ctx.send(date[i])

















bot.run('token')












