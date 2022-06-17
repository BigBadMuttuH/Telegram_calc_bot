import config
import telebot
import sympy

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):# Название функции не играет никакой роли
    bot.send_message(message.chat.id, f'Result =  {sympy.sympify(message.text)}')

if __name__ == '__main__':
    bot.infinity_polling()