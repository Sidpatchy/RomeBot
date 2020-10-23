@echo off

echo This simple script allows you to compile RomeBot by Sidpatchy
echo For a more detailed guide, please check the wiki: https://github.com/Sidpatchy/RomeBot/wiki/How-to-use-RomeBot.py-(version-2)

python -m pip install –upgrade pip    # Remove this line if you do not want PIP to be updated

pip install pyinstaller
pip install asyncio
pip install discord.py

cd bot

pyinstaller -F RomeBot.py

cd dist

copy RomeBot.exe ..

echo Done! You may now use RomeBot.

pause
