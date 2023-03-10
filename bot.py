import guilded
from guilded.ext import commands
from dotenv import load_dotenv
import os
import random

load_dotenv()
token = os.environ["TOKEN"]
print(token)

bot = commands.Bot(command_prefix='>')


@bot.event
async def on_ready():
    print('Ready')

@bot.command(description='For when you wanna settle the score some other way')
async def ping(ctx, *choices: str):
    await ctx.send("Pong")

@bot.command(description='For when you wanna settle the score some other way')
async def embed(ctx, *choices: str):
    embed = guilded.Embed(title="Türk Oyuncu Topluluğu", description="Merhabalar!")
    await ctx.send(embed=embed)

bot.run(token)