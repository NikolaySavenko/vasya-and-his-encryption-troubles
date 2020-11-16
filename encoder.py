def encode(word: str) -> str:
	"""
	:param word: just a word which should be encoded to key
	:return: encoded key
	"""
	print(f"encoding from {word}")
	key = word[::-1]
	return key


# deprecated
def decode(key: str) -> str:
	"""
	maybe not needed
	:param key: just a word which should be decoded to key
	:return: decoded word
	"""
	print(f"decoding from {key}")
	word = key[::-1]
	return word
