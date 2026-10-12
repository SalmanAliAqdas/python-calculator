"""Simple command-line calculator."""


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


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Python Calculator (type 'q' as the operator to quit)")
    while True:
        op = input("Operator (+, -, *, /): ").strip()
        if op.lower() == "q":
            print("Goodbye!")
            break
        if op not in OPERATIONS:
            print("Unknown operator. Try again.")
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")

        try:
            result = OPERATIONS[op](a, b)
            print(f"{a} {op} {b} = {result}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
