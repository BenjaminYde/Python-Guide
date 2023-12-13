# Strings

## Introduction to Strings
Strings in Python are sequences of Unicode characters. 
They are used to store and manipulate text-based data. 
Python provides a wide range of tools and methods for working with strings, making text processing efficient and straightforward.

### Basic String Creation

Strings can be created by enclosing characters in quotes.
Both single `('...')` and double `("...")` quotes are used to define strings.

```python
s1 = 'Hello'
s2 = "World"
```

### Multiline Strings

Triple quotes (`'''...'''` or `"""..."""`) are used for multiline strings.

```python
s3 = '''This is
a multiline
string'''
```

### Immutable Nature

Strings in Python are immutable, meaning once a string is created, its contents cannot be changed.

## String Operations

### Concatenation

Use `+` to concatenate strings.
Be aware of the performance cost in repeated concatenations. Consider using `str.join()` for combining many strings.

```python
# Concatenation using '+'
hello = "Hello"
world = "World"
greeting = hello + ", " + world + "!"  # "Hello, World!"

# Using 'str.join()' for efficient concatenation
words = ["Python", "is", "awesome"]
sentence = " ".join(words)  # "Python is awesome"
```

### Repetition

Strings can be repeated using `*`.

```python
echo = "Echo! " * 3  # "Echo! Echo! Echo! "
```

### Slicing and Indexing

Access characters by index (0-based).
Negative indexing is supported (starts from the end).
Slicing syntax: [start:end:step].

```python
# Indexing
name = "Python"
first_char = name[0]   # 'P'
last_char = name[-1]   # 'n'

# Slicing
substring = name[1:4]  # "yth" (characters from index 1 to 3)
step_slice = name[0:6:2]  # "Pto" (every second character from index 0 to 5)
```

### Length

Use `len(string)` to get the length of a string.

```python
# Length of a string
length = len("Hello, World!")  # 13
```

### Iterating

Strings are iterable. You can loop over them character by character.

```python
# Iterating over a string
for char in "Hello":
    print(char)
# This will print each character in "Hello" on a new line
```

## String Methods

### Case Conversion

- `str.lower()`: Converts all characters in the string to lowercase.
  - "PYTHON".lower() → 'python'
- `str.upper()`: Converts all characters in the string to uppercase.
  - "python".upper() → 'PYTHON'  
- `str.title()`: Converts the first character of each word to uppercase and the rest to lowercase.
  - "hello world".title() → 'Hello World'
- `str.capitalize()`: Converts the first character to uppercase and the rest to lowercase.
  - "hello".capitalize() → 'Hello'
- `str.swapcase()`: Swaps the case of each character in the string.
  - "PyThOn".swapcase() → 'pYtHoN'

### Searching and Replacing

- `str.find()`: Returns the lowest index of the substring if found, otherwise -1.
  - "Hello".find("e") → 1
- `str.index()`: Similar to find(), but raises ValueError if the substring is not found.
  - "Hello".index("e") → 1
- `str.rfind()`: Returns the highest index of the substring (searches from the end).
  - "Hello".rfind("l") → 3
- `str.count()`: Counts how many times a substring occurs in the string.
  - "Hello".count("l") → 2
- `str.replace(old, new)`: Replaces occurrences of a substring with another.
  - "Hello".replace("l", "p") → 'Heppo'

### Checking Contents

- `str.isdigit()`: Checks if all characters in the string are digits.
  - "123".isdigit() → True
- `str.isalpha()`: Checks if all characters are alphabetic.
  - "abc".isalpha() → True
- `str.isspace()`: Checks if all characters in the string are whitespace.
  - " ".isspace() → True

### Trimming and Stripping

- `str.strip()`: Removes leading and trailing whitespace (or other specified characters).
  - " Hello ".strip() → 'Hello'
- `str.rstrip()`: Removes trailing whitespace (or other specified characters).
  - "Hello ".rstrip() → 'Hello'
- `str.lstrip()`: Removes leading whitespace (or other specified characters).
  - " Hello".lstrip() → 'Hello'

### Splitting and Joining

- `str.split()`: Splits the string into a list by the specified delimiter.
    - "a,b,c".split(",") → ['a', 'b', 'c']
- `str.join()`: Joins elements of an iterable into a single string with the string as the delimiter.
  - ", ".join(["a", "b", "c"]) → 'a, b, c'

### Formatting

- `str.format()`: Formats the string, replacing placeholders with values.
  - "{} and {}".format("Tea", "Coffee") → 'Tea and Coffee'


## String Interpolations (f-strings)

Introduced in Python 3.6, f-strings (formatted string literals) provide a concise and readable way to embed expressions inside string literals. They are prefixed with f or F before the opening quote.

Example:

```python
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: "Hello, my name is Alice and I am 30 years old."=
```

- F-strings are generally faster than the older methods of string formatting (like % formatting or str.format()), as the expressions are evaluated at runtime and directly embedded into the string.
- This makes them not only more efficient in terms of writing code but also in terms of execution speed.

## String Escaping

- String escaping is used to insert characters in a string that are otherwise illegal or difficult to include.

- The backslash (`\`) is used as an escape character in Python.

### Examples:

#### Newline: `\n``

```python
print("Hello\nWorld")  # Output will be on two lines
```

#### Tab: \t

```python
print("Hello\tWorld")  # Output: "Hello   World" (with a tab space)
```

#### Escaping quotes

```python
print("He said, \"Hello World\"")  # Output: He said, "Hello World"
```

## String Parsing

Parsing strings in Python often involves converting string data into more appropriate data types (like integers, floats, or booleans) and vice versa. This is a common task in data handling, especially when dealing with input/output operations.

### Converting String to Int/Float

```python
# String to int
number_str = "123"
number_int = int(number_str)
print(number_int)  # Output: 123

# String to float
float_str = "123.45"
float_num = float(float_str)
print(float_num)  # Output: 123.45
```

### Converting String to Boolean

Python doesn't have a built-in method for this, but you can define a simple function. Typically, strings like "True" or "False" are converted respectively.

```python
def str_to_bool(s):
    return s.lower() in ["true", "t", "yes", "1"]

bool_str = "True"
bool_val = str_to_bool(bool_str)
print(bool_val)  # Output: True
```
### Converting Int/Float to String

```python
# Integer to string
int_num = 123
int_str = str(int_num)
print(int_str)  # Output: "123"

# Float to string
float_num = 123.45
float_str = str(float_num)
print(float_str)  # Output: "123.45"
```

### Example - Handling Errors

Parsing can fail if the string doesn't represent a valid value of the target type. For instance, int('abc') will raise a ValueError. It's often good practice to handle these cases, possibly using try-except blocks.

```python
s = "not a number"
try:
    val = int(s)
except ValueError:
    print(f"Cannot convert '{s}' to an integer.")
```