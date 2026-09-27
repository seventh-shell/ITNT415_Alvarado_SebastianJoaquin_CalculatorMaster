# Author: Alvarado Sebastian Joaquin S.
# ITNT415 Midterm Calculator

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

        print("This operation is not implemented yet.")


if __name__ == "__main__":
    main()