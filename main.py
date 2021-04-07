#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helpinfo import OutputInterceptor
import telebot
import config
import tkinter
import pydoc
import pygame

from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    # image1 = open('stick/sticker.webp', 'rb')
    # bot.send_sticker(message.chat.id, image1)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton(config.b0[0])
    item2 = types.KeyboardButton(config.b0[1])
    items = [item1, item2]
    markup.row(item1, item2)

    bot.send_message(message.chat.id, config.starttext1.format(message.from_user, bot.get_me()),
                     parse_mode='html')

    bot.send_message(message.chat.id, config.starttext2.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):

    if message.chat.type == 'private':
        if message.text == config.b0[0]:  ##Ответ 'Да'

            bot.send_message(message.chat.id, config.teachtext1.format(message.from_user, bot.get_me()),
                             parse_mode='html')

            # # keyboard
            # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            # item1 = types.KeyboardButton(config.b6)
            # item2 = types.KeyboardButton(config.b9)
            # item4 = types.KeyboardButton(config.b10)
            #
            # item3 = types.KeyboardButton(config.b5)
            # markup.row(item1, item2)
            # markup.row(item4)
            # markup.row(item3)
            # bot.send_message(message.chat.id, config.prisetext1.format(message.from_user, bot.get_me()),
            #                  parse_mode='html', reply_markup=markup)
        elif message.text == config.b0[1]:  ##Ответ 'Нет'
            bot.send_message(message.chat.id, config.localtext1.format(message.from_user, bot.get_me()),
                             parse_mode='html')
        else:
            answer = ''
            with OutputInterceptor() as output:
                help(message.text)
            answer = '\n'.join(output)
            answer = answer.replace('|', '')

            if len(answer) >= 4096:
                for x in range(0, len(answer), 4096):
                    bot.send_message(message.chat.id, answer[x:x+4096])
            else:
                bot.send_message(message.chat.id, answer)

# def helpinfo():
#     @bot.callback_query_handler(func=lambda call: True)
#     def query_handler(call):
#         answer = ''
#         print(call)
#         if call.data == call.message.text:
#             with OutputInterceptor() as output:
#                 help(call.message.text)
#             answer = '\n'.join(output)
#             print(answer)
#
#         if len(answer[:500]) > 4096:
#             for x in range(0, len(answer), 4096):
#                 bot.send_message(call.message.chat.id, answer[x:x + 4096])
#         else:
#             bot.send_message(call.message.chat.id, answer[:500].format(call.message.from_user), bot.get_me())

# def outhelp():

# RUN
bot.polling(none_stop=True)
