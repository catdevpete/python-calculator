# Messing around with operations
# https://docs.python.org/3/tutorial/introduction.html

import ast

class Calculator:
    def __init__(self):
        print()

    def addition(self, *args):
        value = 0
        for i in args:
            value += i
        return value

    def subtraction(self, *args):
        value = args[0]
        for i in args[1:]:
            value -= i
        return value

    def multiplication(self, *args):
        value = args[0]
        for i in args[1:]:
            value *= i
        return value

    def division(self, *args):
        value = args[0]
        for i in args[1:]:
            value /= i
        return value

    def modulo(self, val, mod):
        return val % mod

    def exponent(self, val, exp):
        return val ** exp

    def root_extration(self, val, rt):
        return val ** (1 / rt)