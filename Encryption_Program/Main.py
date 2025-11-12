#Phthon Encryption-Decryption Program
import random
import string

def generate_key():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    return chars, key

def encrypt(chars, key):
    plain_text = input("Enter a Message to Encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"original message: {plain_text}")
    print(f"encrypted meassage: {cipher_text}")
    return cipher_text

def decrypt(chars, key):
    cipher_text = input("Enter a Message to Decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Decrypt message: {plain_text}")

def main():
    chars, key = generate_key()
    encrypt(chars, key)
    decrypt(chars, key)

if __name__ == "__main__":
    main()
