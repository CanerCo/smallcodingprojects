# Introduction

This repository hosts a collection of small coding projects I've worked on over the years. While the repository itself is new, the projects within date back several years.

# Band Name Generator

This project is a simple Python program that generates a band name based on user inputs. The user is asked for the name of the city they grew up in and the name of their pet, and the program combines these inputs to generate a band name.

## Features

- Greets the user.
- Asks the user for the name of the city they grew up in.
- Asks the user for the name of their pet.
- Combines the inputs to generate and display a band name.

## Requirements

- Python 3.x

## How to Use

1. Clone the repository or download the script `band_name_generator.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
    ```bash
    python band_name_generator.py
    ```
4. Follow the prompts to input the name of the city you grew up in and the name of your pet.
5. The script will display your band name.

## Example

```bash
Welcome to the Band Name Generator.
What is the name of the city you grew up in?
Paris
What is your pet's name?
Max
Your band name could be Paris Max
```

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

# Caesar Cipher

This project is a Python implementation of the Caesar Cipher encryption technique. The user can choose to either encode or decode a message by shifting the letters of the alphabet by a specified amount.

## Features

- User input for choosing between encoding and decoding
- User input for the message to be encrypted or decrypted
- User input for the shift amount
- Ability to restart the program for multiple uses

## Requirements

- Python 3.x

## How to Use

1. Clone the repository or download the script `caesar_cipher.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
    ```bash
    python caesar_cipher.py
    ```
4. Follow the prompts to encode or decode a message:
    - Type 'encode' to encrypt a message
    - Type 'decode' to decrypt a message
5. Enter your message and the shift amount when prompted.
6. The script will display the encoded or decoded result.
7. You can choose to restart the program or exit.

## Example

```bash
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here's the encoded result: mjqqt btwqi
Do you want to restart the cipher program? Type Yes or No
yes
...
```
# Blind Auction

This project is a Python implementation of a blind auction. Multiple users can input their bids, and the script determines the highest bidder.

## Features

- User input for bidder's name and bid amount
- Option to add multiple bidders
- Automatically clears the console for new bids
- Determines and announces the highest bidder

## Requirements

- Python 3.x
- `replit` module (for clearing the console)

## How to Use

1. Clone the repository or download the script `blind_auction.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
    ```bash
    python blind_auction.py
    ```
4. Follow the prompts to enter bidders' names and their bids.
5. After all bids are entered, the script will display the highest bidder.

## Example

```bash
What is your name?: Alice
What's your bid?: $150
Are there any other bidders? Type 'yes' or 'no': yes
# (Console clears)
What is your name?: Bob
What's your bid?: $200
Are there any other bidders? Type 'yes' or 'no': no
The winner is Bob with a bid of $200
```

# Tip Calculator

This project is a simple Python program that calculates the amount each person should pay when a bill is split among multiple people, including a specified tip percentage.

## Features

- Greets the user.
- Asks the user for the total bill amount.
- Asks the user for the desired tip percentage (10%, 12%, or 15%).
- Asks the user for the number of people to split the bill.
- Calculates the total amount each person should pay, including the tip.
- Formats the result to 2 decimal places.

## Requirements

- Python 3.x

## How to Use

1. Clone the repository or download the script `tip_calculator.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
    ```bash
    python tip_calculator.py
    ```
4. Follow the prompts to input the total bill amount, tip percentage, and number of people splitting the bill.
5. The script will display the amount each person should pay.

## Example

```bash
Welcome to the tip calculator
What was the total bill? $150
How much tip would you like to give? 10, 12, or 15?12
How many people to split the bill?5
Each person should pay: $33.60
```

# Calculator

This project is a simple calculator implemented in Python. It can perform basic arithmetic operations like addition, subtraction, multiplication, and division.

## Features

- Perform addition, subtraction, multiplication, and division
- Continue calculations with the previous result
- Option to start a new calculation

## Requirements

- Python 3.x
- `art` module (for displaying the logo)

## How to Use

1. Clone the repository or download the script `calculator.py`.
2. Ensure you have the `art.py` file in the same directory, containing the `logo` variable.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using Python:
    ```bash
    python calculator.py
    ```
5. Follow the prompts to perform calculations:
    - Enter the first number.
    - Pick an operation symbol from the displayed list.
    - Enter the next number.
    - The script will display the result.
    - You can choose to continue with the current result or start a new calculation.

## Example

```bash
What is the first number?: 5
+
-
*
/
Pick an operation symbol: +
What is the next number?: 3
5 + 3 = 8.0
Type 'y' to continue calculating with 8.0, or type 'n' to start a new calculation: y
Pick an operation symbol: *
What is the next number?: 2
8.0 * 2 = 16.0
Type 'y' to continue calculating with 16.0, or type 'n' to start a new calculation: n
