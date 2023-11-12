# Array

Python doesn't have a native array data type in the same sense as languages like C or Java. However, Python provides a module named array that offers a compact, efficient array storage and manipulation for basic types like integers and floating point numbers.

The array module in Python is useful when you need to manipulate a large number of same type elements efficiently. Arrays in Python are different from lists because they can store elements of a single data type, making them more compact and efficient for specific tasks.

## Creating an Array

To use arrays, you need to import the array module. Arrays are created using the array.array class. The class takes two arguments: the type code, which defines the type of elements the array will hold, and an optional initial sequence of values.

```python
import array

# Creating an integer array
intArray = array.array('i', [1, 2, 3, 4, 5])

# Creating a floating point array
floatArray = array.array('f', [1.0, 2.0, 3.0, 4.0])
```

The type code is important as it explicitly defines the type of the array and its elements. Some common type codes include:

- 'b' for signed char
- 'B' for unsigned char
- 'u' for Py_UNICODE (wide char)
- 'h' for signed short
- 'H' for unsigned short
- 'i' for signed int
- 'I' for unsigned int
- 'l' for signed long
- 'L' for unsigned long
- 'q' for signed long long
- 'Q' for unsigned long long
- 'f' for float
- 'd' for double

## Accessing Array Elements

Array elements can be accessed using indices, just like in lists.

```python
print(intArray[0])  # Outputs: 1
print(floatArray[3]) # Outputs: 4.0
```

## Array Methods

```python
array.array(typecode[, initializer])    # Creates a new array
array.typecodes                         # List of typecodes that are recognized by the array module
array.typecode                          # The typecode character used to create the array
array.itemsize                          # The size in bytes of one array item
array.append(x)                         # Appends a new item to the end of the array
array.buffer_info()                     # Returns a tuple (address, length) giving the current memory address and the length in elements of the buffer
array.byteswap()                        # Byteswaps all items of the array
array.count(x)                          # Returns the number of occurrences of x in the array
array.extend(iterable)                  # Appends items from the iterable to the end of the array
array.frombytes(s)                      # Appends items from the string, interpreting it as an array of machine values
array.fromfile(f, n)                    # Reads n items (as machine values) from the file object f and appends them to the end of the array
array.fromlist(list)                    # Appends items from the list
array.fromunicode(s)                    # Extends this array with data from the unicode string s
array.index(x)                          # Returns the smallest index i such that i is the index of the first occurrence of x in the array
array.insert(i, x)                      # Inserts a new item x into the array before position i
array.pop([i])                          # Removes the item with the index i from the array and returns it
array.remove(x)                         # Removes the first occurrence of x from the array
array.reverse()                         # Reverses the order of the items in the array
array.tobytes()                         # Converts the array to a bytes object
array.tofile(f)                         # Writes all items (as machine values) to the file object f
array.tolist()                          # Converts the array to an ordinary list with the same items
array.tounicode()                       # Converts the array to a unicode string
```

## Using classes with Array

The array module in Python does not support arrays of custom class objects. The array module is specifically designed for efficient storage and manipulation of basic data types like integers, floats, and characters. It's optimized for these basic types and doesn't support complex data structures or custom objects.

If you need to create an array-like structure that holds custom class objects, you should use Python's built-in list or a numpy array (if you're dealing with large amounts of numerical data and need the additional functionality and efficiency that numpy provides).