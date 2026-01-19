try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f"Addition = {a + b}")
    print(f"Subtraction = {a - b}")
    
    if b != 0:
        print(f"Division = {a / b}")
    else:
        print("Division by zero is not allowed")
except ValueError:
    print("Enter a valid number!")
