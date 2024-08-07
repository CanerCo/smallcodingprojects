#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

bill = float(bill)
tip = int(tip)
people = int(people)

tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
payment = round(bill_per_person, 2)
payment = "{:.2f}".format(payment)
print(f"Each person should pay: ${payment}")