# Bytes

## What are bytes?

### Definition

- A byte is a unit of digital information in computing and telecommunications.
- It typically consists of eight bits, where a bit is the smallest unit of data in a computer, represented as either 0 or 1.
- The byte is a common unit of measurement for data size and storage.

### Bytes and Characters

In computer systems, a byte can represent a character such as a letter, number, or typographic symbol. For example, in the ASCII (American Standard Code for Information Interchange) character encoding, each character is represented by a specific byte value.

### How Bytes Work

#### Binary Representation

- Each bit in a byte can be in one of two states, 0 or 1. This binary system is the foundation of all modern computing.
- The combination of eight bits (or one byte) allows for 256 different combinations (2^8), ranging from 00000000 to 11111111 in binary, which can represent 256 different values or symbols.

#### Encoding

- To represent characters, bytes must be interpreted through a character encoding. ASCII is one of the simplest forms of encoding, where each character is assigned a specific byte value. For example, the ASCII code for 'A' is 65 (or 01000001 in binary).
- Other encodings, like UTF-8, use one or more bytes to represent a single character, allowing them to cover a much wider range of characters, including those from non-Latin scripts.

### Usage of Bytes

#### Data Storage and Transmission

- Bytes are the fundamental building blocks of data storage. Files on a computer, for instance, are measured in bytes, as well as kilobytes (1024 bytes), megabytes (1024^2 bytes), and so on.
- In data transmission, such as over the internet, the speed is often measured in bits per second or bytes per second.

#### Memory Representation

- In computer memory, bytes are used to store data. Each byte has a specific address that the computer's processor can use to access its value.
- Programming languages provide various ways to manipulate bytes, often through data types and structures that abstract away the binary complexity.

#### Networking
- Network protocols, like TCP/IP, structure data into packets consisting of bytes. Each byte in a packet can represent part of a header, payload, or footer, as defined by the protocol.

## Creating Bytes Objects

### Literal Byte Sequences

- Syntax: `b'Hello World'` creates a byte object directly.
- Each character in the literal is converted to its corresponding ASCII value.

### Using the `bytes()` constructor

- The bytes() function creates a new bytes object.
- `bytes([72, 101, 108, 108, 111])` which is equivalent to `b'Hello'`

## Converting Between Bytes and Strings

### Encoding a String to Bytes

- Strings in Python are sequences of Unicode characters.
- Encoding is the process of converting these characters into a sequence of bytes.
- Use the `encode()` method on a string, specifying the encoding (like 'utf-8', 'ascii', 'latin1').
- Example: `'Hello'.encode('utf-8')` converts `'Hello'` to its UTF-8 encoded byte representation.
- Encoding is crucial for storing text in files, sending over networks, or processing in binary formats.

```python
data_str = "Hello, World!"
data_bytes = data_str.encode('utf-8')
print(data_bytes)
```

### Decoding Bytes to a String

- Decoding is the reverse process of encoding, converting bytes back into a string.
- Use the `decode()` method on a bytes object, specifying the encoding.
- Example: `b'Hello'.decode('utf-8')` converts the bytes back to the string `'Hello'`.
- Incorrect decoding (using the wrong encoding) can lead to errors or garbled text.
- Important for reading text from binary files, network responses, or processing any data that comes in a byte format.

```python
data_bytes = b"Hello, Bytes!"
data_str = data_bytes.decode('utf-8')
print(data_str)
```

## Byte Manipulation

Byte manipulation refers to the process of modifying or interpreting bytes at the bit level. This is often done using bitwise operators, which operate on individual bits within a byte or group of bytes.

### AND Operator `&`

Each bit of the output is 1 if the corresponding bits of both operands are 1, else 0.

```python
a = 0b1100  # 12 in binary
b = 0b1010  # 10 in binary
result = a & b  # 0b1000 (8 in decimal)
```

### OR Operator `|`

Each bit of the output is 1 if at least one of the corresponding bits of either operand is 1.

```python
a = 0b1100  # 12 in binary
b = 0b1010  # 10 in binary
result = a | b  # 0b1110 (14 in decimal)
```

