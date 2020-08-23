import telebot
import mysql.connector
from telebot import types
from datetime import datetime
import uuid
import openpyxl
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='undertalefanatic_45',
    port='3306',
    database='mydatabase'
)
cursor = db.cursor()
directory = 'c:/users/user/desktop/'

bot = telebot.TeleBot('1133046539:AAGD-vuFM-29tJ9ovDGvtj7_dLLAUqSmXo8')
test = '1000002'
pepperoni = 'https://imbt.ga/2y2Q0RkacL'
cursor.execute('SELECT phone_number FROM users WHERE user_id = 724952483')





@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    contact = types.InlineKeyboardMarkup(row_width=3)
    contact_button = types.InlineKeyboardButton(text='Отправить контакты', callback_data='yolo')
    button = types.InlineKeyboardButton('odood', callback_data='sasa')
    contact.add(button)
    contact.row(contact_button)

    test = types.InlineKeyboardButton(text='test button', callback_data='yolo too?')
    contact.row(test)
    bot.send_message(text='Чтобы продолжить вы должны отправить нам ваши контактные данные для дальнейших услуг',
                          chat_id=message.chat.id, reply_markup=contact)


@bot.message_handler(content_types=['text', 'photo'])
def testthingy(message):
    if message.text.startswith('a'):
        bot.send_message(message.chat.id, message.text)
        print(message.text)
@bot.callback_query_handler(func=lambda call: True)
def sthnewidk(call):
    if call.data.isdigit():
        if int(call.data) == 123123:
            print('wowie this really works fuck yeah')
            bot.edit_message_text('okie dokie', call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'ya ok')
    if call.data == 'okok':
        idk = 5
        print(idk)


@bot.message_handler(content_types='text')
def contact_send(message):
    bot.reply_to(message, 'ok')


bot.polling(none_stop=True)
