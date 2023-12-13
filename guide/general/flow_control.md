# Flow Control

## Introduction to Control Flow

Control flow in Python refers to the order in which the program's code executes. The control flow of a program is regulated by conditional statements, loops, and function calls. Python provides various constructs to manage the flow, making the code flexible and adaptable to different scenarios and logic.

## Conditional Statements

Conditional statements allow the program to execute certain pieces of code depending on whether a specific condition is true or false.

### if Statement

- The `if` statement is used to test a condition and execute a block of code if the condition is true.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

- `elif` and `else` Statements
- `elif` (short for else if) is used to test additional conditions if the previous conditions were false.
- `else` provides a block of code that runs if all previous conditions are false.

```python
if x < 5:
    print("x is less than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is greater than 5")
```

## match Statement

The `match` statement introduced in Python 3.10 provides functionality similar to the switch/case statements found in other languages but with more advanced pattern matching capabilities. It allows matching not only single values but also complex data structures, class types, and more.

### Match Statement with Single Values

The `match` statement allows you to compare a value against several patterns and execute the block of code corresponding to the first matching pattern.

Example:

```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Other"
```

### Matching Multiple Values

You can match multiple values using the `|` operator (which signifies "`or`") or by matching against an iterable like a list.

#### Using the `|` operator:

```python
match status:
    case 200 | 201:
        return "Success"
    case 404:
        return "Not Found"
    case _:
        return "Other"
```

#### Using Iterable `[...]`:

```python
match status:
    case [200, 201]:
        return "Success"
    case [404]:
        return "Not Found"
    case _:
        return "Other"
```

### Default Value

The wildcard `_` is used as a default case to match any value. It's similar to the default case in other languages' switch/case constructs.

Example:

```python
match status:
    case 200:
        return "OK"
    case 404:
        return "Not Found"
    case _:
        return "Other"  # Default case
```

### Matching with Enums

match works well with Enums, providing a clean way to handle enumerated values.

```python
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

color = Color.RED

match color:
    case Color.RED:
        print("Red")
    case Color.GREEN:
        print("Green")
    case Color.BLUE:
        print("Blue")
```

### Deep Pattern Matching

The match statement supports deep matching within data structures, allowing you to match patterns within nested sequences or objects.

Example:

```python
match point:
    case (x, y) if x == y:
        return "Point is on the y = x line"
    case (x, y):
        return f"Point({x}, {y})"
```

### Matching Class Types

The match statement can also be used to match types of objects, which is particularly useful in dealing with different classes or data structures.

#### Default Types

```python
response_code = "300"
 match response_code:
     case int():
             print('Code is a number')
     case str():
             print('Code is a string')
     case _:
             print('Code is neither a string nor a number')
```

#### Custom Types

```python
class Error:
    code: int
    message: str

match response:
    case Error(code=404, message=msg):
        return f"Not Found: {msg}"
    case Error(code=code, message=_):
        return f"Error {code}"
    case _:
        return "Success"
```

#### Matching Against a Single Attribute

When using pattern matching with custom classes, you can match based on just one attribute of the object. You don't have to match against all attributes of the object.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

match point:
    case Point(x=0, y=_):
        return "Point is on the Y-axis"
    case Point(x=x, y=_):
        return f"Point is at x={x}"
    case _:
        return "Unknown"
```