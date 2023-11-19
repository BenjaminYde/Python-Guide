# Class Methods

Class methods are methods that are bound to the class rather than its objects. They can modify the class state that applies across all instances of the class.

## Characteristics of Class Methods:

- **Bound to the Class**: Class methods take a reference to the class, cls, as their first argument. This is similar to how instance methods take self, the instance, as their first argument.
- **Decorator Used**: Class methods are defined using the `@classmethod` decorator.
- **Modifying Class State**: Since they are bound to the class, these methods can modify class state that would apply across all instances of the class.

## Class Methods To Create An Instance

Let's consider a simple Person class that can be created using a method.

```python
from datetime import date
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # Returns a Person object created by birth year.
    @classmethod
    def from_birthyear(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)
 
    def display(self):
        print("Name : ", self.name, "Age : ", self.age)

person = Person.from_birthyear('Benjamin', 1998)
person.display()
```

## No Constructor Overloading in Python

In Python, unlike some other programming languages like Java or C++, constructor overloading is not directly supported. This limitation is due to the way Python handles method overloading in general. However, Python provides alternative ways to achieve similar functionality, and one such way is through the use of class methods.

In languages that support constructor overloading, you can define multiple constructors in a class, each with a different set of parameters. Python, however, does not support this.

- Single `__init__` Method: In Python, you can only define one `__init__` method per class. If you define more than one, the last definition overrides the previous ones.

## Class Methods To Access Class Variables

Let's consider a simple Book class that keeps track of the number of books created.

```python
class Book:
    total_books = 0  # Class variable to track total books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def book_count(cls):
        return f"Total books created: {cls.total_books}"

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(Book.book_count())  # Output: Total books created: 2
```

## Class method vs Static Method

The difference between the Class method and the static method is:

- A class method takes cls as the first parameter while a static method needs no specific parameters.
- A class method can access or modify the class state while a static method can’t access or modify it.
- In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
- We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

## When to use the class or static method?

- We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
- We generally use static methods to create utility functions.