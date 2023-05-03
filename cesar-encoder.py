ALPHABET_LENGTH = 26
ASCII_UPPERCASE_START = 65
ASCII_LOWERCASE_START = 97


def get_encoded_char(char, shift):
    ascii_adjust = 0
    if 65 <= ord(char) <= 90:
        ascii_adjust = ASCII_UPPERCASE_START
    elif 97 <= ord(char) <= 122:
        ascii_adjust = ASCII_LOWERCASE_START

    ascii_value = ord(char) - ascii_adjust
    ascii_value += shift
    ascii_value = ascii_value % ALPHABET_LENGTH
    return chr(ascii_value + ascii_adjust)


raw_string = input().strip()
shift = int(input().strip())

encoded_string = ""

for char in raw_string:
    encoded_string += get_encoded_char(char, shift)

print(encoded_string)