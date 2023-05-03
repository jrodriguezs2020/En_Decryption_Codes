ALPHABET_LENGTH = 26
ASCII_UPPERCASE_START = 65
ASCII_LOWERCASE_START = 97


def get_decoded_char(char, shift):
    ascii_adjust = 0
    if 65 <= ord(char) <= 90:
        ascii_adjust = ASCII_UPPERCASE_START
    elif 97 <= ord(char) <= 122:
        ascii_adjust = ASCII_LOWERCASE_START

    ascii_value = ord(char) - ascii_adjust
    ascii_value += shift
    ascii_value = ascii_value % ALPHABET_LENGTH
    return chr(ascii_value + ascii_adjust)


coded_string = str(input().strip())

for leap in range(ALPHABET_LENGTH):
    decoded_string = ""

    for char in coded_string:
        decoded_string += get_decoded_char(char, leap+1)

    print(decoded_string)
