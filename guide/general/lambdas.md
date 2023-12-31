# Lambdas

Lambdas in Python are a way to create small, anonymous functions. These functions are typically used for a limited purpose and have a single expression. They are defined using the `lambda` keyword. Let's explore lambdas in depth, covering various aspects and use cases.

## Basic Syntax

The basic syntax of a lambda function is:

```python
lambda arguments: expression
```

Lambda functions can take any number of arguments but can only have one expression. The expression is evaluated and returned.

### Example

Here's a simple example of a lambda function:

```python
add = lambda x, y: x + y
print(add(5, 3))  # Outputs: 8
```

## Use Cases for Lambda Functions

### As Inline Functions

Lambdas are often used in places where you need a small function for a short period.


With `map()`: Applying a function to all items in a list.

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Outputs: [1, 4, 9, 16]
```

With `filter()`: Filtering items in a list.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Outputs: [2, 4, 6]
```

With `sorted()` and `list.sort()`: Sorting collections based on custom criteria.

```python
points = [(1, 2), (3, 1), (5, 0)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Outputs: [(5, 0), (3, 1), (1, 2)]
```

### In Callbacks

Lambdas are used as quick and throwaway functions for callbacks or event handlers.

For example with timers or scheduled tasks:

```python
import threading

def timed_task():
    print("Task executed")

# Setting a timer to execute a task after 5 seconds
timer = threading.Timer(5.0, timed_task)
timer.start()
```

## Late Binding Closures

Another common source of confusion is the way Python binds its variables in closures (or in the surrounding global scope).

```python
def create_functions():
    functions = []
    for i in range(5):
        def function():
            return i
        functions.append(function)
    return functions
```

### The Problem

The function inside the loop does not capture the value of i at the time it's created. Instead, it captures a reference to i, and all functions in the functions list end up referring to the same i, which is the last value after the loop ends.

### Illustration of the Issue

```python
funcs = create_functions()
result0 = funcs[0]()  # Expected to be 0, but will be 4
result1 = funcs[1]()  # Expected to be 1, but will also be 4
# ... and so on for funcs[2], funcs[3], funcs[4]
```

### How to Fix It

To fix this, we can use a default argument in the function definition, which captures the current value of i:

```python
def create_functions():
    functions = []
    for i in range(5):
        def function(i=i):
            return i
        functions.append(function)
    return functions
```

### The same problem but with lambdas

```python
def create_multipliers():
    return [lambda x : i * x for i in range(5)]
```

```python
for multiplier in create_multipliers():
    print(multiplier(2))

# output: 8 8 8 8 8
# instead of: 0 2 4 6 8
```