"""
Mad Libs
    - Allows a user to respond to prompts and then generates a Mad Lib
    from the user's answers.
"""

welcome_message = """
    Welcome to the 'Mad Libs' app!

    In this app, you'll respond to the prompts 
    with the correct type of word. A Mad Lib will
    then be generated from your responses.
"""

print(welcome_message)

place = input("Enter a place: ")
year = input("Enter a year: ")
number = input("Enter a number: ")
adjective = input("Enter an adjective: ")
ing_verb1 = input("Enter a verb ending in 'ing': ")
ing_verb2 = input("Enter another verb ending in 'ing': ")

mad_lib = f"""
    Last summer for a vacation, my dad drove us to
    (the) {place}. Our car is a/an {year} sedan with
    {number} doors and a/an {adjective} motor. We started
    out at sunrise. My mom and dad spent all night {ing_verb1}
    the house and {ing_verb2}!
"""

print("Here's your Mad Lib!")
print(mad_lib)
