import base64

print('Introduzca la cadena a descodificar')
encoded_string = input()

decoded_string = base64.b64decode(encoded_string)

print(decoded_string.decode("UTF-8"))
