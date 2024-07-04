# NumPy

## Introduction to NumPy

NumPy, short for Numerical Python, is a powerful library in Python for numerical computing. It provides support for large multidimensional arrays and matrices, along with a wide variety of mathematical functions to operate on these arrays. NumPy is essential for scientific computing and is the foundation of many other libraries, including SciPy, Matplotlib, and pandas.

At the core of the NumPy package, is the `ndarray` object. This encapsulates n-dimensional arrays of homogeneous data types, with many operations being performed in compiled code for performance.

### Installation

To install NumPy, you can use pip:

```bash
pip install numpy
```

Website: https://numpy.org/

## Basics of NumPy Arrays

### Creating Arrays

NumPy arrays can be created in several ways. The most common method is to use the `numpy.array()` function:

```python
import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Creating an array with a specified data type
arr3 = np.array([1, 2, 3], dtype=float)
```

### Array Attributes

NumPy arrays have several attributes that provide information about the array:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape:", arr.shape)  # Output: (2, 3)
print("Number of dimensions:", arr.ndim)  # Output: 2
print("Size:", arr.size)  # Output: 6
print("Data type:", arr.dtype)  # Output: int64 (or int32 depending on the system)
print("Item size:", arr.itemsize)  # Output: 8 (or 4 depending on the system)
```

### Creating a Function With NumPy Array Return Value

```python
def create_array() -> np.ndarray:
    return np.array([[1, 2, 3], [4, 5, 6]])
```

### More On Array Shape

In the context of a NumPy array's shape, this tuple contains integers that represent the size of the array along each dimension.

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1.shape)  # Output: (5,)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.shape)  # Output: (2, 3)

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3.shape)  # Output: (2, 2, 2)
```

### Array Initialization

NumPy provides functions to create arrays with initial placeholder content:

```python
# Array of zeros
zeros = np.zeros((2, 3))

# Array of ones
ones = np.ones((3, 2))

# Arrange
np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(2, 10, dtype=float) # array([2., 3., 4., 5., 6., 7., 8., 9.])
np.arange(2, 3, 0.1) # array([2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])

# Equally space elements in range
np.linspace(1., 4., 6) # array([1. ,  1.6,  2.2,  2.8,  3.4,  4. ])

# Array of a constant value
full = np.full((2, 2), 7)

# Identity matrix
identity = np.eye(3)
#array([[1., 0., 0.],
#       [0., 1., 0.],
#       [0., 0., 1.]])

# Array of random values
random = np.random.random((2, 2))

# Diagonal 
np.diag([1, 2, 3])
#array([[1, 0, 0],
#       [0, 2, 0],
#       [0, 0, 3]])
```

## Indexing, Slicing and Views

### Accessing Array Elements

Array elements can be accessed using square brackets, similar to Python lists:

```python
# Accessing elements
print(arr1[0])  # First element of arr1
print(arr2[1, 2])  # Element at row 1, column 2 of arr2
```

### Slicing Arrays

You can extract a subset of an array using slicing:

```python
# Slicing a 1D array
slice1 = arr1[1:4]  # Elements from index 1 to 3

# Slicing a 2D array
slice2 = arr2[:, 1:3]  # All rows, columns 1 and 2
```

### Boolean Indexing

Boolean indexing allows you to select elements based on a condition:

```python
bool_idx = arr1 > 2
print(arr1[bool_idx])  # Elements greater than 2
```

### Views

A view in NumPy is a way of looking at the same data stored in an array from different perspectives. Views are created using slicing or other functions and do not copy the underlying data. Instead, they create a new array object that shares the same data buffer as the original array.

```python
arr = np.array([[1, 2], [3, 4], [5, 6]])
view = arr.view()
print(view)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]
```

#### Assignment vs View

Assignment:

```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
assigned = arr
print(arr is assigned)  # Output: True
```

View:

```python
view = arr.view()
print(arr is view)  # Output: False
print(view.base is arr)  # Output: True
```

- **Assignment**: Simply references the same object.
- **.view()**: Creates a new array object that views the same data.

#### Making a view read-only

A view in NumPy is not read-only. Modifying the view will modify the original array since they share the same data buffer. If you need a read-only version of the array, you can use the flags attribute to set the WRITEABLE flag to False.

```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
view = arr.view()
view.flags.writeable = False

try:
    view[0, 0] = 10
except ValueError as e:
    print(e)  # Output: assignment destination is read-only
```

## Operations on Arrays

### Basic Arithmetic

NumPy supports element-wise arithmetic operations:

```python
# Element-wise addition
sum_arr = arr1 + 1

# Element-wise subtraction
diff_arr = arr1 - 1

# Element-wise multiplication
prod_arr = arr1 * 2

# Element-wise division
quot_arr = arr1 / 2
```

