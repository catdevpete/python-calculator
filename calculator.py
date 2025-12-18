# Messing around with operations
# https://docs.python.org/3/tutorial/introduction.html

import ast

class Calculator:
    current_value = ""
    cache_value = 0.0

    def __init__(self):
        print()
    
    def all_clear(self):
        self.current_value = 0.0
        self.cache_value = 0.0

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
        value = val % mod
        return value

    def exponent(self, val, exp):
        value = val ** exp
        return value

    def root_extration(self, val, rt):
        value = val ** (1 / rt)
        return value