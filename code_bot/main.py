import telebot
from telebot import types
import os
import sqlite3 as sl
import data_control as dc


token=os.getenv('TOKEN1')
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    with open('images/image.jpg', 'rb') as img:
        link='https://google.com'
        bot.send_photo(message.chat.id, img, caption=f"Приветствую тебя, {message.from_user.first_name}, в моем боте.\nВот тебе ссылка на гугл:{link}")
    info = dc.get_records(connection)
    for i in info:
        if int(i[0])==int(message.chat.id):
            break
    else:
        dc.create_record(connection, message.chat.id, message.from_user.first_name, message.date)

if __name__=='__main__':
    connection = dc.create_connection("reports.db")
    dc.create_table(connection)

    bot.polling(none_stop=True)
