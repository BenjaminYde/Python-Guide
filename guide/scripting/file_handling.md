# File Handling

## Introduction to pathlib

pathlib is a module in Python that provides an object-oriented interface for working with file system paths. Introduced in Python 3.4, it represents filesystem paths as objects instead of strings, making path manipulations more intuitive and less error-prone.

## Why Use pathlib?

- **Object-Oriented Approach**: Paths are represented as objects, enabling methods and properties to be called on them directly.
- **Readability**: Code using pathlib tends to be more readable compared to traditional file handling methods.
- **Cross-platform Compatibility**: Automatically handles different file system path conventions (Windows, Unix, etc.).
- **Comprehensive**: Offers a wide array of methods for common path manipulations and file operations.

## Basic Path Operations

### Creating Path Objects

```python
from pathlib import Path

# Create a Path object for current directory
path = Path('.')

# Create a Path object for a specific file/directory
file_path = Path('/path/to/file')
dir_path = Path('/path/to/directory')
```

### Path Properties

- `path.exists()`: Checks if the path exists.
- `path.is_file()`: Checks if the path is a file.
- `path.is_dir()`: Checks if the path is a directory.
- `path.name`: Gets the name of the file or directory.
- `path.suffix`: Gets the file extension.
- `path.stem:` Gets the file name without the suffix.
- `path.parent`: Gets the directory containing the file.

### Navigating and Joining Paths

```python
# Joining paths
new_path = dir_path / 'subdirectory' / 'file.txt'

# Parent directory
parent_dir = file_path.parent
```

## File Operations

### Reading and Writing Files

```python
# Writing to a file
with open(file_path, 'w') as f:
    f.write('Hello, World!')

# Reading from a file
with open(file_path, 'r') as f:
    content = f.read()
```

#### Reading and Writing Without open()

Methods like `Path.read_text()`, `Path.write_text()`, `Path.read_bytes()`, and `Path.write_bytes()` allow for quick reading and writing operations without needing to explicitly open the file.

### Iterating Over Directory Contents

```python
# List all files in a directory
for child in dir_path.iterdir():
    print(child)
```

### Globbing: Pattern matching for files

```python
for file in dir_path.glob('*.txt'):
    print(file)
```

Using `**` in `glob()` or `rglob()` for recursive pattern matching.     
For example, `path.rglob('*.py')` finds all Python files in the current directory and all subdirectories.     
This is particularly useful for searching through directory trees.

### Reading and Writing Bytes: For binary file handling

```python
with open(file_path, 'rb') as f:
    bytes_data = f.read()
```

### Creation and Deletion of Files and Directories

Creation:

- `Path.mkdir()`: Creates a new directory at this given path.
- `Path.touch()`: Creates a file if it does not exist

Deletion:

- `Path.rmdir()`: Removes a directory, which must be empty.
- `Path.unlink()`: Deletes a file.

## Path Manipulation

### Changing File Extensions

```python
new_file = file_path.with_suffix('.md')
```

### Resolving Paths

`Path.resolve()`: Resolves relative paths to absolute paths, and can also normalize the path (e.g., resolving .. and . components).        
Useful for ensuring that you are working with the definitive path to a file or directory.

### Symlinks

- `Path.symlink_to(target)`: Creates a symbolic link pointing to the target.
- `Path.is_symlink()`: Checks if the path is a symbolic link.
- Handling symbolic links is crucial in environments where they are commonly used, like Unix/Linux systems.

## Working with File System Metadata

### Accessing File Properties:

- `Path.stat()`: Returns information like size, modification time, etc.
- This method is vital for scripts that need to monitor or react to changes in file properties.

### Ownership and Permissions

- Methods like `Path.chmod()`, `Path.owner()`, and `Path.group()` allow you to change file permissions and examine file ownership.
- Important for scripts that manage file security or need to modify access rights.

## Error Handling in pathlib

It's important to handle exceptions when working with file operations to avoid crashes due to issues like missing files or permission errors.

```python
from pathlib import Path, PathError

try:
    with open(file_path, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PathError as e:
    print(f"Path error: {e}")
```

## Introduction to shutil

`shutil` is a Python module that offers a number of high-level operations on files and collections of files. This module is part of the Python Standard Library and provides functionality for file copying, moving, renaming, and deletion, as well as directory and archive management. While `pathlib` is excellent for file path manipulations and basic file operations, `shutil` complements it by providing more advanced and specialized file operations.

## Why shutil Exists Alongside pathlib

- **Different Focus and Scope**: While pathlib is primarily designed for path manipulation and basic file operations (like reading/writing files), shutil is focused on high-level file operations like copying, moving, and archiving files and directories.

- **Complementary Functionality**: shutil complements pathlib by providing functionality that pathlib does not, particularly in handling operations involving multiple files or directories.

- **Legacy Support**: shutil has been part of Python for a longer time and provides some functionalities that predate pathlib. It's well-integrated into existing Python codebases.

## Key Functionalities of shutil

### File Copying and Moving

#### Copying Files:

- `shutil.copy(src, dst)`: Copies the file src to the file or directory dst. If dst specifies a directory, the file will be copied into dst using the base filename from src.
- `shutil.copy2(src, dst)`: Similar to shutil.copy(), but copy2() also attempts to preserve file metadata.

#### Copying Directories:

- `shutil.copytree(src, dst)`: Recursively copies an entire directory tree rooted at src to a directory named dst.

#### Moving Files and Directories:

- `shutil.move(src, dst)`: Recursively moves a file or directory (src) to another location (dst).

### Directory Management

#### Removing Directories:

- `shutil.rmtree(path)`: Recursively deletes a directory and all its contents.

#### Changing Ownership and Permissions:

- `shutil.chown()` allows changing the owner and group of a file or directory.

### Disk Space

- `shutil.disk_usage(path)`: Returns disk usage statistics about the path as a named tuple with the attributes total, used, and free, representing the total, used, and free space in bytes.

### Archiving Operations

#### Creating and Extracting Archives:

- `shutil.make_archive(base_name, format, root_dir)`: Creates an archive (like zip or tar) of the root_dir.
- `shutil.unpack_archive(filename, extract_dir)`: Extracts an archive into the extract_dir.
