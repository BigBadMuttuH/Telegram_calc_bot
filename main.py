import types

import requests
import sympy
from telebot import *
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def main_func(message):
    x = message.text
    def has_numbers(x):
        for word in str(x):
            if word.isdigit():
                return True
            else:
                continue
        return False

    print(has_numbers(x), message.text)
    has_numbers(message)
    if message.text in ['help', '/help']:
        def help(message):
            # types это объект через который можно создавать различные кнопки
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('GitHub', url='https://github.com/GoldReserve/Telegram_calc_bot'))
            bot.send_message(message.chat.id,
                             'Данный бот умеет выполнять различные арифметические операции, а также может '
                             'менять приоритет при записи в (). \n\n<b>Ниже список основных команд:</b>'
                             '\n\n<b>+</b>      Сложение'
                             '\n<b>-</b>       Вычитание'
                             '\n<b>*</b>       Умножение'
                             '\n<b>/</b>       Деление'
                             '\n<b>**</b>     Возведение в степень'
                             '\n<b>//</b>      Деление нацело'
                             '\n<b>%</b>      Остаток от деления\n'
                             '\n<b>Примеры выполнения:</b>'
                             '\n\n2**3 ---> 8\n'
                             '4*(10/2) ---> 20\n'
                             '16**0.5 ---> 4.0\n'
                             '149//6 ---> 24\n'
                             '\nТакже, как это ни странно, бот умеет показывать погоду.\n'
                             'Чтобы узнать погоду просто пропишите или нажмите /weather', reply_markup=markup,
                             parse_mode='html')

        help(message)
    elif message.text in ['start', '/start']:
        def start(message):
            mess = f'Привет, <b>{message.from_user.first_name}</b> данный telegram бот умеет вычислять <i>выражения,</i> ' \
                   f'<i>сумму</i>, <i>разность</i>, <i>умножение</i>, <i>деление</i> и <i>возведение</i> в степень. Если нужна ' \
                   f'помощь c командами или хочешь ' \
                   f'почитать об этом подробнее вызови /help'  # можно еще и last_name
            bot.send_message(message.chat.id, mess, parse_mode='html')

        start(message)
    elif message.text in ['weather', '/weather']:
        def get_weather(message):
            url = 'http://wttr.in/?0T'
            response = requests.get(url)
            bot.reply_to(message, response)

        get_weather(message)

    elif has_numbers(x):
        def calculating_message(message):
            bot.send_message(message.chat.id, f'Result =  {sympy.sympify(message.text)}')

        calculating_message(message)
    else:
        def wrong(message):
            bot.send_message(message.chat.id, '<s>Ты втираешь мне какую-то дичь</s>'
                                              'Эээ в смысле введенной вами команды не существует.'
                                              '\nВведите корректную команду или посмотрите /help', parse_mode='html')

        wrong(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
