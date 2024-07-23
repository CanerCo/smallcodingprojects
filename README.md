# Introduction

This repository hosts a collection of small coding projects I've worked on over the years. While the repository itself is new, the projects within date back several years.

# Rock-Paper-Scissors Game

This is a simple command-line implementation of the classic game Rock-Paper-Scissors. The user can choose between rock, paper, or scissors, and the computer will randomly choose its move. The outcome of the game is then displayed: win, lose, or draw.

## Features

- User input for choosing rock, paper, or scissors
- Random choice generation for the computer
- Determination and display of game result (win, lose, draw)

## Requirements

- Python 3.x

## How to Play

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
    ```bash
    python rock_paper_scissors.py
    ```
4. Follow the prompts to enter your choice (rock, paper, or scissors).
5. The computer will randomly select its choice and the result will be displayed.

## Example

```bash
Enter your choice (rock, paper, scissors): rock

You chose: rock
Computer chose: scissors
You win!
```
# Password Generator Project

This project is a simple Python script to generate random passwords. The user can specify the number of letters, symbols, and numbers they want in their password, and the script will generate a password accordingly. Additionally, the script provides an option to shuffle the characters in the generated password for added security.

## Features

- User input for specifying the number of letters, symbols, and numbers in the password
- Random generation of password based on user input
- Option to shuffle the generated password for added randomness

## Requirements

- Python 3.x

## How to Use

1. Clone the repository or download the script `PasswordGenerator.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
    ```bash
    python PasswordGenerator.py
    ```
4. Follow the prompts to enter the desired number of letters, symbols, and numbers for your password.
5. The script will generate and display a password, and then show a shuffled version of the password.

## Example

```bash
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
2
Your password: Abcd!@12
Shuffled version of the password: b@2Ad1c!
```
# Hangman Game

This project is a Python implementation of the classic Hangman game. The user has to guess the letters of a randomly chosen word within a limited number of attempts.

## Features

- Random word selection from a predefined list
- User input to guess letters
- Feedback on correct and incorrect guesses
- Display of the current state of the word
- Display of a hangman graphic that changes with each incorrect guess
- Win or lose notification

## Files
* **`hangman.py`**: Main script to run the Hangman game.
* **`hangman_words.py`**: Contains the list of words to be used in the game.
* **`hangman_art.py`**: Contains the hangman stages and logo art
## Requirements

- Python 3.x
- `replit` module (for clearing the console)

## How to Play

1. Clone the repository or download the script `hangman.py`.
2. Ensure you have `hangman_words.py` and `hangman_art.py` in the same directory. These files should contain the word list and art for the game.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using Python:
    ```bash
    python hangman.py
    ```
5. Follow the prompts to guess letters and try to figure out the word before running out of lives.

## Example

```bash
_ _ _ _ _ _ _
Guess a letter: a
You guessed a, that's not in the word. You lose a life.
_ _ _ _ _ _ _
[Hangman stage graphic]
...
```
