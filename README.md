Timi Resistance Calculator

What it does

Timi Resistance Calculator is a Python program that calculates the total resistance of resistors connected in series and the equivalent resistance of resistors connected in parallel. It also compares resistor values by showing the highest, lowest, and average resistance.

How to run it

Install Python 3, then run:

python timi_resistance_calculator.py

Resistance formulas

Series resistance

For resistors connected in series, add all resistor values together:

R_total = R1 + R2 + R3 + ... + Rn

For example, if the resistor values are 10 ohms and 20 ohms:

R_total = 10 + 20 = 30 ohms

Parallel resistance

For resistors connected in parallel, calculate the reciprocal of the sum of their reciprocals:

1 / R_total = 1 / R1 + 1 / R2 + 1 / R3 + ... + 1 / Rn

For two resistors, the formula can also be written as:

R_total = (R1 × R2) / (R1 + R2)

For example, if the resistor values are 10 ohms and 20 ohms:

R_total = (10 × 20) / (10 + 20)
R_total = 200 / 30
R_total = 6.67 ohms

Supported input rules

The program supports the following input rules:

* The menu choice must be 1, 2, or 3.
* The number of resistors must be a whole number greater than zero.
* Resistor values must be positive numbers greater than zero.
* Decimal resistor values are accepted, such as 4.7 or 10.5.
* Negative numbers, zero, blank input, and non-numeric text are rejected.
* The program continues requesting input until a valid value is entered.
* The program displays resistance values in ohms, formatted to two decimal places.

Invalid input handling

If the user enters an invalid menu choice, the program displays an error message and asks for another choice:

Enter your choice: 5
Invalid choice. Please enter 1, 2, or 3.

If the user enters text instead of a number of resistors, the program rejects it:

How many resistors do you have? two
Invalid input. Please enter a whole number greater than zero.

If the user enters zero or a negative number of resistors, the program requests a valid value:

How many resistors do you have? 0
Invalid input. The number of resistors must be greater than zero.

If the user enters a negative or zero resistance value, the program rejects it:

Enter resistor 1 value (ohms): -10
Invalid input. Resistance must be greater than zero.

If the user enters non-numeric text for a resistor value, the program displays an error:

Enter resistor 1 value (ohms): ten
Invalid input. Please enter a positive number.

Sample output

TIMI RESISTANCE CALCULATOR
1. Calculate series and parallel resistance
2. Compare resistor values
3. Exit
Enter your choice: 1
How many resistors do you have? 2
Enter resistor 1 value (ohms): 10
Enter resistor 2 value (ohms): 20
Series resistance: 30.00 ohms
Parallel resistance: 6.67 ohms

My own twist

I added a resistor comparison feature that displays the highest, lowest, and average resistance. I also included input validation to prevent invalid values and ensure that only positive resistor values are used in the calculations.

What I learned

I learned how to use Python functions, loops, and conditional statements. I also learned how to apply series and parallel resistance formulas in programming, format numerical results, and handle invalid user input.

Author

Adebowale Timileyin Paul
ND2 Mechatronics Engineering, YabaTech.
