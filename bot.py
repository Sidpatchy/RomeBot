# Rome Bot by Rainverm38
# More info can be found on the GitHub here: https://github.com/Rainverm38/RomeBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime


# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')

# Gets time when bot is opened this has no use currently
currentDT = datetime.datetime.now()

# Notify in console when bot is loaded and sets bot currently playing status
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Salting Carthage'))   # Sets the bot's presence status. By default it is 'Salting Carthage'
    print('--------------------------')
    currentDT = datetime.datetime.now()     # Gets current time
    print(currentDT)    # Prints current time in console
    print('Done Loading!')      # Prints 'Done Loading!' in console
    print('--------------------------')

# Test command
@bot.command(pass_context=True)
async def test(ctx):
    currentDT = datetime.datetime.now()     # Gets current time
    print(' ')      # Skips a line in console
    await bot.say('Working!')      # Types 'Working!' in discord channel where command was run
    print('--------------------------')     # Divider to make console readable
    print(currentDT)       # Prints time command was initiated in console
    print('test has been run')     # Prints 'test has been run' in console
    print('--------------------------')     # Divider to make console readable

# Info command
@bot.command(pass_context=True)
async def info(ctx):
    currentDT = datetime.datetime.now()
    print(' ')
    await bot.say('This is a bot that Rainverm38 thought was a good idea to make. Why? because he was bored. This was written in Python 3.6 using Discord.py')
    print('--------------------------')
    print(currentDT)
    print('info has been run')
    print('--------------------------')

# Lists available commands
@bot.command(pass_context=True)
async def commands(ctx):
    currentDT = datetime.datetime.now()
    print(' ')
    await bot.say('```Commands:```')
    await bot.say('```!test: Tests to see if the bot is working (if you are seeing this guess what? It is.)```')
    await bot.say('```!help: Lists commands and what they do (this)```')
    await bot.say('```!info: lists some info about the bot```')
    await bot.say('```!joined @user: Tells you what time the user mentioned joined the server```')
    await bot.say('```!time: Lists the current time on the server hosting the bot, just cuz```')
    await bot.say('```!crucify @user: crucifies a mentioned user```')
    await bot.say('```!carthago_delanda_est: Rants in Latin about how CARTHAGO DELANDA EST!!!!!!```')

# Joined command
@bot.command(pass_context=True)
async def joined(ctx, user: discord.Member):
    currentDT = datetime.datetime.now()
    print(' ')
    await bot.say('The User: {}'.format(user.name))
    await bot.say('Joined At: {}'.format(user.joined_at))
    print('--------------------------')
    print(currentDT)
    print('joined has been run')
    print('--------------------------')

# Crucify command (WIP)
@bot.command(pass_context=True)
async def crucify(ctx, user: discord.Member):
    currentDT = datetime.datetime.now()
    print(' ')
    await bot.say('({} HAS BEEN CRUCIFIED!'.format(user.name))
    await bot.say('https://i.imgur.com/iFEBFmX.jpg')
    print('--------------------------')
    print(currentDT)
    print('crucified has been run')
    print('--------------------------')

# Prints server time
@bot.command(pass_context=True)
async def time(ctx):
    currentDT = datetime.datetime.now()
    print(' ')
    await bot.say('Server time is:')
    await bot.say(currentDT)
    print('--------------------------')
    print(currentDT)
    print('time has been run')
    print('--------------------------')

# Carthago Delanda Est!
@bot.command(pass_context=True)
async def carthago_delanda_est(ctx):
    currentDT = datetime.datetime.now()
    print(' ')
    await bot.say('CARTHAGO DELANDA EST!!!')
    await bot.say('QUAE CARTHAGINE CAPTA ESSE!')
    await bot.say('SALSURA CARTHAGO!')
    await bot.say('ROMA INVICTA! ROMA INVICTA! ROMA INVICTA! ROMA INVICTA!')
    print('--------------------------')
    print(currentDT)
    print('carthago_delanda_est has been run')
    print('--------------------------')

bot.run('BOT_TOKEN_HERE')       # User defined bot token, get one here: https://discordapp.com/developers/applications/