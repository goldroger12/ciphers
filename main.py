import string

MORSECODE = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}
character_digits = {'a': '01',
                    'b': '02',
                    'c': '03',
                    'd': '04',
                    'e': '05',
                    'f': '06',
                    'g': '07',
                    'h': '08',
                    'i': '09',
                    'j': '10',
                    'k': '11',
                    'l': '12',
                    'm': '13',
                    'n': '14',
                    'o': '15',
                    'p': '16',
                    'q': '17',
                    'r': '18',
                    's': '19',
                    't': '20',
                    'u': '21',
                    'v': '22',
                    'w': '23',
                    'x': '24',
                    'y': '25',
                    'z': '26'
                    }
alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
            'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
            'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}


def encrypt(text):
    cipher = ''
    for i in text:
        if i != ' ':
            cipher += MORSECODE[i] + ' '
        else:
            cipher += ' '
    return cipher


def decrypt(text):
    x = 0
    text += ' '
    storage = ''
    container = ''
    for i in text:
        if i != ' ':
            x = 0
            container += i
        else:
            x += 1
            if x == 2:
                storage += ' '
            else:
                storage += list(MORSECODE.keys())[list(MORSECODE.values()).index(container)]
                container = ''
    return storage


def encryptIndexSubstitutionCipher(text):
    translated = ''
    for i in text:
        if i != ' ':
            translated += character_digits[i] + ' '
        else:
            translated += ' '
    return translated


def decryptIndexSubstitutionCipher(text):
    x = 0
    text += ' '
    storage = ''
    container = ''
    for i in text:
        if i != ' ':
            x = 0
            container += i
        else:
            x += 1
            if x == 2:
                storage += ' '
            else:
                storage += list(character_digits.keys())[list(character_digits
                                                              .values()).index(container)]
                container = ''
    return storage


def encryptAffineCipher(text, a, b):
    y = 0
    x = ''
    container = ''  #
    for i in text:
        for j in alphabet:
            if i.lower() == j:
                y = (a * alphabet.get(j) + b) % 26
                key_list = list(alphabet.keys())
                value_list = list(alphabet.values())
                x = value_list.index(y)
                container += key_list[x]

    return container


def decryptaffinecipher(text, a, b):
    mir = 0
    x = ''
    container = ''
    for i in text:
        for j in alphabet:
            if i == j:
                mir = (pow(a, -1, 26) * (alphabet.get(j) - b)) % 26
                key_list = list(alphabet.keys())
                value_list = list(alphabet.values())
                x = value_list.index(mir)
                container += key_list[x]
    return container


def encryptCaesarCipher(text, key1, key2):
    alphabet_lower = list(string.ascii_lowercase)

    storage = ''
    space = ''
    index_alp = 0
    x = 1

    for ch in text:
        if ch == ' ':
            storage += ''
        if not ch.isalpha() and not ch.isdigit() and not ch.upper().isalpha():
            storage += ch
            if x == 1:
                x += 1
            else:
                x -= 1

        if ch.isdigit():
            if x == 1:
                ch = int(ch) + key1
                while int(ch) > 9:
                    ch -= 10
                while int(ch) < 0:
                    ch += 10
                storage += str(ch)
                x += 1
            else:
                ch = int(ch) + key2
                while int(ch) > 9:
                    ch -= 10
                while int(ch) < 0:
                    ch += 10
                storage += str(ch)
                x -= 1
        for low in alphabet_lower:
            if ch == low:
                if x == 1:
                    index_alp = alphabet_lower.index(low)
                    while index_alp + key1 > 25:
                        index_alp -= 26
                    while index_alp + key1 < 0:
                        index_alp += 26
                    space = alphabet_lower[index_alp + key1]
                    storage += space
                    x += 1
                else:
                    index_alp = alphabet_lower.index(low)
                    while index_alp + key2 > 25:
                        index_alp -= 26
                    while index_alp + key2 < 0:
                        index_alp += 26
                    space = alphabet_lower[index_alp + key2]
                    storage += space
                    x -= 1
            if ch == low.upper():
                if x == 1:
                    index_alp = alphabet_lower.index(low)
                    while index_alp + key1 > 25:
                        index_alp -= 26
                    while index_alp + key1 < 0:
                        index_alp += 26
                    space = alphabet_lower[index_alp + key1]
                    storage += space.upper()
                    x += 1
                else:
                    index_alp = alphabet_lower.index(low)
                    while index_alp + key2 > 25:
                        index_alp -= 26
                    while index_alp + key2 < 0:
                        index_alp += 26
                    space = alphabet_lower[index_alp + key2]
                    storage += space.upper()
                    x -= 1

    return storage


