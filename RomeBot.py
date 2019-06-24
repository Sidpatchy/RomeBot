# RomeBot by Rainverm38
# More info can be found on the GitHub here: https://github.com/Rainverm38/RomeBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                           # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
#import time                                    # Doesn't appear to be working here, must be imported before the command that requires it is run.


# Checks time that bot was started
startTime = DT.datetime.now()

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Notify in console when bot is loaded and sets bot currently playing status, basically any commands entered here are run when the bot is loaded and connected to Discord's servers
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Salting Carthage'))   # Sets the bot's presence status. In this case it is 'Salting Carthage'
    print('--------------------------')
    timeToLoad = DT.datetime.now() - startTime
    currentDT = DT.datetime.now()               # Gets current time
    print('Time to load:', timeToLoad)          # Prints the time to load
    print('Current Time:', currentDT)           # Prints current time in console
    print('Done Loading!')                      # Prints 'Done Loading!' in console
    print('--------------------------')

# Test command
@bot.command(pass_context=True)
async def test(ctx):                            # Defines the command 'test' so to run this command you type '!test'
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()               # Gets current time and assigns it to a variable
    print(' ')                                  # Skips a line in console to help make it more readable
    await ctx.send('Working!')                   # Types 'Working!' in discord channel where command was run
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')         # Divider to make console readable
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)           # Prints time command was run in the console, from the variable 'currentDT'
    print('test has been run')                  # Prints 'test has been run' in console
    print('--------------------------')         # Divider to make console readable

# Info command
@bot.command(pass_context=True)
async def info(ctx):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('This is a bot that Rainverm38 thought was a good idea to make. Why? because he was bored. This was written in Python 3.7 using Discord.py')
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('info has been run')
    print('--------------------------')

# Originally listed commands. Now, it just tells the user to type !help instead
@bot.command(pass_context=True)
async def commands(ctx):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    await ctx.send('That command is no longer used, please use \'!help\' instead')
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('commands has been run')
    print('--------------------------')

# Joined command
@bot.command(pass_context=True)
async def joined(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('The User: {}'.format(user.name))
    await ctx.send('Joined At: {}'.format(user.joined_at))
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('joined has been run')
    print('--------------------------')

# Crucify command
@bot.command(pass_context=True)
async def crucify(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('{} HAS BEEN CRUCIFIED!'.format(user.name))
    await ctx.send('https://i.imgur.com/iFEBFmX.jpg')
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run', timeToRun)
    print('Current Time:', currentDT)
    print('crucified has been run')
    print('--------------------------')

# Prints server time
@bot.command(pass_context=True)
async def time(ctx):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('Server time is:')
    await ctx.send(currentDT)
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run', timeToRun)
    print('Current Time:', currentDT)
    print('time has been run')
    print('--------------------------')

# Carthago Delanda Est!
@bot.command(pass_context=True)
async def carthago_delanda_est(ctx):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('CARTHAGO DELANDA EST!!!')
    await ctx.send('QUAE CARTHAGINE CAPTA ESSE!')
    await ctx.send('SALSURA CARTHAGO!')
    await ctx.send('ROMA INVICTA! ROMA INVICTA! ROMA INVICTA! ROMA INVICTA!')
    await ctx.send('This crappy translation is brought to you by Google Translate')
    await ctx.send('https://imgur.com/a/vSGcvtA')
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('carthago_delanda_est has been run')
    print('--------------------------')

# !hangme command
@bot.command(pass_context=True)
async def hangme(ctx):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('I got u fam:')
    await ctx.send('https://i.imgur.com/y4OuT7p.jpg')    # This is how I am showing images in the chat. There are more proper ways but this is easier and more reliable.
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('hangme has been run')
    print('--------------------------')

# isplaying command, no real purpose, just a learning thing
@bot.command(pass_context=True)
async def isplaying(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('Playing: {}'.format(user.activity))
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('isplaying has been run')
    print('--------------------------')

# Impale! Sends an image of mentioned @user being impaled
@bot.command(pass_context=True)
async def impale(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('{} Has Been Impaled!'.format(user.name))
    await ctx.send('https://i.imgur.com/rdSIwoq.jpg')
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run', timeToRun)
    print('Current Time:', currentDT)
    print('impale has been run')
    print('--------------------------')

# Stab! Sends an image of mentioned @user being impaled
@bot.command(pass_context=True)
async def stab(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    await ctx.send('{} HAS BEEN STABBED!'.format(user.name))
    await ctx.send('https://i.imgur.com/Hx1pCcZ.jpg')
    import time                                                                                                                     # Imports time, it doesn't work when imported when the bot is started
    time.sleep(3)                                                                                                                   # Waits 3 seconds
    await ctx.send('Oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooof (the 3 second delay was intentional btw)')
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('stab has been run')
    print('--------------------------')

# The bot flexes how badly written it's code is
@bot.command(pass_context=True)
async def flex(ctx):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('YOU ARE THE ONLY REAL PLEB! Your code is flawed my code however, is written in the most perfect and efficent way possible. If you somehow find that impossible to believe have a look at my GitHub. Then you\'ll truly see who is flawed, pleb. GIT REKT SCRUB!')
    await ctx.send('*hint click the link: https://github.com/Rainverm38/RomeBot*')
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('flex has been run')
    print('--------------------------')

# Assassinates a mentioned pleb
@bot.command(pass_context=True)
async def assassinate(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    print(' ')
    await ctx.send('WHOOP! WHOOP! {} HAS BEEN ASSASSINATED!!!'.format(user.name))
    await ctx.send('https://i.imgur.com/bgwNfdl.jpg this isn\'t insensitive, right?')
    import time
    time.sleep(2.5)
    await ctx.send('It took more effort than I want to admit to select an image that wont offend a (normal) person. After all, Hitler = bad. The delay in this message being sent was on purpose btw.')
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('assassinate has been run')
    print('--------------------------')
    
# Adds a help command that sends a message to the user rather than spamming the chat, WIP
@bot.command(pass_context=True)
async def help(ctx):
    startTime = DT.datetime.now()
    currentDT = DT.datetime.now()
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.set_author(name='Help')
    embed.add_field(name='!test', value='Responds \'Working!\'', inline=False)
    embed.add_field(name='!info', value='Gives some information about the bot', inline=False)
    embed.add_field(name='!joined @user', value='States when a user joined the server', inline=False)
    embed.add_field(name='!time', value='States what time it is on the server that the bot is hosted on', inline=False)
    embed.add_field(name='!crucify @user', value='Crucifies a mentioned user', inline=False)
    embed.add_field(name='!impale @user', value='Impales a mentioned user', inline=False)
    embed.add_field(name='!stab @user', value='Stabs a mentioned user', inline=False)
    embed.add_field(name='!assassinate @user', value='Has a user assassinated with the least offensive image possible (when talking about assassination)', inline=False)
    embed.add_field(name='!carthago_delanda_est', value='Rants in Latin about how CARTHAGO DELANDA EST!!!', inline=False)
    embed.add_field(name='!hangme', value='MLG I want to go home from (insert place name here)', inline=False)
    embed.add_field(name='!flex', value='The bot flexes on how badly it is written and advertises it\'s GitHub', inline=False)
    await author.send(embed=embed)
    timeToRun = DT.datetime.now() - startTime
    print('--------------------------')
    print('Time to Run:', timeToRun)
    print('Current Time:', currentDT)
    print('Help has been run')
    print('--------------------------')

bot.run('INSERT_TOKEN')       # User defined bot token, get one here: https://discordapp.com/developers/applications/