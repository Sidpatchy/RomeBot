@echo off

echo This simple script allows you to compile RomeBot by Rainverm38

pip install pyinstaller

set /P token=Insert Your Bot Token: 

echo bot.run('%token%')       # User defined bot token, get one here: https://discordapp.com/developers/applications/ >> RomeBot.py

pyinstaller -F RomeBot.py

cd dist

copy RomeBot.exe ..

echo Done! You may now use RomeBot.

pause