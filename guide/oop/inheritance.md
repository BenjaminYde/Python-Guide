# Inheritance

## Introduction to Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and methods from another class. 
This promotes code reusability and establishes a relationship between classes. 
In Python, inheritance is implemented by defining a new class that receives attributes and methods from an existing class.

## Base Class and Derived Class

- **Base Class (Parent Class)**: The class whose properties and methods are inherited.
- **Derived Class (Child Class)**: The class that inherits from the base class.

Example: 

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
```

Here, `Dog` is a derived class that inherits from the `Animal` base class.

## Types of Inheritance

- **Single Inheritance**: When a child class inherits from only one parent class.
- **Multiple Inheritance**: When a child class inherits from multiple parent classes.
- **Multilevel Inheritance**: A form of inheritance in which a class is derived from a base class, which in turn is derived from another base class.
- **Hierarchical Inheritance**: Multiple classes inherit from a single parent class.

Example:

```python
class Father:
    def gardening(self):
        return "I enjoy gardening"

class Mother:
    def cooking(self):
        return "I love cooking"

class Child(Father, Mother):
    pass

child = Child()
print(child.gardening())  # From Father
print(child.cooking())    # From Mother
```

## Overriding Methods

Inheritance allows a child class to override or modify the behavior of methods defined in its parent class.

Example:

```python
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

bird = Bird("Sunny")
print(bird.speak())  # Outputs: Sunny says Tweet!
```

## Super Function

super() is used to call methods from the parent class in the derived class, especially when overriding methods.

Example:

```python
class Mammal(Animal):
    def __init__(self, name, is_warm_blooded):
        super().__init__(name)
        self.is_warm_blooded = is_warm_blooded
```

## The isinstance() and issubclass() Functions

- **isinstance(object, class)**: Checks if an object is an instance of a class or a subclass thereof.
- **issubclass(class1, class2)**: Checks if class1 is a subclass of class2.

## Diamond Problem in Multiple Inheritance

The diamond problem occurs in a multiple inheritance scenario when a class inherits from two classes that both inherit from the same base class. This can create ambiguity in the method resolution order (MRO).

Example:

```python
class A:
    def method(self):
        return "A method"

class B(A):
    def method(self):
        return "B method"

class C(A):
    def method(self):
        return "C method"

class D(B, C):
    pass

d = D()
print(d.method())  # method of class B is called
```

In this scenario, Python will look at the MRO of class D to determine which method() to call. The MRO for D is determined in the order that classes are listed in its definition. So, in class D(B, C), it first looks in B, then in C, and finally in A (if the method isn't found in B or C).

Therefore, when d.method() is called, Python will use the method() from the first class in the MRO of D where it finds a matching method. In this case, it will be the method() from class B, since B is listed before C in the definition of D.