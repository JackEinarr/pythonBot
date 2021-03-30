import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):

    image1 = open('stick/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, image1)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,  one_time_keyboard=True)
    item1 = types.KeyboardButton(config.b1)
    item2 = types.KeyboardButton(config.b2)
    item3 = types.KeyboardButton(config.b3)
    item4 = types.KeyboardButton(config.b4)
    items = [item1, item2, item3, item4]
    markup.row(item1, item2)
    markup.row(item3, item4)

    bot.send_message(message.chat.id, config.starttext1.format(message.from_user, bot.get_me()),
        parse_mode='html')

    bot.send_message(message.chat.id, config.starttext2.format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == config.b1: ##AllPrice

            # keyboard
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton(config.b6)
            item2 = types.KeyboardButton(config.b9)
            item4 = types.KeyboardButton(config.b10)

            item3 = types.KeyboardButton(config.b5)
            markup.row(item1, item2)
            markup.row(item4)
            markup.row(item3)
            bot.send_message(message.chat.id, config.prisetext1.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

        elif message.text == config.b2: ##BrandNew
            # keyboard
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton(config.b8)
            item3 = types.KeyboardButton(config.b5)
            item2 = types.KeyboardButton(config.b11)
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(message.chat.id, config.localtext4.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, config.localtext6.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        elif message.text == config.b11:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item3 = types.KeyboardButton(config.b5)
            markup.row(item3)
            bot.send_message(message.chat.id, config.localtext4.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        elif message.text == config.b5:  ##Menu
            image3 = open('stick/sticker2.webp', 'rb')
            bot.send_sticker(message.chat.id, image3)
            # keyboard
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True,  one_time_keyboard=True)
            item1 = types.KeyboardButton(config.b1)
            item2 = types.KeyboardButton(config.b2)
            item3 = types.KeyboardButton(config.b3)
            item4 = types.KeyboardButton(config.b4)
            items = [item1, item2, item3, item4]
            markup.row(item1, item2)
            markup.row(item3, item4)

            bot.send_message(message.chat.id, config.localtext2.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        elif message.text == config.b8: ##Instructions
            # keyboard
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item3 = types.KeyboardButton(config.b5)
            markup.row(item3)
            bot.send_message(message.chat.id, config.teachtext1.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, config.teachtext2.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, config.teachtext3.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        elif message.text == config.b6: ##Bike
            image2 = open('stick/sticker1.webp', 'rb')
            bot.send_sticker(message.chat.id, image2)
            # keyboard
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton(config.b5)
            markup.row(item1)

            bot.send_message(message.chat.id, config.localtext1.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
            for k, v in config.priceBicke.items():
                bot.send_message(message.chat.id, k.format(message.from_user, bot.get_me()), parse_mode='html')
                for img in v:
                    image32 = open(img, 'rb')
                    bot.send_photo(message.chat.id, image32)
        elif message.text == config.b10: ##KickScooter

            image2 = open('stick/sticker1.webp', 'rb')
            bot.send_sticker(message.chat.id, image2)
            # keyboard
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton(config.b5)
            markup.row(item1)

            bot.send_message(message.chat.id, config.localtext1.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
            for k, v in config.priceScooter.items():
                bot.send_message(message.chat.id, k.format(message.from_user, bot.get_me()), parse_mode='html')
                bot.send_message(message.chat.id, v.format(message.from_user, bot.get_me()), parse_mode='html')
        elif message.text == config.b9: ##Telephone

            image2 = open('stick/sticker1.webp', 'rb')
            bot.send_sticker(message.chat.id, image2)
            # keyboard
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton(config.b5)
            markup.row(item1)

            bot.send_message(message.chat.id, config.localtext1.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
            for k, v in config.pricePhone.items():
                bot.send_message(message.chat.id, k.format(message.from_user, bot.get_me()), parse_mode='html')
                for img in v:
                    image32 = open(img, 'rb')
                    bot.send_photo(message.chat.id, image32)

        else:
            bot.send_message(message.chat.id, config.localtext3)
# RUN
bot.polling(none_stop=True)
