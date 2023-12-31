# asyncio Module

`asyncio` is a vital part of the Python standard library, introduced in Python 3.4. It's designed to write concurrent code using the `async/await` syntax and is particularly effective for developing scalable network applications. The library enables the efficient execution of I/O-bound and high-level structured network code, operating in a single-threaded, single-process design.

## Core Concepts of asyncio

### Event Loop

The central feature of asyncio is the event loop, which is the core of every asyncio application. It's responsible for executing asynchronous tasks, managing network IO requests, running subprocesses, handling OS signals, and more. Essentially, the event loop is the mechanism that enables the asynchronous execution of code.

**How it Works**: The event loop runs in a loop (as the name suggests), continuously collecting and dispatching events. It keeps track of all the running tasks and when a task yields control (typically using `await`), the loop pauses it and switches to another task, resuming the first task when it's ready to continue.

```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)  # Simulates a non-blocking wait
    print('World')

asyncio.run(main())  # Starts the event loop and executes 'main'
```

**Example Explained**: In the provided example, `asyncio.run(main())` starts the event loop and runs the `main` coroutine. Inside `main`, the `await` `asyncio.sleep(1)` call makes the coroutine pause for 1 second. During this pause, the event loop could run other tasks (if any). After 1 second, it resumes the `main` coroutine, which then prints 'World'.

### Coroutines

Coroutines are at the heart of asyncio. They are special functions that can be paused and resumed, allowing other code to run in the meantime.

**Async/Await Syntax**: Defined with `async def`, coroutines are designed to work with `await`, which pauses the coroutine's execution until the awaited object (often a coroutine) completes. This non-blocking behavior is what allows `asyncio` to handle I/O operations efficiently.

```python
async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)  # Simulates a time-consuming asynchronous operation
    print("Done fetching")
    return {'data': 1}
```

**Example Explained**: In the `fetch_data` coroutine, `await asyncio.sleep(2)` pauses the coroutine. This is the point where the event loop can run other tasks. After 2 seconds, the event loop resumes `fetch_data`, which then completes and returns a dictionary.

### Tasks

Tasks are used to schedule coroutines concurrently. They wrap coroutines and keep track of their state and result, allowing the event loop to manage their execution properly.

**Concurrency with asyncio**: By default, coroutines are not run in parallel but are executed sequentially. To run them concurrently, you use `asyncio.create_task()`, which schedules the coroutine to be run on the event loop.

```python
async def main():
    task = asyncio.create_task(fetch_data())  # Schedules 'fetch_data' for execution
    await task  # Waits for the completion of the task

asyncio.run(main())
```

**Example Explained**: In your main function, `asyncio.create_task(fetch_data())` schedules the `fetch_data` coroutine to run as a task. The `await` task then waits for its completion. While `fetch_data` is sleeping, the event loop could potentially run other tasks.

### Awaiting

The `await` keyword is essential for working with `asyncio`. It's used to yield control from a coroutine back to the event loop, which can then run other tasks until the awaited operation is complete.

**How await Works**: When a coroutine `await`'s another coroutine or an awaitable object, it pauses and gives control back to the event loop. The event loop resumes the coroutine once the awaited operation is finished.

```python
async def main():
    data = await fetch_data()  # Pauses 'main' until 'fetch_data' completes
    print(data)

asyncio.run(main())
```

**Example Explained**: In your `main` function, `data = await fetch_data()` pauses `main` and waits for `fetch_data` to complete. During this time, the event loop could run other tasks. Once `fetch_data` finishes, `main` resumes and prints the data.

### Full Example'

Let's say we want to simulate fetching data from a remote source, handling exceptions, and incorporating asynchronous function calls within the coroutine. Here's an enhanced version of the `fetch_data` coroutine:

