import os
import telebot
import logging
from config import *
from flask import Flask, request

# основные экземпляры бота и сервера (heroku)
bot = telebot.TeleBot(bot_token)
server = Flask(__name__)

# настройка отображения отладочных (ошибок) сообщений на сервере (heroku)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start(message):
    username = message.from_user.username
    bot.reply_to(message, f'Hi, {username}!')


@server.route(f'/{bot_token}', methods=['POST'])
def redirect_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


# запуск сервера при инициализации скрипта (main.py)
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=app_url)
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
