import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')

bot.activity = discord.Game(name='Demon Slayer')

@bot.event
async def on_ready():
    print(f'{bot.user.name} si e\' connesso al server Cazzate Time!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    b8ne_quotes = [
        'ABABABABABA',
        'UGU GAGA UGU GAGA',
        'Coglione',
        'Fallito',
        'Ucciditi'
    ]
    
    if message.content == 'scimmia':
        response = random.choice(b8ne_quotes)
        await message.channel.send(response)

@bot.command(name='hi', help='Say hi')
async def hi(ctx):
    print(f'Test')
    
bot.run(TOKEN)
