# Generics

## What are Generics?

Generics are powerful tools in Python, allowing for the creation of flexible and reusable components. By using generics, you can write code that is type-agnostic, meaning it can operate on various data types. This enhances code maintainability and reduces the need for repetitive code.

### Type Variables

**Type Variables**: A type variable is created using the TypeVar class from the typing module. It acts as a placeholder for any type:

```python
from typing import TypeVar

T = TypeVar('T')  # The string 'T' identifies this type variable

```

Here, `T` is a generic type variable that can represent any type.

Passing a string to TypeVar in Python serves several purposes, mainly related to readability and the functioning of static type checkers. When you define a type variable using TypeVar, the string argument you provide is essentially the name of the type variable. This practice stems from Python's dynamic nature and its approach to handling types, especially in the context of type hinting and static type analysis

### Why Use Generics?

- **Flexibility**: They allow you to write functions and classes that can work with various data types.
- **Type Safety**: Despite the flexibility, they help in catching type-related errors at development time, which is especially useful in large codebases.
- **Code Reusability**: Promote writing more generic and reusable code, reducing redundancy.


Python is a dynamically typed language, and the type system in Python, including the use of generics and TypeVar, is part of its type hinting functionality. This system is designed for use by static type checkers, like `mypy`, to catch type-related issues at development time, rather than at runtime.

## Generic Functions

Generic functions are those that can operate with different types, as defined by their type variables. For example:

```python
from typing import TypeVar

T = TypeVar('T')

def identity(value: T) -> T:
    return value
```
Here, identity is a generic function that can accept and return a value of any type.

The following example creates a function that merges two lists regardless of their element types. This demonstrates how generics can be used to create functions that work with multiple types in a type-safe way.

```python
from typing import TypeVar, List

T = TypeVar('T')

def merge_lists(list1: List[T], list2: List[T]) -> List[T]:
    return list1 + list2

# Usage
numbers = merge_lists([1, 2, 3], [4, 5])
strings = merge_lists(["apple", "banana"], ["cherry"])
```
This merge_lists function can now work with lists of any type (int, str, etc.), while still being type-safe.

## Generic Classes

Now consider a KeyValueStore class. This class will store key-value pairs where both the keys and values can be of any type. This is useful for creating a type-safe map-like structure.

```python
from typing import Generic, TypeVar, Dict

K = TypeVar('K')
V = TypeVar('V')

class KeyValueStore(Generic[K, V]):
    def __init__(self):
        self.store: Dict[K, V] = {}

    def set_item(self, key: K, value: V):
        self.store[key] = value

    def get_item(self, key: K) -> V:
        return self.store[key]

    def remove_item(self, key: K):
        if key in self.store:
            del self.store[key]

# Usage
store = KeyValueStore[str, int]()
store.set_item("age", 25)
print(store.get_item("age"))  # Outputs: 25
```

This KeyValueStore class is a versatile data structure that can adapt to various types of keys and values, showcasing the power of generics in creating flexible and reusable components.

## Multiple Types in TypeVar

When you create a TypeVar with multiple types, it means that the type variable is restricted to being one of those types. This makes the intended use of the function or class more explicit, which can be particularly useful for those who will use or maintain your code.

Example:

```python
from typing import TypeVar

T = TypeVar("T", int, float)
```

In this case, `T` is a type variable that can be either an int or a float.

### Practical Usage

This feature allows for more controlled generic programming. You can define functions, methods, or classes that are generic but within a specific set of types. 

Example:

```python
def add(a: T, b: T) -> T:
    return a + b

# This is valid
result1 = add(1, 2)
result2 = add(3.5, 4.5)

# This would typically raise a type hinting error
# result3 = add("string1", "string2")
```

In the add function, the type of a and b is restricted to either `int` or `float`. This allows the function to be somewhat generic (working with both integers and floats) but still maintains type safety by not allowing other types like `str`.

## Bound in TypeVar

The `bound` argument in `TypeVar` is used to specify an upper bound for the type variable. This means the type variable must be a subtype of the specified bound.

Example:

```python
from typing import TypeVar, Generic

class Animal:
    pass

class Dog(Animal):
    pass

T = TypeVar('T', bound=Animal)

class Shelter(Generic[T]):
    pass

# Shelter can be of type Animal or any subclass of Animal
dog_shelter = Shelter[Dog]()
```

**Implication**: By setting a bound, you restrict the generic type to the bound class or its subclasses, enhancing type safety.


## Invariance, Covariant, Contravariant

