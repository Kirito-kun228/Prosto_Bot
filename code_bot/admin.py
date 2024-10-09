import telebot
from telebot import types
import os
import sqlite3 as sl
from datetime import datetime
import data_control as dc

token=os.getenv('TOKEN2')
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/all_invited")
    btn2 = types.KeyboardButton("/new_this_day")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Какую статистику вы хотите получить?', reply_markup=markup)


@bot.message_handler(commands=['all_invited'])
def all_invited(message):
    bot.send_message(message.chat.id, text='Пользователей бота за все время')
    info = dc.get_records(connection)
    k=0
    for i in info:
        k+=1
        timeing=datetime.fromtimestamp(i[2])
        bot.send_message(message.chat.id, f"{k}. ID: {i[0]}, Имя: {i[1]}, Время: {timeing}")

@bot.message_handler(commands=['new_this_day'])
def new_this_day(message):
    bot.send_message(message.chat.id, text='Пользователей бота за 24 часа')
    info = dc.get_records(connection)
    k = 0
    for i in info:
        if int(i[2])>=int(datetime.now().timestamp())-86400:
            print('1')
            k += 1
            timeing = datetime.fromtimestamp(i[2])
            bot.send_message(message.chat.id, f"{k}. ID: {i[0]}, Имя: {i[1]}, Время: {timeing}")


connection = dc.create_connection("../reports.db")
dc.create_table(connection)

bot.polling(none_stop=True)