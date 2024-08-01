line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Choose from A,B,C and 1,2,3 Ex: A3 ") # Where do you want to put the treasure?
 
if position[0] == "A" and position[1] == "1":
  line1[0] = "X"
if position[0] == "A" and position[1] == "2":
  line2[0] = "X"
if position[0] == "A" and position[1] == "3":
  line3[0] = "X"
if position[0] == "B" and position[1] == "1":
  line1[1] = "X"
if position[0] == "B" and position[1] == "2":
  line2[1] = "X"
if position[0] == "B" and position[1] == "3":
  line3[1] = "X"
if position[0] == "C" and position[1] == "1":
  line1[2] = "X"
if position[0] == "C" and position[1] == "2":
  line2[2] = "X"
if position[0] == "C" and position[1] == "3":
  line3[2] = "X"


print(f"{line1}\n{line2}\n{line3}")