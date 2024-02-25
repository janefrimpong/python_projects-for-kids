"""
Atbash Cipher 
    - Allows a user to enter a message, and then returns the encrypted 
    or decrypted version using the Atbash Cipher. 
"""

from string import ascii_lowercase, punctuation
from random import randint


def run_atbash_cipher(text):
    cipher_text = ""
    for character in text:
        if character in punctuation or character.isspace():
            cipher_text += character
        else:
            original_index = ascii_lowercase.index(character) + 1
            cipher_character = ascii_lowercase[-original_index]
            cipher_text += cipher_character

    return cipher_text


welcome_message = """
    Welcome to the 'Atbash Cipher' app!

    In this app, you'll enter text and then 
    choose to encrypt or decrypt it using the
    Atbash Cipher. Note that the text will be
    all lowercase for encryption or decryption,
    regardless of how you enter the text.
"""

ENCRYPT = 1
DECRYPT = 2
encrypted_text = ""

print(welcome_message)

text = input("Enter the text you'd like to encrypt or decrypt: ").lower()
option = int(input("Would you like to (1) encrypt or (2) decrypt the text? "))

if option == ENCRYPT:
    encrypted_text = run_atbash_cipher(text)
    print(f"Your encrypted text is: {encrypted_text}")
elif option == DECRYPT:
    decrypted_text = run_atbash_cipher(text)
    print(f"Your decrypted text is: {decrypted_text}")
