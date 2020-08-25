# RomeBot by Sidpatchy
# More info can be found on the GitHub here: https://github.com/Sidpatchy/RomeBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                           # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
from time import sleep                          # Imports sleep because time.sleep() doesn't work
import os
import sLOUT as lout

# Checks time that bot was started
botStartTime = DT.datetime.now()

# Define a config file for use in the log commands. 
config = 'config.yml'

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Creates a log file if it doesn't already exist, and then writes to the file.
lout.writeFile('RomeBotLogs.txt', '\nRomeBot Initialized Successfully!', True)

# Things to run when the bot successfully connects to Discord
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='RomeBot v2-a3 | !help'))
    lout.log(config, botStartTime, None, lout.readConfig(config, 'botName'), True)

# Info Command
@bot.command(pass_context=True)
async def info(ctx):
    startTime = DT.datetime.now()                                                                                                                                                   # Get the time the command was initiated at
    await ctx.send('RomeBot by Sidpatchy. You can find my GitHub here: https://github.com/Sidpatchy/RomeBot')                                                                       # Send a message in the channel the command was run in
    lout.log(config, startTime, 'info')                                                                                                                                                     # Write to log

# Joined command
@bot.command(pass_context=True)
async def joined(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} joined at {}'.format(user.display_name, user.joined_at))             # Sends a message that looks like "Julius Caesar joined at July 7 100BC"
    lout.log(config, startTime, 'joined')                                                   # Use slout to write to the log and console

# Crucify command
@bot.command(pass_context=True)
async def crucify(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} HAS BEEN CRUCIFIED!'.format(user.display_name), file=discord.File('images/crucified.jpg'))
    lout.log(config, startTime, 'crucify')

# this will be changed
@bot.command(pass_context=True)
async def version(ctx):
    startTime = DT.datetime.now()
    await ctx.send('RomeBot Version v2-a2 | Released 2020-05-20')
    lout.log(config, startTime, 'version')

# !time, states the server time
@bot.command(pass_context=True)
async def time(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Server time is: {}'.format(DT.datetime.now()))
    lout.log(config, startTime, 'time')

# Carthago Delanda Est!
@bot.command(pass_context=True)
async def carthago_delanda_est(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Ceterum autem censeo Carthaginem esse delendam', file=discord.File('images/delanda.jpg'))    # Because old RomeBot was cringy
    lout.log(config, startTime, 'carthago_delanda_est')

# isplaying (might not be added back)

# Impale, impales a mentioned @user
@bot.command(pass_context=True)
async def impale(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} has been impaled!'.format(user.display_name), file=discord.File('images/impale.jpg'))
    lout.log(config, startTime, 'impale')

# Stab, stabs a mentioned @user
@bot.command(pass_context=True)
async def stab(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} HAS BEEN STABBED!!!! OOOOOOOOOOOOOOOOOOF'.format(user.display_name), file=discord.File('images/stab.jpg'))
    lout.log(config, startTime, 'stab')

# GitHub
@bot.command(pass_context=True)
async def github(ctx):
    startTime = DT.datetime.now()
    await ctx.send('My code is the most perfectly written, commented, and organized code to ever grace mankind. If you\'d like to have a look check my GitHub here: https://github.com/Sidpatchy/RomeBot')
    lout.log(config, startTime, 'github')

# Assassinates a mentioned pleb
@bot.command(pass_context=True)
async def assassinate(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('WHOOP! WHOOP! {} HAS BEEN ASSASSINATED!!!'.format(user.display_name), file=discord.File('images/assassinate.jpg'))
    lout.log(config, startTime, 'assassinate')

# Uptime, reports how long the bot has gone without a crash (or restart)
@bot.command(pass_context=True)
async def uptime(ctx):
    startTime = DT.datetime.now()
    runTime = DT.datetime.now() - botStartTime
    await ctx.send('I have been online for: {}'.format(runTime))
    lout.log(config, startTime, 'uptime')

# Enslave command
@bot.command(pass_context=True)
async def enslave(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('I THINK I SMELL CASH MONEY BABY!!! {} HAS BEEN ENSLAVED!'.format(user.display_name), file=discord.File('images/enslave.jpg'))
    lout.log(config, startTime, 'enslave')

# Servers, lists the number of servers the bot is in
@bot.command(pass_context=True)
async def servers(ctx):
    startTime = DT.datetime.now()
    numServers = len(bot.guilds)
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='Number of servers enlightened:', value=numServers, inline=False)
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'servers')

# sack, sacks a mentioned user
@bot.command(pass_context=True)
async def sack(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('OOOHHHH FUK! {} got the sack!'.format(user.display_name), file=discord.File('images/sacked.jpg'))
    lout.log(config, startTime, 'sack')

# jupiterhates, strikes down a user
@bot.command(pass_context=True)
async def jupiterhates(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} insulted Jupiter, they\'re now dead press \'F\''.format(user.display_name), file=discord.File('images/jupiter.jpg'))
    lout.log(config, startTime, 'jupiterhates')

# Caesar natalis 
@bot.command(pass_context=True)
async def caesarnatalis(ctx):
    startTime = DT.datetime.now()
    year = startTime.year
    birthday = startTime.replace(year=year, month=7, day=12, hour=12, minute=0, second=0, microsecond=0)
    if startTime >= birthday:
        year = year + 1
        birthday = startTime.replace(year=year, month=7, day=12, hour=12, minute=0, second=0, microsecond=0)
    
    # Create an embeded message
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='We only have to wait:', value=(birthday - startTime), inline=False)
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'caesarnatalis')

