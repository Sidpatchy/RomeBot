# RomeBot by Sidpatchy
# More info can be found on the GitHub here: https://github.com/Sidpatchy/RomeBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                           # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
from time import sleep                          # Imports sleep because time.sleep() doesn't work
import os

# Checks time that bot was started
botStartTime = DT.datetime.now()

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Creates a log file if it doesn't exist and then writes to the log file, whether or not it just created it, what time the bot was started.
f = open('RomeBotLogs.txt', 'a')
f.write('\nRomeBot ready! | ')
f.write(str(DT.datetime.now()))
f.write('\n')
f.close()

# this will be changed
async def version(ctx):
    startTime = DT.datetime.now()
    await ctx.send('RomeBot Version v2-a1 | Released 2020-05-18')
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
    embed.add_field(name='MOST COMMANDS ARE NOT IN THIS VERSION. The only available commands are shown.')                                                                            # Will be removed in v2 release
#    embed.add_field(name='!test', value='Responds \'Working!\'', inline=False)                                                                                                      # Remove?
#    embed.add_field(name='!info', value='Gives some information about the bot', inline=False)                                                                                       # No significant changes are planned
#    embed.add_field(name='!joined @user', value='States when a user joined the server', inline=False)                                                                               # Visual changes
#    embed.add_field(name='!time', value='States what time it is on the server that the bot is hosted on', inline=False)                                                             # Remove?
#    embed.add_field(name='!crucify @user', value='Crucifies a mentioned user', inline=False)                                                                                        # No significant changes are planned
#    embed.add_field(name='!impale @user', value='Impales a mentioned user', inline=False)                                                                                           # No significant changes are planned
#    embed.add_field(name='!stab @user', value='Stabs a mentioned user', inline=False)                                                                                               # No significant changes are planned
#    embed.add_field(name='!assassinate @user', value='Has a user assassinated with the least offensive image possible', inline=False)                                               # No significant changes are planned
#    embed.add_field(name='!carthago_delanda_est', value='Rants in (bad) Latin about how CARTHAGE MUST BE DESTROYED!!!', inline=False)                                               # Likely to use a better Latin translation (or none at all)
#    embed.add_field(name='!hangme', value='Helps out people who dislike Rome', inline=False)                                                                                        # Likely to be removed
#    embed.add_field(name='!flex', value='The bot flexes on how badly it is written and advertises it\'s GitHub', inline=False)                                                      # Likely to be changed
#    embed.add_field(name='!uptime', value='RomeBot reports how long it has gone without crashing, previously, this number has been above 30 days!', inline=False)                   # No significant changes are planned (this was already significantly fixed in v1)
#    embed.add_field(name='!lastupdate', value='RomeBot reports how long he has gone without adding glory', inline=False)                                                            # Visual changes
#    embed.add_field(name='!enslave @user', value='Enslaves a mentioned user for the betterment of the Rome', inline=False)                                                          # Potential visual changes (new meme?)
#    embed.add_field(name='!servers', value='RomeBot states how many servers it is a member of', inline=False)                                                                       # No significant changes are planned
#    embed.add_field(name='!poneacullei @user', value='Ponea cullei, punishment of the sack. Sacks a mentioned user.', inline=False)                                                 # Likely to be made less spammy
#    embed.add_field(name='!jupiterhates @user', value='Jupiter strikes down a mentioned user', inline=False)                                                                        # Small changes are possible
#    embed.add_field(name='!ides', value='Cries about the sad thing it was just reminded of', inline=False)                                                                          # Likely to be reworded
#    embed.add_field(name='!brutussupporter @user', value='Calls out a Brutus supporter\'s BS and calls for their ass kicking', inline=False)                                        # Highly likely to be reworded
#    embed.add_field(name='!caesarnatalis', value='Lists how long it is until Julius Caesar\'s birthday. Uses July 7th at 12pm (CST).', inline=False)                                # Date will likely be changed
    embed.add_field(name='!version', value='Gives the version (and its release date) being run', inline=False)                                                                      # Visual changes are possible
    await author.send(embed=embed)
    consoleOutput('help', startTime)

# UNCOMMENT THE NEXT LINE IF YOU AREN'T COMPILING USING THE BATCH FILE (chances are, you aren't)
#bot.run('INSERT_TOKEN')       # User defined bot token, get one here: https://discordapp.com/developers/applications/
