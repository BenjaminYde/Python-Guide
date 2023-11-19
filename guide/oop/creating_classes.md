# Creating Classes

## Syntax for Class Definition
In Python, a class is defined using the class keyword, followed by the class name and a colon. The class name typically follows the CapWords convention. Here’s a basic example:

```python
class Car:
    # class body
```

## Class Attributes and Methods

- **Class Attributes**: These are variables that are shared by all instances of a class. They are defined within the class but outside of any methods. Class attributes are used for data that is common to all instances.

```python
class Car:
    wheels = 4  # Class attribute
```

- **Class Methods**: Methods are functions defined within the class. They describe the behaviors that instances of the class can perform.

```python
class Car:
    def start_engine(self):
        print("Engine started")
```

## The `__init__` Method (Constructor)

The `__init__` method in Python is a special method that is automatically called when a new instance of a class is created. It is used to initialize the instance.

- **self Parameter**: The first parameter of `__init__` (and typically all instance methods) is self, which refers to the instance being created.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
```

## Creating an Instance of a Class

To create an instance of a class, you simply call the class as if it were a function, passing the arguments that its `__init__` method expect

```python
my_car = Car("Toyota", "Corolla")
```

## Instance Variables vs. Class Variables

- **Instance Variables**: These are variables that are unique to each instance of a class. They are typically defined within methods, using the self parameter. Each instance has its own copy of instance variables.

```python
class Car:
    def __init__(self, make, model):
        self.make = make  # Instance variable
        self.model = model  # Instance variable
```

- **Class Variables**: In contrast, class variables are shared by all instances of the class. They are defined at the class level, outside of any methods.

```python
class Car:
    wheels = 4  # Class variable

    def __init__(self, make, model):
        self.make = make
        self.model = model
```

## Creating Methods in a Class

Methods in a class need the self parameter to access and modify the instance's attributes.      
`self` refers to the current instance of the class.

```python
class Car:
    # ...

    def display_info(self):
        """Prints information about the car."""
        print(f"This is a {self.make} {self.model}.")s
```

Attributes of an instance can be accessed and modified using the dot notation. This is done using the `self` keyword within class methods.

```python
class Car:
    # ...

    def update_model(self, new_model):
        """Updates the car's model."""
        self.model = new_model
```

## Documentation

In Python, documenting a class is done using docstrings, which are multiline strings enclosed in triple quotes. Docstrings provide a convenient way of associating documentation with Python code.

```python
class Car:
    """
    Class representing a car.

    Attributes:
        wheels (int): Number of wheels the car has.
        make (str): The manufacturer of the car.
        model (str): The model of the car.
    """

    wheels = 4

    def __init__(self, make, model):
        """
        Initialize a new Car instance.

        Parameters:
            make (str): The manufacturer of the car.
            model (str): The model of the car.
        """
        self.make = make
        self.model = model
```

## References

- [PythonDocs](https://docs.python.org/3/tutorial/classes.html)
- [RealPython](https://realpython.com/python-classes/)