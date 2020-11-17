def Text2(text): #каждый символ в двоичный код
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
def code(text): #что-то типа шифра Цезаря
    #import random
    ALPHA = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
    #step = random.randint(2, 15)
    if len(text) > 4:
        step = len(text)//4
    else:
        step = len(text)*4//2
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))
def decode(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))