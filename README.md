# Telegram_calc_bot
Repository to work together on homework to create telegram bot.
## Импорты:
* `import config` - Импортируем токен, созданный самим Telegram, чтобы тестировать работу в реальном клиенте мессенджера.
* `import telebot` - Импортируем библиотеку для работы с ботом.
* `import sympy` - импорт специальной библиотеки для символьных вычислений.
## Что нам нужно перед описанием функции?
1. `bot = telebot.TeleBot(config.token)` - объявляем бот с индивидуальным токеном, который был импортирован ранее.
2. `@bot.message_handler(content_types=["text"])` - команда у нас всего 1 - численное выражение, которое нам и нужно вычислить.
## Функция main_func()
Функция принимает на вход текст из сообщения и в зависимости от содепжимого перенаправляет на другие под функции:
1. help() выводит справку об использовании бота
2. start() здоровается с пользователем и пишет приветственное сообщение
3. calculating_message() высчитывает результат при помощи sumpy
### bot.send_message(message.chat.id, f'Result =  {sympy.sympify(message.text)}')
* `bot.send_message`('Кому в какой чат отправить', 'что отправить') - функция отправки собщения тому, кто обратился к боту.
В скобках описывается кому и в какой чат отправить, и что именно отправить.
* `f'Result =  {sympy.sympify(message.text)}'` - здесь рассмотрим конкретно функцию `sympy.sympify`.

SymPy — это библиотека Python для символьной математики.
Он стремится стать полнофункциональной системой компьютерной алгебры (CAS), сохраняя при этом максимально простой код, чтобы он был понятным и легко расширяемым.
SymPy полностью написан на Python.

`sympify` - это функция библиотеки SymPy для упрощения выражения. В нашем случае она используется для вычисления введённого пользователем выражения.
Всё на столько просто, что для работы функции с введёнными данными не требуется никакой предварительной обработки этих самых данных.
```
Для определенных видов математических функций существуют более конкретные функции для упрощения выражений.
Так, для упрощения степенных функций есть функция `powsimp`, для тригонометрических - `trigsimp`, а для логарифмических - `logcombine`, `radsimp`.
```

`if __name__ == '__main__': bot.infinity_polling()` - пока находимся в главном файле, происходит бесконечный опрос бота в клиенте Telegram.