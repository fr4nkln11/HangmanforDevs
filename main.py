import os
import random

class Hangman:
    LIFE_COUNT = 5
    word_list = ["HELICOPTER", "CHOPPER", "APACHE", "CHINOOK"]
    guessed_letters = []

    def word_picker(self):
        for word in self.word_list:
            yield word
    
    secret_word = None

    letters = None # a dictionary of letters that have either been guessed or not

    def render(self, word: dict) -> str:
        """
        Display the updated status of the game
        * Lives
        * Guesses
        * Letter board

        For each letter in the secret word,
        check if the letter has been guessed (guessed letters have a boolean value of True)
        if so, append the letter to the screen
        if not, append a dash to the screen
        """

        screen = [] # initialize screen with an empty list
        for letter in self.secret_word:
            if word[letter]:
                screen.append(letter)
            else:
                screen.append("_")

        os.system("cls||clear")
        print(f"\n{''.join(screen)} \n | Lives: {self.LIFE_COUNT}\n | Guesses made: {','.join(self.guessed_letters)}\n") # display current status
    
    def check(self, guess: str):
        """
        First check if the letter has already been guessed,
        if so, continue
        if not, the letter is invalid and the user should guess again

        Then check if the valid guessed letter is in the secret word,
        if so, update the screen
        if not, reduce life count
        
        """
        
        if len(guess) == 1:
            if guess not in self.guessed_letters and guess != "":
                if guess in self.letters.keys():
                    self.letters[guess] = True
                    self.render(self.letters)
                else:
                    self.LIFE_COUNT -= 1
                self.guessed_letters.append(guess)
            else:
                print("You have already guessed this letter, try something else")
        elif any(char.isdigit() for char in guess): # check if input contains digit
            print("you can only guess one letter not a number")
        else:
            print("you can only guess one letter at a time")
    
    def word_complete(self):
        if all(list(self.letters.values())):
            return True

    def run(self):
        new_word = self.word_picker()
        self.secret_word = next(new_word)
        self.letters = {letter : False for letter in self.secret_word}
        while True:
            self.render(self.letters)
            guess = str(input("pick a letter from A - Z: ")).upper()
            self.check(guess)

            if self.word_complete():
                print("Word completed!!!")
                game_continue = input("would you like to keep playing by guessing another word? (Y/N):").upper()
                if game_continue == "Y":
                    try:
                        self.secret_word = next(new_word)
                        self.letters = {letter : False for letter in self.secret_word}
                        self.guessed_letters = []
                        self.render(self.letters)
                    except StopIteration:
                        print("Ooops! we've run out of words")
                        print("Thank you for sticking around!")
                        break

                elif game_continue == "N":
                    print("Thank you for sticking around!")
                    break
            elif self.LIFE_COUNT == 0:
                print("You ran out of chances, Game Over!!!")
                break

if __name__ == "__main__":
    game = Hangman()
    print("Hangman game by fr4nkln11 2023")
    game.run()



