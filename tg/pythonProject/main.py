import telebot
import time
from telebot import types
import sys
flag = True
bot = telebot.TeleBot('6658329963:AAHYdHCjPsLcdH9VIFtHEwEazjUyUBIZvoM')

adm_list = ['shabo1da', 'Niks_kam']
infor = 'Created by legion_team special unit [Legion_G_A_V_]\nsquad list:\n alcoprogers: Niko, t33nsy\n alcotesters: fhg341, Grayrest'


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
base = dict()
print(base)


@bot.message_handler(commands=['start'])
def start(message):
    send_m(message.chat.id, 'Вы согласны на использование ботом вашего тега в telegram?', key_start)


@bot.message_handler(commands=['all'])
def all(message):
    print(base)
    try:
        send_m(message.chat.id, ' '.join(set(base[message.chat.id])), key_standart) if base[
                                                                                           message.chat.id] != None else send_m(
            message.chat.id, 'Сначала нужно хоть одно разрешение', key_standart)
    except:
        print("Some error")


@bot.message_handler(commands=['info'])
def info(message):
    send_m(message.chat.id, infor, key_standart)


@bot.message_handler(commands=['help'])
def help(message):
    send_m(message.chat.id, 'hihihaha', key_standart)


@bot.message_handler(commands=['stop'])
def stop(message):
    global flag
    if (message.from_user.username in adm_list):
        f = open("bd.txt", "w")
        for i in base.keys():
            f.write(str(i)+'\n')
            f.write(str(base[i]))
        f.close()
        print('fa')
        flag = False
        print(flag)
        bot.stop_polling()
    else:

        bot.send_message(chat_id=message.chat.id, text="Вы не в списке администраторов")


@bot.message_handler(content_types=['text'])
def lets_go(message):
    if message.text == "Согласен!!!": bot.send_message(chat_id=message.chat.id, text='Спасибо',
                                                       reply_markup=key_standart)
    print(message)
    if message.chat.id in base.keys() and '@' + message.from_user.username not in base[message.chat.id]:
        base[message.chat.id].append('@' + message.from_user.username)
    else:
        base[message.chat.id] = ['@' + message.from_user.username]
    print(base)

while flag:
    try:
        status = "Connected to Telegram"
        bot.polling(none_stop=True)
    except:
        status = "Disconnected from Telegram"
    print(status)
    time.sleep(1)
