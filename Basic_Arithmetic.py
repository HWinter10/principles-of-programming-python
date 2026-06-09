"""
Basic Arithmatic Program
    Input: two numbers from user
    Output: results of various calulations done on user inputted values

Pseudocode:
    START
        Ask user to enter number
        Store first number as num1

        Ask user to enter second number
        Store second number as num2

        Calculate addition:
            add num1 + num2
        
        Calculate subtraction:
            subtract num1 - num2
        
        Calculate multiplication:
            multiply num1 * num2

        IF num2 is not 0:
            Calculate division:
                divide num1 / num2
        ELSE
            Output division by zero is not possible

        Display results of each calculation performed
    END
"""

# Asks user for two input values, storing them into variables 
num1 = float(input("Hello user! Please enter a number: "))
num2 = float(input("Please enter a second number greater than zero: "))

# Performs arithetic calulations on the two variables
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero."

print("\nBased on your inputs.. your arithmetic results are")
print("------------------------------------------------------")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("------------------------------------------------------")