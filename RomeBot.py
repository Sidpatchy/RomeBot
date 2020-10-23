# RomeBot by Sidpatchy
# More info can be found on the GitHub here: https://github.com/Sidpatchy/RomeBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT       # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
from time import sleep      # Imports sleep because time.sleep() doesn't work
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
    await bot.change_presence(activity=discord.Game(name='RomeBot v2-RC1 | !help'))
    lout.log(config, botStartTime, None, lout.readConfig(config, 'botName'), True)

# Info Command
@bot.command(pass_context=True)
async def info(ctx):
    startTime = DT.datetime.now()       # Get the time the command was initiated at
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='Need Help?', value='You can get help by creating an issue on our [GitHub](https://github.com/Sidpatchy/RomeBot/issues) or by joining our [support server](https://discord.gg/NwQUkZQ)')
    embed.add_field(name='Add Me to a Server', value='Adding me to a server is simple, all you have to do is click [here](https://discord.bots.gg/bots/511050489928876052)')
    embed.add_field(name='GitHub', value='RomeBot is open source, that means you can view all of its code! Check out its [GitHub!](https://github.com/Sidpatchy/RomeBot)')
    await ctx.send(embed=embed)             # Send the embed created above in the channel the command was run in.
    lout.log(config, startTime, 'info')     # Write to log

# Joined command
@bot.command(pass_context=True)
async def joined(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name=user.display_name, value='Join date: {}'.format(user.joined_at))
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'joined')       # Use slout to write to the log and console

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
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='RomeBot v2-RC1', value='Released 2020-10-22')
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'version (v2-RC1)')

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

# isplaying: Removed due to changes in Discord TOS.

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
    runTime = startTime.replace(microsecond=0) - botStartTime.replace(microsecond=0)
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='Uptime:', value=runTime)
    await ctx.send(embed=embed)
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
async def birthday(ctx):
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
    lout.log(config, startTime, 'birthday')

# Adds a help command that sends a message to the user rather than spamming the chat with a long message
@bot.command(pass_context=True)
async def help(ctx):
    startTime = DT.datetime.now()
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.set_author(name='Help')
    embed.add_field(value='This is an early version of RomeBot v2. Please note that some features may not work as expected.', name='RomeBot v2-RC1', inline=False)                  # Will be removed with v2 release
#    embed.add_field(name='!test', value='Responds \'Working!\'', inline=False)                                                                                                     # Removed, use !servers or !uptime instead.
    embed.add_field(name='!info', value='Get help, an invite link, and a link to RomeBot GitHub', inline=False)                                                                     # Replaced with an embeded message which contains actual information of the bot and a way to invite it to the server
    embed.add_field(name='!joined @user', value='States when a user joined the server', inline=False)                                                                               # Replaced with an embed
    embed.add_field(name='!time', value='States what time it is on the server that the bot is hosted on', inline=False)                                                             # Very slight visual changes
    embed.add_field(name='!crucify @user', value='Crucifies a mentioned user', inline=False)                                                                                        # Made command send one message and switched to sending images from the server, rather than linking Imgur
    embed.add_field(name='!impale @user', value='Impales a mentioned user', inline=False)                                                                                           # Made command send one message and switched to sending images from the server, rather than linking Imgur
    embed.add_field(name='!stab @user', value='Stabs a mentioned user', inline=False)                                                                                               # Made command send one message and switched to sending images from the server, rather than linking Imgur
    embed.add_field(name='!assassinate @user', value='Has a user assassinated with the least offensive image possible', inline=False)                                               # Made command send one message and switched to sending images from the server, rather than linking Imgur
    embed.add_field(name='!carthago_delanda_est', value='Rants in (bad) Latin about how CARTHAGE MUST BE DESTROYED!!!', inline=False)                                               # Made command send one message and switched to sending images from the server, rather than linking Imgur. Also made it less cringy
#    embed.add_field(name='!flex', value='The bot flexes on how badly it is written and advertises it\'s GitHub', inline=False)                                                     # Removed. Replaced by the info command.
    embed.add_field(name='!uptime', value='RomeBot reports how long it has gone without crashing, previously, this number has been above 30 days!', inline=False)                   # Replaced with an embed
    embed.add_field(name='!enslave @user', value='Enslaves a mentioned user for the betterment of the Rome', inline=False)                                                          # Made command send one message and switched to sending images from the server, rather than linking Imgur. Also changed the message text.
    embed.add_field(name='!servers', value='RomeBot states how many servers it is a member of', inline=False)                                                                       # Replaced with an embed
    embed.add_field(name='!sack @user', value='Ponea cullei, punishment of the sack. Sacks a mentioned user.', inline=False)                                                        # Made command send one message and switched to sending images from the server, rather than linking Imgur.
    embed.add_field(name='!jupiterhates @user', value='Jupiter strikes down a mentioned user', inline=False)                                                                        # Made significantly less graphic to appeal to more Discord bot lists.
#    embed.add_field(name='!ides', value='Cries about the sad thing it was just reminded of', inline=False)                                                                         # Removed
#    embed.add_field(name='!brutussupporter @user', value='Calls out a Brutus supporter\'s BS and calls for their ass kicking', inline=False)                                       # Removed
    embed.add_field(name='!caesarnatalis', value='Lists how long it is until Julius Caesar\'s birthday. Uses July 7th at 12pm (CST).', inline=False)                                # I don't feel like checking this one right now, if I had to guess I didn't change anything
    embed.add_field(name='!version', value='Gives the version (and its release date) being run', inline=False)                                                                      # Replaced with an embed.
    await author.send(embed=embed)
    lout.log(config, startTime, 'help')

# Remind me to install windows and then update compiler.bat
bot.run(lout.fetchToken(config))       # User defined bot token, get one here: https://discordapp.com/developers/applications/, then place it inside config.yml