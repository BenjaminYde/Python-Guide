# Final

`Final` is used in type hinting to indicate that a particular variable, class, or method should not be overridden or changed. It serves as a way to enforce certain aspects of the design of your code.

## Final Variables

A variable annotated with `Final` indicates that its value should not be reassigned.

```python
from typing import Final

MAX_SIZE: Final[int] = 100
```

## Final Methods

When you annotate a method with `Final`, it indicates that the method should not be overridden in subclasses.

```python
from typing import final

class Base:
    @final
    def my_method(self):
        print("This method should not be overridden.")
```

## Final Classes

`Final` can also be used on classes to indicate that they should not be subclassed.

```python
from typing import final

@final
class MyFinalClass:
    pass
```