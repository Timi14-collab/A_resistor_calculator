"""
TIMI RESISTANCE CALCULATOR
A simple program for calculating and comparing resistor values.
"""

def get_resistors():
    """Collect positive resistor values from the user."""
    while True:
        try:
            count = int(input("How many resistors do you have? "))
            if count > 0:
                break
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Enter a whole number.")

    resistors = []
    for i in range(count):
        while True:
            try:
                value = float(input(f"Enter resistor {i + 1} value (ohms): "))
                if value > 0:
                    resistors.append(value)
                    break
                print("Resistance must be greater than zero.")
            except ValueError:
                print("Invalid input. Enter a numeric value.")

    return resistors


def calculate_series(resistors):
    """Return total resistance for a series connection."""
    return sum(resistors)


def calculate_parallel(resistors):
    """Return equivalent resistance for a parallel connection."""
    return 1 / sum(1 / value for value in resistors)


def compare_resistors(resistors):
    """Display the highest, lowest, and average resistance."""
    print("\n----- RESISTOR COMPARISON -----")
    print(f"Highest resistance: {max(resistors):.2f} ohms")
    print(f"Lowest resistance:  {min(resistors):.2f} ohms")
    print(f"Average resistance: {sum(resistors) / len(resistors):.2f} ohms")


def main():
    """Run the calculator menu."""
    while True:
        print("\n================================")
        print("     TIMI RESISTANCE CALCULATOR")
        print("================================")
        print("1. Calculate series and parallel resistance")
        print("2. Compare resistor values")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            values = get_resistors()
            print("\n----- CALCULATION RESULTS -----")
            print(f"Series resistance:   {calculate_series(values):.2f} ohms")
            print(f"Parallel resistance: {calculate_parallel(values):.2f} ohms")
        elif choice == "2":
            values = get_resistors()
            compare_resistors(values)
        elif choice == "3":
            print("\nThank you for using Timi Resistance Calculator!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
