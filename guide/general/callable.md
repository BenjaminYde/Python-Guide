# Callable

## What is a Callable?

In Python, a "callable" is any object that can be called using the `()` notation, typically as if it were a function. Understanding callables is crucial for grasping many of Python's dynamic features, including functions, methods, classes, and even instances of classes with a `__call__` method.

A callable is anything that can be called. In Python, you can determine whether an object is callable by using the `callable()` built-in function.

```python
def my_function():
    pass

print(callable(my_function))  # True
```

```python
class MyClass:
    def __init__(self):
        print("Instance created")

print(callable(MyClass))  # True
```

## Types of Callables

- **Functions**:
  - Defined using the def keyword.
  - Example: def func(): ...
- **Methods**:
  - Functions that are part of a class.
  - Example: class MyClass: def my_method(self): ...
- **Classes**:
  - Calling a class runs its constructor (__init__) and returns a new instance.
  - Example: class MyClass: ...; my_instance = MyClass()
- **Class Instances**:
  - If a class defines a __call__ method, its instances are callable.
  - Example: class CallableClass: def __call__(self): ...; instance = CallableClass(); instance()
- **Built-in Functions and Methods**:
  - Functions like len(), range(), etc.
  - Example: len([1, 2, 3])
- **Lambda Functions**:
  - Anonymous, inline functions defined using the lambda keyword.
  - Example: lambda x: x * 2

## Typing.Callable

The `typing.Callable` type can be used to indicate that an object is not just any callable, but one that takes certain types of arguments and returns a specific type of value.

### Syntax

The basic syntax of `typing.Callable` is:

```python
Callable[[Arg1Type, Arg2Type], ReturnType]
```

- `Arg1Type`, `Arg2Type`, etc., are the types of arguments that the callable expects.
- `ReturnType` is the type of value that the callable will return.

### Callable Without a Return Type

In Python, if you have a callable that does not return anything (analogous to Action in C#), it's typically a function that returns `None`. You can specify this using `typing.Callable`:

```python
from typing import Callable

def no_return_func(a: int, b: int) -> None:
    print(a + b)

def execute_action(action: Callable[[int, int], None]) -> None:
    action(5, 10)

execute_action(no_return_func)

```

### Callable With a Return Type

For callables that return a value (similar to Func in C#), you can specify the return type in the typing.Callable annotation:

```python
from typing import Callable

def sum_func(a: int, b: int) -> int:
    return a + b

def execute_func(func: Callable[[int, int], int]) -> int:
    return func(3, 7)

result = execute_func(sum_func)
print(result)  # Outputs: 10
```

In this case, sum_func is a callable that takes two integers and returns an integer. The execute_func function is designed to accept a callable that matches this signature and returns the result of calling it.

### Variadic Arguments

For callables with a variable number of arguments, you can use`... as a placeholder:

```python
Callable[..., ReturnType]
```