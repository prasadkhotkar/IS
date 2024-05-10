from Crypto.Cipher import DES
from Crypto.Cipher import get_random_bytes

def pad(data):
    padding_length=8 -(len(data) % 8)
    padding_data=data + bytes([padding_length] *padding_length)
    return padded_data

def unpad(data):
    padding_length =data[-1]
    return data[:-padding_length]

key = get_random_bytes(8)
cipher= DES.new(key, DES.MODE_ECB)

plaintext='prasad'
padded_plaintext=pad(plaintext)
ciphertext=cipher.encrypt(padded_plaintext)
decrypted_text=cipher.decrypt(ciphertext)

original_plaintext=unpad(decrypted_text)

print("Encrypted:", ciphertext)
print("Decrypted:", original_plaintext.decode())