### XOR Operator `^`

Each bit of the output is 1 if the corresponding bits of the operands are different.

```python
a = 0b1100  # 12 in binary
b = 0b1010  # 10 in binary
result = a ^ b  # 0b0110 (6 in decimal)
```

### NOT Operator `~`

Inverts the bits of the operand.

```python
a = 0b1100  # 12 in binary
result = ~a  # Inverts all bits
```

### Bit Shifts

- **Left Shift (<<)**: Shifts the bits to the left, padding with zeros.
  - Multiplies the number by 2 for each shift.
  - **Example**: a << 2 shifts a two bits to the left.

- **Right Shift (>>)**: Shifts the bits to the right.
  - Divides the number by 2 for each shift, discarding fractions.
  - For signed integers, the sign bit (leftmost bit) is used to fill the vacancies.
  - **Example**: a >> 2 shifts a two bits to the right.

## `struct` module

The `struct` module in Python is used for converting between Python values and C structs represented as Python bytes objects. This is particularly useful for reading and writing binary data, or for interfacing with C code. It's a key tool for handling binary data in Python, especially when dealing with files, network protocols, or other binary formats.

### Packing and Unpacking Data

#### Format strings

- Used to specify the layout of the data being packed/unpacked.
- Consist of format characters, which indicate the data type and size.
- Common format characters include:
  - `i`: Represents an integer. Size: 4 bytes.
  - `f`: Represents a floating-point number. Size: 4 bytes.
  - `d`: Represents a double precision floating-point number. Size: 8 bytes.
  - `c`: Represents a single byte character. Size: 1 byte.
  - `s`: Represents a sequence of characters (string). Size: 1 byte per character.
  - `b`: Represents a signed byte. Size: 1 byte.
  - `B`: Represents an unsigned byte. Size: 1 byte.
  - `h`: Represents a short integer. Size: 2 bytes.
  - `H`: Represents an unsigned short integer. Size: 2 bytes.
  - `l`: Represents a long integer. Size: 4 bytes. (Note: On some platforms, it might be 8 bytes).
  - `L`: Represents an unsigned long integer. Size: 4 bytes. (Note: On some platforms, it might be 8 bytes).
  - `q`: Represents a long long integer. Size: 8 bytes.
  - `Q`: Represents an unsigned long long integer. Size: 8 bytes.
  - `?`: Represents a boolean value. Size: 1 byte.

In the format strings used with Python's struct module, whitespace characters between format specifiers are indeed ignored. This means you can include spaces for readability without affecting the functionality.

#### Count Numbers

A number preceding a format character indicates a sequence or array of that type.
For example:

- `4i` represents four integers
- `10s` represents a string of 10 characters.

#### Packing

Converts Python objects to bytes (binary data).

```python
import struct

# Pack an integer and a float into bytes
packed_data = struct.pack('if', 123, 45.67)
```

#### Unpacking

Converts bytes (binary data) back into Python objects.

```python
import struct

# Whitespace for readability is allowed between format characters
packed_data = struct.pack('i f', 123, 45.67)

# Unpacking the data
unpacked_data = struct.unpack('i f', packed_data)

# Accessing the unpacked data
unpacked_integer = unpacked_data[0]  # 123
unpacked_float = unpacked_data[1]    # 45.67
```

### Combining with Data Classes

Python's `dataclasses` module, introduced in Python 3.7, is designed for classes that are mainly used to store data. By combining data classes with struct, you can create a more readable and maintainable structure for handling binary data.

Example:

```python
from dataclasses import dataclass
import struct

@dataclass
class MyData:
    value1: int
    value2: float
    value3: int

    def pack(self):
        return struct.pack('ifi', self.value1, self.value2, self.value3)

    @staticmethod
    def unpack(data):
        values = struct.unpack('ifi', data)
        return MyData(*values)

# Create an instance of MyData
data_instance = MyData(100, 25.75, 200)

# Pack the data into bytes
packed_data = data_instance.pack()

# Unpack the data back into a dataclass instance
unpacked_instance = MyData.unpack(packed_data)
```