import telebot
import os
from answers import answer_correct, answer_incorrect
from helper import get_challenge_text, get_solved_challenge_text, is_correct_answer

bot = telebot.TeleBot(os.environ.get('API_KEY_TELEGRAM'))
default_parse_mode = "Markdown"


@bot.message_handler(commands=['start'])
def welcome(message):
	print("/start detected")
	print("[------------------------------]")
	bot.send_message(message.chat.id, "Hello, use /new_game %code% to create challenge")


@bot.message_handler(commands=['new_game'])
def new_game(message):
	print(f"try new game with message: {message.text}")
	answer = ""
	try:
		answer = get_challenge_text(message.text)
		print("Challenge successfully created")
	except ValueError as exception:
		answer = exception
		print(f"ValueError occurred: {exception}")
	bot.send_message(message.chat.id, answer, parse_mode=default_parse_mode)
	print("[------------------------------]")


@bot.message_handler(content_types=['text'])
def message_listener(message):
	reply_message = message.reply_to_message
	if reply_message is not None:
		print(f"Try to answer with: {message.text}")
		answer = ""
		try:
			if is_correct_answer(message.text, reply_message):
				answer = answer_correct
				solved_challenge = get_solved_challenge_text(reply_message.text)
				# set challenge status
				bot.edit_message_text(chat_id=reply_message.chat.id, message_id=reply_message.message_id,
									  text=solved_challenge,
									  parse_mode=default_parse_mode)
				print("Correct answer")
			else:
				answer = answer_incorrect
				print("Incorrect answer")
		except Exception as exception:
			answer = exception
			print("Already solved")
		print("[------------------------------]")
		bot.reply_to(message, answer)


# RUN
print("Bot started!")
print("[------------------------------]")
bot.polling(none_stop=True)