# Adds a help command that sends a message to the user rather than spamming the chat with a long message
@bot.command(pass_context=True)
async def help(ctx):
    startTime = DT.datetime.now()
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.set_author(name='Help')
    embed.add_field(value='This is an early version of RomeBot v2. Please note that some features may not work as expected.', name='RomeBot v2-a2', inline=False)                    # Will be removed in v2 release
#    embed.add_field(name='!test', value='Responds \'Working!\'', inline=False)                                                                                                      # Remove?
    embed.add_field(name='!info', value='Gives some information about the bot', inline=False)                                                                                       # No significant changes are planned
    embed.add_field(name='!joined @user', value='States when a user joined the server', inline=False)                                                                               # Visual changes
    embed.add_field(name='!time', value='States what time it is on the server that the bot is hosted on', inline=False)                                                             # Likely to be excluded unless I have a change of heart. It's not very useful.
    embed.add_field(name='!crucify @user', value='Crucifies a mentioned user', inline=False)                                                                                        # No significant changes are planned
    embed.add_field(name='!impale @user', value='Impales a mentioned user', inline=False)                                                                                           # No significant changes are planned
    embed.add_field(name='!stab @user', value='Stabs a mentioned user', inline=False)                                                                                               # No significant changes are planned
    embed.add_field(name='!assassinate @user', value='Has a user assassinated with the least offensive image possible', inline=False)                                               # No significant changes are planned
    embed.add_field(name='!carthago_delanda_est', value='Rants in (bad) Latin about how CARTHAGE MUST BE DESTROYED!!!', inline=False)                                               # Likely to use a better Latin translation (or none at all)                                                                                   # Will be removed
    embed.add_field(name='!flex', value='The bot flexes on how badly it is written and advertises it\'s GitHub', inline=False)                                                      # Likely to be changed
    embed.add_field(name='!uptime', value='RomeBot reports how long it has gone without crashing, previously, this number has been above 30 days!', inline=False)                   # No significant changes are planned (this was already significantly fixed in v1)
    embed.add_field(name='!enslave @user', value='Enslaves a mentioned user for the betterment of the Rome', inline=False)                                                          # Potential visual changes (new meme?)
    embed.add_field(name='!servers', value='RomeBot states how many servers it is a member of', inline=False)                                                                       # No significant changes are planned
    embed.add_field(name='!sack @user', value='Ponea cullei, punishment of the sack. Sacks a mentioned user.', inline=False)                                                 # Likely to be made less spammy
    embed.add_field(name='!jupiterhates @user', value='Jupiter strikes down a mentioned user', inline=False)                                                                        # Small changes are possible
#    embed.add_field(name='!ides', value='Cries about the sad thing it was just reminded of', inline=False)                                                                          # Likely to be reworded
#    embed.add_field(name='!brutussupporter @user', value='Calls out a Brutus supporter\'s BS and calls for their ass kicking', inline=False)                                        # Highly likely to be reworded
    embed.add_field(name='!caesarnatalis', value='Lists how long it is until Julius Caesar\'s birthday. Uses July 7th at 12pm (CST).', inline=False)                                # Date will likely be changed
    embed.add_field(name='!version', value='Gives the version (and its release date) being run', inline=False)                                                                      # Visual changes are possible
    await author.send(embed=embed)
    lout.log(config, startTime, 'help')

# Remind me to install windows and then update compiler.bat
bot.run(lout.fetchToken(config))       # User defined bot token, get one here: https://discordapp.com/developers/applications/, then place it inside token.txt