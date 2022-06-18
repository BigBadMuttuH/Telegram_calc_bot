import config
import telebot
import sympy


bot = telebot.TeleBot(config.token)

"""Message это целиком всё сообщение которое содержит не только текст но и другие данные которые можно получить
обращаясь к message.content_type.text или message.is_bot или message.first_name. Для того чтобы увидеть полный список
этого всего можно прописать:
@bot.message_handler()
def helping(message):
    bot.send_message(message.chat.id, message, parse_mode='html') 
Тогда при введении любого сообщения бот ответит простыней из списка элементов к которым можно получить доступ"""


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b> данный telegram бот умеет вычислять <i>выражения,</i> ' \
           f'<i>сумму</i>, <i>разность</i>, <i>умножение</i>, <i>деление</i> и <i>возведение</i> в степень. Если нужна ' \
           f'помощь c командами или хочешь ' \
           f'почитать об этом подробнее вызови /help'# можно еще и last_name
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Вот тебе и хелп', parse_mode='html')

@bot.message_handler()
def helping(message):
    if message.text == 'все_атрибуты':
        bot.send_message(message.chat.id, message, parse_mode='html')
    else:
        if message.text not in ['start', 'help', '/start', '/help', 'все_атрибуты']:
            bot.send_message(message.chat.id, f'Result =  {sympy.sympify(message.text)}')


@bot.message_handler(content_types=["text"])
def calculating_message(message):
    if message.text not in ['start', 'help', '/start', '/help', 'все_атрибуты']:
        bot.send_message(message.chat.id, f'Result =  {sympy.sympify(message.text)}')




bot.polling(none_stop=True)


#TODO сделать функцию выводящую info по требованию
