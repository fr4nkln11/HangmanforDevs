# Hangman game by Franklin

"""
Overview:
* Pick secret word
* hide secret word, replace each letter with dashes
* give a hint (optional)
* player has to guess all the letters
* player fails after 5 wrong guesses
* player wins if all letters are guessed correctly before 5 wrong guesses are made
* give player a score based on how well they guessed

mechanism:
* store secret word
* display dashes on screen
* ask user for a letter
* check if letter in word
** update screen with guessed letter if correct
** reduce life count by 1 if wrong
* repeat process until life count is 0 or all letters have been guessed
"""
import os
import time

class Hangman:
    """
    This is the main class for the Hangman game    
    """
    LIFE_COUNT = 5
    word_list = ["HELICOPTER", "CHOPPER", "APACHE", "CHINOOK"]
    guessed_letters = []
    correct_guesses = 0

    def word_picker(self):
        for word in self.word_list:
            yield word
    
    new_word = None
    secret_word = None
    letters = None 
    
    def message(self, prompt):
        print(prompt)

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
                if guess in self.letters.keys(): # correct guess
                    self.letters[guess] = True
                    self.correct_guesses += 1
                    self.render(self.letters)
                else: # incorrect guess
                    self.LIFE_COUNT -= 1
                self.guessed_letters.append(guess)
            else:
                print("You have already guessed this letter, try something else")
        else:
            print("you can only guess one letter at a time")
    
    # def word_complete(self):
    #     if all(list(self.letters.values())):
    #         return True
    
    def reset(self):
        self.secret_word = next(self.new_word)
        self.letters = {letter : False for letter in self.secret_word}
        self.guessed_letters = []
        self.LIFE_COUNT = 5
        self.render(self.letters)

    def game_stop(self):
        if all(list(self.letters.values())): # check if all letters have been correctly guessed 
            print("Word completed!!!")
            game_continue = input("Enter any key to continue, Enter 'Q' to quit:").upper()
            if game_continue != "Q":
                try:
                    self.reset()
                except StopIteration:
                    print("Ooops! we've run out of words")
                    return True
            else:
                return True
        elif self.LIFE_COUNT == 0:
           print("You ran out of chances, Game Over!!!")
           return True

    def run(self):
        self.new_word = self.word_picker()
        self.secret_word = next(self.new_word)
        self.letters = {letter : False for letter in self.secret_word}
        while True:
            self.render(self.letters)
            guess = str(input("pick a letter from A - Z: ")).upper()
            self.check(guess)
            if self.game_stop():
                print("Thank you for playing my game!")
                break

if __name__ == "__main__":
    game = Hangman()
    print("Hangman game by fr4nkln11 2023")
    game.run()



