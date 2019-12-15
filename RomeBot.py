# RomeBot by Sidpatchy
# More info can be found on the GitHub here: https://github.com/Sidpatchy/RomeBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                           # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
from time import sleep                          # Imports sleep because time.sleep() doesn't work


# Checks time that bot was started
botStartTime = DT.datetime.now()

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Handles what needs to be printed in the console
def consoleOutput(commandName, commandTime):    # Defines consoleOutput()
    startTime = commandTime                     # (laziness) passing startTime from the beginning of the command into the function
    timeToRun = DT.datetime.now() - startTime
    print('')
    print('---------RomeBot----------')         # Divider to make console readable
    print('Time to Run:', timeToRun)            # Prints how long it took the bot to run the command
    print('Current Time:', DT.datetime.now())   # Prints time command was run in the console, from the variable 'currentDT'
    print(commandName, 'has been run')          # Prints 'test has been run' in console
    print('--------------------------')         # Divider to make console readable

# Notify in console when bot is loaded and sets bot currently playing status, basically any commands entered here are run when the bot is loaded and connected to Discord's servers
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Salting Carthage | !help'))   # Sets the bot's presence status. In this case it is 'Salting Carthage'
    print('---------RomeBot----------')
    timeToLoad = DT.datetime.now() - botStartTime
    print('Time to load:', timeToLoad)              # Prints the time to load
    print('Current Time:', DT.datetime.now())       # Prints current time in console
    print('Done Loading!')                          # Prints 'Done Loading!' in console
    print('--------------------------')

# Test command
@bot.command(pass_context=True)
async def test(ctx):                             # Defines the command 'test' so to run this command you type '!test'
    startTime = DT.datetime.now()                # Stores the time the command was initiated at
    await ctx.send('Working!')                   # Types 'Working!' in discord channel where command was run
    consoleOutput('test', startTime)
    
# Info command
@bot.command(pass_context=True)
async def info(ctx):
    startTime = DT.datetime.now()
    await ctx.send('This is a bot that Rainverm38 thought was a good idea to make. Why? because he was bored. This was written in Python 3.7 using Discord.py')
    consoleOutput('info', startTime)

# Originally listed commands, now, it just tells the user to type '!help' instead
@bot.command(pass_context=True)
async def commands(ctx):
    startTime = DT.datetime.now()
    await ctx.send('That command is no longer used, please use \'!help\' instead')
    consoleOutput('commands', startTime)

