from views.view import HangmanView
from models.model import HangmanModel
from rich import print 

class HangmanController:
    def __init__(self) -> None:
        self.model = HangmanModel()
        self.view = HangmanView()
    
    def run(self) -> None:
        while not self.model.game_over:
            self.view.render(self.model)
            guess = input("pick a letter from A - Z (type '.quit' if you wish to end the game): ").upper()
            message = self.model.check_guess(guess)
            self.view.message(message)
        
        self.view.render(self.model)
        print("Thank you for playing my game!")


if __name__ == "__main__":
    game = HangmanController()
    game.run()