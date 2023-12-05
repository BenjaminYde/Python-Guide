# Properties

Property decorators in Python provide a way to use getters, setters, and deleters in an object-oriented fashion. This approach allows for controlled access to class attributes, ensuring encapsulation and offering additional functionality like validation and automatic calculations.

## `@property`

The `@property` decorator turns a method into a 'getter' for a class attribute. This allows the method to be accessed like an attribute, without the need to call it like a function.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
```

## `@property.setter`

The `@property.setter` decorator is used alongside @property. It defines a method that acts as the setter for a property, allowing for additional logic (like validation) when a property's value is set.

```python
class MyClass:
    # ...

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be positive")
        self._value = new_value
```

## `@property.deleter`

The `@property.deleter` decorator allows you to define custom behavior when a property is deleted with the `del` statement.

```python
class MyClass:
    # ...

    @value.deleter
    def value(self):
        print("Value is being deleted")
        del self._value
```

## Full Example

Here is a complete example of a class using all three decorators:

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be positive")
        self._value = new_value

    @value.deleter
    def value(self):
        print("Value is being deleted")
        del self._value

# Usage
obj = MyClass(10)
print(obj.value)  # Getter
obj.value = 20    # Setter
del obj.value     # Deleter
```