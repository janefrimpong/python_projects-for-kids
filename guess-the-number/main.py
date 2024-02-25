"""
Guess The Number
    - Allows a user to guess a number between 1 and 10 and tells them
    if they are too high or too low. The user has three turns to 
    guess the number. If they guess within three turns, a success
    message is displayed. Otherwise, a losing message is displayed.
"""

from random import randint


welcome_message = """
    Welcome to 'Guess The Number'!

    In this app, you'll need to guess a number between
    1 and 10. You have 3 turns to guess correctly. 
    If you guess within 3 turns, you'll be told how many
    turns it took you to guess. If you can't guess, a 
    losing message will be displayed along with the 
    random number.
"""

num_guesses = 0
random_number = randint(1, 10)
user_won = False

for turn in range(3):
    user_guess = int(input("What is your guess? "))
    num_guesses += 1

    if user_guess == random_number:
        print("That's correct!")
        print(f"You guessed the number in {num_guesses} guesses.")
        user_won = True
    else:
        print("Sorry, that's incorrect, try again!")


if not user_won:
    print(f"Game over! The random number was: {random_number}.")
