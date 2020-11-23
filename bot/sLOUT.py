# sLOUT by Sidpatchy v0.1
# This was originally intended to be used in a (currently) unreleased discord bot maker. However, I have slowly built more and more functions into it. Now it is integrated in many of my projects.
# If you experience any issues, please open an issue on the GitHub: https://github.com/Sidpatchy/sLOUT

import os
import datetime as DT
import platform
import glob
from time import sleep
import yaml

version = 'v0.1'

# writeFile() writes a string to the specified file
# Usage:
#   file: string, filename
#   string: string to be written to file.
#   time: Boolean, whether or not the time should be logged.
def writeFile(file, string, time=False):
    try:
        f = open(file, 'a')
        f.write(string)
        if time == True:
            f.write(' | {}'.format(str(DT.datetime.now())))
        f.write('\n')
        f.close()
    except:
        print('ERROR: Failed to write file. Make sure your user has permission to write to the file \'{}\'. If you have the correct permissions, please open an issue here: https://github.com/Sidpatchy/sLOUT'.format(file))
        writeFile('sLOUT-error.txt', 'ERROR: Failed to write file. Make sure your user has permission to write to the file \'{}\'. If you have the correct permissions, please open an issue here: https://github.com/Sidpatchy/sLOUT'.format(file), True)
        sleep(5)

# readFile() reads a file
# Usage:
#   file: string, filename
def readFile(file):
    try:
        f = open(file, 'r')
        contents = f.read()
        f.close()
        return contents
    except:
        print('ERROR: Failed to read file. Make sure your user has permission to read the file \'{}\'. If you have the correct permissions, please open an issue here: https://github.com/Sidpatchy/sLOUT'.format(file))
        writeFile('sLOUT-error.txt', 'ERROR: Failed to read file. Make sure your user has permission to read the file \'{}\'. If you have the correct permissions, please open an issue here: https://github.com/Sidpatchy/sLOUT'.format(file), True)
        sleep(5)

# fetchToken() reads the bot token from token.txt
# Usage:
#   configFile: string, name of configuration file
def fetchToken(configFile):
    return readConfig(configFile, 'token')

# clearScreen()
# Uses the appropriate clear command for your OS
def clearScreen():
    OS = platform.system()
    if OS.upper() == 'LINUX' or OS.upper() == 'DARWIN':
        try:
            os.system('clear')          # Runs the command 'clear'
        except:
            print('ERROR: Unable to clear screen')
            print('       Please include the information below in a GitHub issue, along with your actual OS. https://github.com/Sidpatchy/sLOUT')
            print('       Detected OS: {}'.format(OS))
            writeFile('sLOUT-error.txt', 'ERROR: Unable to clear screen \n       Please include the information below in a GitHub issue, along with your actual OS. https://github.com/Sidpatchy/sLOUT \n       Detected OS: {} \n       sLOUT version: {}'.format(OS, version), True)
            sleep(5)

    elif OS.upper() == 'WINDOWS':
        try:
            os.system('cls')            # Runs the command 'cls'
        except:
            print('ERROR: Unable to clear screen')
            print('       Please include the information below in a GitHub issue, along with your actual OS. https://github.com/Sidpatchy/sLOUT')
            print('       Detected OS: {}'.format(OS))
            print('       sLOUT version: {}'.format(version))
            writeFile('sLOUT-error.txt', 'ERROR: Unable to clear screen \n       Please include the information below in a GitHub issue, along with your actual OS. https://github.com/Sidpatchy/sLOUT \n       Detected OS: {} \n       sLOUT version: {}'.format(OS, version), True)
            sleep(5)
    else:
        print('ERROR: The OS I detected ({}) is not supported. Please open a GitHub issue here: https://github.com/Sidpatchy/sLOUT')
        writeFile('sLOUT-error.txt', 'ERROR: The OS I detected ({}) is not supported. Please open a GitHub issue here: https://github.com/Sidpatchy/sLOUT')
        sleep(5)

