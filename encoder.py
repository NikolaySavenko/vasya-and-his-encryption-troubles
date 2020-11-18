from func import txt_to_num, convert_base, alohomora, code


def encode(word: str) -> str:
	"""
	:param word: just a word which should be encoded to key
	:return: encoded key
	"""
	print(f"encoding from {word}")
	text_ch = code(word)  #to_simple_Caesar_cipher
	chisl = txt_to_num(text_ch)  #10СС
	cod = alohomora(chisl)

	if len(cod) % 2 == 1:
		x = 0
		for i in range(len(cod)):
			x += int(cod[i])
		cod.append(x)
	N = len(cod)
	cod_2 = [0] * (N // 2)
	for i in range(N // 2):
		cod_2[i] = abs(int(cod[i], 10) - int(cod[N - 1 - i]))
	for i in range(len(cod_2)):
		cod_2[i] = cod_2[i] = convert_base(cod_2[i], to_base=6, from_base=16)
	return "".join(cod_2)


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
