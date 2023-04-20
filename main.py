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

secret_word = "HELICOPTER"
# Pick a secret word
LIFE_COUNT = 5
letters = {letter : False for letter in secret_word} # a dictionary of letters that have either been guessed or not
guessed_letters = []

def update(word: dict) -> str:
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
    for letter in secret_word:
        if word[letter]:
            screen.append(letter)
        else:
            screen.append("_")
    
    print(f"\n{''.join(screen)} \n | Lives: {LIFE_COUNT}\n | Guesses made: {','.join(guessed_letters)}\n") # display current status

def check(guess: str):
    """
    First check if the letter has already been guessed,
    if so, continue
    if not, the letter is invalid and the user should guess again

    Then check if the valid guessed letter is in the secret word,
    if so, update the screen
    if not, reduce life count
    
    """

    global LIFE_COUNT
    if guess not in guessed_letters and guess != "":
        if guess in letters.keys():
            letters[guess] = True
            update(letters)
        else:
            LIFE_COUNT -= 1
        guessed_letters.append(guess)
    else:
        print("You have already guessed this letter, try something else")

if __name__ == "__main__":
    while True:
        update(letters)
        guess = str(input("pick a letter from A - Z: ")).upper()
        check(guess)

        if all(list(letters.values())):
            print("YOU WIN!!")
            break
        elif LIFE_COUNT == 0:
            print("YOU LOSE!!")
            break