# writePy() essentially writeFile but targets a python fle in the directory bots/
# Usage:
#   file: string, filename
#   string: string to be written to file.
#   time: Boolean, whether or not the time should be logged.
def writePy(file, string, time=False):
    try:
        f = open('bots/{}.py'.format(file), 'a')
        f.write(string)
        if time == True:
            f.write(str(DT.datetime.now()))
        f.write('\n')
        f.close()
    except:
        print('ERROR: Failed to read file. Make sure your user has permission to write to the file \'bots/{}.py\'. If you have the correct permissions, please open an issue here: https://github.com/Sidpatchy/sLOUT'.format(file))
        writeFile('sLOUT-error.txt', 'ERROR: Failed to read file. Make sure your user has permission to write to the file \'bots/{}.py\'. If you have the correct permissions, please open an issue here: https://github.com/Sidpatchy/sLOUT'.format(file), True)
        sleep(5)

# log()
# Usage:
#   startTime: the time the command was initiated at, use a variable formed using datetime. import datetime and then use datetime.datetime.now()
#   processName: string, the name of the command/process that was run
#   botName: string, the name of the bot. Can be suplemented by placing the name you would like to use in a file named bot.txt
#   startup: boolean, when true, it will print done loading and the time. If you are using bot.txt insert lout.readFile('bot.txt') as the third parameter or just insert the bot name as a string.
def log(file, startTime=DT.datetime.now(), processName='Unknown', name=True, startup=False):
    if startup == True:

        # read the botname from the config
        botName = readConfig(file, 'botName')
        
        # Console Stuff
        print('--------------{}---------------'.format(botName))                # Divder in the console
        print('Time since startup: {}'.format(DT.datetime.now() - startTime))   # Prints how long it has been since the bot was started
        print('Current Time: {}'.format(DT.datetime.now()))                     # Prints the current time
        print('Done Loading!')                                                  # States that the bot is done loading
        print()                                                                 # SPACER!

        try:
            # Log stuff. This could all be achieved with one line but this looks better, it's slower but doesn't matter for now.
            writeFile('{}Logs.txt'.format(botName), '\n--------------{}---------------'.format(botName))
            writeFile('{}Logs.txt'.format(botName), 'Time since startup: {}'.format(DT.datetime.now() - startTime))
            writeFile('{}Logs.txt'.format(botName), 'Current Time: {}'.format(DT.datetime.now()))
            writeFile('{}Logs.txt'.format(botName), 'Done Loading!\n')
        except:
            print('ERROR: Unable to write to log file \'{}Logs.txt\'.'.format(botName))
            sleep(5)

    elif startup == False:
        # read the botname from the config
        botName = readConfig(file, 'botName')

        # Console Stuff
        print('--------------{}---------------'.format(botName))                # Divder in the console
        print('Current Time: {}'.format(DT.datetime.now()))                     # Prints the current time
        print('Time to run: {}'.format((DT.datetime.now() - startTime)))        # Subtracts the time passed in via startTime from the current time
        print('{} was run'.format(processName))                                 # States which process was run
        print()                                                                 # SPACER!

        try:
            # Log stuff. This could all be achieved with one line but this looks better, it's slower but doesn't matter for now.
            writeFile('{}Logs.txt'.format(botName), '\n--------------{}---------------'.format(botName))
            writeFile('{}Logs.txt'.format(botName), 'Current Time: {}'.format(DT.datetime.now()))
            writeFile('{}Logs.txt'.format(botName), 'Time to run: {}'.format((DT.datetime.now() - startTime)))
            writeFile('{}Logs.txt'.format(botName), '{} was run\n'.format(processName))
        except:
            print('ERROR: Unable to write to log file \'{}Logs.txt\'.'.format(botName))
            sleep(5)

# readConfig() configuration reader
# Usage:
#   file: string, file to read from
#   parameter: string, name of "varible" in config file, must be exact.
# Structure of config file:
# parameter = put stuff here
def readConfig(file, parameter):
    with open(file) as f:
        config = yaml.safe_load(f)
    return config[parameter]

# time() simple method to get time that requires less typing than datetime.datetime.now()
def time():
    return DT.datetime.now()