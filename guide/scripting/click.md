# Click

## What is Click?

Click is a Python package for creating command-line interfaces (CLI) with minimal code. 

## Why Use Click?

- **Simplicity**: Click is designed to make CLI development straightforward. Its use of decorators and context management simplifies parsing command-line arguments and options.

- **Composability**: Click supports creating complex CLI applications by composing commands and parameters.

- **Flexibility**: It's adaptable to a wide range of CLI application needs, from simple scripts to complex applications.

- **Automatic Help Page Generation**: Click automatically generates help pages for commands, reducing the effort needed for documentation.

- **Extensibility**: Developers can extend Click with custom types, commands, and even entirely new paradigms.

## Creating Your First Click Command

```python
import click

@click.command()
def hello() -> None:
    """Simple program that greets NAME for a total of COUNT times."""
    print('Hello, World!')

if __name__ == '__main__':
    hello()
```

- `@click.command()` turns the hello function into a command-line command.

Running the Command:

- Save the script as `hello.py`.
- Run it using `python hello.py` in your terminal.

## Options vs Arguments

### Arguments

**Definition**: Arguments are the most basic form of input. They are straightforward and positional.

Example:

```python
@click.command()
@click.argument('name')
def hello(name: str) -> None:
    print(f'Hello, {name}')
```

**Usage**: `python hello.py Alice` would print Hello, Alice.

### Options

**Definition**: Options are more flexible than arguments. They are named and not positional. Options can have default values and support various data types.

Example:

```python
@click.command()
@click.option(
    '--name', 
    default='World', 
    help='Who to greet.'
)
def hello(name: str) -> None:
    print(f'Hello, {name}')
```

**Usage**: `python hello.py --name Alice` would print Hello, Alice.

### Differences

- **Positional vs Named**: Arguments are positional; options are named.
- **Flexibility**: Options can have default values and various types; arguments are more straightforward.
- **Usage Scenario**: Use arguments for essential inputs and options for optional or configurable inputs.

### Matching Option Names to Function Arguments

When you define a Click command with options, the names of the parameters in your function should match the long names of the options. Click uses these names to pass the command-line arguments to the correct function parameters.

- **Option Names**: The long form of the option name (e.g., `--username`) is used to define the option.
The name directly after the `--` is what Click uses to map the command line input to the function argument.

- **Function Arguments**: The names of the arguments in the function must match the long option names (minus the `--`).
If the option is `--username`, the function parameter should be `username`.

- **Handling Hyphens**: If an option name contains hyphens (e.g., `--user-name`), they are converted to underscores in the function argument name (`user_name`).

### Short and Long Options

```python
@click.command()
@click.option(
    '--username',
    '-u', 
    help='Your username'
)
@click.option(
    '--password',
    '-p', 
    help='Your password', 
    hide_input=True
)
def login(username: str, password: str) -> None:
    print(f'Logging in with username: {username}')
    # Add logic to handle login
```

## Parameter Types in Click

Click offers a variety of parameter types to handle different kinds of command-line input. These types provide a way to specify the kind of data your command expects and can automatically validate and convert the input to the appropriate Python type.

Common Parameter Types:

### String

**String**: The default type for parameters. Accepts any text without whitespace.

```python
@click.command()
@click.option(
    '--name', 
    type=str
)
def greet(name: str) -> None:
    print(f'Hello, {name}')
```

### Int / Float

**Integer**: Accepts an integer value       
**Float**: Accepts a floating-point number.

```python
@click.command()
@click.option(
    '--price',
     type=float
)
def show_price(price: float) -> None:
    print(f'The price is {price}')
```

### Boolean

**Boolean**: Accepts `True` or `False` (often used for flags).

```python
@click.command()
@click.option(
    '--verbose', 
    is_flag=True
)
def log(verbose: bool) -> None:
    if verbose:
        print('Verbose mode is on')
```

### Choice

**Choice**: Restricts the input to a few choices.

```python
@click.command()
@click.option(
    '--color', 
    type=click.Choice(['red', 'green', 'blue'], 
    case_sensitive=False)
)
def color_choice(color: str) -> None:
    print(f'You chose {color}')
```

### Ranged Type

