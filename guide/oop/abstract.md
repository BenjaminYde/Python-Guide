# Abstract

Abstract classes in Python are a way to define a class that cannot be instantiated on its own and is intended to serve as a base class for other classes. They are particularly useful for defining a common interface for a set of subclasses.

## Abstract Methods

Abstract methods are declared with the @abstractmethod decorator. A class containing one or more abstract methods cannot be instantiated. Instead, any subclass of this class must override all its abstract methods before an instance of the subclass can be created.

Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# rect = Rectangle(3, 4)  # This will work
# shape = Shape()         # This will raise an error
```

## Abstract Properties

Abstract properties work similarly to abstract methods but for class properties. They are defined using the @property decorator in combination with @abstractmethod.

Example:

```python
class MyAbstractClass(ABC):

    @property
    @abstractmethod
    def my_abstract_property(self):
        pass
```

## Abstract Classes

To make a class abstract in Python, you need to follow these steps:

1. **Import ABC and abstractmethod**: Import the ABC class and the abstractmethod decorator from the abc (Abstract Base Classes) module. This module provides the infrastructure for defining abstract base classes.

1. **Inherit from ABC**: Your class should inherit from the ABC class. This makes your class an abstract base class.

1. **Define Abstract Methods**: Use the @abstractmethod decorator to define abstract methods in your class. These methods should have a declaration but no implementation. Subclasses of your abstract class will be required to implement these methods.

Example:

```python
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    
    @abstractmethod
    def my_abstract_method(self):
        """Method documentation."""
        pass

    @abstractmethod
    def another_abstract_method(self, arg1, arg2):
        """Another method documentation."""
        pass
```

In this example, MyAbstractClass is an abstract base class with two abstract methods my_abstract_method and another_abstract_method. Any subclass of MyAbstractClass will have to provide implementations for these methods.

Here's an example of a subclass implementing the abstract methods:

```python
class ConcreteClass(MyAbstractClass):
    
    def my_abstract_method(self):
        print("Implementation of the first method.")

    def another_abstract_method(self, arg1, arg2):
        print(f"Implementation of the second method with {arg1} and {arg2}.")
```

## Specify override explicitly

The overrides package in Python provides a way to explicitly mark methods as overrides of methods in a superclass.
This package helps to ensure that your method overrides are correct and intentional. 

### How overrides Works

- **@override Decorator**: The @override decorator is used to explicitly indicate that a method in a subclass is intended to override a method in the superclass.

- **Signature Checking**: When you use @override, it checks that the decorated method actually overrides some method in the superclass. It also checks that the method signatures are compatible (i.e., they should match in terms of arguments and return types).

- **Error Raising**: If a method marked with @override does not override any method in the superclass, or if there is a signature mismatch, the overrides package will raise an error.

Example:

```python
from overrides import override

class SuperClass:

    def foo(self):
        """This docstring will be inherited by any method that overrides this!"""
        return 1

    def bar(self, x) -> str:
        return x

class SubClass(SuperClass):

    @override
    def foo(self):
        return 2

    @override
    def bar(self, y) -> int:  # Raises, because the signature is not compatible.
        return y

    @override
    def zoo(self):  # Raises, because does not exist in the super class.
        return "foobarzoo"
```

### Python 3.12 overrides

As of **python 3.12** (release date fall 2023) this can be done.

Example:

```python
from typing import override

class Parent:
    def foo(self) -> int:
        return 1

    def bar(self, x: str) -> str:
        return x

class Child(Parent):
    @override
    def foo(self) -> int:
        return 2

    @override
    def baz() -> int:  # Type check error: no matching signature in ancestor
        return 1
```