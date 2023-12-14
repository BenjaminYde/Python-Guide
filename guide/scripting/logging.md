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

## Logging to a File

Instead of displaying log messages to the console, you can write them to a file:

```python
logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO)
logging.info('This will get logged to a file')
```