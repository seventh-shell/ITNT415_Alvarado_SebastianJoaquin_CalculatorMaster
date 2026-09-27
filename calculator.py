# Author: Alvarado Sebastian Joaquin S.
# ITNT415 Midterm Calculator


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def main():
    while True:
        print("\nCalculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please choose 1-5.")
            continue

        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        try:
            if choice == "1":
                result = add(first, second)
                operator = "+"
            elif choice == "2":
                result = subtract(first, second)
                operator = "-"
            elif choice == "3":
                result = multiply(first, second)
                operator = "*"
            else:
                result = divide(first, second)
                operator = "/"
        except ZeroDivisionError as error:
            print(error)
            continue

        print(f"Result: {first:g} {operator} {second:g} = {result:g}")


if __name__ == "__main__":
    main()