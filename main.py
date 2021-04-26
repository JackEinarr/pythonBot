#!/usr/bin/env python
# -*- coding: utf-8 -*-

from helpinfo import OutputInterceptor
from mssqlserver import cnxn, req
import telebot
import config
import schedule
import tkinter
import pydoc
import pyodbc
import pandas as pd

from telebot import types

bot = telebot.TeleBot(config.token)
bot = bot
@bot.message_handler(commands=['start'])
def welcome(message):
    # image1 = open('stick/sticker.webp', 'rb')
    # bot.send_sticker(message.chat.id, image1)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton(config.b0[0])
    item2 = types.KeyboardButton(config.b0[1])
    markup.row(item1, item2)

    bot.send_message(message.chat.id, config.starttext1.format(message.from_user, bot.get_me()),
                     parse_mode='html')

    bot.send_message(message.chat.id, config.starttext2.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    #schedule.every(30).seconds.do()


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == config.b0[0]:        ##Ответ 'Да'
            timer_send_message(message)
        elif message.text == config.b0[1]:  ##Ответ 'Нет'
            bot.send_message(message.chat.id, config.localtext1.format(message.from_user, bot.get_me()),
                             parse_mode='html')
        else:
            answer = '' #dasdsade
            with OutputInterceptor() as output:
                help(message.text)
            answer = '\n'.join(output)
            answer = answer.replace('|', '')

            if len(answer) >= 4096:
                for x in range(0, len(answer), 4096):
                    bot.send_message(message.chat.id, answer[x:x + 4096])
            else:
                bot.send_message(message.chat.id, answer)


def timer_send_message(message):
    with open('last_id_update', 'r') as f:  # Достаём код последних данных в базе
        last_id_update = int(f.read())
    df = pd.read_sql_query(req + f' WHERE SprStudents.TelegramId={message.chat.id} and Sessiya_id>{last_id_update}',
                           cnxn)  ##Получаем данные в df по SQL запросу req
    stud = ' '
    for columns in df.columns:
        stud += columns + ' '
    stud = ' '.join(stud.split())
    bot.send_message(1296226183, stud, parse_mode='html')
    stud = ' '
    for col in df.values:
        for val in col:
            stud += str(val) + ' '

        stud = ' '.join(stud.split())
        bot.send_message(message.chat.id, stud, parse_mode='html')
        stud = ' '
    df = pd.read_sql_query('SELECT max([Sessiya_id]) FROM [Dekanat2021].[dbo].[Sessiya]',
                           cnxn)  ##Получаем код псоледних данных в Sessiya
    last_id_update = df.values[0][0]
    # print(last_id_update)
    print(message.chat.id)
    with open('last_id_update', 'w') as f:  # Записываем в базу данных новый код обнавления
        f.write(str(last_id_update))

# @bot.message_handler(content_types=['text'])
# def send_mes(message):
#     timer_send_message(message)
#     print(1)
# RUN
bot.polling(none_stop=True)
