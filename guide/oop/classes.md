# Object Oriented Programming (OOP)

Python is a multiparadigm programming language that supports object-oriented programming (OOP) through classes that you can define with the `class` keyword. You can think of a class as a piece of code that specifies the **data** and **behavior** that represent and model a particular type of object.

## What is a class?

A class in Python can be likened to a blueprint for a car. This blueprint outlines the fundamental structure and capabilities that every car built from this blueprint will possess. Just as multiple cars can be manufactured from the same blueprint, in Python, a class allows for the creation of numerous objects, each an instance of that class.

Each car instance can have unique properties. Additionally, each car can perform various behaviors like starting the engine, honking, or accelerating, illustrating the diverse functionalities of different car instances. These properties carry what’s commonly known as the object’s state.

### Attributes and Methods

- **Attributes (Properties)**: These are akin to the characteristics or features of a car. In Python, attributes are variables defined within a class to store data. For a Car class, attributes might include color, brand, model, and horsepower.

- **Methods (Behaviors)**: Methods represent the actions or functions that a car can perform, akin to functions within a class. For the Car class, methods might include start_engine(), accelerate(), brake(), and turn(). These methods define what a car can do and often interact with the car's attributes.

## Benefits of Using OOP

- **Modularity**: OOP in Python promotes modularity, allowing complex problems to be broken down into smaller, more manageable parts (objects).

- **Reusability**: Through classes, Python allows the creation of reusable code. Once a class is written, it can be used to create multiple objects.
 
- **Encapsulation**: Python classes encapsulate data and functions that operate on that data, hiding the internal workings of objects from the outside world.

- **Inheritance**: Classes can inherit capabilities from other classes, leading to code reuse and reduction of redundancy.

- **Polymorphism**: OOP in Python enables defining methods in the child class with the same name as defined in their parent class. This allows the implementation to vary while the interface remains consistent.

## References

- [PythonDocs](https://docs.python.org/3/tutorial/classes.html)
- [RealPython](https://realpython.com/python-classes/)