Once you have created arrays, you can replicate, join, or mutate those existing arrays to create new arrays. When you assign an array or its elements to a new variable, you have to explicitly numpy.copy the array, otherwise the variable is a view into the original array. Consider the following example:

```python
a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]
b += 1
print('a =', a, '; b =', b) # a = [2 3 3 4 5 6] ; b = [2 3]
```

### Universal Functions (ufuncs)

NumPy provides many mathematical functions, called ufuncs, that operate element-wise on arrays:

```python
# Square root
sqrt_arr = np.sqrt(arr1)

# Exponential
exp_arr = np.exp(arr1)

# Sine
sin_arr = np.sin(arr1)

# Logarithm
log_arr = np.log(arr1)
```

### Aggregation Functions

NumPy provides functions to perform various aggregations:

```python
print(np.sum(arr1))      # Sum of all elements
print(np.mean(arr1))     # Mean of all elements
print(np.std(arr1))      # Standard deviation of all elements
print(np.min(arr1))      # Minimum element
print(np.max(arr1))      # Maximum element
print(np.prod(arr1))     # Product of all elements
```

### Dot Product and Matrix Multiplication

NumPy supports both element-wise multiplication and matrix multiplication:

```python
# Element-wise multiplication
elem_mult = arr1 * arr1

# Dot product
dot_prod = np.dot(arr1, arr1)

# Matrix multiplication
mat_mult = np.matmul(arr2, arr2.T)
```

## Reshaping and Flattening Arrays

### Reshaping Arrays

You can change the shape of an array using the reshape method:

```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape((2, 3))
print(reshaped)
```

Output:
```
[[1 2 3]
 [4 5 6]]
```

### Flattening Arrays

Flattening an array converts it to a 1D array:

```python
flattened = arr2.flatten()
```

## Advanced Topics

### Vectorization

Vectorization is the process of converting iterative operations to array operations, which are much faster:

```python
# Without vectorization
result = np.zeros_like(arr1)
for i in range(len(arr1)):
    result[i] = arr1[i] + 1

# With vectorization
result = arr1 + 1
```

## Data Types in NumPy

### Importance of Data Types

Choosing the correct data type for your arrays can impact both performance and memory usage. NumPy supports a wide range of data types, allowing you to optimize for specific needs.

### Common Data Types

- `int8, int16, int32, int64`: Signed integer types with different bit-widths.
- `uint8, uint16, uint32, uint64`: Unsigned integer types with different bit-widths.
- `float16, float32, float64`: Floating-point types with different precision.

### Specifying Data Types

You can specify the data type when creating an array:

```python
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)
```

### Type Conversion

You can convert between data types using the astype method:

```python
arr = np.array([1, 2, 3], dtype=np.int32)
arr_float = arr.astype(np.float64)
print(arr_float)
```

### Errors

When you use numpy.array to define a new array, you should consider the dtype of the elements in the array, which can be specified explicitly. This feature gives you more control over the underlying data structures and how the elements are handled in C/C++ functions. When values do not fit and you are using a dtype, NumPy may raise an error:

```python
np.array([127, 128, 129], dtype=np.int8)
# OverflowError: Python integer 128 out of bounds for int8
```

## Iterating

### Basic Iteration

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
for element in arr:
    print(element)
```
 
Or using indexes:

```python
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        for k in range(arr.shape[2]):
            print(arr[i, j, k])
```

### Using `np.nditer()`

`np.nditer()` provides an efficient way to iterate over all elements in a multi-dimensional array:

```python
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
```

### Using `np.ndenumerate()`

`np.ndenumerate()` is another method that provides both the index and the value:

```python
for index, value in np.ndenumerate(arr):
    print(index, value)
```

## Searching for Items

## Using `np.all()`

`np.all()` checks if all elements along a given axis evaluate to `True`:

```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
result = np.all(arr2 > 0)
print(result)  # Output: True
```

### Using `np.any()`

`np.any()` checks if any elements along a given axis evaluate to `True`:

```python
import numpy as np

arr = np.array([1, 2, 3, -4])
result = np.any(arr < 0)
print(result)  # Output: True
```

### Using `np.where()`

`np.where()` returns the indices of elements that meet a condition:

```python
arr = np.array([1, 2, 3, 4])
indices = np.where(arr > 2)
print(indices)  
# Output: (array([2, 3]),)
```

Using np.where to choose elements:

```
result = np.where(arr > 2, arr, -1)
print(result)  
# Output: [-1 -1  3  4]
```

- **Condition: arr > 2**
  - This creates a boolean array where each element is True if the corresponding element in arr is greater than 2, and - False otherwise.
- **Selection: np.where(arr > 2, arr, -1)**
  - If the condition is True, the element from arr is selected.
  - If the condition is False, -1 is selected

### Using `np.argwhere()`

`np.argwhere()` returns the indices of elements that meet a condition, but the output is formatted as a 2D array with each row being the index of an element.

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

indices = np.argwhere(arr > 5)
print(indices)
# Output: [[1, 2]
#          [2, 0]
#          [2, 1]
#          [2, 2]]
```

