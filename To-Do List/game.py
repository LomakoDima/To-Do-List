import random
import time
from speech import speach

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]
}

def play_game(level):
    words = levels.get(level,[])

    if not words:
        print('Некорректный уровень сложности')
        return

    score = 0
    num = 3

    for i in range(len(words)):
        random_word = random.choice(words)
        print(f'Произнесите слово{random_word}')
        rec_word = speach()
        print(rec_word)
