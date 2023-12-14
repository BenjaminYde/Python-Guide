# Mapping

## What is Mapping?

The `Mapping` type, part of Python's `typing` module, is a generic container type used to represent objects that map keys to values. It's an important concept in type hinting and is used to ensure that function arguments and return types conform to expected data structures.

To use `Mapping`, you must first import it:

```python
from typing import Mapping
```

## Basic Usage

The `Mapping` type can be used as a type hint to indicate that a function parameter or return type is expected to be a mapping of keys to values.

Example:

```python
def process_data(data: Mapping[str, int]) -> None:
    # process the data here
    ...
```

## Key Characteristics

- **Immutability**: Unlike dictionaries, Mapping is typically used to represent immutable mappings. This means that once a Mapping object is created, it cannot be altered.

- **Generics**: Mapping is a generic type, meaning it can be parameterized with other types. For example, Mapping[str, int] represents a mapping with string keys and integer values.

- **Subtyping**: Mapping is considered a more abstract type than dict. This means that while a dict can be used wherever a Mapping is expected, the reverse is not necessarily true.

- **Methods**: Mapping includes several methods such as keys(), values(), and items() similar to a dictionary.

### Example 1: ReadOnly Parameter

```python
def display_student_data(student_data: Mapping[str, str]) -> None:
    for key, value in student_data.items():
        print(f"{key}: {value}")
```

### Example 2: ReadOnly Parameters and Mutable Output

```python
def merge_mappings(map1: Mapping[int, str], map2: Mapping[int, str]) -> dict:
    merged = {**map1, **map2}
    return merged
```