"""
Chatbot
    - Allows a user to interact with a Chatbot, which will respond
    to certain standard commands and do things like give the user
    a random fact, perform math, etc.
"""

from random import choice

welcome_message = """
    Welcome to the "Python Chatbot" app!

    This is a simple chatbot that you can send commands
    to and it will perform some action. The five recognized
    commands are shown below:

        1. Tell me your name
            - Responds with: "Python Chatbot"

        2.  What is the meaning of life?
            - Responds with: "Programming!"

        3. Calculate [expression]
            - Performs whatever mathematical expression appears after
            the word "Calculate" and returns the answer in the form:
            "[expression] = [answer]"
                - For example: "Calculate 3 + 4 - (2 * 5)" would 
                display:
                    - 3 + 4 - (2 * 5) = -3

        4. Give me a random fact
            - Responds with a random fact, such as:
                - "The eye of an ostrich is bigger than its brain"

        5. Goodbye
            - Responds with "See ya later!" and exits the app

    Any command sent outside of the ones listed above will result
    in the chatbot responding with: "Sorry, I don't know that command!"
"""

random_facts = [
    "The eye of an ostrich is bigger than its brain.",
    "A dime has 118 ridges on its edge.",
    "Putting sugar on a cut will make it heal faster.",
    "Sign language has tongue twisters.",
    "The plastic tips of shoelaces are called aglets.",
    "Buttermilk does not contain any butter.",
    "The continental plates move at the same rate that fingernails grow.",
]

print(welcome_message)

while True:
    command = input("Enter your command: ")

    if command == "Tell me your name":
        print("Python Chatbot")
    elif command == "What is the meaning of life?":
        print("Programming!")
    elif command.startswith("Calculate"):
        expression = command.strip("Calculate ")
        result = eval(expression)
        print(f"{expression} = {result}")
    elif command == "Give me a random fact":
        random_fact = choice(random_facts)
        print(random_fact)
    elif command == "Goodbye":
        print("See ya later!")
        break
    else:
        print("Sorry, I don't know that command!")
