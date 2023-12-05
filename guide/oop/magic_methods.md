# Magic Methods

## What are Magic Methods?

Magic methods, also known as dunder (double underscore) methods, are special methods in Python that have double underscores at the beginning and the end of their names. They are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action. For example, when you add two numbers using the + operator, internally, the `__add__` method will be called.

## Common Magic Methods
- `__init__(self, [...])`: The constructor of the class, called when a new instance is created.
- `__str__(self)`: Returns a human-readable string representation of the object, called by the str(object) method and also used by the print function.
- `__repr__(self)`: Returns an unambiguous string representation of the object, useful for debugging. Called by the repr(object) method.
- `__add__(self, other)`: Defines the behavior of the addition + operator.
- `__sub__(self, other)`: Defines the behavior of the subtraction - operator.
- `__len__(self)`: Returns the length of the container. Called by the len(object) method.
- `__getitem__v(self, key)`: Defines the behavior of accessing an item using indexing or slicing.
- `__setitem__(self, key, value)`: Assigns a value to an item at a specific index or key.
- `__delitem__(self, key)`: Deletes an item at a specific index or key.

## Example: Implementing Magic Methods

Here is an example of how to implement some of these magic methods in our Car class:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"

    # Add more magic methods as necessary
```

In this example, __str__ returns a user-friendly string, while __repr__ returns a more formal representation suitable for debugging.

```python
my_car = Car("Toyota", "Corolla")
print(my_car)  # Calls __str__
print(repr(my_car))  # Calls __repr__
```

## Arithmetic Magic Methods
These methods allow objects to emulate numeric types through operators.

- `__add__(self, other)`: Implements addition.
- `__mul__(self, other)`: Implements multiplication.
- `__truediv__(self, other)`: Implements true division (`/`).

## Comparison Magic Methods

These methods allow objects to be compared using comparison operators.

- `__eq__(self, other)`: Implements equality (==).
- `__lt__(self, other)`: Implements less than (<).
- `__gt__(self, other)`: Implements greater than (>).

## Container Magic Methods

These methods allow objects to behave like containers.

- `__len__(self)`: Returns the length of the container.
- `__getitem__(self, key)`: Retrieves an item using the key.
- `__setitem__(self, key, value)`: Sets an item at a given key.
- `__delitem__(self, key)`: Deletes an item at a given key.

## Context Manager Magic Methods

These methods enable objects to be used in with statements.

- `__enter__(self)`
- `__exit__(self, exc_type, exc_val, exc_tb)`

Example:

```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
```

Usage:

```python
with ManagedFile('hello.txt') as f:
    f.write('hello, world!')
```

## Callable Objects

- `__call__(self, [...])`: Allows the instance to be called as a function.

Example:

```python
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x
```

Usage:

```python
add_five = Adder(5)
print(add_five(10))  # Outputs: 15
```

## Customizing Attribute Access

Customizing attribute access in Python refers to the ability to define custom behavior when getting, setting, or deleting attributes on objects. This is achieved using the magic methods `__getattr__`, `__setattr__`, and `__delattr__`. Let's delve into each of these to understand their use and impact better.

### `__getattr__(self, name)`

- **Usage**: This method is invoked when an attempt is made to access an attribute that doesn't exist in an object.

- **Purpose**: It's useful for creating objects that behave like they have more attributes than they actually do, such as for delegation or proxy objects.

- **Example**: In a class DynamicAttributes, if an attribute is not found, __getattr__ can return a default value or message.

```python
class DynamicAttributes:
    def __getattr__(self, name):
        return f"'{name}' attribute not found"

obj = DynamicAttributes()
print(obj.some_nonexistent_attribute)  # Outputs: 'some_nonexistent_attribute' attribute not found
```

### `__setattr__(self, name, value)`

- **Usage**: This method is called whenever an attribute's value is set. This includes both new and existing attributes.

- **Purpose**: It allows for validation, logging, or other side effects whenever a property is changed.

- **Caution**: Inside __setattr__, direct assignment to an attribute (e.g., self.name = value) would call __setattr__ again, causing a recursive loop. To avoid this, set the attribute directly in the instance's __dict__.

```python
class ValidatedAttributes:
    def __setattr__(self, name, value):
        if name == "age" and not isinstance(value, int):
            raise ValueError("age must be an integer")
        self.__dict__[name] = value

obj = ValidatedAttributes()
obj.age = 30  # Valid assignment
# obj.age = "thirty"  # This will raise ValueError: age must be an integer
```

### `__delattr__(self, name)`

- **Usage**: This method is invoked when an attribute is deleted using del.

- **Purpose**: It allows for cleanup activities, logging, or other actions to occur alongside the deletion of an attribute.

- **Implementation**: Similar to __setattr__, use the object's __dict__ to avoid recursive calls.

```python
class LoggedDeletion:
    def __delattr__(self, name):
        print(f"Attribute '{name}' is being deleted")
        del self.__dict__[name]

obj = LoggedDeletion()
obj.attr = 100
del obj.attr  # Outputs: Attribute 'attr' is being deleted
```