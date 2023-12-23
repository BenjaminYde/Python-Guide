# Logging

## Understanding the Logging Module

The `logging` module in Python offers a standard way for applications to log events. It can be used to report errors and exceptions, debug information, or other important events.

## Log Levels

Python defines several log levels, which indicate the severity of events.   
Here's a breakdown of the different logging levels, from least to most severe:

- **DEBUG**: Detailed information, typically of interest only when diagnosing problems.
  
- **INFO**: Confirmation that things are working as expected.
  
- **WARNING**: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., 'disk space low'). The software is still working as expected.
  
- **ERROR**: Due to a more serious problem, the software has not been able to perform some function.
  
- **CRITICAL**: A serious error, indicating that the program itself may be unable to continue running.

## Basic Concepts

- **Loggers**: The primary interface that your application will use. Loggers expose the interface that application code directly uses.

- **Handlers**: Send the log records (created by loggers) to the appropriate destination.

- **Filters**: Provide a finer-grained facility for determining which log records to output.

- **Formatters**: Specify the layout of log records in the final output.

### Loggers

Loggers are the entry point of the logging system. Each instance of a `Logger` class provides an interface through which applications can log events. A logger can have multiple handlers, which helps in directing the same log message to different outputs (console, file, etc.). Loggers are organized in a hierarchical structure based on their names using a dot-separated hierarchical structure (e.g., "main.sub"), which means that "sub" is a child of "main".

Key points about loggers:

- **Creation**: Loggers are created using the logging.getLogger(name) factory method.

- **Levels**: Loggers have a concept of levels of severity for events (DEBUG, INFO, WARNING, ERROR, CRITICAL).

- **Propagation**: By default, loggers propagate messages to their parent loggers unless the propagation is set to False.

- **Configuration**: Loggers can be configured to filter and direct log messages independently from other loggers.

### Handlers

Handlers are responsible for dispatching the log messages to specific destinations. You can add multiple handlers to a logger to route log output to different locations. Common handler types include `StreamHandler` (for console output), `FileHandler` (for writing to files), `SocketHandler` (for sending over the network), and more specialized handlers like `RotatingFileHandler` or `TimedRotatingFileHandler` (for log file rotation).

Key points about handlers:

- **Destination**: Each handler can be set to output log records to a different destination.

- **Level**: Handlers can also have levels, allowing for different logging levels to be set for each handler.

- **Formatter**: Each handler can have its own formatter to control the output format of its log messages.

### Filters

Filters provide a mechanism for fine-grained control over which log records are passed from logger to handler. They are used to provide additional control over which log records are output by a handler or logger.

Key points about filters:

- **Criteria**: Filters can be based on any criteria you can think of: the content of the log message, the severity, contextual information, etc.

- **Customization**: You can implement custom filter logic by subclassing the `Filter` class and overriding its `filter()` method.

### Formatters

Formatters specify the layout of log records in the final output. They are associated with handlers which use them to turn a log record into a string that can be interpreted by the handler's destination (e.g., writing a formatted string to console or a file).

Key points about formatters:

- **Structure**: Formatters define the structure and content of the log message, such as timestamps, logger names, severity levels, and the actual log message.

- **Custom Formats**: You can define a custom format string that includes various attributes of log records, such as asctime (formatted timestamp), levelname (text logging level), message (log message), and more.

## Basic Logging

### Creating a Logger

You can start logging by importing the module and using basic functions:

```python
import logging

# enable the following to display debug & info messages too
#logging.getLogger().setLevel(logging.DEBUG)

logging.debug('This is a debug message') # will not be displayed
logging.info('Informational message') # will NOT be displayed
logging.warning('Warning occurred')
logging.error('An error has happened')
logging.critical('Critical issue')
```

In your code, the debug and info messages are less severe than the default `WARNING` level, so they are not displayed.

By setting the level to `DEBUG`, you are telling the logging system to handle all log messages from `DEBUG` level and above, thus all your log messages will be displayed in the console.

Never call `logging.basicConfig(...)` because this function can only be called once.    
The second time this is called it will have no effect: 

```python
logging.basicConfig(level=logging.INFO)
```

### Creating a Handler

Setting up 2 log handlers:

```python
# Continue from the logger example above

# Create handlers
console_handler = logging.StreamHandler()  # Log to console
file_handler = logging.FileHandler('app.log')  # Log to a file

# Set level for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

Now we can start logging:

```python
# These messages will go to different destinations depending on their level
logger.debug('DEBUG: This will go to console')
logger.warning('WARNING: This will go to console')
logger.error('ERROR: This will go to both console and file')
```

### Creating a Filter

Let's say we want to exclude debug logs:

```python
# Continue from the logger and handler examples above

# Define a filter
class NoDebugFilter(logging.Filter):
    def filter(self, record) -> bool:
        # Only allow log messages that are not DEBUG
        return record.levelno != logging.DEBUG

# Add filter to console handler
console_handler.addFilter(NoDebugFilter())

# Now, DEBUG messages won't be printed to the console
logger.debug('DEBUG: This debug message will not be shown in the console')
logger.warning('WARNING: This debug message will not be shown in the console')
```

### Formatting Our Messages

```python
# Continue from the logger, handler, and filter examples above

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Now, log messages will include the timestamp, logger name, level, and message
logger.info('This info message will have a specific format in console and file')
```

## Logging to a File

Instead of displaying log messages to the console, you can write them to a file:

```python
logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO)
logging.info('This will get logged to a file')
```

## Adding contextual data to your logs

Contextual logging is about including additional information in log messages that can help to identify and understand the context in which the log message was generated. 

### f-strings

f-strings allow you to embed expressions inside string literals, using curly braces `{}`.

```python
import logging