The `FloatRange` type is similar to IntRange but for floating-point numbers.

#### Features:

- **Minimum and Maximum Values**: Set the minimum and maximum floating-point values.
- **Inclusivity**: Inclusive range by default, but this can be adjusted.
- **Clamping**: Clamping to the range boundaries is also available for FloatRange.

```python
@click.command()
@click.option(
    '--temperature', 
    type=click.FloatRange(min=0.0, max=100.0)
)
def check_temperature(temperature: float) -> None:
    print(f'Temperature: {temperature}°C')
```

**Usage**: `python script.py --temperature 37.5` would output "Temperature: 37.5°C". An error is raised if the value is outside the 0.0-100.0 range.

### Path (pathlib)

Click integrates with `pathlib` to handle file and directory paths efficiently and pythonically.

```python
import click
from pathlib import Path

@click.command()
@click.option(
    '--path', 
    type=Path(exists=True)
)
def process_file(path: Path) -> None:
    print(f'Processing file at {path}')
```

## Grouping Commands

Grouping commands is a powerful feature in Click that allows you to organize multiple commands into a single interface, similar to how `git` or `docker` CLI works.

### Creating a Command Group

```python
@click.group()
def my_cli():
    pass

@my_cli.command()
def initdb() -> None:
    print('Initialized the database')

@my_cli.command()
def dropdb() -> None:
    print('Dropped the database')

if __name__ == '__main__':
    cli()
```

**Usage**:

- `python script.py initdb`
- `python script.py dropdb`
- The `my_cli()` function serves as the entry point for the group.
  - `my_cli()` function name can be whatever you like
- Use the `@my_cli.command()` decorator to add commands to the group.


## Naming Commands

You can specify a custom name for a command by passing it to the `@click.command()` decorator.

```python
@click.command('list')
def list_items() -> None:
    print('Listing items...')
```

**Usage**: `python script.py list`

## Avoiding Direct Script Execution with Click

When developing Python packages with Click, it's a best practice to avoid directly executing scripts (e.g., `python script.py`). Instead, you can set up Click commands as entry points in your package's s`etup.py`. This method offers a cleaner, more robust approach, especially for distribution and usage.

### What are Entry Points?

Entry points are a feature provided by setuptools, allowing you to specify command-line scripts that should be installed with your package. When your package is installed, setuptools automatically creates a command-line wrapper for each entry point, making your Click commands available as standalone commands.

### Example setup.py with Click Entry Points

Here's an example of how you might set up setup.py for a package with a Click command:

```python
from setuptools import setup, find_packages

setup(
    name='your_package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        your-command=your_package.module:cli_function
    ''',
)
```

In this example:

1. Replace `your_package` with the name of your package.
1. Replace `your-command` with the name of the command you want users to run.
1. Replace `your_package.module` with the module in your package containing the Click command.
1. Replace `cli_function` with the name of the Click function.

### Using the Entry Point

Once the package is installed (e.g., via `pip install` . in the directory containing setup.py), users can run the command `your-command` directly from the terminal, regardless of their current directory.

### Advantages for Development and Deployment

Using this approach, your Click-based CLI tool behaves like a typical command-line tool. This method is particularly advantageous when you are developing larger or more complex CLI tools that you plan to distribute to other users. It abstracts away the need to run Python scripts directly and offers a more professional, polished feel to your CLI tool.

## Best Practice: Separating Click Functionality and Implementation

In the development of command-line interfaces (CLI) using Click, adopting best practices for code organization is crucial for maintainability, readability, and scalability. One such best practice is to separate the CLI interface (the part that handles user input and command-line parsing) from the business logic (the actual implementation of what each command does). This is typically achieved by having at least two separate files: one for Click functionality (`cli.py`) and another for the implementation of the Click functions (`logic.py` or a similar name).

### Example Structure

#### cli.py

This file contains the Click command definitions and options. It's responsible for CLI interactions and parsing user input.

```python
import click
from .logic import process_data

@click.group()
def my_cli():
    pass

@my_cli.command()
@click.option('--data', required=True)
def process_cli(data: str) -> None:
    process_data(data)
```

#### logic.py

```python
def process_data(data):
    # Process the data
    pass
```