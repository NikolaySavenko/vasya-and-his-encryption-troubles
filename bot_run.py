import telebot
import os
from answers import answer_correct, answer_incorrect
from helper import get_challenge_text, get_change_challenge_answer_text, is_correct_answer, get_key_via_message

bot = telebot.TeleBot(os.environ.get('API_KEY_TELEGRAM'))
default_parse_mode = "Markdown"


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Hello, use /new_game %code%\nto create challenge")


@bot.message_handler(commands=['new_game'])
def new_game(message):
	bot.send_message(message.chat.id, get_challenge_text(message.text), parse_mode=default_parse_mode)


@bot.message_handler(content_types=['text'])
def message_listener(message):
	try:
		reply_message = message.reply_to_message
		if reply_message is not None:
			answer = answer_incorrect
			if is_correct_answer(message.text, reply_message):
				answer = answer_correct
				bot.edit_message_text(chat_id=reply_message.chat.id, message_id=reply_message.message_id,
										text=get_change_challenge_answer_text(reply_message.text),
										parse_mode=default_parse_mode)
			bot.reply_to(message, answer)
	finally:
		pass


# RUN
bot.polling(none_stop=True)
