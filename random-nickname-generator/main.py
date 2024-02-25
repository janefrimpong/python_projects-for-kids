"""
Project Name: Random Nickname Generator

Difficulty Level (1 = easy -> 10 = hard): 2

Example Output:
----------------------------------------------------

    Welcome to the 'Random Nickname Generator'!

    In this app, you'll enter your first and last
    name, and then we'll choose a random nickname
    for you. You'll then see your new full name in
    the form:

    first_name 'random_nickname' last_name

What is your first name? Daniel
What is your last name? Schroeder
Your random nickname is: Head Honcho
Your new full name is: Daniel 'Head Honcho' Schroeder

----------------------------------------------------
"""

# This is a comment. It doesn't show up on the screen,
# and it starts with a `#` on the line. We'll use them
# in all of the apps in this blog post to explain each
# line of code.


# The `random` module is a builtin Python module, and
# the `choice()` function allows us to pick a random
# item from a sequence (like a `list` or `str`). You
# should always import your modules at the top of your
# file before writing any of your application code.
from random import choice

# Here, we create a variable called `welcome_message`
# A variable is a name that is assigned to a value.
#
# The `welcome_message` variable holds a multiline string.
# These are handy for printing large blocks of text with
# a single `print()` function.
welcome_message = """
    Welcome to the 'Random Nickname Generator'!

    In this app, you'll enter your first and last
    name, and then we'll choose a random nickname
    for you. You'll then see your new full name in
    the form:

    first_name 'random_nickname' last_name
"""


# The `print()` function displays data on the screen.
# Here, it's displaying the multiline string stored
# in our `welcome_message` variable.
print(welcome_message)


# The `[]` characters are how you create a `list`. A `list` is a
# sequence of values (of any data type). Here, we create a `list`
# of `str` (text data) that represents the possible nicknames
# for a user of our app.
nicknames = ["The Big Cheese", "Head Honcho", "Baby Face", "Tater Tot"]


# The `input()` function prints text to the screen and then
# waits for the user to type some text and press the "Enter"
# key on their keyboard. Any text the user types is then
# returned from the function and can be assigned a variable
# name.
#
# In this section of our program, we're asking the user
# for their first and last name and then storing the
# data they give us into `first_name` and `last_name`
# variables.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")


# The `choice()` function (which we imported at the beginning of our program)
# allows you to pull a random value from a sequence (like a `list` or a `str`).
#
# The `random_nickname` variable will hold a random value from the
# `nicknames` list we created earlier in our program.
random_nickname = choice(nicknames)


# The `random_fullname` variable will hold a `str` that we create
# using `f-strings`. An `f-string` is a special string that starts
# with the `f` character and allows you to insert the value of
# variables into a `str` between `{}` characters. The `{}` characters
# will disappear in the final `str` and be replaced by the value stored
# in the variable.
random_fullname = f"{first_name} '{random_nickname}' {last_name}"


# You can print `f-strings` directly instead of assigning them
# to variables, and this is a common way to use them.
print(f"Your random nickname is: {random_nickname}")
print(f"Your new full name is: {random_fullname}")
