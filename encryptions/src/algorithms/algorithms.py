IMPLEMENTED_ALGORITHMS = ['Caesar Cipher', ]


# Only works with English
def encode_caesar_cipher(data, rotate):
    if rotate < 0:
        return "Cannot have a negative rotation"
    if rotate == 0:
        return data
    encoded_string = ''
    for char in data:
        if char == ' ':
            encoded_string += ' '
            continue
        char_int = ord(char)
        # Do not want to change special characters
        if char_int < 65:
            encoded_string += char
            continue
        if 90 < char_int < 97:
            encoded_string += char
            continue
        if char_int > 122:
            encoded_string += char
            continue
        if check_capital_letter(char):
            char_int -= 65
            char_int += rotate
            char_int %= 26
            char_int += 65
            encoded_string += chr(char_int)
        else:
            char_int -= 97
            char_int += rotate
            char_int %= 26
            char_int += 97
            encoded_string += chr(char_int)
    return encoded_string


# Only works with English
def decode_caesar_cipher(data, rotate):
    if rotate < 0:
        return "Cannot have a negative rotation"
    if rotate == 0:
        return data
    decoded_string = ''
    for char in data:
        if char == ' ':
            decoded_string += ' '
            continue
        char_int = ord(char)
        # Do not want to change special characters
        if char_int < 65:
            decoded_string += char
            continue
        if 90 < char_int < 97:
            decoded_string += char
            continue
        if char_int > 122:
            decoded_string += char
            continue
        if check_capital_letter(char):
            char_int -= 65
            char_int = rotate_backwards(char_int, rotate)
            char_int += 65
            decoded_string += chr(char_int)
        else:
            char_int -= 97
            char_int = rotate_backwards(char_int, rotate)
            char_int += 97
            decoded_string += chr(char_int)
    return decoded_string


# Auxiliary function to decode caesar
def rotate_backwards(char_int, amount):
    for i in range(amount):
        char_int -= 1
        if char_int < 0:
            char_int = 25
    return char_int


# Checking whether a character is a capital or not using Ascii encodings
def check_capital_letter(char):
    return ord(char) < 91
