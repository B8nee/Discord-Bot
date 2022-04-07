
import os
import random
import discord

from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f'{bot.user.name} si e\' connesso a Cazzate Time!')
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Non ho capito cosa vuoi che faccia.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Non hai i permessi per eseguire questo comando.')

@bot.command(name='ban', help='Banna un utente.')
@commands.has_any_role('TheFighaBoss')
async def ban(ctx, member: discord.Member=None, reason=None):
        if reason == None:
            await ctx.send(f'{ctx.author.mention} fornisci una ragione per il ban di {member.name}.')
        else:
            messageok = f"Sei stato bannato da {ctx.guild.name} per {reason}"
            await member.send(messageok)
            await member.ban(reason=reason)

@bot.command(name='kick', help='Espelli un utente.')
@commands.has_any_role('TheFighaBoss')
async def kick(ctx, member: discord.Member=None, reason=None):
        if reason == None:
            await ctx.send(f'{ctx.author.mention} fornisci una ragione per il kick di {member.name}.')
        else:
            messageok = f"Sei stato kickato da {ctx.guild.name} per {reason}"
            await member.send(messageok)
            await member.kick(reason=reason)
    
@bot.command(name='play', help='Riproduci un file audio: die | faccetta')
async def play(ctx, name):
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    if name == 'die':
        source = FFmpegPCMAudio('sounds/die.mp3')
        player = voice.play(source)
    if name == 'faccetta':
        source = FFmpegPCMAudio('sounds/faccetta.mp3')
        player = voice.play(source)   

@bot.command(name='stop', help='Stoppa la riproduzione.')
async def disconnect(ctx):
    await ctx.voice_client.disconnect()

bot.activity = discord.Activity(name='Demon Slayer', type=discord.ActivityType.watching)
bot.run(TOKEN)