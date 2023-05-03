def get_decoded_char(char, key_char):
    return ord(char) ^ ord(key_char)

# main
print('Introduzca la cadena a modificar')
encoded_string = input().strip()
print('Introduzca la clave')
key = input().strip()
decoded_string = ''

for pos in range(len(encoded_string)):
    char = encoded_string[pos]
    key_char = key[pos % len(key)]
    decoded_string += chr(get_decoded_char(char, key_char))

print(decoded_string)
