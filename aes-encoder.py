from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def string_padding(bytes):
    while len(bytes) % 16 != 0:
        bytes = pad(bytes, 16)
    return bytes


# main
print('Introduce el texto')
string = input().strip()
string = string_padding(bytes(string.encode()))

print('Introduce la contraseña')
key = input().strip()
key = string_padding(bytes(key.encode()))

print('Introduce el IV')
iv = input().strip()
iv = string_padding(bytes(iv.encode()))


print(AES.new(key, AES.MODE_CBC, iv).encrypt(string).hex())
