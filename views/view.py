import os
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.columns import Columns

custom_theme = Theme({
    "hint": "cyan",
    "success": "green",
    "wrong": "red",
    "prompt": "yellow"
})

console = Console()

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
        console.rule("Hangman for Devs", align="left")

        hint_view = Panel.fit(model.secret_word['hint'], title="Hint", title_align="left")
        board_view = Panel.fit(''.join(screen))
        life_count_view = Panel.fit(str(model.LIFE_COUNT), title="Lives left", title_align="left")
        score_view = Panel.fit(str(model.total_score), title="Score", title_align="left")
        guesses_view = Panel.fit(','.join(model.guessed_letters), title="guessed letters", title_align="left")

        console.print(Columns([life_count_view,score_view,guesses_view]))
        console.print(Panel.fit(Columns([board_view,hint_view]), title="Guess the word", title_align="left"))
        if self.message_box:
            console.print(Panel(self.message_box))