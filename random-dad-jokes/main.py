# Base URL: https://projects.flask.cwhq-apps.com/dad-joke-api/
# Endpoint: /random/jokes

# Example request: https://projects.flask.cwhq-apps.com/dad-joke-api/random/jokes

# Docs: https://github.com/KegenGuyll/DadJokes_API#getting-started

# We're using a locally-hosted version of this API instead of the URL from the docs.

from urllib.request import urlopen
from json import loads


def get_random_joke():
    BASE_URL = "https://projects.flask.cwhq-apps.com/dad-joke-api"
    endpoint = "/random/jokes"

    request_url = f"{BASE_URL}{endpoint}"
    with urlopen(request_url) as response:
        joke = loads(response.read())

    return joke


def display_joke(joke):
    punchline = joke["punchline"]
    setup = joke["setup"]
    print(f"Setup: {setup}")
    input("[Press `Enter` to hear the punchline...]")
    print(f"Punchline: {punchline}")


welcome_message = """
    Welcome to the `Random Dad Joke` app!

    This app uses an API to fetch a random setup
    and punchline to a dad joke. The setup will
    be displayed to you, and if you guess the punchline,
    a message like "That's correct!" will be displayed.
    Otherwise, you'll be shown the punchline.
"""

options = """
    (1) Get Dad Joke (2) Exit
"""

GET_JOKE = 1
EXIT = 2

while True:
    user_choice = int(input(options))

    if user_choice == GET_JOKE:
        random_joke = get_random_joke()
        display_joke(random_joke)
    elif user_choice == EXIT:
        break