def decryptCaesarCipher(text, key1, key2):
    alphabet_lower = list(string.ascii_lowercase)
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    storage = ''
    space = ''
    index_alp = 0
    x = 1

    for ch in text:
        if ch == ' ':
            storage += ''
        if not ch.isalpha() and not ch.isdigit() and not ch.upper().isalpha():
            storage += ch
            if x == 1:
                x += 1
            else:
                x -= 1
        if ch.isdigit():
            if x == 1:
                ch = int(ch) - key1
                while int(ch) > 9:
                    ch -= 10
                while int(ch) < 0:
                    ch += 10
                storage += str(ch)
                x += 1
            else:
                ch = int(ch) - key2
                while int(ch) > 9:
                    ch -= 10
                while int(ch) < 0:
                    ch += 10
                storage += str(ch)
                x -= 1
        for low in alphabet_lower:
            if ch == low:
                if x == 1:
                    index_alp = alphabet_lower.index(low)
                    while index_alp - key1 < 0:
                        index_alp += 26
                    while index_alp - key1 > 25:
                        index_alp -= 26
                    space = alphabet_lower[index_alp - key1]
                    storage += space
                    x += 1
                else:
                    index_alp = alphabet_lower.index(low)
                    while index_alp - key2 < 0:
                        index_alp += 26
                    while index_alp - key2 > 25:
                        index_alp -= 26
                    space = alphabet_lower[index_alp - key2]
                    storage += space
                    x -= 1
            if ch == low.upper():
                if x == 1:
                    index_alp = alphabet_lower.index(low)
                    while index_alp - key1 < 0:
                        index_alp += 26
                    while index_alp - key1 > 25:
                        index_alp -= 26
                    space = alphabet_lower[index_alp - key1]
                    storage += space.upper()
                    x += 1
                else:
                    index_alp = alphabet_lower.index(low)
                    while index_alp - key2 < 25:
                        index_alp += 26
                    while index_alp - key2 > 25:
                        index_alp -= 26
                    space = alphabet_lower[index_alp - key2]
                    storage += space.upper()
                    x -= 1
    return storage


def encryptTranspositionCipher(text, key):
    space = ''
    list0 = []
    for i in range(len(text)):
        if len(space) != key:
            space += text[i]
            if i == len(text) - 1:
                list0.append(space)
        elif len(space) == key:
            list0.append(space)
            space = ''
            space += text[i]
            if i == len(text) - 1:
                list0.append(space)
    result = ''

    for i in range(len(list0[0])):
        for k in list0:
            if i < len(k):
                result += k[i]

    return result


def decryptTranspositionCipher(text, key):
    x = len(text) // key + 1
    y = len(text) % key
    z = x
    zero = 0
    array = []
    result = ""
    textLengthCounter = len(text)
    while True:
        if textLengthCounter == 0:

            # Same code
            for i in range(len(array[0])):
                for k in array:
                    if i < len(k):
                        result += k[i]
            return result
            # --------------------------------
        if y == 0:
            break
        array.append(text[zero:x])
        textLengthCounter = textLengthCounter - len(text[zero:x])
        zero = x
        x = x + z
        y -= 1

    x = x - 1
    while True:
        if textLengthCounter == 0:

            # Same code
            for i in range(len(array[0])):
                for k in array:
                    if i < len(k):
                        result += k[i]
            return result
            # ----------------------------
        array.append(text[zero:x])
        textLengthCounter = textLengthCounter - len(text[zero:x])
        zero = x
        x = x + (z - 1)


print(encrypt('gaga'))
print(decrypt('__. ._ __. ._ '))
print(encryptIndexSubstitutionCipher('gela'))
print(decryptIndexSubstitutionCipher('07 05 12 01'))
print(encryptAffineCipher('Affine', 11, 5))
print(decryptaffinecipher('fiipsx', 11, 5))
print(encryptCaesarCipher('Cipher Programming - 101!', 3, 2))
print(decryptCaesarCipher('Fksjht Ruqjtdopkqi - 333!', 3, 2))
print(encryptTranspositionCipher('Cipher Programming - 101!', 3))
print(decryptTranspositionCipher('Ch oai 1!iePgmn-0prrrmg 1', 3))
