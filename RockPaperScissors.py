rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
human = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
human = int(human)
if human == 0:
    print(rock)
elif human == 1:
    print(paper)
elif human == 2:
    print(scissors)
else:
    print("Error: Unvalid number!")

computer = random.randint(0,2)

if computer == 0:
    print("Computer chose:\n")
    print(rock)
elif computer == 1:
    print("Computer chose:\n")
    print(paper)
elif computer == 2:
    print("Computer chose:\n")
    print(scissors)
else:
    print("Error: Unvalid number!")

if human == 0 and computer == 0:
    print("Draw!")
elif human == 0 and computer == 1:
    print("You lose")
elif human == 0 and computer == 2:
    print("You win")
elif human == 1 and computer == 0:
    print("You win")
elif human == 1 and computer == 1:
    print("Draw")
elif human == 1 and computer == 2:
    print("You lose")
elif human == 2 and computer == 0:
    print("You lose")
elif human == 2 and computer == 1:
    print("You win")
elif human == 2 and computer == 2:
    print("Draw")
