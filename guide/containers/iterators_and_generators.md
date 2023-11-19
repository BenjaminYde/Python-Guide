# Iterators and Generators

Python's approach to iteration is deeply integrated with its use of generators and iterators, providing a powerful and flexible way to process data without the overhead of loading everything into memory. This document delves into the concepts of generators and iterators, explaining their workings and showcasing their usage.

## Understanding Iterators

An iterator in Python is an object that contains a countable number of values and lets you traverse through these values, one by one. It implements two special methods, `__iter__()` and `__next__()`.

### Creating an Iterator

To demonstrate this functionality, we will instantiate a list, which is an iterable, and produce an iterator by calling the `iter()` built-in function on the list.

```python
list_instance = [1, 2, 3, 4]
print(iter(list_instance))

#prints: list_iterator object at 0x7fd946309e90>
```

Although the list by itself is not an iterator, calling the `iter()` function converts it to an iterator and returns the iterator object.

### Accessing items in an iterator

```python
# instantiate a list object
list_instance = [1, 2, 3, 4]

# convert the list to an iterator
iterator = iter(list_instance)

# return items one at a time
print(next(iterator)) # prints: 1
print(next(iterator)) # prints: 2
print(next(iterator)) # prints: 3
print(next(iterator)) # prints: 4
```

### Not all iterables are iterators:

Although the list by itself is not an iterator, calling the iter() function converts it to an iterator and returns the iterator object.

To demonstrate that not all iterables are iterators, we will instantiate the same list object and attempt to call the next() function, which is used to return the next item in an iterator.  

```python
list_instance = [1, 2, 3, 4]
print(next(list_instance))

# prints:
# --------------------------------------------------------------------
# TypeError                         Traceback (most recent call last)
# <ipython-input-2-0cb076ed2d65> in <module>()
#     3 print(iter(list_instance))
#     4
# ----> 5 print(next(list_instance))
# TypeError: 'list' object is not an iterator

```

All of the values from an iterator may be extracted at once by calling a built-in iterable data 
structure container (i.e., list(), set(), tuple()) on the iterator object to force the iterator to 
generate all its elements at once.

```python
# instantiate iterable
list_instance = [1, 2, 3, 4]

# produce an iterator from an iterable
iterator = iter(list_instance)

# convert to list and print
print(list(iterator)) # prints: [1, 2, 3, 4]
```

### Creating Custom Iterators

```python
class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current

# Using the iterator
for num in CountDown(5):
    print(num)
```

## Understanding Generators

The most expedient alternative to implementing an iterator is to use a generator. Although generators may look like ordinary Python functions, they are different. For starters, a generator object does not return items. Instead, it uses the `yield` keyword to generate items on the fly. Thus, we can say a generator is a special kind of function that leverages lazy evaluation.

### Creating Generator Functions

```python
def countdown_generator(start):
    while start > 0:
        yield start
        start -= 1

# Using the generator
for num in countdown_generator(5):
    print(num)
```

### Generator Expressions

Similar to list comprehensions, Python supports generator expressions, which allow for creating generators in a concise and memory-efficient way.

```python
squared_numbers = (x*x for x in range(10))
for num in squared_numbers:
    print(num)
```

## Using next() and iter()

Beyond for loops, Python provides the next() function to manually iterate through an iterator, and iter() to convert iterables into iterators.

```python
num_gen = countdown_generator(3)
print(next(num_gen))  # Outputs: 3
print(next(num_gen))  # Outputs: 2
```

## References

[Datacamp](https://www.datacamp.com/tutorial/python-iterators-generators-tutorial?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720818&utm_adgroupid=157156373751&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=680291483268&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=1001270&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-eu_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-bfcm23&gad_source=1&gclid=CjwKCAiAgeeqBhBAEiwAoDDhn9qct-zZxmv1OwoEyL0OjlQMWYqp98ixfJX7K-sOc7E9OHle26XY2RoCPesQAvD_BwE)