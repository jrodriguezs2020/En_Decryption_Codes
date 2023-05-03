from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def string_padding(bytes):
    while len(bytes) % 16 != 0:
        bytes = pad(bytes, 16)
    return bytes


# main
print('Introduce el codigo encriptado')
hex_code = input().strip()
string = string_padding(bytes.fromhex(hex_code))

print('Introduce la contraseña')
key = input().strip()
key = string_padding(bytes(key.encode()))

print('Introduce el IV')
iv = input().strip()
iv = string_padding(bytes(iv.encode()))


print(unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(string), 16).decode())
