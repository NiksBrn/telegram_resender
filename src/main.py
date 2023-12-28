import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Hello \n Write /help for help.')
    print(message.chat.id)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, 'This bot is using for resend to you messages from some public channel')

@bot.message_handler(commands=["spam_petr"])
def spam_petr(message):
    m1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bm1 = types.KeyboardButton("начать!")
    m1.add(bm1)
    m2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bm2 = types.KeyboardButton("достать пальчик")
    m2.add(bm2)
    m3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bm3 = types.KeyboardButton("почухать пальчиком в попе")
    m3.add(bm3)
    m4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bm4 = types.KeyboardButton("потереть ножки")
    bm5 = types.KeyboardButton("game_over")
    m4.add(bm4,bm3,bm5)
    s = bot.send_message(message.chat.id,'lets go?',reply_markup=m1)
    #if(message)
    #bot.send_photo(message.chat.id,photo1)
    #bot.send_photo(message.chat.id,photo2)
    #bot.send_video(message.chat.id,w)
    #while(True):
    #    bot.send_photo(message.chat.id,open("C:/Users/nikit/Desktop/petr.jpg",'rb'))
# @bot.message_handler(content_types=["text"])
# def messages(message):
#     # print(message.chat.id)
#     # print(int(message.chat.id))
#     if int(message.chat.id) == int(config.owner):
#         try:
#             chatID = message.text.split(': ')[0]
#             text = message.text.split(': ')[1]
#             bot.send_message(chatID, text)
#         except:
#             pass
#     else:
#         bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
#         bot.send_message(message.chat.id, '%s Wait, please' % message.chat.username)

@bot.message_handler(content_types=['text'])
def go(message):
    r = message.text

    m2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bm2 = types.KeyboardButton("достать пальчик")
    m2.add(bm2)
    m3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bm3 = types.KeyboardButton("почухать пальчиком в попе")
    m3.add(bm3)
    m4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bm4 = types.KeyboardButton("потереть ножки")
    bm5 = types.KeyboardButton("game_over")
    m4.add(bm4)
    m4.add(bm3)
    m4.add(bm5)
    m5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    photo1 = open('p2.jpg', 'rb')
    photo2 = open('p1.jpg', 'rb')
    w = open('g1.mp4', 'rb')
    w1 = open('g2.mp4', 'rb')
    w2 = open('game_over.mp4', 'rb')
    # bot.send_photo(message.chat.id,photo1)
    # bot.send_photo(message.chat.id,photo2)
    # bot.send_video(message.chat.id,w)


    if(r == 'начать!'):
        bot.send_photo(message.chat.id,photo1,reply_markup=m2)
    elif r == 'достать пальчик':
        bot.send_photo(message.chat.id, photo2,reply_markup=m3)
    elif r == 'почухать пальчиком в попе':
        bot.send_video(message.chat.id, w,reply_markup=m4)
    elif r == 'потереть ножки':
        bot.send_video(message.chat.id, w1, reply_markup=m4)
    elif r == 'game_over':
        bot.send_video(message.chat.id, w2, reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')


@bot.channel_post_handler()
def messages(message):
    bot.forward_message(chat_id=config.owner, from_chat_id=message.chat.id, message_id=message.id)

if __name__ == '__main__':
    bot.polling(none_stop=True)
