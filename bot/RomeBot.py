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

# Store the bot version and release date
ver = ['v2.1a', '2020-12-18']

# Define a config file for use in the log commands. 
config = 'config.yml'

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'info'
bot.remove_command('help')                  # Removes the default help command

# Creates a log file if it doesn't already exist, and then writes to the file.
lout.writeFile('RomeBotLogs.txt', '\nRomeBot Initialized Successfully!', True)

# Things to run when the bot successfully connects to Discord
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=1, name='The Salting of Carthage | !help', url='https://www.youtube.com/watch?v=ygI-2F8ApUM', platform='YouTube'))
    lout.log(config, botStartTime, None, None, True)

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
    embed.add_field(name='RomeBot {}'.format(ver[0]), value='Released {}'.format(ver[1]))
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'version ({})'.format(ver[0]))

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
    await ctx.send('Ceterum autem censeo Carthaginem esse delendam', file=discord.File('images/delanda.jpg'))
    lout.log(config, startTime, 'carthago_delanda_est')

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
    await ctx.send('I THINK I SMELL CASH MONEY BABY!!! {} HAS BEEN ENSLAVED!'.format((user.display_name).upper()), file=discord.File('images/enslave.jpg'))
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

# Polling function
@bot.command(pass_context=True)
async def poll(ctx):
    startTime = DT.datetime.now()

    # Create a list of the emoji to be used in the message and reactions
    emoji = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

    # Store the contents of the message in a variable and remove the command
    msg = ctx.message.content
    msg = msg.replace('!poll ', '')

    # Split the message into a list
    data = msg.split(",")

    query = data[0]
    data.pop(0)

    # Create the embed and add fields to the embed
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='{} asks:'.format(ctx.author.display_name), value='{}'.format(query), inline=False)

    if len(data) <= 1:
        embed.set_footer(text='React to this message with 👍 or 👎 to vote')
    else:
        for i in range(len(data)):
            embed.add_field(name=emoji[i], value=data[i], inline=True)
        embed.set_footer(text='React to this message with the corresponding emoji to vote')

    # Send the message and store its context in message
    message = await ctx.send(embed=embed)

    # Add reactions
    if len(data) <= 1:
        await message.add_reaction('<👍>')
        await message.add_reaction('<👎>')
    else:
        for i in range(len(data)):
            await message.add_reaction('<{}>'.format(emoji[i]))

    await ctx.message.add_reaction('<✅>')
    lout.log(config, startTime, 'poll')

# Adds a help command that sends a message to the user rather than spamming the chat with a long message
@bot.command(pass_context=True)
async def help(ctx):
    startTime = DT.datetime.now()
    author = ctx.message.author
    
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.set_author(name='Help')
    embed.add_field(name='!info', value='Get help, an invite link, and a link to RomeBot GitHub', inline=False)
    embed.add_field(name='!joined @user', value='States when a user joined the server', inline=False)
    embed.add_field(name='!time', value='States what time it is on the server that the bot is hosted on', inline=False)
    embed.add_field(name='!crucify @user', value='Crucifies a mentioned user', inline=False)
    embed.add_field(name='!impale @user', value='Impales a mentioned user', inline=False)
    embed.add_field(name='!stab @user', value='Stabs a mentioned user', inline=False)
    embed.add_field(name='!assassinate @user', value='Has a user assassinated with the least offensive image possible', inline=False)
    embed.add_field(name='!carthago_delanda_est', value='Rants in (bad) Latin about how CARTHAGE MUST BE DESTROYED!!!', inline=False)
    embed.add_field(name='!uptime', value='RomeBot reports how long it has gone without crashing, previously, this number has been above 30 days!', inline=False)
    embed.add_field(name='!enslave @user', value='Enslaves a mentioned user for the betterment of the Rome', inline=False)
    embed.add_field(name='!servers', value='RomeBot states how many servers it is a member of', inline=False)
    embed.add_field(name='!sack @user', value='Ponea cullei, punishment of the sack. Sacks a mentioned user.', inline=False)
    embed.add_field(name='!jupiterhates @user', value='Jupiter strikes down a mentioned user', inline=False)
    embed.add_field(name='!birthday', value='Lists how long it is until Julius Caesar\'s birthday. Uses July 7th at 12pm (CST).', inline=False)
    embed.add_field(name='!version', value='Gives the version (and its release date) being run', inline=False)
    embed.add_field(name='!poll <question>, <query>...', value='Creates a poll, for more info run "!help poll"')
    
    await author.send(embed=embed)
    lout.log(config, startTime, 'help')

# Remind me to install windows and then update compiler.bat
bot.run(lout.fetchToken(config))       # User defined bot token, get one here: https://discordapp.com/developers/applications/, then place it inside config.yml