### Invariance

- When both `covariant` and `contravariant` are set to `False`, the `TypeVar` is considered invariant
- This is considered **default** behaviour when creating a `TypeVar`.
- **Invariance** means that you cannot substitute a type variable with its subtype or supertype. A generic class with an invariant type variable will only accept that specific type.

Example:

```python
from typing import TypeVar, Generic

T = TypeVar('T')  # Invariant by default

class Container(Generic[T]):
    pass

class Animal:
    pass

class Dog(Animal):
    pass

animal_container = Container[Animal]()
dog_container = Container[Dog]()

# The following assignment is invalid with invariant TypeVars:
# animal_container = dog_container  # Type error! (mypy)
```

### Covariant

In a **covariant** situation, if `Dog` is a subtype of `Animal`, then `Container[Dog]` is a subtype of `Container[Animal]`. This is intuitive and aligns with how we typically think about inheritance and subtypes.

#### Example (part 1): base setup

```python
from typing import TypeVar, Generic

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Define a covariant TypeVar
T_co = TypeVar('T_co', covariant=True)

# A read-only container that is covariant in its type parameter
class Container(Generic[T_co]):
    def __init__(self, item: T_co):
        self._item = item

    def get_item(self) -> T_co:
        return self._item

```

#### Example (part 2): display animal

```python
def display_animal(animal_container: Container[Animal]):
    print(animal_container.get_item())

# Correct Usage
dog_container = Container[Dog](Dog())
display_animal(dog_container) # OK, Container[Dog] is acceptable for Container[Animal]

# Correct Usage
cat_container = Container[Cat](Cat())
display_animal(cat_container)  # OK, Container[Cat] is acceptable for Container[Animal]
```

#### Example (part 3): display dog

```python
def display_dog(dog_container: Container[Dog]):
    print(f"Displaying Dog: {dog_container.get_item()}")

# Correct Usage
dog_container = Container[Dog](Dog())
display_dog(dog_container)  # OK, using Container[Dog] where Container[Dog] is expected

# Incorrect Usage
animal_container = Container[Animal](Animal())
# The following line would raise a type error with static type checkers,
# but not at runtime in Python
display_dog(animal_container) # Not OK, using Container[Animal] where Container[Dog] is expected

# Incorrect Usage
cat_container = Container[Cat](Cat())
# The following line would also raise a type error with static type checkers
display_dog(cat_container) # Not OK, using Container[Cat] where Container[Dog] is expected
```

#### Conclusion

In a covariant situation, while you can use a `Container[Dog]` where a `Container[Animal]` is expected (due to `Dog` being a subtype of `Animal`), you cannot use a `Container[Animal]` or `Container[Cat]` where a `Container[Dog]` is specifically expected. This is a key distinction in understanding and applying covariance correctly.

### Contravariant

In a **contravariant** situation, it's the reverse. If `Dog` is a subtype of `Animal`, then `Consumer[Animal]` is a subtype of `Consumer[Dog]`. This means a consumer of `Animal` can also consume `Dog`, but not necessarily vice versa.

#### Example (part 1): base setup

```python
from typing import TypeVar, Generic

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Define a contravariant TypeVar
T_contra = TypeVar('T_contra', contravariant=True)

# A handler that is contravariant in its type parameter
class Handler(Generic[T_contra]):
    def handle(self, animal: T_contra) -> str:
        return f"Handling {type(animal).__name__}"
```

#### Example (part 2): handle animal

```python
def handle_animal(handler: Handler[Animal]):
    print(handler.handle(Animal()))

# Correct Usage
dog_handler = Handler[Dog]()
handle_animal(dog_handler)  # OK, Handler[Dog] is acceptable for Handler[Animal]

# Correct Usage
cat_handler = Handler[Cat]()
handle_animal(cat_handler)  # OK, Handler[Cat] is acceptable for Handler[Animal]

```

#### Example (part 2): train a dog

```python
def train_dog(dog_handler: Handler[Dog]):
    print(dog_handler.handle(Dog()))

# Correct Usage (train dog using animal), dog is super of animal
animal_handler = Handler[Animal]()
train_dog(animal_handler) # OK, Handler[Animal] can be used for Handler[Dog]

# Incorrect Usage (train dog using cat), dog is not super of animal
cat_handler = Handler[Cat]()
train_dog(cat_handler) # Not OK, Handler[Cat] can't handle Dog
```

Contravariance is typically used in scenarios where you have a producer of data (covariance) and a consumer of data (contravariance).
