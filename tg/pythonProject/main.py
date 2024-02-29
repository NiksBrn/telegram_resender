import telebot
from telebot import types

bot = telebot.TeleBot('6658329963:AAHYdHCjPsLcdH9VIFtHEwEazjUyUBIZvoM')

infor = 'Created by legion_team special unit [Legion_G_A_V_]\nsquad list:\n alcoprogers: Niko,t33nsy\n alco testers: fhg341, Grayrest'

def send_m(id, mes, key):
    bot.send_message(id, mes, reply_markup=key)

def create_but(key, but):
    key.add(types.KeyboardButton(but))

key_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
create_but(key_start, 'Согласен!!!')

key_standart = types.ReplyKeyboardMarkup(resize_keyboard=True)
create_but(key_standart, '/info')
create_but(key_standart, '/all')
create_but(key_standart, '/help')
base = []
@bot.message_handler(commands=['start'])
def start (message):
    send_m(message.chat.id, 'Вы согласны на использование ботом вашего тега в telegram?', key_start)
@bot.message_handler(commands=['all'])
def all(message):
    send_m(message.chat.id, ' '.join(base), key_standart)

@bot.message_handler(commands=['info'])
def info(message):
    send_m(message.chat.id, infor, key_standart)
@bot.message_handler(commands=['help'])
def help(message):
    send_m(message.chat.id, 'hihihaha', key_standart)
@bot.message_handler(content_types=['text'])
def lets_go(message):
    bot.send_message(chat_id= message.chat.id, text =  'Спасибо',reply_markup= key_standart)
    print(message)
    base.append('@'+message.from_user.username)
if __name__ == '__main__':
    bot.polling(none_stop=True)