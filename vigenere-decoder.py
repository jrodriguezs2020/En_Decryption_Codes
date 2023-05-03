def decoded_vigenere_char(string_char, key_char):
	string_alphabet = alphabet
	if string_char.isupper():
		string_alphabet = alphabet_upper

	key_alphabet = alphabet
	if key_char.isupper():
		key_alphabet = alphabet_upper

	position = ((string_alphabet.find(string_char) - key_alphabet.find(key_char)) % len(string_alphabet))
	return string_alphabet[position]


# main
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print('Introduzca la cadena a decodificar')
encoded_string = input().strip()

print('Introduzca la clave')
key = input().strip()

decoded_string = ""
for index in range(len(encoded_string)):
	decoded_string += decoded_vigenere_char(encoded_string[index], key[index % len(key)])

print(decoded_string)