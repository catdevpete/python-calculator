# Messing around with operations
# https://docs.python.org/3/tutorial/introduction.html

import ast

def addition(*args):
    value = 0
    for i in args:
        value += i
    print("Answer: {0}".format(value))

def subtraction(*args):
    value = args[0]
    for i in args[1:]:
        value -= i
    print("Answer: {0}".format(value))

def multiplication(*args):
    value = args[0]
    for i in args[1:]:
        value *= i
    print("Answer: {0}".format(value))

def division(*args):
    value = args[0]
    for i in args[1:]:
        value /= i
    print("Answer: {0}".format(value))

def modulo(val, mod):
    print("Answer: {0}".format(val % mod))

def exponent(val, exp):
    print("Answer: {0}".format(val ** exp))

def root_extration(val, rt):
    print("Answer: {0}".format(val ** (1 / rt)))

intro_label = """\
Enter the number of the desired operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulo
    6. Exponent
    7. Root Extraction"""

operation_description = [
    "Enter the range of numbers to be added, separated by commas.",
    "Enter the range of numbers to be subtracted, separated by commas. Order of operation matters.",
    "Enter the range of numbers to be multiplied, separated by commas.",
    "Enter the range of numbers to be divided, separated by commas. Order of operation matters.",
    "Enter the value then the modulus, separated by commas. Enter exactly two values.",
    "Enter the value then the exponent, separated by commas. Enter exactly two values.",
    "Enter the value then the nth root, separated by commas. Enter exactly two values."
]

operation_func = (
    addition,
    subtraction,
    multiplication,
    division,
    modulo,
    exponent,
    root_extration
)

def process_operation_values(operation):
    print(operation_description[operation - 1])
    try:
        input_values = input()
        values = list(map(float, input_values.split(',')))

        # 4.7 https://docs.python.org/3/tutorial/controlflow.html
        match operation:
            case 1 | 2 | 3 | 4:
                operation_func[operation - 1](*values)
            case 5 | 6 | 7:
                if (len(values) != 2):
                    print("Error: There must be exactly 2 input values for this operation! Try again, returning to operations selection.")
                else:
                    operation_func[operation - 1](*values)
            case _:
                raise IndexError("list index out of range")
    except ValueError:
        print("Error: Entered number is outside of the range of operations! Try again, returning to operations selection.")

def determine_operation(input_value):
    try:
        operation = int(input_value)

        if (operation > len(operation_description) or operation <= 0):
            print("Error: Entered number is outside of the range of operations! Try again.")
        else:
            process_operation_values(operation)
    except ValueError:
        print("Error: Entered input is not a valid number or operation! Try again.")
    print("\r")

def await_input():
    while True:
        print(intro_label)
        input_value = input()
        print("\r")

        if (input_value == "quit()" or input_value == "^Z"):
            break
        else:
            determine_operation(input_value)

def main():
    await_input()

if __name__ == "__main__":
    main()