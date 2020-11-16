from encoder import encode, decode
from answers import challenge_desc

correct_bot_name = 'VasyaAndHisEncryptionTroublesBot'
solved_state = "solved"
non_solved_state = "non-solved"
challenge_keyword = "Challenge"


def get_key_via_message(text: str):
	words = text.split()
	if len(words) == 2:
		return words[1]
	raise Exception("no no no")


def get_challenge_text(text: str):
	try:
		word = get_key_via_message(text)
		challenge = challenge_desc.replace("$CODE$", encode(word))
		challenge = challenge.replace("$STATE$", non_solved_state)
		return challenge
	except:
		return "Please write keyword after space with command"


def get_change_challenge_answer_text(challenge_text: str):
	if challenge_text.find(non_solved_state):
		return challenge_text.replace(non_solved_state, solved_state, 1)
	return challenge_text


def is_challenge_from_bot_text(text):
	words = text.split()
	return words[0] == challenge_keyword


def is_correct_answer(answer: str, reply_message):
	return encode(answer) == reply_message.text.split()[4]


# deprecated
def get_secret_via_message(reply_message):
	if reply_message.from_user.username == correct_bot_name and \
			is_challenge_from_bot_text(reply_message.text):
		return decode(reply_message.text.split()[4])
	raise Exception("not correct reply")
