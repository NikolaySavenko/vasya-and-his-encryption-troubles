import time
import telebot
import os
import threading


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


# Please, stop this madman!
def rolling(sleep_time: int):
	while True:
		print("Rolling!")
		time.sleep(sleep_time)


# don't beat me pls
roll_thread = threading.Thread(target=rolling, args=(3,), daemon=False)
roll_thread.start()