# Joined command
@bot.command(pass_context=True)
async def joined(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('The User: {}'.format(user.name))
    await ctx.send('Joined At: {}'.format(user.joined_at))
    consoleOutput('joined', startTime)

# Crucify command
@bot.command(pass_context=True)
async def crucify(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} HAS BEEN CRUCIFIED!'.format(user.name))
    await ctx.send('https://i.imgur.com/iFEBFmX.jpg')
    consoleOutput('crucify', startTime)

# Prints server time
@bot.command(pass_context=True)
async def time(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Server time is:')
    await ctx.send(DT.datetime.now())
    consoleOutput('time', startTime)

# Carthago Delanda Est!
@bot.command(pass_context=True)
async def carthago_delanda_est(ctx):
    startTime = DT.datetime.now()
    await ctx.send('CARTHAGO DELANDA EST!!!')
    await ctx.send('QUAE CARTHAGINE CAPTA ESSE!')
    await ctx.send('SALSURA CARTHAGO!')
    await ctx.send('ROMA INVICTA! ROMA INVICTA! ROMA INVICTA! ROMA INVICTA!')
    await ctx.send('This crappy translation is brought to you by Google Translate')
    await ctx.send('https://imgur.com/a/vSGcvtA')
    consoleOutput('carthago_delanda_est', startTime)

# !hangme command
@bot.command(pass_context=True)
async def hangme(ctx):
    startTime = DT.datetime.now()
    await ctx.send('I got u fam:')
    await ctx.send('https://i.imgur.com/y4OuT7p.jpg')    # This is how I am showing images in the chat. There are other ways but this is easier and more reliable.
    consoleOutput('hangme', startTime)

# isplaying command, no real purpose, just a learning thing
@bot.command(pass_context=True)
async def isplaying(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('Playing: {}'.format(user.activity))
    consoleOutput('isplaying', startTime)

# Impale! Sends an image of mentioned @user being impaled
@bot.command(pass_context=True)
async def impale(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} Has Been Impaled!'.format(user.name))
    await ctx.send('https://i.imgur.com/rdSIwoq.jpg')
    consoleOutput('impale', startTime)

# Stab! Sends an image of mentioned @user being stabbed
@bot.command(pass_context=True)
async def stab(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} HAS BEEN STABBED!'.format(user.name))
    await ctx.send('https://i.imgur.com/Hx1pCcZ.jpg')
    sleep(3)                                                                                                                   # Waits 3 seconds
    await ctx.send('Oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooof (the 3 second delay was intentional btw)')
    consoleOutput('stab', startTime)

# The bot flexes how badly written its code is
@bot.command(pass_context=True)
async def flex(ctx):
    startTime = DT.datetime.now()
    await ctx.send('YOU\'RE A PLEB! Your code is flawed my code however, is written in the most perfect and efficent way possible. If you somehow find that impossible to believe have a look at my GitHub. Then you\'ll truly see who is flawed, pleb. GIT REKT SCRUB!')
    await ctx.send('*hint click the link: https://github.com/Sidpatchy/RomeBot*')
    consoleOutput('flex', startTime)

# Assassinates a mentioned pleb
@bot.command(pass_context=True)
async def assassinate(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('WHOOP! WHOOP! {} HAS BEEN ASSASSINATED!!!'.format(user.name))
    await ctx.send('https://i.imgur.com/bgwNfdl.jpg this isn\'t insensitive, right?')
    sleep(2.5)
    await ctx.send('It took more effort than I want to admit to select an image that wont offend a (normal) person. After all, Hitler = bad. The delay in this message being sent was on purpose btw.')
    consoleOutput('assassinate', startTime)

# Uptime command
@bot.command(pass_context=True)
async def uptime(ctx):
    startTime = DT.datetime.now()
    runTime = DT.datetime.now() - botStartTime
    await ctx.send('I have been online for:')
    await ctx.send(runTime)
    consoleOutput('uptime', startTime)

# Enslave Command
@bot.command(pass_context=True)
async def enslave(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('OHHHH SHIT LOOK AT THE ECONOMY TICK, {} HAS BEEN ENSLAVED!'.format(user.name))
    await ctx.send('CHUGA CHUGA CHOO CHOO')
    await ctx.send('https://i.imgur.com/XsCNL8o.jpg, this was stolen from r/RoughRomanMemes')
    consoleOutput('enslave', startTime)

# lastupdate command
@bot.command(pass_context=True)
async def lastupdate(ctx):
    startTime = DT.datetime.now()
    date = DT.datetime.now()
    updateTime = date.replace(year=2019, month=12, day=15, hour=12, minute=29, second=13, microsecond=585921)
    timeSinceUpdate = DT.datetime.now() - updateTime
    await ctx.send('It has been')
    await ctx.send(timeSinceUpdate) 
    await ctx.send('since I was last updated')
    consoleOutput('lastupdate', startTime)

# server command. Lists the number of servers RomeBot is in
@bot.command(pass_context=True)
async def servers(ctx):
    startTime = DT.datetime.now()
    numberOfServers = len(bot.guilds)
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='Number of Servers:', value=numberOfServers, inline=False)
    await ctx.send(embed=embed)
    consoleOutput('servers', startTime)

# Poena cullei (penalty of the sack) command, seriously, read about it: https://en.wikipedia.org/wiki/Poena_cullei
# I almost don't want to joke about it and you've seen some of the other crap that I've put in here
@bot.command(pass_context=True)
async def poneacullei(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('FUUUUUUUUCK {} GOT SACKED!'.format(user.name))
    await ctx.send('Like literally, he got sacked, I highly recommend you read this page on it: https://en.wikipedia.org/wiki/Poena_cullei')
    await ctx.send('They blindfolded them, said you were unworthy of light, took them to a field and beat them until they couldn\'t take it anymore, then threw them into a sack along with a serpent, an ape, a dog, and a rooster, then they sewed it up, THEN, they threw you into the sea.')
    await ctx.send('https://i.imgur.com/yReOk5o.jpg')
    consoleOutput('poneacullei', startTime)

# Jupiterhates left command
@bot.command(pass_context=True)
async def jupiterhates(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('{} pissed off Jupiter, they\'re now dead press \'F\''.format(user.name))
    await ctx.send('https://i.imgur.com/u6h7E8y.jpg')
    consoleOutput('jupiterhates', startTime)

# Idus Martiae
@bot.command(pass_context=True)
async def ides(ctx):
    startTime = DT.datetime.now()
    await ctx.send('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF RIP RIP R I P RIP A RONI SAD ROMEBOT HOURS')
    await ctx.send('GOD DIED ON THE IDES (of March) WE DON\'T JOKE ABOUT THAT!')
    consoleOutput('ides', startTime)

# Brutus supporter
@bot.command(pass_context=True)
async def brutussupporter(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    await ctx.send('Guess what! That\'s right! {} is a dick, ass kickings can be sent directly to their house'.format(user.name))
    await ctx.send('https://i.imgur.com/WIa1uIC.jpg')
    consoleOutput('brutussupporter', startTime)

# Caesar natalis command
@bot.command(pass_context=True)
async def caesarnatalis(ctx):
    startTime = DT.datetime.now()
    year = startTime.year
    time = startTime.replace(year=year, month=7, day=7, hour=12, minute=0, second=0, microsecond=0)
    if DT.datetime.now() >= time:
        year = year + 1
    godBirthday = startTime.replace(year=year, month=7, day=7, hour=12, minute=0, second=0, microsecond=0)
    timeTo = godBirthday - DT.datetime.now()
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='We only have to wait:', value=timeTo, inline=False)
    await ctx.send(embed=embed)
    consoleOutput('caesarnatalis', startTime)

# Version command
@bot.command(pass_context=True)
async def version(ctx):
    startTime = DT.datetime.now()
    await ctx.send('RomeBot Version 1.0.2 | Released 12/15/2019')
    consoleOutput('version', startTime)

# Adds a help command that sends a message to the user rather than spamming the chat with a long message
@bot.command(pass_context=True)
async def help(ctx):
    startTime = DT.datetime.now()
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
    embed.add_field(name='!uptime', value='RomeBot reports how long it has gone without crashing, previously, this number has been above 2 days!', inline=False)
    embed.add_field(name='!lastupdate', value='RomeBot reports how long he has gone without adding glory', inline=False)
    embed.add_field(name='!enslave @user', value='Enslaves a mentioned user for the betterment of the Rome', inline=False)
    embed.add_field(name='!servers', value='RomeBot states how many servers it is a member of', inline=False)
    embed.add_field(name='!poneacullei @user', value='Ponea cullei, punishment of the sack. Sacks a mentioned user.', inline=False)
    embed.add_field(name='!jupiterhates @user', value='Jupiter strikes down a mentioned user', inline=False)
    embed.add_field(name='!ides', value='Cries about the sad thing it was just reminded of', inline=False)
    embed.add_field(name='!brutussupporter @user', value='Calls out a Brutus supporter\'s BS and calls for their ass kicking', inline=False)
    embed.add_field(name='!caesarnatalis', value='Lists how long it is until Julius Caesar\'s birthday. Since we don\'t know which day it was I calculate from July 7 at 12pm to get the midpoint between the 2 days.', inline=False)
    embed.add_field(name='!version', value='Gives the version number and release date being run', inline=False)
    await author.send(embed=embed)
    consoleOutput('help', startTime)

# UNCOMMENT THE NEXT LINE IF YOU AREN'T COMPILING USING THE BATCH FILE
#bot.run('INSERT_TOKEN')       # User defined bot token, get one here: https://discordapp.com/developers/applications/