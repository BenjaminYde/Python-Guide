# Exceptions

## Introduction to Exceptions

In Python, exceptions are events that occur during the execution of a program that disrupts the normal flow of the program's instructions. Handling exceptions is crucial for building robust and error-tolerant applications.

### What are Exceptions?

Exceptions are errors that are detected during execution. They might be caused by invalid input, logical errors, resource constraints, etc.
Python has numerous built-in exceptions like ValueError, TypeError, IndexError, etc., and allows the creation of custom exceptions.

## Basic Exception Handling

### Try and Except Blocks

The primary mechanism for handling exceptions in Python is the try and except statement.

Example:

```python
try:
    # Code that may cause an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero")
```

### Catching Multiple Exceptions

You can catch multiple exceptions in a single except block or use multiple except blocks.

Example:

```python
try:
    # Code that may cause an exception
except (TypeError, ValueError):
    # Handle multiple exceptions
    print("Type or Value Error occurred")
except Exception as e:
    # General exception block
    print(f"An error occurred: {e}")
```

### The Else Clause

An else block can be used to execute code if no exception was raised in the try block.

Example:

```python
try:
    result = 10 / 5
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
```

### The Finally Clause

A finally block is executed no matter whether an exception was raised or not, often used for clean-up actions.

Example:

```python
try:
    file = open('file.txt', 'r')
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
```

## Advanced Exception Handling

### Raising Exceptions

You can raise exceptions using the raise statement, either re-raising a caught exception or raising a new one.

Example:

```python
if some_condition:
    raise ValueError("A value error happened!")
```

### Creating Custom Exceptions

Custom exceptions can be defined by subclassing Exception or any other built-in exception class.

Example:

```python
class CustomError(Exception):
    pass

raise CustomError("This is a custom error message")
```

### Exception Chaining

Exception chaining occurs when an exception is raised while handling another exception. Use from to chain exceptions.

Example:

```python
try:
    # some code
except SomeException as e:
    raise NewException("An error occurred") from e
```

### Assertions

Assertions are a debugging aid that test a condition as an internal self-check in your program.
They are not intended to handle expected runtime errors, but rather to identify issues in code logic during the development phase.

Example:

```python
assert condition, "Error message if condition is False"
```

#### When Asserts Can Be Beneficial:

- **Debugging and Development**: assert statements are excellent for catching unexpected conditions during the development phase. They can quickly point out flaws in logic or incorrect assumptions.

- **Self-Documenting Code**: They can serve as a form of documentation, clearly stating the assumptions made at certain points in the code.

- **Unit Testing**: In test environments, assert statements are commonly used to verify that a piece of code behaves as expected.

Having zero assert statements in production code is a practice followed by many developers, especially in critical applications where reliability is paramount. However, in development, testing, and non-critical code, assert can be a useful tool. 
