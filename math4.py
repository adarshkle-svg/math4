try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f"Addition = {a + b}")
    print(f"Subtraction = {a - b}")
except ValueError:
    print("Enter a valid number!")
