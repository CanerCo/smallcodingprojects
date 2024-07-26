from art import logo
# Calculator

# Add function
def add(n1, n2):
  return n1 + n2

# Subtract function
def subtract(n1, n2):
  return n1 - n2

# Multiply function
def multiply(n1, n2):
  return n1 * n2

# Divide function
def divide(n1,n2):
  return n1 / n2

# Create a dictionary for symbols and function names
operations  = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}



def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What is the first number?: "))
    for key in operations:
        print(key)
    
    while should_continue:
        operation_symbol = input("Pick an operation symbol: ")
        calculation_function = operations[operation_symbol]
        num2 = float(input("What is the next number?: "))
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        more_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new: ")
        if more_calculation == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
        
    
calculator()