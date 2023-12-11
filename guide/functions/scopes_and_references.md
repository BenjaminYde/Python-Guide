# Scopes and References

## Python's Variable Scopes

Python has three main scopes:

### Local Scope

**Local Scope**: Variables defined within a function are in the local scope of that function. They are only accessible within that function.

```python
def local_scope_example():
    local_var = 10  # Local variable
    print(local_var)  # Accessible here

local_scope_example()
# print(local_var)  # This would result in an error since local_var is not accessible here
```


### Global Scope

**Global Scope**: Variables defined at the top level of a script or module or explicitly declared global inside a function are in the global scope. They are accessible anywhere in the module.

```python
global_var = 5  # Global variable

def global_scope_example():
    print(global_var)  # Accessible here

global_scope_example()
print(global_var)  # Also accessible here
```

### Enclosing (Nonlocal) Scope

**Enclosing (Nonlocal) Scope**: This scope is specific to nested functions where a variable is neither in the local nor the global scope. It refers to the scope of the enclosing function.

```python
def outer_function():
    enclosing_var = "Python"

    def inner_function():
        nonlocal enclosing_var  # Referencing the enclosing scope variable
        enclosing_var = "Coding"

    inner_function()
    print(enclosing_var)  # Prints "Coding"

outer_function()
```

## Mutable Default Arguments

A common pitfall in Python is using mutable default arguments in functions. Let's see why it's problematic:

```python
def append_to_list(element, my_list=[]):
    my_list.append(element)
    return my_list

print(append_to_list(1))  # Expected: [1], Actual: [1]
print(append_to_list(2))  # Expected: [2], Actual: [1, 2]
```

In this example, the list my_list is created only once when the function is defined, not each time it's called. As a result, every time you call the function, you're modifying the same list. This behavior can lead to unexpected results and bugs.

### How to Avoid This Issue

To avoid this issue, use None as the default argument and then initialize the mutable object inside the function:

```python
def append_to_list(element, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(element)
    return my_list

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [2], not [1, 2]
```

This way, a new list is created every time the function is called, unless an existing list is explicitly passed as an argument.

## Optional Type Over None

In Python, using None as a default argument is a common practice to avoid mutable default argument issues. However, a more explicit and self-documenting approach is to use the `Optional` type from the `typing` module. This is particularly useful in type-annotated code.

```python
from typing import List, Optional

def append_to_element(element, my_list: Optional[List] = None):
    if my_list is None:
        my_list = []
    my_list.append(element)
    return my_list
```

Using `Optional[List]` as the type hint explicitly indicates that the function accepts either a `List` or `None`. This makes the code more readable and maintainable, especially in larger codebases or when working with teams.