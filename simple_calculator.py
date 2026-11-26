# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (x)")
    print("4. Divide (÷)")
    print("5. Clear / Exit")

while True:
    show_menu()
    choice = input("Choose (1-5): ")

    if choice == "5":
        print("Calculator cleared. Bye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Try again.")
        continue

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
