import os

class HangmanView:
    def __init__(self) -> None:
        self.message_box = []
    
    def message(self, prompt):
        self.message_box.append(prompt)
    
    def render(self, model: object) -> str:
        screen = [] # initialize screen with an empty list
        for letter in model.secret_word['word']:
            if letter in model.correct_guesses:
                screen.append(letter)
            else:
                screen.append("_")

        os.system("cls||clear")
        print(f"\n{''.join(screen)} \n | Lives: {model.LIFE_COUNT}\n | Guesses made: {','.join(model.guessed_letters)}\n") # display current status
        if self.message_box:
            print(self.message_box[0])
            self.message_box.pop()