# Executable Python

## Running Python Scripts

Python scripts, typically saved with a `.py` extension, contain executable code and can be run in several ways:

**1. Direct Execution through an Interpreter**: By invoking the Python interpreter with a script as an argument:

```bash
python script.py
```

**2. Making Python Scripts Executable**: Particularly on Unix-like systems, Python scripts can be run as standalone executables by adding a `shebang` line and modifying file permissions.

## Making Python Scripts Executable

To run a Python script as an executable file:

### 1. Add a Shebang line

#### What is a Shebang?

- **Definition**: A shebang line in a script is the very first line that starts with #!. It is followed by the path to the interpreter that should execute the script.

- **Purpose**: It tells the system which interpreter to use to run the file, allowing scripts to be executed as standalone programs.

This is the first line of the script, guiding the system to the Python interpreter.

**Basic Syntax**: The shebang line is written as:

```python
#!/path/to/interpreter
```

**Common Python Shebang**: For Python, it typically looks like:

```python
#!/usr/bin/env python3
```
`env Command`: Using /usr/bin/env `python3` ensures that the system uses the first `python3` interpreter in your environment's `$PATH`.

### 2. Change File Permissions (on Unix-like systems)

Use the `chmod` command to make the script executable:

```bash
chmod +x script.py
```

### 3. Execution

After these steps, the script can be run like any other executable:

```bash
./script.py
```

## Cross-Platform Considerations

- **Unix-Like Systems**: Shebangs are primarily a Unix concept and are used extensively on Linux and macOS.

- **Windows**: Windows does not natively support shebang lines, but certain environments like Cygwin or the Windows Subsystem for Linux (WSL) do.


## Best Practices

- Use `/usr/bin/env`: It's considered a best practice to use `#!/usr/bin/env python3` instead of hard-coding the path to the Python interpreter. This approach increases the portability of your script across different environments where the Python interpreter's location might vary.

## Running Python Scripts from Other Python Scripts

### exec()

`exec()` is a built-in Python function that dynamically executes Python code. It can execute a string containing a Python script, and it's often used in scenarios where you need to run code that is generated dynamically.

```python
code = """
def say_hello(name):
    print(f'Hello, {name}!')
"""

exec(code)
say_hello('Alice')
```

### eval()

`eval()` is another built-in function in Python used for evaluating simple Python expressions. It evaluates a string as a Python expression and returns the result.

```python
result = eval("5 * 10 + 2")
print(result)  # Output: 52
```