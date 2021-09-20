# VLC-Remote-Bot
A remote controller for VLC written in Python.

## Introduction
Whenever I wanted to binge watch a TV series with my friends, we were too lazy to play the next episode everytime it got over. So I ended up coding this Telegram bot in Python which automates the controls of VLC Media Player such as selecting which season and episode to watch. It has additional functionalities such as `\play`, `\pause`, `\next`, `\stop`. This bot made binging HIMYM seamlessly easy, Just pull out your phone and type few commands and there you have it, the script processses your request and plays the episode.

## Technologies
* [VLC](https://pypi.org/project/python-vlc/)
* [Telegram Bot API](https://pypi.org/project/pyTelegramBotAPI/)
* glob
* time
* os

## Setup
* Create a Telegram Bot using [BotFather](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* Copy and Paste the API Key inside `bot.py`
* Make sure you've downloaded the 64bit version of [VLC](https://get.videolan.org/vlc/3.0.16/win64/vlc-3.0.16-win64.exe)
* After installing VLC, locate `libvlc.dll` inside the directory where VLC was installed
* Add `libvlc.dll` to PATH Environment Variable. [help](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)
* Download and Install [Python](https://www.python.org/downloads/)
* Make neccessary changes in the `bot.py`
* To run the script `python bot.py`

## Screenshots 
* Using `\season` command 
![using \season command](https://user-images.githubusercontent.com/53237259/134043908-1e2ae8b0-f8aa-428e-8c07-a3d4f20f4bd5.jpg)
* Using `\episode` command
![using \episode command](https://user-images.githubusercontent.com/53237259/134043989-3a974ec6-e937-4105-b840-303b24338a18.jpg)
