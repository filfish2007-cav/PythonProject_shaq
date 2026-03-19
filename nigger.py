import random

def get_player_names():
    names = input("Input player names with spaces: ")
    spisok_hravciv = names.split()
    return spisok_hravciv
def ask_truth_or_dare(player):
    choice = input((f'{player} Truth or Dare? '))
    return choice.lower()
def ask_truth_question(player):
    truth_questions = [
        "What is the most embarrassing thing you've ever done?",
        "What is your biggest fear?",
        "Have you ever lied to get out of trouble?",
        "What is a secret you've never told anyone?",
        "What is the most childish thing you still do?",
        "If you could be invisible for a day, what would you do?",
        "What is your biggest regret?",
        "Who is your secret crush?",
        "What is the worst gift you have ever received?",
        "What is the most expensive thing you've ever broken?"
    ]
    question = random.choice(truth_questions)
    answer = input((f'{player}: {question} '))
    return answer
def perform_dare(player):
    dare_tasks = [
        "Do 20 push-ups right now.",
        "Sing the chorus of your favorite song loudly.",
        "Dance for 60 seconds without any music.",
        "Call a friend and try to convince them it’s raining when it’s not.",
        "Eat a spoonful of a condiment of the group's choice (e.g., mustard or hot sauce).",
        "Speak in an accent for the next three rounds.",
        "Try to touch your nose with your tongue.",
        "Let another player redo your hair however they want.",
        "Post a random picture from your gallery on your social media story.",
        "Send a 'Hi' text to the 5th person in your recent messages."
    ]
    task = random.choice(dare_tasks)
    answer = input((f'{player}: {task} '))
    return answer
playerz = get_player_names()
def play_game(players):
    for player in players:
        choice = ask_truth_or_dare(player)
        if choice.lower() == "dare":
            choice2 = perform_dare(player)
            if choice2 == "no":
                print("Ok u lost ")
        if choice.lower() == "truth":
            ask_truth_question(player)
play_game(playerz)

