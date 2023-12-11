# Modules

## What is a Module?

A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix .py added. Modules in Python serve as a way to organize code logically by grouping related functions, classes, and variables.

## Creating a Module

Creating a module is as simple as writing Python code and saving it with a .py extension. For example, a file named my_module.py contains:

```python
# my_module.py
def greeting(name):
    return f"Hello, {name}"
```

## Importing Modules

You can use any Python file as a module by executing an import statement in another Python script or interpreter session. If my_module.py is in the same directory as your script, you can import it directly.

```python
import my_module
print(my_module.greeting("Alice"))
```

## Import with Alias

You can import a module with an alias using the as keyword. This is often used for modules with longer names.

```python
import my_module as mm
print(mm.greeting("Bob"))
```

## Importing Specific Items

To import specific functions, classes, or variables from a module:

```python
from my_module import greeting
print(greeting("Charlie"))
```

## Importing All Names (not recommended)

You can import all names (functions, variables, classes) from a module using *. This is generally discouraged as it can lead to unclear code.

```python
from my_module import *
print(greeting("Dave"))
```

## The Module Search Path

When a module is imported, Python searches for the module in a list of directories given by the variable sys.path. The search order is:

- The directory containing the input script (or the current directory).
- PYTHONPATH environment variable (a list of directory names, with the same syntax as the shell variable PATH).
- The installation-dependent default (like /usr/local/lib/python).

## Compiled Python Files

To speed up loading modules, Python caches the compiled version of each module in the `__pycache__` directory under the name `module.version.pyc`, where "version" encodes the format of the compiled file.

## Reloading a Module

The reload() function in the importlib module can be used to reload a previously imported module. This is useful if you have made changes to the module's source code and want to test these changes without restarting the interpreter.

```python
from importlib import reload
reload(my_module)
```