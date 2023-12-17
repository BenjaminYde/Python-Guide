# Subprocess

## What is subprocess?

- **Definition**: The subprocess module in Python is a powerful tool for spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes. It is a part of Python's standard library.

- **Purpose**: It is used for running external commands and interacting with other applications or scripts that are not written in Python from within a Python script. This  provides control over external processes, which is essential for tasks that require automation or scripting of system-level operations.

## subprocess.run

`subprocess.run()`: This is the most straightforward way to execute an external command. It blocks until the command completes and returns a CompletedProcess instance.

The `subprocess.run()` method takes several arguments, some of which are:

- `args`: The command to run and its arguments, passed as a list of strings.

- `capture_output`: When set to True, will capture the standard output and standard error.

- `text`: When set to True, will return the stdout and stderr as string, otherwise as bytes.

- `check`: a boolean value that indicates whether to check the return code of the subprocess, if check is true and the return code is non-zero, then subprocess `CalledProcessError` is raised.

- `env`: This allows you to set environment variables for the subprocess. It's a dictionary of environment variable names and their values.

- `cwd`: Sets the current working directory for the subprocess. This is useful if you need the subprocess to run in a different directory from the Python script

- `timeout`: A value in seconds that specifies how long to wait for the subprocess to complete before timing out.

- `shell`: A boolean value that indicates whether to run the command in a shell. This means that the command is passed as a string, and shell-specific features, such as wildcard expansion and variable substitution, can be used.

The `subprocess.run()` method also returns a `CompletedProcess` object, which contains the following attributes:

- `args`: The command and arguments that were run.

- `returncode`: The return code of the subprocess.

- `stdout`: The standard output of the subprocess, as a bytes object.

- `stderr`: The standard error of the subprocess, as a bytes object.

### Example: Running a simple command like ls or dir:

```python
import subprocess
result = subprocess.run(['ls', '-l'])
print(result.stdout)
```

### Example: Capturing command output:

```python
result = subprocess.run(['echo', 'Hello World'], capture_output=True, text=True)
print(result.stdout)
```

## Error Handling

Handling errors and non-zero exit statuses:

```python
result = subprocess.run(['ls', 'non_existent_file'], capture_output=True, text=True)
if result.returncode != 0:
    print("Error:", result.stderr)
```

## Timeouts

Implementing timeouts:

```python
try:
    result = subprocess.run(['sleep', '10'], timeout=5)
except subprocess.TimeoutExpired:
    print("Process timed out")
```

## Environment Variables

Modifying environment variables for subprocesses:

```python
result = subprocess.run(['printenv'], env={"NEW_VAR": "value"}, capture_output=True, text=True)
print(result.stdout)
```

## Piping Data

### Basic Concept

- **Pipe**: A pipe is a method used in operating systems to enable inter-process communication (IPC). It creates a communication channel where data output by one process can be fed directly as input to another process.

- **Standard Streams**: In the context of subprocess piping, the primary focus is on standard streams - standard input (stdin), standard output (stdout), and standard error (stderr).

### Implementation in Python

- Python’s `subprocess` module can create pipes between processes using the `Popen` class and redirect these standard streams.

- You can create a pipe by setting the `stdout` of one process to `subprocess.PIPE`, and then use this output as the `stdin` of another process.

Example:

```python
from subprocess import Popen, PIPE

# Create the first process
p1 = Popen(["ls", "-l"], stdout=PIPE)

# Use the output of p1 as input for p2
p2 = Popen(["grep", "txt"], stdin=p1.stdout, stdout=PIPE)

# Close the output of p1 to signal that we're done with it
p1.stdout.close()

# Get the output from p2
stdout, stderr = p.communicate()
print(stdout.decode())

# Access the return code
return_code = p2.returncode
print("Return code:", return_code)
```

This example lists all files, then filters to show only those containing 'txt'.

## shell=True Argument

### What is shell=True?

When you set `shell=True` in `subprocess.run()` or `Popen()`, it means that the command you pass is executed through the shell (like bash on Linux or cmd on Windows). This allows you to leverage shell-specific features such as wildcard expansion, variable substitution, command chaining, and more.

For example:

```python
subprocess.run("echo $HOME", shell=True)
```

This command prints the home directory using shell's variable substitution feature.

### Why Use shell=True?

- **Convenience**: It can be more convenient for complex shell commands.
- **Shell Features**: It allows the use of shell features like pipe `|`, logical operators `&&` and `||`, wildcards `*`, etc.
- **Command String**: It enables executing the command as a single string, which can sometimes be simpler to construct.

### Risks and Why to Avoid

**Security Vulnerability**: The most significant risk of using shell=True is the potential for shell injection attacks. If you construct a shell command by concatenating strings, and one of those strings is untrusted input (like user input), you might inadvertently create a security hole. For example, if you concatenate a user-provided filename into a shell command, a malicious user could provide a filename that includes shell commands, leading to arbitrary command execution.

### Example of a Shell Injection Vulnerability

Consider a Python script that constructs a command to list files in a directory specified by the user:

```python
import subprocess

user_input = input("Enter directory to list: ")
command = f"ls {user_input}"
subprocess.run(command, shell=True)
```

If the user enters a directory name, the script works as intended. However, if an attacker inputs something like ; rm -rf /, the command becomes ls ; rm -rf /. When executed, it will list the files in the current directory and then proceed to delete everything on the root filesystem (if run with sufficient privileges).

### Avoid shell=True

Avoid `shell=True` When Possible: Use `shell=False` (the default) to avoid security issues related to shell injection. This is especially important when the command includes input from untrusted sources.