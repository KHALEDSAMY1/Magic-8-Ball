import random
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
