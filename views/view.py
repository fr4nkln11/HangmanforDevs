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

console = Console(theme=custom_theme)

class HangmanView:
    def __init__(self) -> None:
        self.message_box = None
    
    def message(self, prompt: str) -> None:
        self.message_box = prompt
    
    def render(self, model: object) -> str | None:
        screen = [] # initialize screen with an empty list
        for letter in model.secret_word['word'].upper():
            if letter in model.correct_guesses:
                screen.append(letter)
            elif letter in ("-"," "):
                screen.append(" ")
            else:
                screen.append("_")

        os.system("cls||clear")

        hint_panel = Panel.fit(model.secret_word['hint'], title="Hint", title_align="left")
        board_panel = Panel.fit(''.join(screen))
        life_panel = Panel.fit(str(model.LIFE_COUNT), title="Lives left", title_align="left")
        score_panel = Panel.fit(str(model.total_score), title="Score", title_align="left")
        guesses_panel = Panel.fit(','.join(model.guessed_letters), title="guessed letters", title_align="left")

        main_layout = [Columns([life_panel,score_panel,guesses_panel]),
                  Panel.fit(Columns([board_panel,hint_panel]), title="Guess the word", title_align="left")]
        
        if self.message_box:
            main_layout.append(Panel(self.message_box, style="prompt"))

        console.print(Panel.fit(Columns(main_layout, column_first=True), title="Hangman for Devs"))
        
