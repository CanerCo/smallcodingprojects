import random

# Possible cards for the deck
cards  = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function to create a deck from cards
def create_desk():
    desk = random.sample(cards, 2)
    return desk

# Function to calculate the score of a deck
def calculate_score(desk):
    score = sum(desk)
    if 11 in desk and score > 21:
        desk.remove(11)
        desk.append(1)
        score = sum(desk)# Adjust for Ace being 1 instead of 11
    return score

# Function to check if the score is a blackjack
def blackjack_check(score):
    return score == 21

# Function to add a card to the deck
def add_card(desk):
    next_card = random.choice(cards)
    desk.append(next_card)
    return desk

# Function to determine the winner
def get_winner(user_score, computer_score):
    if user_score > 21:
        print("Computer Wins")
    elif computer_score > 21:
        print("User Wins")
    elif computer_score >= user_score:
        print("Computer Wins")
    else:
        print("User Wins")






