"""Command-line calculator, version 2.

Type a full calculation on one line, for example:  5 + 3,  2 ** 3,  sqrt 16
Type 'help' to see all commands.
"""

import math
import re

DECIMAL_PLACES = 4
NUMBER = r"-?(?:\d+\.?\d*|\.\d+)"
OPERAND = rf"(?:{NUMBER}|ans)"
BINARY_PATTERN = re.compile(rf"^({OPERAND})\s*(\*\*|//|[+\-*/%])\s*({OPERAND})$")
SQRT_PATTERN = re.compile(rf"^sqrt\s+({OPERAND})$")

HELP_TEXT = """\
Examples:
  5 + 3        addition
  9 - 4        subtraction
  6 * 7        multiplication
  10 / 4       division
  2 ** 3       power
  10 % 3       remainder (modulo)
  10 // 3      whole-number division
  sqrt 16      square root
  ans * 2      'ans' means the previous result

Commands:
  history      show previous calculations
  clear        clear the history
  help         show this message
  q            quit"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot take a remainder with zero.")
    return a % b


def power(a, b):
    if a == 0 and b < 0:
        raise ValueError("Zero cannot be raised to a negative power.")
    if a < 0 and b != int(b):
        raise ValueError("Negative number to a fractional power is not supported.")
    try:
        return a ** b
    except OverflowError:
        raise ValueError("Result is too large.")


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": floor_divide,
    "%": modulo,
    "**": power,
}


def to_number(token, last_answer):
    """Turn text like '5' or 'ans' into a number."""
    if token == "ans":
        if last_answer is None:
            raise ValueError("No previous answer yet.")
        return last_answer
    return float(token)


def format_number(value):
    """Round the result and hide '.0' on whole numbers (8.0 -> 8)."""
    value = round(value, DECIMAL_PLACES)
    if value == int(value):
        return str(int(value))
    return str(value)


def evaluate(text, last_answer=None):
    """Calculate one line of input and return (result, display_text)."""
    text = text.strip().lower()

    match = SQRT_PATTERN.match(text)
    if match:
        a = to_number(match.group(1), last_answer)
        result = square_root(a)
        return result, f"sqrt({format_number(a)}) = {format_number(result)}"

    match = BINARY_PATTERN.match(text)
    if match:
        a = to_number(match.group(1), last_answer)
        op = match.group(2)
        b = to_number(match.group(3), last_answer)
        result = OPERATIONS[op](a, b)
        return result, f"{format_number(a)} {op} {format_number(b)} = {format_number(result)}"

    raise ValueError("I did not understand that. Type 'help' for examples.")


def main():
    print("Python Calculator v2  (type 'help' for examples, 'q' to quit)")
    history = []
    last_answer = None

    while True:
        text = input("> ").strip()
        command = text.lower()

        if command in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        if command == "":
            continue
        if command == "help":
            print(HELP_TEXT)
            continue
        if command == "history":
            if not history:
                print("No calculations yet.")
            for number, entry in enumerate(history, start=1):
                print(f"{number}. {entry}")
            continue
        if command == "clear":
            history.clear()
            last_answer = None
            print("History cleared.")
            continue

        try:
            result, display = evaluate(text, last_answer)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        last_answer = result
        history.append(display)
        print(display)


if __name__ == "__main__":
    main()
