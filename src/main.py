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

@bot.channel_post_handler()
def messages(message):
    bot.forward_message(chat_id=config.owner, from_chat_id=message.chat.id, message_id=message.id)

if __name__ == '__main__':
    bot.polling(none_stop=True)
