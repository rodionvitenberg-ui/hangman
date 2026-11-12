import random
from pathlib import Path

def load_words(dictionary):
    
    word_list = []

    with open(dictionary) as file:
        for line in file:
            word = line.strip().lower()
            if len(word) >= 6:
                word_list.append(word)

    return tuple(word_list)

dictionary_path = Path(__file__).parent / "dictionary.txt"
words = load_words(dictionary_path)





STAGES = [
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

def menu():
    while True:

        print("Welcome to HANGMAN.")
        print("#1 - Start a new game.")
        print("#2 - Leave game.")

        game_choice = input("Chose 1 or 2: ").strip()

        if game_choice == "1":
            play_game()
        elif game_choice == "2":
            break
        else:
            print("The input is incorrect.")

def build_mask(word, guessed_letters):

    display = ""
    
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display

        


def play_game():

    guessed_word = random.choice(words)
    guessed_letters = []
    lives = 6
    message = ""
    
    
    while True:

        print(STAGES[lives])
        print(build_mask(guessed_word, guessed_letters))
        if message != "":
            print(message)
            message = ""
         

        letter = input("Guess a letter: ").lower().strip()

        if letter in guessed_letters:
            message = "This letter is already guessed. Try again"
            continue

        if len(letter) > 1:
            message = "The input is incorrect. Try again."
            continue

        if len(letter) <= 0:
            message = "The input is incorrect. Try again."
            continue

        if not letter.isalpha():
            message = "The input is incorrect. Try again."
            continue
        

        guessed_letters.append(letter)

        if letter in guessed_word:
            message = "Correct."
        else:
            lives -= 1
            message = f"Incorrect. {lives} lives left."

        if set(guessed_word).issubset(guessed_letters):
            print("You won.")
            break

        if lives <= 0:
            print(STAGES[0])
            print(f"You lost. The word was {guessed_word}.")
            break
    
    input("Press ENTER to continue: ")

menu()