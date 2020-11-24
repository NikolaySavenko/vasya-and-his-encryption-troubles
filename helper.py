from encoder import encode, decode
from answers import challenge_desc
from func import check_alpha

correct_bot_name = 'VasyaAndHisEncryptionTroublesBot'
solved_state = "🥳решено🥳"
non_solved_state = "🤜не решено🤛"
challenge_keyword = "☠️Испытание"
code_keyword = "🧠Шифр:"

code_word_not_defined = "Кодовое слово не обнаружно"
len_exception = "Слово должно состоять как минимум из 3х символов"
incorrect_alphabet = "Пожалуйста используйте только кириллицу"
solved_exception = "Уже решено"


def get_key_via_message(text: str):
	words = text.split()
	if len(words) == 2:
		return words[1]
	raise ValueError(code_word_not_defined)


def get_challenge_text(text: str):
	try:
		word = get_key_via_message(text)
		if len(word) < 3:
			raise ValueError(len_exception)
		if not check_alpha(word):
			raise ValueError(incorrect_alphabet)
		challenge = challenge_desc.replace("$CODE$", encode(word))
		challenge = challenge.replace("$STATE$", non_solved_state)
		return challenge
	except ValueError as value_error:
		# return exception from get_key_via_message() to high level
		raise value_error


def get_solved_challenge_text(challenge_text: str):
	if challenge_text.find(non_solved_state) >= 0:
		return challenge_text.replace(non_solved_state, solved_state, 1)
	raise Exception(solved_exception)


def is_challenge_from_bot_text(text):
	words = text.split()
	return words[0] == challenge_keyword


def is_correct_answer(answer: str, reply_message):
	words = reply_message.text.split()
	encoded_answer = encode(answer)
	print(f"Checking correct answer: {encoded_answer} equals? {words[words.index(code_keyword) + 1]}")
	return encoded_answer == words[words.index(code_keyword) + 1]