```python
import asyncio

# Simulating a network request
async def fetch_from_remote(url):
    print(f"Fetching data from {url}")
    await asyncio.sleep(1)
    if "2" in url: # simulate a network error with http://example.com/data2
        raise Exception("Network Error")
    return f"Data from {url}"

# Extended coroutine
async def fetch_data():
    urls = ["http://example.com/data1", "http://example.com/data2"]
    results = []

    print("Start fetching")

    for url in urls:
        try:
            # Fetching data from each URL
            data = await fetch_from_remote(url)
            results.append(data)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            results.append(None)  # Handling the error by appending None

    print("Done fetching")
    return results

# Running the coroutine
async def main():
    fetched_data = await fetch_data()
    print(f"Fetched data: {fetched_data}")

asyncio.run(main())
```

In this example:

1. **fetch_from_remote**: This coroutine simulates a network request to a given URL. It randomly introduces a delay and sometimes raises an exception to simulate network errors.

2. **fetch_data**: This is the main coroutine. It now includes multiple URLs to fetch data from. It iterates over the URLs, calls `fetch_from_remote` for each, and handles any exceptions that might occur during the fetch operation.

3. **Error Handling**: The `try...except` block in `fetch_data` is used to handle potential exceptions from `fetch_from_remote`. If an error occurs, it prints a message and appends `None` to the results list, ensuring that the coroutine can continue executing even after an error.

4. **main**: This is the entry point for running the coroutine using` asyncio.run()`. It awaits the `fetch_data` coroutine and then prints the fetched data.

## Common Methods

There are several other important functions and concepts in `asyncio` that are useful to understand. Each serves a different purpose in managing and orchestrating asynchronous operations:

### asyncio.create_task

`asyncio.create_task` is used to schedule the execution of a coroutine. It returns a `Task` object, which is a subclass of `Future`.

**Usage**: This is the standard way to run coroutines concurrently when you need to have a handle to the tasks for later manipulation (like cancelling).

Syntax: 

```python
task = asyncio.create_task(my_task())
```

Example:

```python
async def my_task():
    await asyncio.sleep(1)
    print("Task completed")

async def main():
    task = asyncio.create_task(my_task())
    await task

asyncio.run(main())
```

### asyncio.gather

`asyncio.gather` is used for the following purposes:

- **Concurrent Execution**: It allows you to run multiple asynchronous tasks concurrently. This is particularly useful when you have several operations that can be performed in parallel, such as making multiple network requests or performing I/O operations.

- **Result Aggregation**: It not only runs these tasks concurrently but also aggregates their results into a single list, preserving the order of tasks as they were passed to gather.

Syntax:

```python
results = await asyncio.gather(*tasks)
```

Example:

```python
import asyncio

async def task1():
    await asyncio.sleep(2)
    return 'Result of task1'

async def task2():
    await asyncio.sleep(1)
    return 'Result of task2'

async def main():
    results = await asyncio.gather(task1(), task2())
    for result in results:
        print(result)

asyncio.run(main())
```

### asyncio.wait

`asyncio.wait` is used to wait for the completion of multiple `Future` or coroutine objects. Unlike `gather`, it does not necessarily return the results of these awaitables.

- **Flexibility in Handling Task Completion**: asyncio.wait allows you to specify how you want to wait for the tasks to complete. For example, you can choose to continue as soon as any task is done, all tasks are done, or after a certain timeout.

- **Returns Two Sets**: It returns two sets of tasks: one for completed (or failed) tasks and another for pending tasks. This is useful for scenarios where you want to perform different actions based on whether tasks are completed or still pending.

- **Independent Task Handling**: You can handle the results or exceptions of each task individually, which offers more control in case of tasks that might result in exceptions.

Syntax:

```python
done, pending = await asyncio.wait(my_task, timeout=None, return_when=FIRST_COMPLETED)
```

Example:

