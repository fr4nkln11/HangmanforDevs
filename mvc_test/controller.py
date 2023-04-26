from model import HangmanModel
from rich import print

game = HangmanModel()

new_word = game.get_new_word()

for i in range(3):
    print(new := next(new_word), game.get_word_meaning(new))

