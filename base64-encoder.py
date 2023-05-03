import base64

print('Introduzca la cadena a codificar')
raw_string = input()

encoded_string = base64.b64encode(bytes(raw_string, 'UTF-8'))

print(encoded_string.decode("UTF-8"))
