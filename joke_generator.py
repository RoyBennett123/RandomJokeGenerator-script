import random

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? Because it was two-tired!"
]

def get_random_joke():
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_random_joke())
