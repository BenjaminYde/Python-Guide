# Typing

## Introduction

Typing in Python refers to type annotations, a feature introduced in Python 3.5 that allows for explicit indication of the types of variables, function parameters, and return values. It's a form of "type hinting" that helps in static type checking.

## Why Use Typing?

- **Code Readability and Clarity**: Clarifies what types of values are expected and returned, making the code more readable and understandable.

- **Error Detection**: Early error detection during development. Tools like Mypy can analyze code for type inconsistencies before runtime.

- **Better IDE Support**: Improved autocomplete, function signatures, and error highlighting in Integrated Development Environments (IDEs).

- **Facilitates Refactoring**: Makes refactoring safer and easier by catching type-related errors.

- **Documentation**: 
Serves as an additional form of documentation for how the code is supposed to be used.

## Basic Syntax

### Variable Annotations:

```python
age: int = 25
name: str = "Alice"
```

### Function Annotations:

Parameters and return types can be annotated.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Type Aliases

Creating custom names for types, useful for simplifying complex type definitions.

```python
Vector = list[float] # Vector is an alias for a list of floats
```

```python
def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

The `type` statement is new in **Python 3.12**.     
For backwards compatibility, type aliases can also be created through simple assignment:

```python
type Vector = list[float] # Vector is an alias for a list of floats
```

Or marked with `TypeAlias` to make it explicit that this is a type alias, not a normal variable assignment:

```python
from typing import TypeAlias

Vector: TypeAlias = list[float]
```

## The typing Module

Provides several types like List, Dict, Tuple, Optional, Union, etc.

```python
from typing import List, Optional

def process_items(items: List[str]) -> None:
    #...
```

##  Optional

In Python, `Optional` is a type hint (introduced in Python 3.5 and the typing module) that indicates that a variable may have a value of a specified type, or it could be None. It's a way to explicitly document that None is an acceptable value for a variable, in addition to other types.

Usage:

```python
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest"
    return f"Hello, {name}"
```

In this example, the greet function accepts either a string or None as its argument.

## Tuple

In Python, a tuple is similar to a list, but it is immutable, meaning that its elements cannot be changed after it is created. Tuples are defined using parentheses, with elements separated by commas. 

Here is how you can initialize a tuple:

```python
myTuple = (10, 20, 30, 40, 50) # A tuple of integers
anotherTuple = ('apple', 'banana', 'cherry') # A tuple of strings
```
#### Characteristics of Tuples

- **Immutable**: Once a tuple is created, you cannot add, remove, or modify its elements.
- **Ordered**: Like lists, tuples maintain the order of elements.
- **Indexable** and Slicable: You can access elements by their index and slice tuples.
- **Allow Duplicate Elements**: Tuples can contain duplicate elements.

##  Union

The Union type hint is used to indicate that a variable can be one of several types.        
It is useful when a function can accept arguments of different types.

Usage:

```python
from typing import Union

def process(data: Union[int, str]):
    if isinstance(data, int):
        return data * 2
    return f"Received string: {data}"

process(1) # ok
process("Hello") # ok
process(1, "Hello") # not ok
```

In the process function, data can either be an int or a str.

- `Union` is about saying "this can be any one of these types" (a logical OR).
- `Tuple` is about saying "this is a collection of items, each with a specific type".
- `Union` does not convey information about the number of elements.
- `Tuple` specifies the exact number and types of elements.

## NewType

`NewType` creates a new type that is semantically distinct from its base type, even if it's technically the same (like an `int` or `str`). For instance, UserID and ProductID may both be integers, but they have different meanings and roles in your code.

Example:

```python
from typing import NewType

UserID = NewType('UserID', int)
ProductID = NewType('ProductID', int)

def get_user_name(user_id: UserID) -> str:
    pass

def get_product_name(product_id: ProductID) -> str:
    pass
```

## Type Guards

Runtime checks that narrow down types of variables within specific scopes.

```python
if isinstance(x, list):
    # x is treated as a list here
```

## Best Practices

- **Consistency**: Apply type hints consistently throughout your codebase.

- **Avoid Overuse**: Use type hints where they add clarity, but avoid over-complicating simple code.

- **Dynamic vs Static Typing**: Remember that Python is dynamically typed, and type hints are mainly for static analysis.

## Limitations and Considerations

- **Runtime Overhead**: Type hints do not affect the runtime performance of Python code.
  
- **Not Enforced at Runtime**: Python does not enforce type hints during execution; they are only for static analysis.

## Conclusion

Using typing in Python, especially in large and complex codebases, can significantly improve code quality, maintainability, and readability. It aids in error detection, enhances IDE features, and serves as an effective form of documentation. However, it's essential to balance its use to maintain the readability and simplicity Python is known for.