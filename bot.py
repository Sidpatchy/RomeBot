# RomeBot by Rainverm38
# More info can be found on the GitHub here: https://github.com/Rainverm38/RomeBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                       # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
#import time                                # Doesn't appear to be working here, must be imported before the command that requires it is run.


# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'

# Gets time when bot is opened this has no use currently
currentDT = DT.datetime.now()

# Notify in console when bot is loaded and sets bot currently playing status, basically any commands entered here are run when the bot is loaded and connected to Discord's servers
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Salting Carthage'))   # Sets the bot's presence status. In this case it is 'Salting Carthage'
    print('--------------------------')
    currentDT = DT.datetime.now()               # Gets current time
    print(currentDT)                            # Prints current time in console
    print('Done Loading!')                      # Prints 'Done Loading!' in console
    print('--------------------------')

# Test command
@bot.command(pass_context=True)
async def test(ctx):                            # Defines the command 'test' so to run this command you type '!test'
    currentDT = DT.datetime.now()               # Gets current time and assigns it to a variable
    print(' ')                                  # Skips a line in console to help make it more readable
    await bot.say('Working!')                   # Types 'Working!' in discord channel where command was run
    print('--------------------------')         # Divider to make console readable
    print(currentDT)                            # Prints time command was run in the console, from the variable 'currentDT'
    print('test has been run')                  # Prints 'test has been run' in console
    print('--------------------------')         # Divider to make console readable

# Info command
@bot.command(pass_context=True)
async def info(ctx):
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('This is a bot that Rainverm38 thought was a good idea to make. Why? because he was bored. This was written in Python 3.6 using Discord.py')
    print('--------------------------')
    print(currentDT)
    print('info has been run')
    print('--------------------------')

# Lists available commands
@bot.command(pass_context=True)
async def commands(ctx):
    currentDT = DT.datetime.now()
    print(' ')
    import time
    time.sleep(.5)      # Allows other bots to send their commands so that all listed commands can be displayed in one block.
    await bot.say('```Commands:```')                                                                                # Lines 57 through 68 are printed in a discord message, each seperately. 
    await bot.say('```!test: Tests to see if the bot is working (if you are seeing this guess what? It is.)```')    
    await bot.say('```!commands: Lists commands and what they do (this)```')
    await bot.say('```!info: lists some info about the bot```')
    await bot.say('```!joined @user: Tells you what time the user mentioned joined the server```')
    await bot.say('```!time: Lists the current time on the server hosting the bot, just cuz```')
    await bot.say('```!crucify @user: crucifies a mentioned user```')
    await bot.say('```!carthago_delanda_est: Rants in Latin about how CARTHAGO DELANDA EST!!!!!!```')
    await bot.say('```!hangme: Dank ass I WANT TO GO HOME FROM WORK meme```')
    await bot.say('```!impale @user: Impales a mentioned user```')
    await bot.say('```!stab @user: Stabs a mentioned user```')                                                       
    await bot.say('```!flex: The bot flexes on how badly it is written```')
    print('--------------------------')
    print(currentDT)
    print('commands has been run')
    print('--------------------------')

# Joined command
@bot.command(pass_context=True)
async def joined(ctx, user: discord.Member):
    currentDT = DT.datetime.now()
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
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('{} HAS BEEN CRUCIFIED!'.format(user.name))
    await bot.say('https://i.imgur.com/iFEBFmX.jpg')
    print('--------------------------')
    print(currentDT)
    print('crucified has been run')
    print('--------------------------')

# Prints server time
@bot.command(pass_context=True)
async def time(ctx):
    currentDT = DT.datetime.now()
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
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('CARTHAGO DELANDA EST!!!')
    await bot.say('QUAE CARTHAGINE CAPTA ESSE!')
    await bot.say('SALSURA CARTHAGO!')
    await bot.say('ROMA INVICTA! ROMA INVICTA! ROMA INVICTA! ROMA INVICTA!')
    print('--------------------------')
    print(currentDT)
    print('carthago_delanda_est has been run')
    print('--------------------------')

# !hangme command
@bot.command(pass_context=True)
async def hangme(ctx):
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('I got u fam:')
    await bot.say('https://i.imgur.com/y4OuT7p.jpg')    # This is how I am showing images in the chat. There are more proper ways but this is easier and more reliable.
    print('--------------------------')
    print(currentDT)
    print('hangme has been run')
    print('--------------------------')

# isplaying command, no real purpose, just a learning thing
@bot.command(pass_context=True)
async def isplaying(ctx, user: discord.Member):
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('Playing: {}'.format(user.game))
    print('--------------------------')
    print(currentDT)
    print('isplaying has been run')
    print('--------------------------')

# FORTNITE DELANDA EST!!!
# if .content.startswith(''):

# Impale! Sends an image of mentioned @user being impaled
@bot.command(pass_context=True)
async def impale(ctx, user: discord.Member):
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('{} Has Been Impaled!'.format(user.name))
    await bot.say('https://i.imgur.com/rdSIwoq.jpg')
    print('--------------------------')
    print(currentDT)
    print('impale has been run')
    print('--------------------------')

# Stab! Sends an image of mentioned @user being impaled
@bot.command(pass_context=True)
async def stab(ctx, user: discord.Member):
    currentDT = DT.datetime.now()
    await bot.say('{} HAS BEEN STABBED!'.format(user.name))
    await bot.say('https://i.imgur.com/Hx1pCcZ.jpg')
    import time                                                                                                                     # Imports time, it doesn't work when imported when the bot is started
    time.sleep(3)                                                                                                                   # Waits 3 seconds
    await bot.say('Oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooof (the 3 second delay was intentional btw)')
    print('--------------------------')
    print(currentDT)
    print('stab has been run')
    print('--------------------------')

# The bot flexes how badly written it's code is
@bot.command(pass_context=True)
async def flex(ctx):
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('YOU ARE THE ONLY REAL PLEB! Your code is flawed my code however, is written in the most perfect and efficent way possible. If you somehow find that impossible to believe have a look at my GitHub. Then you\'ll truly see who is flawed, pleb. GIT REKT SCRUB!')
    await bot.say('*hint click the link: https://github.com/Rainverm38/RomeBot*')
    print('--------------------------')
    print(currentDT)
    print('flex has been run')
    print('--------------------------')
    

bot.run('INSERT_BOT_TOKEN')       # User defined bot token, get one here: https://discordapp.com/developers/applications/
