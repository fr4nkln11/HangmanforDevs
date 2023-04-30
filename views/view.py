import os

class HangmanView:
    def __init__(self) -> None:
        self.message_box = None
    
    def message(self, prompt: str) -> None:
        self.message_box = prompt
    
    def render(self, model: object) -> str:
        screen = [] # initialize screen with an empty list
        for letter in model.secret_word['word'].upper():
            if letter in model.correct_guesses:
                screen.append(letter)
            elif letter in ("-"," "):
                screen.append(" ")
            else:
                screen.append("_")

        os.system("cls||clear")
        print(f"\n{''.join(screen)} \n | Lives: {model.LIFE_COUNT}\n | Score: {model.total_score}\n | Guesses made: {','.join(model.guessed_letters)}\n") # display current status
        print(f"Hint: {model.secret_word['hint']}")
        if self.message_box:
            print(self.message_box)