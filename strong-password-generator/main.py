"""
Strong Password Generator
    - Allows a user to enter the desired password length and then 
    creates a secure password with random letters, numbers, and 
    punctuation.
"""

from string import ascii_letters, digits, punctuation
from random import choice, randint


welcome_message = """
    Welcome to the 'Strong Password Generator'!

    In this app, you'll enter your desired password
    length and then a random password of that length
    will be generated. The password will consist of 
    letters (upper and lowercase), numbers, and
    punctuation characters.
"""

RANDOM_LETTER = 1
RANDOM_DIGIT = 2
RANDOM_PUNCTUATION = 3

print(welcome_message)

password_length = int(input("Enter your desired password length: "))

password = ""
for num in range(password_length):
    random_character = ""
    option = randint(1, 3)

    if option == RANDOM_LETTER:
        random_character = choice(ascii_letters)
    elif option == RANDOM_DIGIT:
        random_character = choice(digits)
    elif option == RANDOM_PUNCTUATION:
        random_character = choice(punctuation)

    password += random_character


print(f"Your password is: {password}")
