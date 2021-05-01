import telebot
import mysql.connector
from telebot import types
from datetime import datetime
import uuid
import openpyxl
import sys

bot = telebot.TeleBot('1133046539:AAGD-vuFM-29tJ9ovDGvtj7_dLLAUqSmXo8')
second = datetime.today().time().second
test = '1000002'
pepperoni = 'https://imbt.ga/2y2Q0RkacL'


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    contact = types.InlineKeyboardMarkup(row_width=3)
    contact_button = types.InlineKeyboardButton(text='Отправить контакты', callback_data='yolo')
    button = types.InlineKeyboardButton('odood', callback_data='sasa')
    contact.add(button)
    contact.row(contact_button)
    test = types.InlineKeyboardButton(text='test button', callback_data='123123')
    contact.row(test)
    bot.send_message(text='<a href="' + pepperoni + '"> </a><b>Чтобы продолжить вы должны отправить нам ваши контактные данные для дальнейших услуг</b>',
                     chat_id=message.chat.id, parse_mode='HTML', reply_markup=contact)


@bot.message_handler(content_types=['text', 'photo'])
def testthingy(message):
    if message.text:
        print('wew')


@bot.callback_query_handler(func=lambda call: True)
def sthnewidk(c):
    if c.data.isdigit():
        if int(c.data) == 123123:
            print('wowie this really works fuck yeah')
            bot.edit_message_text('okie dokie', c.message.chat.id, c.message.message_id)
        bot.send_message(c.message.chat.id, 'ya ok')
    if c.data == 'okok':
        idk = 5
        print(idk)


@bot.message_handler(content_types='text')
def contact_send(message):
    bot.reply_to(message, 'ok')

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)