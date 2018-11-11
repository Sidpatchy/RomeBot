#Rome Bot by Rainverm38

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime


#Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')

#Gets current time for functions which need it
currentDT = datetime.datetime.now()

#Notify in console when bot is loaded and sets bot currently playing status
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Salting Carthage'))
    print('--------------------------')
    print('Done Loading!')
    print(' ')
    print(currentDT)
    print('--------------------------')

#Test command
@bot.command(pass_context=True)
async def test(ctx):
    print(' ')
    await bot.say('Working!')
    print('--------------------------')
    print(currentDT)
    print('test has been run')
    print('--------------------------')

#Info command
@bot.command(pass_context=True)
async def info(ctx):
    print(' ')
    await bot.say('This is a bot that @Julius Caesar#4949 thought was a good idea to make. Why? because he was bored. This was written in Python 3.6 using Discord.py')
    print('--------------------------')
    print(currentDT)
    print('info has been run')
    print('--------------------------')

#Lists available commands
@bot.command(pass_context=True)
async def commands(ctx):
    print(' ')
    await bot.say('```Commands:```')
    await bot.say('```!test: Tests to see if the bot is working (if you are seeing this guess what? It is.)```')
    await bot.say('```!help: Lists commands and what they do (this)```')
    await bot.say('```!info: lists some info about the bot```')
    await bot.say('```!joined @user: Tells you what time the user mentioned joined the server```')
    await bot.say('```!time: Lists the current time on the server hosting the bot, just cuz')
    await bot.say('```!crucify: WIP, may not be finalized```')
    print('--------------------------')
    print(currentDT)
    print('commands has been run')
    print('--------------------------')

#Joined command
@bot.command(pass_context=True)
async def joined(ctx, user: discord.Member):
    print(' ')
    await bot.say('The User: {}'.format(user.name))
    await bot.say('Joined At: {}'.format(user.joined_at))
    print('--------------------------')
    print(currentDT)
    print('joined has been run')
    print('--------------------------')

#Crucify command (WIP)
@bot.command(pass_context=True)
async def crucify(ctx, user: discord.Member):
    print(' ')
    await bot.say('((This command is still a WIP) {} HAS BEEN CRUCIFIED!'.format(user.name))
    print('--------------------------')
    print(currentDT)
    print('crucified has been run')
    print('--------------------------')

#Prints server time
@bot.command(pass_context=True)
async def time(ctx):
    print(' ')
    await bot.say('Server time is:')
    await bot.say(currentDT)
    print('--------------------------')
    print(currentDT)
    print('time has been run')
    print('--------------------------')

bot.run('NTExMDUwNDg5OTI4ODc2MDUy.DslZig.Rcr2feclu9USjdT3GbWoChaCYgE')