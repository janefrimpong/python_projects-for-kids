"""
Quiz App
    - Allows a user to take a quiz and keeps track of correct/incorrect
    answers. Displays different messages based on the number of answers
    the user got correct.
"""

welcome_message = """
    Welcome to the 'Programming Languages Quiz' app!
    
    In this app, you'll be asked a series of questions about
    different programming languages. You'll see a different 
    message based on how many questions you guess correctly.
"""

questions_and_answers = {
    "What programming language took 10 days to develop? ": "JavaScript",
    "What programming language is named after a popular British comedy troupe? ": "Python",
    "What is the primary programming language for writing Roblox games? ": "Lua",
    "What programming language is Minecraft written in? ": "Java",
    "What programming language is primarily used for writing game engines? ": "C++",
    "What is the native programming language in web browsers? ": "JavaScript",
    "What programming language is the foundation of most operating systems? ": "C",
    "What programming language has new version releases every year on Christmas day? ": "Ruby",
}

correct_answers = 0
num_questions = len(questions_and_answers)

print(welcome_message)


for question, answer in questions_and_answers.items():
    user_guess = input(question)

    if user_guess == answer:
        print("That's correct!")
        correct_answers += 1
    else:
        print("Sorry, that's incorrect...")

    print(f"You have answered {correct_answers} questions correct thus far.")


if correct_answers == num_questions:
    print("Congratulations, you got all of the questions correct!")
elif correct_answers == num_questions - 2:
    print("Not bad, you only missed a few questions, good job!")
else:
    print("You should spend some time studying about programming languages!")
