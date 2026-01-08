import calculator

class Calculator_Console:

    calc = calculator.Calculator()
    intro_label = ""
    operation_description = []
    operation_func = ()

    def __init__(self):
        self.intro_label = \
"""Enter the number of the desired operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulo
    6. Exponent
    7. Root Extraction"""

        self.operation_description = [
            "Enter the range of numbers to be added, separated by commas.",
            "Enter the range of numbers to be subtracted, separated by commas. Order of operation matters.",
            "Enter the range of numbers to be multiplied, separated by commas.",
            "Enter the range of numbers to be divided, separated by commas. Order of operation matters.",
            "Enter the value then the modulus, separated by commas. Enter exactly two values.",
            "Enter the value then the exponent, separated by commas. Enter exactly two values.",
            "Enter the value then the nth root, separated by commas. Enter exactly two values."
        ]

        self.operation_func = (
            lambda *args: print("Answer: {0}".format(self.calc.addition(*args))),
            lambda *args: print("Answer: {0}".format(self.calc.subtraction(*args))),
            lambda *args: print("Answer: {0}".format(self.calc.multiplication(*args))),
            lambda *args: print("Answer: {0}".format(self.calc.division(*args))),
            lambda x, y: print("Answer: {0}".format(self.calc.modulo(x, y))),
            lambda x, y: print("Answer: {0}".format(self.calc.exponent(x, y))),
            lambda x, y: print("Answer: {0}".format(self.calc.root_extration(x, y)))
        )

    def process_operation_values(self, operation):
        print(self.operation_description[operation - 1])
        try:
            input_values = input()
            values = list(map(float, input_values.split(',')))

            # 4.7 https://docs.python.org/3/tutorial/controlflow.html
            match operation:
                case 1 | 2 | 3 | 4:
                    self.operation_func[operation - 1](*values)
                case 5 | 6 | 7:
                    if (len(values) != 2):
                        print("Error: There must be exactly 2 input values for this operation! Try again, returning to operations selection.")
                    else:
                        self.operation_func[operation - 1](*values)
                case _:
                    raise IndexError("list index out of range")
        except ValueError:
            print("Error: Entered number is outside of the range of operations! Try again, returning to operations selection.")

    def determine_operation(self, input_value):
        try:
            operation = int(input_value)

            if (operation > len(self.operation_description) or operation <= 0):
                print("Error: Entered number is outside of the range of operations! Try again.")
            else:
                self.process_operation_values(operation)
        except ValueError:
            print("Error: Entered input is not a valid number or operation! Try again.")
        print("\r")

    def await_input(self):
        while True:
            print(self.intro_label)
            input_value = input()
            print("\r")

            if (input_value == "quit()" or input_value == "^Z"):
                break
            else:
                self.determine_operation(input_value)

if __name__ == "__main__":
    calc = Calculator_Console()
    calc.await_input()