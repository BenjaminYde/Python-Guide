# Enum

## Introduction

Enum, short for enumeration, is a data type in Python that enables the creation of named constant values. Introduced in Python 3.4 with the enum module, it allows for the creation of symbolically named values which are immutable and unique.

## Why Use Enum?

- **Readability**: Enums make code more readable and expressive by using meaningful names instead of magic numbers or strings.
- **Uniqueness**: Each Enum member is distinct and cannot be duplicated, reducing errors from using identical values for different constants.
- **Immutable**: Enum members are immutable, ensuring consistency throughout the code.

## Basic Usage

### Creating an Enum:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

### Accessing Enum Members:

```python
my_color = Color.RED
print(my_color)  # Output: Color.RED
```

### Comparison:

```python
if favorite_color is Color.RED:
    print("It's red!")
```

### Iteration:

```python
for color in Color:
    print(color)
```

### name & value Property

- The `name` property of an Enum member returns the name of the member as it is defined in the Enum class.
- The `value` property returns the value assigned to the enum member.

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.name)   # Output: 'RED'
print(Color.RED.value)  # Output: 1
```

The Enum class provides a special method `__getitem__` that allows you to access the members of the enum by passing the name of the member as a string inside square brackets `[]`. This is similar to how you would access the value of a dictionary by key.

```python
print(Color['RED'])   # This is valid and returns Color.RED
print(Color['red'])   # This raises KeyError
```

## Basic Customization

In the simplest form, customizing values in an Enum involves directly assigning unique values to each member. These values can be of any data type – numbers, strings, tuples, objects, etc.

Using strings:

```python
from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
```

Using dictionary:

```python
from enum import Enum

class Status(Enum):
    ACTIVE = {'my_cool_id': 1, 'description': 'The entity is active'}
    INACTIVE = {'my_cool_id': 2, 'description': 'The entity is inactive'}

status_code = Status.ACTIVE.value['my_cool_id']
status_description = Status.ACTIVE.value['description']

print(f"Code: {status_code}, Description: {status_description}")
# Output: Code: 1, Description: The entity is active
```

Using Functions:

```python
class Weekday(Enum):
    MONDAY = (lambda x: x**2)(1)
    TUESDAY = (lambda x: x**2)(2)
    # And so on...
```

## Custom Value Methods

You can define methods in the Enum class to interact with the custom values. For instance, if you have complex data types as values, you might want methods to access or manipulate these data.

```python
class Planet(Enum):
    MERCURY = (1, 'Mercury')
    VENUS = (2, 'Venus')
    EARTH = (3, 'Earth')

    def __init__(self, planet_id, name):
        self.planet_id = planet_id
        self.name = name

    def get_info(self):
        return f"{self.name} (ID: {self.planet_id})"
```

## Auto-Assigning Values:

Python's `auto()` function can be used to automatically generate values for each Enum member. This is useful when the specific values are not important, and you just need unique identifiers for each member.

```python
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
```

## All Enum Types

### Enum

This is the basic Enum type. It's used to create enumerations, which are sets of symbolic names bound to unique, constant values.

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

### IntEnum

This is a specialized enumeration that inherits from both Enum and int. The members of an `IntEnum` are also instances of int. It's useful when you need integer constants that should behave as enumeration members.

```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
```

### IntFlag

An extension of `IntEnum`, used for creating enumerations that can be combined using bitwise operations. It's particularly useful for sets of integer flags.

```python
from enum import IntFlag

class Permissions(IntFlag):
    READ = 1
    WRITE = 2
    EXECUTE = 4
```


#### Flag

Similar to `IntFlag`, but not limited to integers. `Flag` members can be combined using bitwise operations and do not have to be integers.

```python
from enum import Flag, auto

class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    MAGENTA = RED | BLUE
```

### StrEnum (Python 3.11+)

`StrEnum` is a variant of Enum where members are also instances of str. This is useful when the members need to behave as strings.

```python
from enum import StrEnum

class Mood(StrEnum):
    HAPPY = 'happy'
    SAD = 'sad'
    ANGRY = 'angry'
```

## `_missing_` Function

Enum member names are always case-sensitive, which is by design to avoid confusion and to ensure that each member is distinctly identifiable. If you need to be able to access enum members without worrying about case sensitivity, you can implement the `_missing_` method for looking up values not found in `cls`. By default it does nothing, but can be overridden to implement custom search behavior:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
    @classmethod
    def _missing_(cls, name):
        for member in cls:
            if member.name.lower() == name.lower():
                return member
        # Raise a ValueError to indicate that there is no member with the given name.
        raise ValueError(f"No member found for {name}")

# Now you can access enum members case-insensitively:
print(Color("RED"))   # Color.RED
print(Color("red"))   # Color.RED
print(Color("Green")) # Color.GREEN
print(Color("blue"))  # Color.BLUE
```

## Enum Decorators

### The @unique Decorator

The `@unique` decorator is used to ensure that all the values in an enumeration are unique; it will raise a ValueError if any value is repeated.

```python
from enum import Enum, unique

@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # REPEAT = 1  # Uncommenting this line will raise a ValueError.
```

### Custom Verification Decorator (Python 3.11+)

While Python's enum doesn't provide a `@verify` decorator, you could create your own custom decorator to verify other properties of the enum members. For instance, you might want to ensure that all enum values adhere to a certain format or constraint.

Here's an example of how you might create a custom decorator to verify that all enum values are uppercase:

```python
from enum import Enum

def verify_uppercase(enum_class):
    for name, member in enum_class.__members__.items():
        if name.upper() != name:
            raise ValueError(f"Enum name {name} must be uppercase!")
    return enum_class

@verify_uppercase
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # lowercase = 4  # Uncommenting this line will raise a ValueError.
```