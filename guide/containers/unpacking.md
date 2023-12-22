# Unpacking

The asterisk `*`, known as the unpacking operator in Python, is used to unpack iterable objects into individual elements. This operator can be extremely useful in various scenarios, such as function calls, where you have an iterable (like a list or tuple) and you want to pass its elements as separate arguments to a function. Let's explore this concept in more detail.

## List Unpacking with *

### Unpacking In Function Arguments:

When you put `*` before an iterable in a function call, Python unpacks its elements and passes them as individual arguments to the function.

Example:

```python
def sum_numbers(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

# Unpacking list into function arguments
result = sum_numbers(*numbers)
print(result)  # Output: 6
```

In this example, `*numbers` unpacks the list `numbers` into three separate arguments, which are then passed to the `sum_numbers` function.

### Unpacking In Assignments:

```python
first, *rest = [1, 2, 3, 4]
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4]
```

In this case, `first` gets the first element of the list, and `*rest` gets the rest of the list.

### ### Unpacking In Merging Lists:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = [*list1, *list2]
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]
```

Here, `*` is used to merge two lists into a new list.

### Unpacking and Argument Passing

In the context of argument passing (like in your asyncio.gather example), the `*` operator allows a flexible way to call functions with a variable number of arguments:

```python
def print_args(*args):
    for arg in args:
        print(arg)

values = [1, 2, 3, 4]
print_args(*values)
```

This code will print each number in `values` on a new line. The `*values` in the function call unpacks the list, and `*args` in the function definition allows the function to accept any number of positional arguments.

## Dictionary Unpacking with **

The double asterisk `**` in Python is known as the dictionary unpacking operator. Just like the single asterisk `*` unpacks iterable objects like lists and tuples, the `**` operator is used to unpack dictionaries into named arguments when calling a function. This feature is particularly useful when you have a dictionary and you want to pass its key-value pairs as keyword arguments to a function.

### Unpacking In Function Arguments:

When you use `**` before a dictionary in a function call, Python unpacks its key-value pairs and passes them as keyword arguments to the function.

Example of Dictionary Unpacking:

```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

person = {"first_name": "John", "last_name": "Doe"}

# Unpacking dictionary into function arguments
greet(**person)
```

In this example, `**person` unpacks the person dictionary into two separate keyword arguments, `first_name` and `last_name`, which are then passed to the greet function.

### Unpacking In Function Arguments:

You can also use `**` to merge dictionaries. This is particularly useful in Python 3.5 and later:

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Unpacking In Function Definitions:

The `**` operator can also be used in function definitions to allow for an arbitrary number of keyword arguments:

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30)
```

This function will print each key and value passed as keyword arguments.