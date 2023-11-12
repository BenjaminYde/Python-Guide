# Looping and Iterating

Python offers various ways to loop and iterate over elements, making it highly efficient and readable for traversing through data structures like lists, tuples, dictionaries, and sets. This document explores the different methods and nuances associated with looping and iterating in Python.

## The 'while' Loop

In Python, while loops are used for repeated execution as long as an expression is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## The 'for' Loop

The for loop in Python is used for iterating over a sequence (like a list, tuple, set, or string) or other iterable objects. The basic syntax is as follows:

```python
for element in sequence:
    # Do something with element
```

### Iterating Over Lists

```python
myList = [1, 2, 3, 4, 5]
for number in myList:
    print(number)
```

### Iterating Over Strings

```python
for char in "Hello":
    print(char)
```

### Nested Loops

Python allows using one loop inside another loop.

```python
for i in range(1, 4):  # Outer loop
    for j in range(i):  # Inner loop
        print(i, end=" ")
    print()
```


## Loop Control Statements

Loop control statements change the execution from its normal sequence.

**break Statement**

Terminates the loop and transfers execution to the statement immediately following the loop.

```python
for number in myList:
    if number == 3:
        break
    print(number)
```

**continue Statement**

Causes the loop to skip the remainder of its body and immediately retest its condition.

```python
for number in myList:
    if number == 3:
        continue
    print(number)
```

**pass Statement**

The pass statement is a null operation; nothing happens when it executes. It's used as a placeholder.

```python
for number in myList:
    if number == 3:
        pass
    print(number)
```

## The range() Function

`range()` is used to generate a sequence of numbers, often used in for loops.

```python
for i in range(5):  # Generates numbers from 0 to 4
    print(i)
```

**Specifying Start, Stop, and Step**

```python
for i in range(2, 10, 2):  # Starts at 2, stops before 10, steps by 2
    print(i)
```

## Iterating With Index

**Using enumerate()**

Sometimes it's useful to have access to the indices of the values when iterating.

```python
for index, value in enumerate(myList):
    print(index, value)
```
## Iterating Over Multiple Lists

**Using zip()**

zip() is used to iterate over two or more lists in parallel.

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for number, letter in zip(list1, list2):
    print(number, letter)
```