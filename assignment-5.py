# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Erro)r! Division by zero.")
        
# Main function to take user input and perform the operation
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Take input from the user
    num = input("Enter choice (1/2/3/4): ")
    
    if num in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if num == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        
        elif num == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
        elif num == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        elif num == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")

# Run the calculator
calculator()
