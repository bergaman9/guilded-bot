import discord
import guilded
from guilded.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ["TOKEN"]

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.command(description='For when you wanna settle the score some other way')
async def ping(ctx, *choices: str):
    await ctx.send("Pong")

@bot.command(description='For when you wanna settle the score some other way')
async def embed(ctx, *choices: str):
    embed = guilded.Embed(title="Türk Oyuncu Topluluğu", description="Merhabalar!")
    await ctx.send(embed=embed)

@bot.command(description="Clears the chat")
async def clear(ctx, amount: int):
    await ctx.delete(amount)

bot.run(token)