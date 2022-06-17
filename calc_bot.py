import config
import telebot
import sympy

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def calculating_message(message):
    bot.send_message(message.chat.id, f'Result =  {sympy.sympify(message.text)}')

if __name__ == '__main__':
    bot.infinity_polling()

#TODO сделать функцию выводящую info по требованию
#TODO сделать функцию выводящую инфу о создателях кто и что сделал about
#TODO добавить вычисление еще чего-нибудь синусов или расстояний между точками или объемов и т. п.
#