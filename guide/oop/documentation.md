# Documentation

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