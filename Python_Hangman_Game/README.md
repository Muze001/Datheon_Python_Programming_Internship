 Hangman Word Guessing Game

 Project Overview

This is a terminal-based Hangman game developed using Python. The player attempts to guess a randomly selected hidden word one letter at a time, with a maximum of six incorrect guesses.

 Features

* Random word selection from an external word list.
* Interactive letter-by-letter guessing.
* ASCII Hangman artwork that updates after incorrect guesses.
* Tracking of previously guessed letters.
* Prevention of duplicate guesses counting as incorrect attempts.
* Input validation.
* Victory and defeat messages.
* Final score display.
* Option to play multiple rounds.

 Technologies Used

* Python 3
* Python Standard Library (random and os)

 How to Run

1. Ensure Python 3 is installed.
2. Place hangman.py and words.txt in the same working directory.
3. Open a terminal in that directory.
4. Run:

   python hangman.py

   On Windows, you can also use:

   py hangman.py

 How to Play

1. Run the program.
2. Enter one letter at a time.
3. Avoid repeating letters you've already guessed.
4. Guess the hidden word before making six incorrect guesses.
5. Choose whether to play another round when prompted.

 Scoring

The player starts with 100 points. Each incorrect guess reduces the score by 10 points. Losing the round results in a score of zero.

 Author : Muizz Ibrahim

Developed as a Python programming project for the Datheon internship.
