import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import glob
import time
import telebot
from telebot import *

API_KEY = "1963414164:AAHaqMcoZzmgsam_xS-krhb79trm76j7XbE"

# globals
season_directory = ''
episode_number = ''
media = ''

bot = telebot.TeleBot(API_KEY, parse_mode=None)
def select_season(message):
    # season markup
    season_markup = types.ReplyKeyboardMarkup()
    season_markup.one_time_keyboard = True

    # seasons
    season_1 = types.KeyboardButton('Season 1')
    season_2 = types.KeyboardButton('Season 2')
    season_3 = types.KeyboardButton('Season 3')
    season_4 = types.KeyboardButton('Season 4')
    season_5 = types.KeyboardButton('Season 5')
    season_6 = types.KeyboardButton('Season 6')
    season_7 = types.KeyboardButton('Season 7')
    season_8 = types.KeyboardButton('Season 8')
    season_9 = types.KeyboardButton('Season 9')
    
    # season markup keyboard
    season_markup.row(season_1, season_2, season_3)
    season_markup.row(season_4, season_5, season_6)
    season_markup.row(season_7, season_8, season_9)
    
    # season variable
    season = bot.send_message(message.chat.id, 'Which Season to play from?', reply_markup=season_markup)
    return season

def select_episode(message):
    # episode markup
    episode_markup = types.ReplyKeyboardMarkup()
    episode_markup.one_time_keyboard = True
    
    # episodes
    episode_1 = types.KeyboardButton('Episode 1')
    episode_2 = types.KeyboardButton('Episode 2')
    episode_3 = types.KeyboardButton('Episode 3')
    episode_4 = types.KeyboardButton('Episode 4')
    episode_5 = types.KeyboardButton('Episode 5')
    episode_6 = types.KeyboardButton('Episode 6')
    episode_7= types.KeyboardButton('Episode 7')
    episode_8= types.KeyboardButton('Episode 8')
    episode_9 = types.KeyboardButton('Episode 9')
    episode_10 = types.KeyboardButton('Episode 10')
    episode_11= types.KeyboardButton('Episode 11')
    episode_12 = types.KeyboardButton('Episode 12')
    episode_13 = types.KeyboardButton('Episode 13')
    episode_14 = types.KeyboardButton('Episode 14')
    episode_15 = types.KeyboardButton('Episode 15')
    episode_16 = types.KeyboardButton('Episode 16')
    episode_17 = types.KeyboardButton('Episode 17')
    episode_18 = types.KeyboardButton('Episode 18')
    episode_19 = types.KeyboardButton('Episode 19')
    episode_20 = types.KeyboardButton('Episode 20')
    episode_21 = types.KeyboardButton('Episode 21')
    episode_22 = types.KeyboardButton('Episode 22')
    episode_23 = types.KeyboardButton('Episode 23')
    episode_24 = types.KeyboardButton('Episode 24')

    # season markup keyboard
    episode_markup.row(episode_1, episode_2, episode_3)
    episode_markup.row(episode_4, episode_5, episode_6)
    episode_markup.row(episode_7, episode_8, episode_9)
    episode_markup.row(episode_10, episode_11, episode_12)
    episode_markup.row(episode_13, episode_14, episode_15)
    episode_markup.row(episode_16, episode_17, episode_18)
    episode_markup.row(episode_19, episode_20, episode_21)
    episode_markup.row(episode_22, episode_23, episode_24)

    # episode variable
    episode = bot.send_message(message.chat.id, 'Which Episode?', reply_markup=episode_markup)
    return episode

def season_chosen(message):
    global season_directory
    # print(message.text)

    if message.text == 'Season 1':
        season_directory = r'I:\How I Met Your Mother Season 1\ '
    elif message.text == 'Season 2':
        season_directory = r'I:\How I Met Your Mother Season 2\ '
    elif message.text == 'Season 3':
        season_directory = r'I:\How I Met Your Mother Season 3\ '
    elif message.text == 'Season 4':
        season_directory = r'I:\How I Met Your Mother Season 4\ '
    elif message.text == 'Season 5':
        season_directory = r'I:\How I Met Your Mother Season 5\ '
    elif message.text == 'Season 6':
        season_directory = r'I:\How I Met Your Mother Season 6\ '
    elif message.text == 'Season 7':
        season_directory = r'I:\How I Met Your Mother Season 7\ '
    elif message.text == 'Season 8':
        season_directory = r'I:\How I Met Your Mother Season 8\ '
    elif message.text == 'Season 9':
        season_directory = r'I:\How I Met Your Mother Season 9\ '

def episode_chosen(message):
    global season_directory
    global episode_number
    global media

    episode_number = int(message.text[8:]) - 1 # message contains Episode 12 (the number can be anywhere between 1 to 24) we slice it to obtain just the number
    episode_list = glob.glob(season_directory.rstrip() + '*.mkv')
    if episode_list:
        file_to_play = episode_list[episode_number]
        print(file_to_play)
        media = vlc.MediaPlayer(file_to_play)
        media.play()
        media.toggle_fullscreen()
    else:
        bot.send_message(message.chat.id, 'Try again.')

    

@bot.message_handler(commands=['season']) # >>play 3 10 (aka "play season 3 episode 10")
def season(message):
    season = select_season(message)
    bot.register_next_step_handler(season, season_chosen)

@bot.message_handler(commands=['episode']) # >>play 3 10 (aka "play season 3 episode 10")
def episode(message):
    episode = select_episode(message)
    bot.register_next_step_handler(episode, episode_chosen)

@bot.message_handler(commands=['play'])
def play(message):
    global media

    media.play()
    media.toggle_fullscreen()
    bot.send_message(message.chat.id, 'Video is being played.')

@bot.message_handler(commands=['pause'])
def pause(message):
    global media

    media.pause()
    media.toggle_fullscreen()
    bot.send_message(message.chat.id, 'Video is paused.')

@bot.message_handler(commands=['stop'])
def stop(message):
    global media

    media.stop()
    bot.send_message(message.chat.id, 'Video is stopped.')

@bot.message_handler(commands=['next'])
def Next(message):
    global season_directory
    global episode_number
    global media

    media.stop() # stops the player
    time.sleep(1)
    episode_list = glob.glob(season_directory.rstrip() + '*.mkv')
    if episode_list:
        episode_number += 1
        file_to_play = episode_list[episode_number]
        print(file_to_play)
        media = vlc.MediaPlayer(file_to_play)
        media.play()
        media.toggle_fullscreen()
    else:
        bot.send_message(message.chat.id, 'Try again.')

@bot.message_handler(commands=['done'])
def done(message):
    exit() # exits the program


bot.polling()

#----------------------------------------------------------------------------------------------------------------#
# Different episodes have different file extensions (eg. .mp4, .mkv, .webmp) dont forget to change it in the code
# changes to be at lines
#----------------------------------------------------------------------------------------------------------------#