print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N: ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N: ") # Do you want extra cheese? Y or N

bill = 0
if size == "S":
  bill = 15
if size == "M":
  bill = 20
if size == "L":
  bill = 25
if size == "S" and add_pepperoni == "Y":
  bill = bill + 2
if (size == "M" or size == "L") and add_pepperoni == "Y":
  bill = bill + 3
if add_pepperoni == "N":
  bill = bill
if extra_cheese == "Y":
  bill = bill + 1

print(f"Your final bill is: ${bill}.")