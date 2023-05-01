from views.view import HangmanView
from models.model import HangmanModel

class HangmanController:
    def __init__(self) -> None:
        self.model = HangmanModel()
        self.view = HangmanView()
    
    def run(self) -> None:
        while not self.model.game_over:
            self.view.render(self.model)
            guess = input("pick a letter from A - Z (type '.quit' if you wish to end the game): ").upper()
            status = self.model.check_guess(guess)
            if self.model.round_complete:
                self.view.render(self.model)
                print(status)
                user_choice = input("press enter to start the next round...")
                self.model.new_round()
            else:
                self.view.message(status)
        print(f"You ran out of chances, Game Over!!! The word was {self.model.secret_word['word']}")
        print("Thank you for playing my game!")


if __name__ == "__main__":
    game = HangmanController()
    game.run()