# Nex Programming Language

Nex is a powerful, interpreted programming language built with Python. It features a clean syntax, dynamic typing, and a modular architecture.

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Running the Shell
To start the interactive Read-Eval-Print Loop (REPL), run:

```bash
python shell.py
```

You can also execute scripts using the `RUN` command within the shell or by modifying `shell.py` to accept file arguments.

---

## 📖 Language Reference

### Variables & Data Types
Nex supports dynamic typing. Use `VAR` to declare variables.

```nex
VAR age = 25
VAR pi = 3.14
VAR name = "Nex"
VAR numbers = [1, 2, 3]
```

### Arithmetic Operators
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division
- `^` : Power

### Comparison & Logical Operators
- `==` : Equal
- `!=` : Not Equal
- `<` : Less than
- `>` : Greater than
- `<=` : Less than or equal
- `>=` : Greater than or equal
- `AND` : Logical AND
- `OR` : Logical OR
- `NOT` : Logical NOT

### Control Flow

#### If-Elif-Else
```nex
VAR x = 10

IF x > 5 THEN
    PRINT("Greater than 5")
ELIF x == 5 THEN
    PRINT("Equal to 5")
ELSE
    PRINT("Less than 5")
END
```

#### For Loops
Iterate from a start value to an end value (inclusive).

```nex
# Prints 0 to 4
FOR i = 0 TO 4 THEN
    PRINT(i)
END

# With step
FOR i = 0 TO 10 STEP 2 THEN
    PRINT(i)
END
```

#### While Loops
```nex
VAR i = 0
WHILE i < 5 THEN
    PRINT(i)
    VAR i = i + 1
END
```

### Functions
Functions can be defined with a block body or a single expression arrow syntax.

```nex
# Block syntax
FUN add(a, b)
    RETURN a + b
END

# Arrow syntax (implicit return)
FUN multiply(a, b) -> a * b

PRINT(add(2, 3))
PRINT(multiply(4, 5))
```

### Built-in Functions

| Function | Description |
|----------|-------------|
| `PRINT(value)` | Prints the value to the console. |
| `INPUT()` | Reads a string from standard input. |
| `INPUT_INT()` | Reads an integer from standard input. |
| `CLEAR()` / `CLS()` | Clears the console screen. |
| `LEN(list)` | Returns the length of a list. |
| `APPEND(list, value)` | Adds an element to the end of a list. |
| `POP(list, index)` | Removes and returns the element at the given index. |
| `EXTEND(listA, listB)` | Appends elements of listB to listA. |
| `IS_NUM(value)` | Returns true if value is a number. |
| `IS_STR(value)` | Returns true if value is a string. |
| `IS_LIST(value)` | Returns true if value is a list. |
| `IS_FUN(value)` | Returns true if value is a function. |
| `RUN(filename)` | Executes a Nex script file. |

---

## 📂 Project Structure

The project is modularized for maintainability:

- **`nex.py`**: Main entry point and `run` function.
- **`shell.py`**: Interactive shell implementation.
- **`lexer.py`**: Tokenizes the input source code.
- **`parser.py`**: Parses tokens into an Abstract Syntax Tree (AST).
- **`interpreter.py`**: Traverses the AST and executes the code.
- **`values.py`**: Defines runtime values (Number, String, List, Function) and Context.
- **`nodes.py`**: Defines AST nodes.
- **`tokens.py`**: Defines Token class.
- **`errors.py`**: Custom error handling classes.
- **`constants.py`**: Language constants and keywords.
