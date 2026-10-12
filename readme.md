# Python Calculator

A command-line calculator written in Python. Type a full calculation on one line and get the answer instantly.

## Features
- Add, subtract, multiply, divide
- Power (`**`), remainder (`%`), whole-number division (`//`) and square root (`sqrt`)
- Type calculations on one line, with or without spaces (`5 + 3` or `5+3`)
- `ans` reuses the previous result (`ans * 2`)
- History of calculations (`history`, `clear`)
- Friendly error messages (division by zero, invalid input)
- Results rounded to 4 decimal places
- Automated tests

## Requirements
- Python 3 installed
- A terminal (for example the one inside VS Code)

## How to run
```
python calculator.py
```
If `python` is not recognized on Windows, use `py calculator.py`.

## How to use it
Type a calculation and press Enter. Type `help` inside the program to see all commands.

```
> 5 + 3
5 + 3 = 8
> 2 ** 3
2 ** 3 = 8
> 10 / 3
10 / 3 = 3.3333
> sqrt 16
sqrt(16) = 4
> ans * 2
4 * 2 = 8
> 5 / 0
Error: Cannot divide by zero.
> history
1. 5 + 3 = 8
2. 2 ** 3 = 8
3. 10 / 3 = 3.3333
4. sqrt(16) = 4
5. 4 * 2 = 8
> q
Goodbye!
```

| Input | Meaning |
|---|---|
| `+` `-` `*` `/` | add, subtract, multiply, divide |
| `**` | power |
| `%` | remainder |
| `//` | whole-number division |
| `sqrt 16` | square root |
| `ans` | previous result |
| `history` / `clear` | show / clear past calculations |
| `help` | show help |
| `q` | quit |

## Running the tests
```
python -m unittest -v
```

## Project structure
- `calculator.py`: the calculator
- `test_calculator.py`: automated tests
- `readme.md`: this file

## Version history
- **v2**: one-line input, new operations, `ans`, history, tests
- **v1**: step-by-step prompts with four operations

## Possible future improvements
- Brackets and multi-step expressions like `(2 + 3) * 4`
- A graphical version
