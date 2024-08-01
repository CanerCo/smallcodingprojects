print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
x=0

# Multiple If statements
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("How old are you?"))
  if age < 12:
    x = 5
    print(f"You have to pay ${x}")
    photo = input("Do you want to take photos? (yes/no)")
  # elif age <= 18: is also an option.
  if 12 <= age <= 18:
    x = 7
    print(f"You have to pay ${x}")
    photo = input("Do you want to take photos? (yes/no)")
  if age >= 45 and age <= 55:
    x = 0
    print(f"Congratulations, your ticket is free and costs ${x}")
    photo = input("Do you want to take photos? (yes/no)")
  if age > 18 and not age >= 45 and age <= 55:
    x = 12
    print(f"You have to pay ${x}")
    photo = input("Do you want to take photos? (yes/no)")
  if photo == "yes" and not age >= 45 and age <= 55 :
    x = x+3
    print(f"You have to pay extra $3 and full amount is ${x}")
  if photo == "yes" and age >= 45 and age <= 55:
    x = x
    print(f"Not extra cost, you have to pay ${x}")
  if photo == "no":
    x = x
    print(f"Not extra cost, you have to pay ${x}")
else: 
  print("You cant ride the rollercoaster!")


