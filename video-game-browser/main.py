from csv import reader


def load_video_game_data():
    video_game_data = []
    with open("video-game-data.csv", mode="rt", newline="") as csv_file:
        video_game_reader = reader(csv_file)
        for row in video_game_reader:
            video_game_data.append(row)

    return video_game_data


def view_video_game_data(video_game_data):
    for data in video_game_data:
        name, platform, year_of_release = data
        print(f"In {year_of_release} {name} was released on {platform}")


def search_video_game_data(video_game_data, game_name):
    for data in video_game_data:
        name, platform, year_of_release = data
        if game_name in name:
            print(f"In {year_of_release} {name} was released on {platform}")


welcome_message = """
    Welcome to the 'Video Game Browser' app!

    In this app, you can view video game data including the
    year of release, the title, and the platform the game was
    released on. You can also search the data for titles that
    match a keyword of your choosing.
"""

options = """
    1.) View Video Game Data 2.) Search Video Game Data
    3.) Exit
"""

VIEW = 1
SEARCH = 2
EXIT = 3

video_game_data = load_video_game_data()

print(welcome_message)

while True:
    user_choice = int(input(options))

    if user_choice == VIEW:
        view_video_game_data(video_game_data)
    elif user_choice == SEARCH:
        game_name = input("Enter your search term: ")
        search_video_game_data(video_game_data, game_name)
    elif user_choice == EXIT:
        break
