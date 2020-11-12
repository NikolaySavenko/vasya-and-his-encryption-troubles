import argparse
import telebot
import os

"""
parser = argparse.ArgumentParser(description='Can it help to hide secrets?')
parser.add_argument("--token", required=True, type=str, help="Bot token")
args = parser.parse_args()
"""

bot = telebot.TeleBot(os.environ.get('API_KEY_TELEGRAM'))


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Omae wa mou shindeiru")


@bot.message_handler(content_types=['text'])
def message_listener(message):
	bot.send_message(message.chat.id, 'Oh no, im still broken!')


# RUN
bot.polling(none_stop=True)
print("Polling")
