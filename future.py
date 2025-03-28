import random
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess(1-100): "))
            if 1<= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100")
        except ValueError:
                print("invaild input !!")

responses = ["yes,definitely",
             "no, not now",
             "ask again later",
             "it is certain",
             "very doubful",
             "outlook is good",
             "better not tell you now",
             "concentratre and ask again"]
def get_random_response():
    global responses
    return random.choice(responses)