- The element at index [2, 0] (7) is greater than 5.
- The element at index [1, 2] (6) is greater than 5.
- The element at index [2, 1] (8) is greater than 5.
- The element at index [2, 2] (9) is greater than 5.

## Joining Arrays

### Using `np.concatenate()`

`np.concatenate()` joins a sequence of arrays along an existing axis.

Example: Concatenating 1D Arrays

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate((arr1, arr2))
print(result)  # Output: [1 2 3 4 5 6]
```

Example: Concatenating 2D Arrays

```python
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

concat_axis0 = np.concatenate((arr1, arr2), axis=0)
print(concat_axis0)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

concat_axis1 = np.concatenate((arr1, arr2.T), axis=1)
print(concat_axis1)
# Output:
# [[1 2 5]
#  [3 4 6]]
```

The axis parameter is used in many NumPy functions to specify the dimension along which the operation should be performed. It helps control whether the operation is applied across rows, columns, or other dimensions in a multi-dimensional array.

- `Axis 0`: Refers to the vertical direction (down the rows).
- `Axis 1`: Refers to the horizontal direction (across the columns).

```python
sum_axis0 = np.sum(arr, axis=0)
print(sum_axis0)  # Output: [12 15 18]
```


### Using `np.stack()`

`np.stack()` joins a sequence of arrays along a new axis.

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.stack((arr1, arr2), axis=1)
print(result)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
```

### Using `np.hstack()` and `np.vstack()`

`np.hstack()` stacks arrays in sequence horizontally (column-wise) and `np.vstack()` stacks arrays in sequence vertically (row-wise).

Example: Horizontal Stacking

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.hstack((arr1, arr2))
print(result)  # Output: [1 2 3 4 5 6]
```

Example: Vertical Stacking

```python
result = np.vstack((arr1, arr2))
print(result)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

## Copying Arrays

### Using `np.copy()`

Creates a deep copy of the array. Modifying the copy does not affect the original array.

```python
arr = np.array([1, 2, 3])
arr_copy = np.copy(arr)
arr_copy[0] = 10
print(arr)      # Output: [1 2 3]
print(arr_copy) # Output: [10 2 3]
```

### Using `.copy()`

Another method to create a deep copy is using the copy method of the array object.

```python
arr = np.array([1, 2, 3])
arr_copy = arr.copy()
arr_copy[0] = 10
print(arr)      # Output: [1 2 3]
print(arr_copy) # Output: [10 2 3]
```

### Shallow Copy

A shallow copy creates a new array object but does not copy the elements, instead, it references the original array's elements. This is typically done via assignment.

```python
arr = np.array([1, 2, 3])
arr_shallow_copy = arr
arr_shallow_copy[0] = 10
print(arr)              # Output: [10 2 3]
print(arr_shallow_copy) # Output: [10 2 3]
```

## Sorting

### Using `np.sort()`

`np.sort()` returns a sorted copy of an array.

```python
import numpy as np

arr = np.array([3, 1, 2])
sorted_arr = np.sort(arr)
print(sorted_arr)  # Output: [1 2 3]
```

or

```python
arr.sort()
print(arr)  # Output: [1 2 3]
```

### Sorting Along an Axis

You can specify the axis along which to sort.
Axis=0:

```python
arr2 = np.array([[3, 2, 1], [6, 5, 4], [2, 3, 9]])
sorted_arr2 = np.sort(arr2, axis=0)
print(sorted_arr2)
# Output:
# [[2 2 1]
#  [3 3 4]
#  [6 5 9]]
```

Axis=1:

```python
arr2 = np.array([[3, 2, 1], [6, 5, 4]])
sorted_arr2 = np.sort(arr2, axis=1)
print(sorted_arr2)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

### Indirect Sorting Using `np.argsort()`

`np.argsort()` returns the indices that would sort an array. Useful for sorting based on another array.

```python
arr = np.array([3, 1, 2])
indices = np.argsort(arr)
print(indices)  # Output: [1 2 0]
sorted_arr = arr[indices]
print(sorted_arr)  # Output: [1 2 3]
```

### Sorting with a Key Using `np.lexsort()`

np.lexsort() performs an indirect sort using a sequence of keys.

```python
names = np.array(['John', 'Paul', 'George', 'Ringo'])
heights = np.array([180, 175, 178, 172])
indices = np.lexsort((heights, names))
print(names[indices])
# Output: ['George' 'John' 'Paul' 'Ringo']
```