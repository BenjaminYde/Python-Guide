# Creating Functions

## Introduction to Functions

- **Definition**: A function is a reusable block of code that performs a specific task.
- **Purpose**: Functions help in breaking down complex problems into simpler pieces, improve code reusability, and make the code more organized and manageable.

Defining a Function:

```python
def function_name(parameters):
    # Code block
    return result
```

Calling a Function:

```python
result = function_name(arguments)
```

## Parameters and Arguments

### Parameters

Parameters are variables listed inside the parentheses in the function definition. They act as placeholders for the values that the function needs to perform its task. When defining a function, you specify what parameters it requires. Here's a simple function with parameters:

```python
def greet(name, message):
    print(f"Hello, {name}! {message}")
```

In this example, name and message are parameters of the greet function.

### Arguments

Arguments are the actual values you pass to the function when you call it. These values replace the corresponding parameters inside the function. Using the greet function, here's how you pass arguments:

```python
greet("Alice", "Welcome to Python programming!")
```

Here, "Alice" and "Welcome to Python programming!" are arguments.


### Types of Arguments

- **Positional Arguments**: These must be in the same order as the parameters in the function definition.

- **Keyword Arguments**: Identified by the parameter name. Their order doesn't matter. For example:

    ```python
    greet(message="Have a great day!", name="Bob")
    ```

- **Default Arguments**: Provide default values for parameters. They are used if no argument is provided for that parameter.

    ```python
    def greet(name, message="Good morning!"):
        print(f"Hello, {name}! {message}")
    greet("Alice")  # message defaults to "Good morning!"
    ```

- **Variable-length Arguments**: Allow a function to accept an arbitrary number of arguments. They are of two types:

  - **args**: For non-keyword variable-length arguments. It's a tuple.
  - **kwargs**: For keyword variable-length arguments. It's a dictionary.

  ```python
  def function(*args, **kwargs):
      print(args)
      print(kwargs)
  function(1, 2, 3, a=4, b=5)
  ```

## Return Statement

The return statement is used to exit a function and go back to the place from where it was called. It can also return a value or a set of values.

**A simple function with a return statement:**

```python
def add(a, b):
    return a + b

result = add(5, 3)  # result is 8
```

**Returning Multiple Values**

Python functions can return multiple values in the form of a tuple:

```python
def operations(a, b):
    return a+b, a-b, a*b, a/b

sum, difference, product, quotient = operations(10, 2)
```

**Returning None**

If no return statement is used, or if the return statement has no accompanying value, the function returns None.

```python
def no_return():
    print("This function has no return value.")

result = no_return()  # result is None
```