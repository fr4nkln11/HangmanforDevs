import json
import random
from rich import print

def load_word_bank():
    with open('word_bank.json', 'r') as f:
        word_bank_data = json.load(f)
    
    word_bank = {}
    for word_data in word_bank_data["words"]:
        word = word_data['word']
        hint = word_data['hint']
        meaning = word_data['meaning']
        word_bank[word] = {'hint': hint, 'meaning': meaning}
    
    return word_bank

class HangmanModel:
    def __init__(self) -> None:
        self.word_bank = load_word_bank()
        self.word_keys = list(self.word_bank.keys())
        random.shuffle(self.word_keys)
        self.guessed_letters = []
        self.correct_guesses = 0
        self.LIFE_COUNT = 5
        self.game_over = False
        self.word_complete = False
    
    def get_new_word(self):
        for word in self.word_keys:
            yield word
    
    def get_word_hint(self, word):
        return self.word_bank[word]['hint']
    
    def get_word_meaning(self, word):
        return self.word_bank[word]['meaning']