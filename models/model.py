import json
import random
from string import ascii_letters

def load_word_bank() -> list:
    with open('word_bank.json', 'r') as f:
        return json.load(f)

class HangmanModel:
    def __init__(self) -> None:
        self.word_bank = load_word_bank()
        random.shuffle(self.word_bank)
        self.guessed_letters = set()
        self.correct_guesses = set()
        self.LIFE_COUNT = 5
        self.game_over = False
        self.round_complete = False
        self.word_generator = (word for word in self.word_bank) # self.get_words()
        self.secret_word = next(self.word_generator)
        self.base_score = 100
        self.score_board = []
        self.total_score = sum(self.score_board)

    def new_round(self) -> None:
        self.secret_word = next(self.word_generator)
        self.guessed_letters = set()
        self.correct_guesses = set()
        self.LIFE_COUNT = 5
        self.game_over = False
        self.round_complete = False
        self.base_score = 100
    
    def score(self) -> str:
        number_of_incorrect_guesses = len(self.guessed_letters - self.correct_guesses)
        current_score = self.base_score - (number_of_incorrect_guesses * 10)
        self.score_board.append(current_score)
        return str(current_score)

    def check_guess(self, guess: str) -> str | None:
        current_word = set(self.secret_word['word'].upper()) - {" ", "-"}
        # vaidate input: must be only one letter in the alphabet

        if guess.lower() == ".quit":
            self.game_over = True

        elif (guess not in ascii_letters) or (len(guess) != 1):
            return "Invalid Input: only one letter in the alphabet is allowed"
        
        elif guess in self.guessed_letters:
            return "You have guessed this letter before, try another one"
        
        elif guess in current_word:
            self.correct_guesses.add(guess)
            self.guessed_letters.add(guess)
            if set(current_word) == self.correct_guesses:
                self.round_complete = True
                current_score = self.score()
                self.total_score = sum(self.score_board)
                return f"Word completed! You scored +{current_score} points"
            else:
                return "Correct guess!"
        else:
            self.guessed_letters.add(guess)
            self.LIFE_COUNT -= 1
            if self.LIFE_COUNT == 0:
                self.game_over = True
            else:
                return f"Incorrect guess, {self.LIFE_COUNT} lives left"
