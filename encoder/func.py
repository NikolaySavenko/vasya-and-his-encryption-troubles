def Text2(text):  # To_Unicode_Transformation_Format
	text_2 = [bin(c)[2:].rjust(8, '0') for c in text.encode('utf-8')]
	return ''.join(text_2)


def txt_to_num(letter):
	t = []
	for i in range(len(letter)):
		t.append((ord(letter[i].upper()) - 1039))
	return t


def convert_base(num, to_base=10, from_base=10):
	if isinstance(num, str):
		n = int(num, from_base)
	else:
		n = int(num)
	alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if n < to_base:
		return alphabet[n]
	else:
		return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def alohomora(mass):
	for i in range(len(mass)):
		if mass[i] < 0:
			mass[i] = mass[i] * (-1)
		if mass[i] % 2 == 0:
			mass[i] = convert_base(mass[i], to_base=4)
		elif mass[i] % 3 == 0:
			mass[i] = convert_base(mass[i], to_base=9)
		else:
			mass[i] = convert_base(mass[i], to_base=5)
	return mass


def code(text):  # simple_Caesar_cipher
	ALPHA = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
	l = int(convert_base(len(text), to_base=6)) // 6
	if l > 4:
		step = l // 4
	else:
		step = l * 4 // 2
	return text.translate(
		str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decode(text, step):
	return text.translate(
		str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))


def check_alpha(text):
	text = text.lower()
	alpha = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
			 "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
	for one_char in text:
		if one_char not in alpha:
			return False
	return True
