import markup as markup

import config
import telebot
from telebot import types
import sympy

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def calculating_message(message):
    if message not in ['start', 'help', '/start', '/help']:
        bot.send_message(message.chat.id, f'Result =  {sympy.sympify(message.text)}')

@bot.message_handler(commands=['text'])
def help_message(message):
    bot.send_message(message.chat.id, message.text('Привет'))


if __name__ == '__main__':
    bot.infinity_polling()

#TODO сделать функцию выводящую info по требованию
