import telebot
import os


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
