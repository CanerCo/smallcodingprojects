import random
import art
from functions import *

# Possible cards for the deck
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Main game logic

def play_blackjack():
  print(art.logo)
  user_desk = create_desk()
  computer_desk = create_desk()

  user_score = calculate_score(user_desk)
  computer_score = calculate_score(computer_desk)


  # Check for immediate blackjack
  if blackjack_check(user_score):
    print(f"Your cards: {user_desk}, current score: {user_score}")
    print("User Wins with a Blackjack!")
    return
  elif blackjack_check(computer_score):
    print(f"Computer's cards: {computer_desk}, computer score: {computer_score}")
    print("Computer Wins with a Blackjack!")
    return
  continue_game = True
  while continue_game:
    print(f"Your cards: {user_desk}, current score: {user_score}")
    print(f"Computer's first card: {computer_desk[0]}")
    ask_another = input("Do you want to add a card into your desk? Answer 'y' or 'n': ")
    if ask_another == 'y':
      user_desk = add_card(user_desk)
      user_score = calculate_score(user_desk)
      if user_score > 21:
        print(f"Your cards: {user_desk}, current_score: {user_score}")
        print("Computer Wins")
        return
    else:
      continue_game = False
  while computer_score < 17:
    computer_desk = add_card(computer_desk)
    computer_score = calculate_score(computer_desk)

  print(f"Your cards: {user_desk}, final score: {user_score}")
  print(f"Computer's cards: {computer_desk}, final score: {computer_score}")
  get_winner(user_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == 'y':
  print("\n" * 10)
  play_blackjack()