```python
import asyncio

async def task(n):
    await asyncio.sleep(n)
    return n

async def main():
    tasks = [
        asyncio.create_task(task(1)), 
        asyncio.create_task(task(2)), 
        asyncio.create_task(task(3))
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for d in done:
        print(f"Task completed with result: {d.result()}")

    for p in pending:
        print("Cancelling a pending task")
        p.cancel()

asyncio.run(main())
```

### asyncio.wait_for

`asyncio.wait_for` is used to set a timeout for an awaitable. If the awaitable completes within the timeout, `wait_for` returns its result. Otherwise, it cancels the task and raises `asyncio.TimeoutError`.

**Usage**: It's useful for setting a maximum time limit for an operation, beyond which it shouldn't block other operations.

Syntax: 

```python
result = await asyncio.wait_for(my_task, timeout)
```

Example:

```python
async def long_running_task():
    await asyncio.sleep(10)

async def main():
    try:
        await asyncio.wait_for(long_running_task(), timeout=2)
    except asyncio.TimeoutError:
        print("The task took too long to complete")

asyncio.run(main())
```

### asyncio.as_completed

`asyncio.as_completed` is used to iterate over asynchronous tasks as they are completed, regardless of the order in which they were started.

**Usage**: This function is beneficial when you want to start processing the results of tasks as soon as each one is completed, without waiting for all of them to finish.

Syntax:

```python
for routine in asyncio.as_completed(my_task, timeout=None):
    earliest_result = await routine
```

Example:

```python
async def task(delay):
    await asyncio.sleep(delay)
    return delay

async def main():
    tasks = [task(3), task(1), task(2)]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"Completed task with result: {result}")

asyncio.run(main())
```

### asyncio.ensure_future

`asyncio.ensure_future` ensures you are working with a Future object. It's useful in scenarios where you have a coroutine or an awaitable object, and you need to ensure it is wrapped as a Future.

**Usage**: It's useful for converting a coroutine or a coroutine-like object into a Future that can be awaited. This can be helpful when dealing with older code that returns futures rather than coroutines.

Syntax: 

```python
future = asyncio.ensure_future(task)
```

Example:

```python
import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    return "Coroutine result"

async def main():
    # Wrapping a coroutine into a Future object
    future = asyncio.ensure_future(my_coroutine())

    # Do other stuff here if needed
    # ...

    # Wait for the future to be done and get its result
    result = await future
    print(result)

asyncio.run(main())
```

## Cancelling Tasks