user_id = 'user123'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('myapp')

logger.info(f'User action performed by {user_id}')
```

#### Limitations of f-strings

- **Performance**: The f-string is always evaluated, even if the logging level means the message will not be emitted. This can lead to performance overhead.

- **Lack of Lazy Evaluation**: Unlike % formatting or the extra parameter, which are only processed if the message is to be logged, f-strings don't provide this optimization.

### % Formatting

The `%` formatting in loggers is a way to delay string interpolation until it's necessary (lazy evaluation). This is the traditional way to insert contextual information into log messages.

```python
logger.info('User action performed by %s', user_id)
```

#### Limitations of % formatting

- **Readability**: For complex log messages, % formatting can become less readable compared to f-strings.

- **Verbose for Multiple Variables**: It can be verbose if you have multiple variables to log because you need to pass them all as extra arguments.

- **Typing Mistakes**: It's prone to errors if the format string doesn't match the type of the argument.

### Extra Field (dict)

The `extra` parameter allows you to pass a dictionary to the `Logger` method, which then gets added to the `LogRecord` object.

```python
logger.info('User action performed', extra={'user_id': user_id})
```

#### Limitations of using the extra field

- **Key Clashes**: The keys used in the extra dictionary cannot clash with the keys used by LogRecord (like msg, args, etc.). If you accidentally use the same name, it can lead to unexpected behavior or errors.

- **Missing Keys in Formatter**: If your formatter expects a certain key from the extra dict and it's not provided, you will get an error when the logger attempts to format the message.

  - This can be fixed by using the `python-json-logger` library which allows you to add context to your logs through the extra property without needing to modify the log format.

- **Maintenance**: You must ensure that the extra dictionary is consistently used and maintained across different logging calls, which can add to maintenance overhead.

- **Limited to Dictionary**: The extra parameter must be a dictionary. You cannot pass other types of context directly without wrapping them in a dictionary.

## Optimization: Avoid Expensive Functions

**Lazy evaluation** refers to the programming concept where an expression is not evaluated until its value is needed. In the context of logging, this means constructing the log message string only if that message will actually be logged, based on the current logging level.

### % Formatting

When using `%` formatting with the logging module, the message string is constructed only if the logging level is such that the message will be emitted. This is because the formatting operation is handled internally by the logging module, which first checks the log level before formatting the message.

Here's an example using % formatting, which benefits from lazy evaluation:

```python
logger.debug('This is a debug message with a %s', expensive_func())
```

If the logger's level is higher than DEBUG, the message and the associated string formatting are never processed, saving the overhead of the formatting operation.

### f-String Formatting

when using f-strings, the evaluation of the string and its embedded expressions is immediate and happens regardless of whether the log level would allow the message to be emitted. This means that the computation to create the string is done even if the message is never logged.

Here's the same log statement using an f-string:

```python
logger.debug(f'This is a debug message with a {expensive_func()}')
```

**Computing the arguments** passed to the logging method can be **expensive**, and you may want to avoid doing it if the logger will just throw away your event. To decide what to do, you can call the `isEnabledFor()` method which takes a level argument and returns true if the event would be created by the Logger for that level of call. You can write code like this:

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Message with %s, %s', expensive_func)
```

If the logger’s threshold is set above DEBUG, the calls to expensive_func() is never made.

## Automatically Rotate log files

When you're logging to files, you need to be careful not to allow the file grow too large and consume a huge amount of disk space. By rotating log files, older logs can be compressed or deleted, freeing up space and reducing the risk of disk usage issues. Additionally, rotating logs helps to maintain an easily manageable set of log files, and can also be used to reduce the risk of sensitive information exposure by removing logs after a set period of time.

### RotatingFileHandler

This handler rotates the log files based on the file size.

```python
import logging
from logging.handlers import RotatingFileHandler

# Set up a logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Add a RotatingFileHandler
handler = RotatingFileHandler(
    'my_log.log',            # Log file name
    maxBytes=1e6,            # Max size of a log file (1 MB)
    backupCount=5,           # Number of backup files to keep
)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

# Log something
logger.debug('This is a debug message')
```

In the example above, the log file named '`my_log.log`' will be rotated out when it reaches 1 MB in size. At that point, the current my_log.log is renamed to `my_log.log.1`, and a new `my_log.log` is created for future log messages. 

### TimedRotatingFileHandler

This handler rotates the log files at certain timed intervals.

```python
import logging
from logging.handlers import TimedRotatingFileHandler

# Set up a logger
logger = logging.getLogger('my_timed_logger')
logger.setLevel(logging.DEBUG)

# Add a TimedRotatingFileHandler
handler = TimedRotatingFileHandler(
    'timed_log.log',         # Log file name
    when='midnight',         # Rotate at midnight
    interval=1,              # Rotate every day
    backupCount=30,          # Keep 30 days of logs
)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

# Log something
logger.debug('This is a debug message')
```

Here, `timed_log.log` will be rotated each day at midnight. The old log file will be renamed to include a timestamp and a new log file will be created for the new day. The `backupCount` parameter ensures that only the last 30 days of logs are kept.