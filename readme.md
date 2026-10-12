# Python Calculator

A simple command-line calculator written in Python. It runs in the terminal and asks you for an operator and two numbers.

## Features
- Add, subtract, multiply and divide
- Works with whole numbers and decimals
- Shows a friendly error for division by zero
- Asks again if you type an invalid number or operator
- Keeps running until you quit with `q`

## Requirements
- Python 3 installed on your computer
- A terminal (for example the one inside VS Code)

## How to run
1. Download or clone this repository
2. Open a terminal in the project folder
3. Run:

```
python calculator.py
```

If `python` is not recognized on Windows, use `py calculator.py`.

## How to use it
The calculator asks three questions, one at a time. Type only the answer and press Enter after each one. Do not type the whole sum on one line like `2+2`.

1. **Operator**: type one of `+`, `-`, `*`, `/`
2. **First number**: type a number
3. **Second number**: type a number

The result is shown, and then it asks for a new operator so you can keep calculating. Type `q` at the operator question to quit.

## Examples

**Addition**
```
Operator (+, -, *, /): +
First number: 5
Second number: 3
5.0 + 3.0 = 8.0
```

**Division with decimals**
```
Operator (+, -, *, /): /
First number: 10
Second number: 4
10.0 / 4.0 = 2.5
```

**Division by zero**
```
Operator (+, -, *, /): /
First number: 5
Second number: 0
Error: Cannot divide by zero.
```

**Wrong operator**
```
Operator (+, -, *, /): x
Unknown operator. Try again.
```

**Wrong number**
```
Operator (+, -, *, /): *
First number: abc
Please enter a valid number.
First number: 6
Second number: 7
6.0 * 7.0 = 42.0
```

**Quit**
```
Operator (+, -, *, /): q
Goodbye!
```

## How the code is organized
- One small function for each operation (`add`, `subtract`, `multiply`, `divide`)
- An `OPERATIONS` dictionary that connects each symbol to its function
- `get_number()` keeps asking until a valid number is entered
- `main()` runs the loop

## Possible future improvements
- Power and modulo operations
- Type a full expression like `2+2` on one line
- Automated tests
- A graphical version

## License
MIT