Suppose you have a task that periodically checks for updates on a server. You want this task to run indefinitely, but you also want the ability to cancel it under certain conditions (e.g., when shutting down your application or when it's no longer needed).

```python
import asyncio

async def check_updates(interval):
    try:
        while True:
            # Simulate a task that checks for updates
            print("Checking for updates...")
            await asyncio.sleep(interval)
    except asyncio.CancelledError:
        print("Update check has been cancelled")
        # Perform any cleanup here
        raise

async def main():
    # Create the task
    update_task = asyncio.create_task(check_updates(0.75))

    # Run the task for a while
    await asyncio.sleep(3)

    # Cancel the task
    update_task.cancel()

    try:
        # Wait for the cancellation to complete
        await update_task
    except asyncio.CancelledError:
        print("Main: The update task was cancelled")

# Run the main coroutine
asyncio.run(main())
```

## Using async with

The `async with` statement in Python, introduced in Python 3.5, is part of the asynchronous programming features of the language. It is used to work with asynchronous context managers, which are similar to regular (synchronous) context managers but designed for use in 
asynchronous code.

### Asynchronous Context Managers

An asynchronous context manager is an object that defines `__aenter__` and `__aexit__` methods to set up and tear down resources asynchronously. These methods are coroutines and must be defined with the async def syntax.

- `__aenter__`: This coroutine is called when entering the context (the block of code after the async with statement). It performs setup actions and returns an object (if needed) for use within the context.

- `__aexit__`: This coroutine is called when exiting the context. It handles cleanup actions. It accepts three arguments: exc_type, exc_value, and traceback, which describe an exception that occurred in the block if any.

### Using async with

The `async with` statement is used in asynchronous functions (defined with `async def`) to manage resources asynchronously. It ensures that the setup and cleanup code is executed, even if an exception occurs within the block.

Syntax:

```python
async with expression as variable:
    # Asynchronous operations
```

Example:

Here's an example of using `async with` with an asynchronous file I/O operation:

```python
import aiofiles

async def read_file_async(filename):
    async with aiofiles.open(filename, 'r') as file:
        return await file.read()
```

### Creating a Custom Asynchronous Context Manager

First, we'll define an asynchronous context manager class for a hypothetical database connection:

```python
import asyncio

class AsyncDatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    async def connect(self):
        # Simulate an asynchronous connection to a database
        await asyncio.sleep(1)
        print(f"Connected to database: {self.db_name}")

    async def close(self):
        # Simulate closing the database connection
        await asyncio.sleep(1)
        print(f"Connection to {self.db_name} closed")

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
```

In this class:

connect and close methods simulate asynchronous operations to open and close a database connection.

- `__aenter__` method establishes the connection.
- `__aexit__` method closes the connection, ensuring proper cleanup.

Now, let's use this context manager in an asynchronous function:

```python
async def use_database(db_name):
    async with AsyncDatabaseConnection(db_name) as db_conn:
        # Perform database operations here
        print(f"Using {db_conn.conn}")
        await asyncio.sleep(2)  # Simulate a database operation

# Run the async function
asyncio.run(use_database("MyDatabase"))
```

Explantation:

- When the `async with` `AsyncDatabaseConnection("MyDatabase")` line is executed, it calls the `__aenter__` method of `AsyncDatabaseConnection`, which establishes a connection to the database.
- The block of code within the `async with` statement represents operations you might perform with the database connection.
- Once this block is executed (or if an exception occurs), the `__aexit__` method is automatically called, closing the database connection.

## Synchronization Primitives

In `asyncio`, synchronization primitives are used to manage access to shared resources and coordinate the execution of coroutines in a concurrent environment. These primitives are essential for preventing race conditions and ensuring data consistency when multiple coroutines access or modify shared data. Let's explore some of the key synchronization primitives provided by `asyncio`.

### Lock

A `Lock` is a synchronization primitive that can be used to guard access to a shared resource. Only one coroutine at a time can acquire a lock. If a coroutine tries to acquire a lock that is already held by another coroutine, it will be paused until the lock is released.

**Usage**: Locks are commonly used to ensure that only one coroutine is executing a particular section of code at a time. This is particularly useful for protecting access to a shared resource, such as a database or a file.

Syntax:

```python
lock = asyncio.Lock()

async def critical_section():
    async with lock:
        # Access shared resources
        pass
```

Example:

```python
import asyncio

lock = asyncio.Lock()

async def update_shared_resource(num):
    async with lock:
        # Simulate modifying a shared resource
        print(f"Resource accessed by coroutine {num}")
        await asyncio.sleep(1)

async def main():
    # Start multiple coroutines that access the same resource
    coroutines = [update_shared_resource(i) for i in range(5)]
    await asyncio.gather(*coroutines)

asyncio.run(main())
```

### Event

An `Event` is a synchronization primitive that can be used to signal between coroutines. An event object manages an internal flag that can be set to `True` or `False`. Coroutines can wait for an event to be set before continuing.

**Usage**: Events are useful for signaling between coroutines, allowing one coroutine to pause execution until another coroutine signals that it can continue. This is useful for coordinating the start and stop of certain operations between different coroutines.

Syntax:

```python
event = asyncio.Event()

async def waiter():
    await event.wait()
    # Continue after the event is set

async def setter():
    # Set the event, waking up the waiter
    event.set()
```

Example:

```python
import asyncio

event = asyncio.Event()

async def waiter():
    print("Waiting for the event")
    await event.wait()
    print("Continuing after the event is set")

async def setter():
    await asyncio.sleep(2)  # Simulate some processing
    print("Setting the event")
    event.set()

async def main():
    await asyncio.gather(waiter(), setter())

asyncio.run(main())
```

### Semaphore

A `Semaphore` is a more advanced synchronization primitive that is used to limit access to a shared resource. A semaphore has an internal counter that is decremented each time a coroutine acquires the semaphore and incremented when the semaphore is released. If the counter reaches zero, coroutines trying to acquire it will wait until other coroutines release the semaphore.

**Usage**: Semaphores are useful for limiting access to resources that can handle only a limited number of concurrent accesses, such as a network connection pool.

Syntax:

```python
sem = asyncio.Semaphore(2)

async def access_resource():
    async with sem:
        # Access the limited resource
        pass
```

Example:

```python
import asyncio

sem = asyncio.Semaphore(3)  # Limit to 3 concurrent coroutines

async def access_resource(num):
    async with sem:
        print(f"Resource being accessed by coroutine {num}")
        await asyncio.sleep(2)  # Simulate a task using the resource
    print(f"Coroutine {num} released the resource")

async def main():
    coroutines = [access_resource(i) for i in range(10)]
    await asyncio.gather(*coroutines)

asyncio.run(main())
```

### Condition

A `Condition` is a synchronization primitive that allows coroutines to wait for certain conditions to be met. Conditions are associated with a `Lock` that must be held when the condition's `wait()` and `notify()` methods are called.

**Usage**: Conditions are useful in scenarios where you need coroutines to wait for certain states or conditions to change before proceeding. This is often used in producer-consumer problems.

```python
condition = asyncio.Condition()

Syntax:

async def consumer():
    async with condition:
        await condition.wait()
        # Continue after the condition is notified

async def producer():
    async with condition:
        # Modify shared state
        condition.notify()
```

Example:

```python
import asyncio

condition = asyncio.Condition()
queue = []

async def consumer():
    async with condition:
        while not queue:
            print("Consumer waiting")
            await condition.wait()
        item = queue.pop(0)
        print(f"Consumer got item: {item}")

async def producer():
    async with condition:
        for i in range(5):
            queue.append(i)
            condition.notify()  # Notify the consumer
            await asyncio.sleep(1)  # Simulate producing time

async def main():
    await asyncio.gather(producer(), consumer())

asyncio.run(main())
```

## Asynchronous Iterators and Generators

```python
async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for item in async_generator():
        print(item)
```

## Streams 

Streams in `asyncio` provide an abstraction for working with network IO. They allow you to write asynchronous code for handling network connections, such as reading from and writing to sockets, without directly dealing with the lower-level details of the protocol.

Streams are particularly useful for developing network applications where you need to handle multiple connections efficiently.

### Core Concepts of asyncio Streams

The main classes used in `asyncio` streams are `StreamReader` and `StreamWriter`. 
`StreamReader` is used for reading data from a stream, while `StreamWriter` is for writing data to a stream.

`TCP` and `UDP`: asyncio supports both TCP (reliable, connection-oriented protocol) and UDP (unreliable, connectionless protocol) streams.

### Creating a TCP Server

You can use `asyncio.start_server` to create an asynchronous TCP server. This server will handle incoming connections and can read from and write to these connections.

Example:
```python
import asyncio
from asyncio import StreamReader, StreamWriter

async def server_handle_client(reader: StreamReader, writer: StreamWriter):
    # Wait for message from a client
    data = await reader.read(100)  # Read up to 100 bytes
    message = data.decode('utf8')
    address = writer.get_extra_info('peername')
    print(f"Server: Received {message} from {address}")

    # Send a response to the client
    print("Server: Sending response to client...")
    new_message = "Sever is termenating..."
    new_data = new_message.encode('utf8')
    writer.write(new_data)
    await writer.drain()

    # Close the connection
    writer.close()

async def main():
    server = await asyncio.start_server(server_handle_client, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
```

In this example, asyncio.start_server is used to create a server that listens on localhost (`127.0.0.1`) on port `8888`. For each client connection, `server_handle_client` coroutine is called with `StreamReader` and `StreamWriter` instances.

### Creating a TCP Client

To create a TCP client that connects to a server, use `asyncio.open_connection`. This returns `StreamReader` and `StreamWriter` objects for communication with the server.

Example:


```python
import asyncio

async def tcp_echo_client():
    # Connect to the server
    await asyncio.sleep(1)  # Give the server time to start
    reader, writer = await asyncio.open_connection(addres, port)

    # Send a message to the server
    print("Client: Sending message...")
    message = 'Hello World!'
    writer.write(message.encode('utf8'))
    await writer.drain()

    # Receive a response
    data = await reader.read(100)
    print(f"Client: Reveived from Server: {data.decode('utf8')}")

    # Close the connection
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client())
```

In this client example, `asyncio.open_connection` is used to connect to the server running on `127.0.0.1:8888`. The client sends a message, waits for a response, and then closes the connection.

### Handling UDP

For UDP, `asyncio` provides the `loop.create_datagram_endpoint` method to create a datagram endpoint for sending and receiving UDP packets.

Example:

```python
import asyncio

class EchoUDP(asyncio.DatagramProtocol):
    def datagram_received(self, data, address):
        print(f"Received {data.decode()} from {address}")
        self.transport.sendto(data, address)

async def main():
    loop = asyncio.get_running_loop()

    # One protocol instance will be created to serve all client requests
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoUDP(),
        local_address=('127.0.0.1', 9999))

    await asyncio.sleep(3600)  # Serve for 1 hour

    transport.close()

asyncio.run(main())
```

In this UDP example, an instance of `EchoUDP`, which is a subclass of `asyncio.DatagramProtocol`, is created. This server listens on `127.0.0.1:9999` and echoes back any data it receives.

## Subprocesses

`asyncio` subprocesses are a feature of the `asyncio` library in Python that allows you to run and interact with external processes asynchronously. This is particularly useful for executing shell commands, running external programs, and handling their input/output without blocking the main asyncio event loop.

### Core Features

- **Non-blocking Operations**: asyncio subprocess functions are non-blocking and don't freeze the asyncio event loop while waiting for the subprocess to complete.

- **Asynchronous Communication**: You can asynchronously communicate with a subprocess through its standard input, output, and error streams.

- **Integration with asyncio Tasks**: Subprocesses can be managed as asyncio tasks, which allows them to fit neatly into the asyncio framework of coroutines and event loops.

### Creating and Managing Subprocesses

`asyncio.create_subprocess_exec`: Runs a program specified by a series of arguments. More secure and often preferable for running known programs.

```python
process = await asyncio.create_subprocess_exec(
    'ls', '-l',
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE)
```

`asyncio.create_subprocess_shell`: Runs a command specified as a single string through the shell. More convenient for complex commands, but less secure due to shell injection risks.

```python
process = await asyncio.create_subprocess_shell(
    'ls -l | grep test',
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE)
```

### Example: Asynchronous Ping to Multiple Hosts

We'll write a coroutine that pings a given host and reports back the result. Then, we'll use this coroutine to ping several hosts concurrently.

```python
import asyncio

async def ping(host):
    # Build the ping command
    cmd = f'ping -c 1 -W 1 {host}' # try 1x, max wait time 1 sec

    # Start the subprocess
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        # Success, the host is reachable
        print(f"Host {host} is reachable")
    else:
        # An error occurred, the host might be unreachable
        print(f"Host {host} is unreachable")
        if stderr:
            print(f"Error: {stderr.decode().strip()}")

async def main():
    hosts = ["8.8.8.8", "192.168.1.1", "github.com"]
    await asyncio.gather(*(ping(host) for host in hosts))

asyncio.run(main())
```