import pytest
import calculator
import calculator_console
import calculator_ui

# Tests for calculator function logic
def test_basic_operations():
    calc = calculator.Calculator()

    # Testing addition operation
    assert calc.addition(3, 5) == 8
    assert calc.addition(1, 8, 2) == 11
    assert calc.addition(7.42, 3.0, 4) == 14.42
    assert calc.addition(-3.1, -8, 10.2, 4.4) == 3.5

    # Testing subtraction operation
    assert calc.subtraction(10, 4) == 6
    assert calc.subtraction(52, 117) == -65
    assert calc.subtraction(8.8, -1.5, 2) == 8.3
    assert calc.subtraction(-100.0, 50, -50, 5) == -105.0

    # Testing multiplication operation
    assert calc.multiplication(5, 3) == 15
    assert calc.multiplication(-4, 5) == -20
    assert calc.multiplication(2.25, 5, 2.0) == 22.5
    assert calc.multiplication(0, 108.4) == 0

    # Testing division operation
    assert calc.division(15, 3) == 5
    assert calc.division(20, -8) == -2.5
    assert calc.division(0, -2.22) == 0
    with pytest.raises(ZeroDivisionError):
        calc.division(8, 0)

    # Testing modulo operation
    assert calc.modulo(17, 5) == 2
    assert calc.modulo(10, -3) == -2
    assert calc.modulo(10.5, 3) == 1.5
    assert calc.modulo(0, 4.7) == 0

    # Testing exponent operation
    assert calc.exponent(5, 2) == 25
    assert calc.exponent(1.5, 3) == 3.375
    assert calc.exponent(11.4, 0) == 1
    assert calc.exponent(10, -2) == 0.01

    # Testing nth root operation
    assert calc.root_extration(16, 2) == 4
    assert calc.root_extration(27, 3) == 3
    assert calc.root_extration(1, 8) == 1
    assert calc.root_extration(0, 5) == 0


def test_console_output(capfd):
    calc = calculator_console.Calculator_Console()

    # Test addition
    calc.operation_func[0](*list(map(float, [3,19,4.7,-5.2])))
    out, err = capfd.readouterr()
    assert out == "Answer: 21.5\n"

    # Test subtraction
    calc.operation_func[1](*list(map(float, [5,6,9])))
    out, err = capfd.readouterr()
    assert out == "Answer: -10.0\n"

    # Test multiplication
    calc.operation_func[2](*list(map(float, [5,2,7.5])))
    out, err = capfd.readouterr()
    assert out == "Answer: 75.0\n"

    # Test division
    calc.operation_func[3](*list(map(float, [18,4])))
    out, err = capfd.readouterr()
    assert out == "Answer: 4.5\n"

    # Test modulo
    calc.operation_func[4](*list(map(float, [8,3])))
    out, err = capfd.readouterr()
    assert out == "Answer: 2.0\n"

    # Test exponent
    calc.operation_func[5](*list(map(float, [3,4])))
    out, err = capfd.readouterr()
    assert out == "Answer: 81.0\n"

    # Test nth root
    calc.operation_func[6](*list(map(float, [8,3])))
    out, err = capfd.readouterr()
    assert out == "Answer: 2.0\n"

# Tests for UI functionality
# TBD
