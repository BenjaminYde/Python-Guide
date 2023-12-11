# Packages

## Introduction to Packages

A package in Python is a hierarchical file directory structure that defines a single Python application environment consisting of modules and subpackages. Packages allow for a scalable structure for Python projects, enabling efficient management and usage of modules.

## Creating a Package

To create a package in Python, you need to organize your modules (Python files) into a directory hierarchy and include an `__init__.py` file in each directory to be treated as a package or subpackage.

Consider the following directory structure as an example of a Python package:

```
my_package/
├─ my_package/
│  ├─ __init__.py
│  ├─ module1.py
│  ├─ module2.py
│  ├─ subpackage/
│  │  ├─ __init__.py
│  │  ├─ submodule1.py
│  │  ├─ submodule2.py
├─ requirements.txt
├─ setup.py
├─ README.md
```

### Root Directory

**my_package/**: This is the root directory of your project. It is the container that holds all the files related to your package, including the actual package code, configuration files, documentation, and other metadata.

### Package Directory

**my_package/my_package/**: This directory is the actual Python package. It shares the same name as the root directory, which is a common practice in Python to easily identify the main package of the project. This directory will contain all the Python source code (.py files).

### Initialization File

`__init__.py`: This file makes Python treat the directories as containing packages. This is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file.

### Module Files

**module1.py and module2.py**: These are module files that contain various classes, functions, and variables. They represent separate logical sections of the package. Users can import these modules using the dotted module path (e.g., my_package.module1).

### Subpackage

**subpackage/**: Subpackages are used to further organize the code within the package. It's essentially a package nested within another package. This is useful for large packages where similar components are grouped together.

**subpackage/`__init__.py`**: Like the top-level `__init__.py`, this file serves to initialize the subpackage. It can also be empty or contain code to initialize the subpackage environment.

**subpackage/submodule1.py and subpackage/submodule2.py**: These are additional modules that reside within a subpackage. They can be accessed using the path my_package.subpackage.submodule1, for instance.

### Requirements File

**requirements.txt**: This file lists the dependencies needed for your package to run. These dependencies will be installed when someone sets up your package using pip install -r requirements.txt.

### Setup Script

**setup.py**: This is the build script for setuptools. It contains information about your package and the files that need to be included. It's what pip uses to install your package.

### README File

**README.md**: The README file is often the first place where users will look for information on how to install and use your package. Markdown format (.md) is commonly used for its readability and support on platforms like GitHub.

## Installing The Package

### More about the `setup.py`

The `setup.py` file has traditionally been the standard way to specify how a Python package should be built and installed. It's a script that uses `setuptools` to generate package metadata and other necessary information that makes the package installable via `pip`.

Here's a basic rundown of why setup.py is important:

- **Installation**: It allows the package to be installed using pip install . when run from the root directory of the package.

- **Metadata**: It contains metadata about the package such as the name, version, author, and description.

- **Dependencies**: It lists the package's dependencies, which pip will attempt to install when the package is installed.

- **Package Contents**: It can specify which files and directories are included in the package, including package data files.

- **Scripts**: It can define scripts and entry points that allow users to run functions from the command line.

- **Extension Modules**: For packages with C extensions, setup.py can specify how these modules should be built.

### Creating a `setup.py`

Below is a basic structure of what setup.py might look like:

```python
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of the package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',
    },  
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.10',
)
```

In this script, setup() is the main function and it includes the following parameters:

- **name**: The name of the package.
- **version**: The current version of your package. Semantic versioning is usually used.
- **author and author_email**: The name and email address of the package author.
- **description**: A short, one-sentence summary of the package.
- **long_description**: A detailed description of the package. This is often taken from the README file.
- **long_description_content_type**: This specifies the format of the long description (in this case, Markdown).
- **url**: The URL for the package (often a GitHub repository).
- **packages**: This tells setuptools what package directories (and the Python files they contain) to include find_packages() automatically finds these directories for you.
- **install_requires**: This is a list of other Python packages that your package depends on.
- **classifiers**: These are categories and tags that help users find your package on PyPI.
- **python_requires**: This defines the Python version compatibility of your package.

### Installing The Package with Pip

`pip` is a package installer for Python that allows you to install and manage additional libraries that are not part of the Python standard library.

To install a package using `pip`, you would typically use the command:

```bash
pip install my_package
```

#### Editable Installs (Development Mode)

An editable install is a way to install a Python package while linking it directly to its source code. The primary reason to install a package in editable mode is to allow changes in the package source to be immediately reflected in the environment without needing to reinstall the package.

To install a package in editable mode, you would use the `-e` option:

```bash
pip install -e path/to/your/package
```

#### Why Use Editable Installs?

Editable installs are particularly useful during development when you're making frequent changes to the package and you want to test those changes without having to reinstall the package every time.

For example, if you're developing a web application using a framework and you find a bug in the framework, you can clone the framework's repository, install it in editable mode, fix the bug, and immediately test if your application works with the fix.


## Relative and Absolute Imports

Packages support both absolute and relative imports to allow for flexible referencing of modules.

**Absolute imports** use the full path to the module from the project's root directory.

```python
from mypackage import module2
from mypackage.subpackage import submodule1
```

**Relative imports** use leading dots to indicate the current and parent packages involved. One dot means the current package, two dots mean the parent package, and so forth.

```python
# Inside submodule1.py
from . import submodule2  # Importing from the same subpackage
from .. import module1    # Importing from the parent package
```