key = 15

def encode(plaintext, key):
    ciphertext = bin(plaintext) ^ key
    return ciphertext

def decode(ciphertext, key):
    plaintext = bin(ciphertext) ^ key
    return plaintext

print(decode(encode("Hassan is horrible at cp", key), key))