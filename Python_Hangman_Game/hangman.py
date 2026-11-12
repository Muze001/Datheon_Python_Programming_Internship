from pathlib import Path
import random
import os

hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

with open(Path(__file__).parent / "words.txt", "r") as file:
    words = [
        word.strip().lower()
        for word in file
        if word.strip().isalpha() and len(word.strip()) >= 4
    ]

    if not words:
        raise ValueError("The words.txt file is empty or does not contain valid words.")

secret_word = random.choice(words)

print("===============================")
print("  Hangman Word Guessing Game  ")
print("===============================")

print("Welcome to Hangman Game!")
print("Guess the hidden word by suggesting letters one at a time.")
print("You have six incorrect guesses per round. Good luck!\n")


play_again = "yes"

while play_again.lower() == "yes":

    secret_word = random.choice(words)
    display_word = ["_"] * len(secret_word)
    guessed_letters = set()
    incorrect_guesses = 0

    while "_" in display_word and incorrect_guesses < 6:

       os.system('cls' if os.name == 'nt' else 'clear')
       print(hangman_stages[incorrect_guesses])
     #   print("DEBUG: Guessing loop is running.)")
       print("\nWord:", " ".join(display_word))
       print("Guessed letters:", ", ".join(sorted(guessed_letters)))
       print("Incorrect guesses:", incorrect_guesses)
       print("Remaining guesses:", 6 - incorrect_guesses)
       guess = input("Guess a letter: ").lower().strip()

       if len(guess) != 1 or not guess.isalpha():
          print("Please enter a single letter.")
          continue

       if guess in guessed_letters:
         print("You have already guessed that letter. Try again.")
         continue

       guessed_letters.add(guess)

       if guess in secret_word:
         print("Good guess! The letter is in the word.")

         for index, letter in enumerate(secret_word):
             if letter == guess:
                display_word[index] = guess
       else:
        print("Wrong guess! The letter is not in the word.")
        incorrect_guesses += 1
    print(hangman_stages[incorrect_guesses])

    if "_" not in display_word:
      print("\nCongratulations! You guessed the word:", secret_word)
      score = 100 - (incorrect_guesses * 10)
    else:
      print("\nGame over! The secret word was:", secret_word)
      score = 0
    

    print("\nFinal Word:", " ".join(display_word))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print("Incorrect guesses:", incorrect_guesses)
    print("Your score:", score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

    while play_again not in ["yes", "no"]:
      print("Please enter 'yes' or 'no'.")
      play_again = input("Would you like to play again? (yes/no): ").lower().strip()

print("Thanks for playing Hangman! Goodbye!")


