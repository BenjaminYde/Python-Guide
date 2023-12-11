# Namespaces

Namespaces in Python are crucial for structuring and organizing the code. They play a vital role in variable naming and avoiding naming conflicts. Understanding namespaces helps in grasping the scope of variables and functions in Python.

## What are Namespaces?

A namespace in Python is a collection that maps names to objects (such as variables and functions). Different namespaces can co-exist without any interference and Python implements these as dictionaries.

## Types of Namespaces

- **Local Namespace**: Includes local names inside a function. This namespace is created when a function is called and lasts until the function returns.

- **Enclosing Namespace**: Specific to nested functions, where the local namespace of the enclosing function is the enclosing namespace for the nested function.

- **Global Namespace**: Includes names from various imported modules you are using in a script. This namespace is created when the module is included in the script, typically at the start of the script.

- **Built-in Namespace**: Includes built-in functions and built-in exception names. This namespace is created when the Python interpreter starts up and is available as long as the interpreter is running.

## Namespace Example

Here's an example to illustrate different namespaces:

```python
import math

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =', a)  # Local Namespace

    inner_function()
    print('a =', a)  # Enclosing Namespace

a = 10
outer_function()
print('a =', a)  # Global Namespace
print('pi =', math.pi)  # Built-in Namespace

# output: 'a = 30', 'a = 20', 'a = 10', 'pi = 3.141592653589793'
```

## Modifying the Global and Nonlocal Namespaces

**Global Namespace**: The global keyword is used to modify a global variable inside a function.

```python
x = "global"

def change_global():
    global x
    x = "changed"

print(x)  # "output: global"
change_global()
print(x)  # "output: changed"
```

**Nonlocal Namespace**: The nonlocal keyword is used in nested functions to refer to variables in the nearest enclosing scope.

```python
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
    inner()
    print(x)  # "output: nonlocal"

outer()
```