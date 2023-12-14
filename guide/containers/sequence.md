# Sequence

## What is Sequence?

The `Sequence` type in Python's `typing` module is used for type hinting in situations where an ordered collection of items is expected. It's a step towards more precise and readable code, especially when dealing with functions or methods that operate on sequences like lists, tuples, or strings.

To use `Sequence`, you must first import it:

```python
from typing import Sequence
```

## Basic Usage

`Sequence` serves as a type hint to indicate that a function parameter, variable, or return type should be a sequence.

Example:

```python
def process_items(items: Sequence[int]) -> None:
    # process the sequence of items here
    ...
```

## Key Characteristics

- **Immutability**: `Sequence` is typically used to represent immutable sequences. While you can iterate over and access elements in a `Sequence`, modifying it is not allowed.

- **Generics**: As a generic type, `Sequence` can be parameterized with other types, such as` Sequence[str]` for a sequence of strings.

- **Subtyping**: A `Sequence` is more abstract than specific sequence types like `list` or `tuple`. This means a `list` or `tuple` can be used where a `Sequence` is expected, but not vice versa.

- **Common Methods**: Methods such as `__getitem__`, `__len__`, `__contains__`, index, and count are part of the Sequence interface.

### Example 1: ReadOnly Parameter

```python
def sum_sequence(numbers: Sequence[float]) -> float:
    return sum(numbers)
```

### Example 2: ReadOnly Parameter and Mutable Output

```python
def concatenate_strings(strings: Sequence[str]) -> str:
    return ''.join(strings)
```