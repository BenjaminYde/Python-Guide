# multiprocessing Module

## Basics of Multiprocessing

The `multiprocessing` module in Python allows for the execution of multiple processes concurrently. It's particularly useful for CPU-bound applications, leveraging multiple CPU cores for parallel processing. Unlike threading, multiprocessing in Python involves running separate memory spaces.

### Use Cases

- **Data Processing**: Multiprocessing is ideal for scenarios where you have to process large datasets or perform complex mathematical calculations that can be parallelized.

- **Concurrent Execution**: Running multiple operations that are independent of each other and can be executed simultaneously, such as batch processing tasks.

## Processes

### What is a Process?

A **process** is an independent instance of a Python interpreter. The multiprocessing module provides an API similar to the threading module but uses processes instead of threads. This bypasses the Global Interpreter Lock (GIL) and allows full parallelism.

#### Advantages:

- **True Parallelism**: Each process runs in its own Python interpreter and memory space, enabling parallel CPU computation.

- **Bypassing the GIL**: Avoids the limitations of the GIL in CPython, which only allows one thread to execute Python bytecode at a time.

- **Improved Stability**: A crash in one process does not affect other processes.

#### Disadvantages:

- **Higher Overhead**: Processes are heavier than threads and consume more system resources.

- **Inter-process Communication**: Communication between processes is more complex and requires serialization (e.g., using queues or pipes).

### Creating a Process

To create a new process, use the `Process` class from the `multiprocessing` module.

Example:

```python
from multiprocessing import Process

def print_numbers():
    for i in range(1, 6):
        print(i)

# Creating a process
process = Process(target=print_numbers)

# Starting the process
process.start()

# Wait for the process to complete
process.join()

print("Process finished execution.")
```

### Terminating Processes

Sometimes it's necessary to terminate a process forcibly, especially if it's stuck or misbehaving. Use `process.terminate()` to stop a process. It's abrupt and should be used carefully.

Example:

```python
from multiprocessing import Process
import time

def endless_task():
    while True:
        print("Running...")
        time.sleep(1)

def run():
    p = Process(target=endless_task)
    p.start()
    time.sleep(5)
    p.terminate()
    p.join()

run()
```

### Daemon Processes

Daemon processes are processes that run in the background.

- **Non-blocking**: A daemon process does not block the main program from exiting and is killed once all non-daemon processes have completed.
- **Usage**: Useful for background tasks that do not need to keep the program running.

```python
from multiprocessing import Process
import time

def daemon_process():
    while True:
        print("Daemon process running...")
        time.sleep(1)

def run():
    d = Process(target=daemon_process)
    d.daemon = True
    d.start()

    # Main process runs for a few seconds
    time.sleep(5)

run()
```

Example Explained:

The example starts a daemon process that runs a while loop to print a message every second. Since it's a daemon process, it will stop when the main program (which only sleeps for 5 seconds) exits.

### Common Methods & Properties

#### Methods:

- `start()`: 
  - Starts the process’s activity. 
  - This must be called at most once per process object.
  - It arranges for the object’s `run()` method to be invoked in a separate process.
- `run()`:
  - Process Activity: Method representing the process’s activity.
  - You may override this method in a subclass.
- `terminate()`:
  - This method is used to stop the process forcibly.
- `join()`:
  - Wait for Process to Finish: Blocks until the process whose join() method is called terminates or until the optional timeout occurs.
  - Useful for process synchronization.
- `is_alive()`:
  - Check Process Status: Returns True if the process is still running.

#### Properties:

- `daemon`:
  - boolean value indicating whether this process should be a daemon process.
  - Daemon processes are abruptly stopped when the program exits.
- `pid`:
  - Returns the process ID.
  - Useful when you need to perform operations outside Python or monitor specific processes.
- `exitcode`:
  - Exit Code of the Process: The child’s exit code. A None value indicates that the process hasn’t terminated yet.
  - A negative value -N indicates that the child was terminated by signal N.
- `name`: 
  - The process name, used for identification purposes only.

## Inter-Process Communication (IPC)

The multiprocessing module provides several ways for inter-process communication, mainly `Queue` and `Pipe`.

### Queue

The `Queue` class is a thread and process safe queue that is used for sharing data between processes. It is particularly useful when you have multiple processes and you need to distribute or collect data among them.

- **FIFO Structure**: It's a first-in-first-out (FIFO) data structure. Elements added first will be retrieved first.

- **Thread and Process Safe**: Queue is designed to be safe when used by multiple threads or processes, ensuring data integrity.

Example:

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello from the child process!")

def run():
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # Prints the message from the child process
    p.join()

run()
```

### Pipe

A `Pipe` allows for bidirectional communication between two processes. When a Pipe is created, it returns two connection objects representing the two ends of the pipe.

- **Two-way Communication**: Unlike Queue, which is typically used for one-way communication, Pipe allows for two-way data exchange.

- **Efficiency**: Pipe is generally faster than a Queue because it's a simpler construct, suitable for communication between two processes.

- **Corruption Risk**: It's crucial to avoid having two processes writing to or reading from the same end of the pipe at the same time, as this could lead to data corruption.

- **Creation**: Pipes are created using `multiprocessing.Pipe()`. This returns a pair of Connection objects representing the ends of the pipe.

- **Types**: Pipes can be duplex (two-way communication) or half-duplex (one-way communication). In duplex mode, both ends can send and receive messages. In half-duplex, one end can only send messages, and the other can only receive.

- **Blocking**: Pipe operations can be blocking. The send operation blocks if the pipe's buffer is full, and recv blocks until there is something to read.

Example:

```python
from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection

def worker(connection: Connection):
    connection.send("Hello from the child process!")
    connection.close()

def run():
    parent_connection, child_connection = Pipe()
    p = Process(target=worker, args=(child_connection,))
    p.start()
    print(parent_connection.recv())  # Prints the message from the child process
    p.join()

run()
```

## Shared Memory Objects

In `multiprocessing`, shared memory objects allow processes to share data. This is essential for communication and state sharing between processes.

### Unique Memory Space

When working with Python's `multiprocessing` module, one important concept to understand is that global variables do not behave as they might in a single-process program. 

- **Separate Processes**: In multiprocessing, each process is an independent instance of the Python interpreter. Each process has its own memory space, which means that global variables are not shared between them.

- **Global Variables**: If you define a global variable and then modify it in a child process, the modification will only be visible within that child process. The parent process and other child processes will not see this change.

Example:

```python
from multiprocessing import Process

# A global variable
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter in child process: {counter}")

def run():
    p = Process(target=increment)
    p.start()
    p.join()

    print(f"Counter in main process: {counter}")

run()
```

Output:

```
Counter in child process: 1
Counter in child process: 0
```

### Value and Array

- These are the simplest ways to share data between processes.
- Value is used for a single simple data type, while Array is used for multiple values of a standard type.
- Both are synchronized and can be used safely by multiple processes.

Example:

```python
from multiprocessing import Process, Value, Array

def update_shared_value(shared_value, shared_array):
    # Increment the shared value and each element of the shared array
    shared_value.value += 1
    for i in range(len(shared_array)):
        shared_array[i] += 1

def run():
    # Create a shared integer with initial value 0
    shared_value = Value('i', 0)

    # Create a shared array of integers initialized with values 0 to 4
    shared_array = Array('i', range(5))

    # Create and start 4 processes
    # Each process will update the shared value and array
    processes = [Process(target=update_shared_value, args=(shared_value, shared_array)) for _ in range(4)]
    for p in processes:
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Print the final value of the shared integer and array
    print(f"Shared Value: {shared_value.value}")
    print(f"Shared Array: {list(shared_array)}")

run()
```

Output:

```
Shared Value: 4
Shared Array: [4, 5, 6, 7, 8]
```

### Manager

- Used for creating shared objects of more complex data types like lists, dictionaries, etc.
- Slower than Value and Array but more flexible.

Example:

```python
from multiprocessing import Process, Manager

def adder(shared_list):
    # Adds data to the shared list
    for i in range(5):
        shared_list.append(i)
    print("Adder: Added numbers 0-4 to the list.")

def modifier(shared_list):
    # Modifies data in the shared list
    for i in range(5):
        shared_list[i] = shared_list[i] * 2
    print("Modifier: Doubled the numbers in the list.")

def run():
    # Using Manager to create a shared list
    manager = multiprocessing.Manager()
    shared_list = manager.list()

    # Creating two processes
    p1 = multiprocessing.Process(target=adder, args=(shared_list,))
    p2 = multiprocessing.Process(target=modifier, args=(shared_list,))

    # Starting the processes
    p1.start()
    p1.join()  # Wait for p1 to finish before starting p2

    p2.start()
    p2.join()  # Wait for p2 to finish

    # Accessing the modified list in the main process
    print(f"Final list: {list(shared_list)}")


run()
```

Output:

```
Adder: Added numbers 0-4 to the list.
Modifier: Doubled the numbers in the list.
Final list: [0, 2, 4, 6, 8]
```

## Synchronization

Synchronization is crucial in multiprocessing to manage access to shared resources and to coordinate processes. The `multiprocessing` module in Python provides several synchronization primitives. These are especially important in multiprocessing because each process has its own memory space, and managing the state across processes becomes vital for consistency and data integrity.

`multiprocessing` provides synchronization primitives like `Lock`, `Event`, `Condition`, `Semaphore`, and `Barrier`, similar to those in the `threading` module but designed for processes.

### Lock

A `Lock` in multiprocessing is used to prevent simultaneous access to a shared resource by multiple processes. It is similar to a threading lock but works across different processes, not just threads.

- **Usage**: A process acquires a lock before accessing a shared resource and releases it after the access is complete.

- **Prevents Race Conditions**: Ensures that only one process at a time can access the shared resource, preventing data corruption.

Example:

```python
from multiprocessing import Process, Lock

def printer(item, lock):
    with lock:
        print(item)

def run():
    lock = Lock()
    items = ["tango", "foxtrot", "alpha"]
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()

run()
```

Example Explained:

The example demonstrates using a lock to synchronize access to a print operation, which is a shared resource in this context. Each process acquires the lock before printing and releases it afterward, ensuring orderly access to the standard output.

#### Methods:

- `acquire(blocking=True, timeout=-1)`: Acquires the lock. If blocking is False and the lock cannot be acquired immediately, it returns False.
- `release()`: Releases the lock.

### Event

An `Event` is a simple synchronization object; its primary purpose is to signal between processes. One process signals an event and other processes wait for it.

- **Set and Wait**: A process can wait for an event to be set. When the event is set by any process, all waiting processes are awakened.

- **Usage**: Commonly used for signaling between processes, like indicating that some data is available to process.

Example:

```python
from multiprocessing import Process, Event
import time

def wait_for_event(e):
    print("Waiting for event to be set...")
    e.wait()
    print("Event has been set, continuing with the process.")

def trigger_event(e):
    time.sleep(3)
    print("Triggering event")
    e.set()

def run():
    e = Event()

    p1 = Process(target=wait_for_event, args=(e,))
    p2 = Process(target=trigger_event, args=(e,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

run()
```

#### Methods:

- `set()`: Sets the event, waking up all the processes waiting for it.
- `clear()`: Resets the event. Processes that call wait() once the event is cleared will block.
- `wait(timeout=None)`: Blocks until the event is set. If timeout is provided, it will block for at most timeout seconds.
- `is_set()`: Returns True if the event is set, False otherwise.

### Condition

A Condition is a more complex synchronization tool that combines a lock with a condition variable.

- **Wait and Notify**: Processes can wait for a condition to become true, and a process can notify other processes that the condition is true.

- **Usage**: Useful in producer-consumer problems where the state of the shared resource (like a buffer) changes over time.

Example:

```python
from multiprocessing import Process, Condition
import time

def consumer(cond):
    with cond:
        print("Consumer is waiting.")
        cond.wait()
        print("Consumer consumed the resource.")

def producer(cond):
    with cond:
        time.sleep(2)
        print("Producer produced a resource.")
        cond.notify()

def run():
    condition = Condition()
    p1 = Process(target=consumer, args=(condition,))
    p2 = Process(target=producer, args=(condition,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

run()
```

#### Methods

- `acquire(*args)`: Acquires the underlying lock.
- `release()`: Releases the underlying lock.
- `wait(timeout=None)`: Wait until notified or until a timeout occurs.
- `wait_for(predicate, timeout=None)`: Wait until a condition or timeout. Predicate should be a callable which result will be evaluated in a boolean context.
- `notify(n=1)`: Wake up one or more processes waiting on this condition, if any.
- `notify_all()`:Wake up all processes waiting on this condition.

### Semaphore

A Semaphore is used to control access to a common resource by multiple processes and is often used to enforce a limit on the number of processes that can access the particular resource.

- **Counter-based**: Unlike a lock, which allows only one process to access a shared resource, a semaphore allows a fixed number of processes to access a shared resource.

- **Usage**: Manage a fixed number of resources, like a pool of database connections.

Example:

```python
from multiprocessing import Process, Semaphore
import time

def access_resource(semaphore, process_id):
    with semaphore:
        print(f"Process {process_id} is accessing the resource")
        time.sleep(2)  # Simulate resource access
    print(f"Process {process_id} released the resource")

def run():
    semaphore = Semaphore(2)

    processes = [Process(target=access_resource, args=(semaphore, i)) for i in range(4)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

run()
```

#### Methods

- `acquire(blocking=True, timeout=None)`: Acquire a semaphore.
- `release()`: Release a semaphore, incrementing the internal counter by one.

### Barrier

A Barrier is a synchronization primitive that is used to make a set of processes wait until a certain condition is met.

- **All Processes Wait**: All participating processes wait for each other to reach the barrier. Once all have reached, they are all released.

- **Usage**: Useful for parallel tasks that need to start executing at the same time, like parallel computations that must proceed in lockstep.

Example:

```python
from multiprocessing import Process, Barrier
import time

def task(barrier, process_id):
    print(f"Process {process_id} is performing its task")
    time.sleep(2)
    barrier.wait()
    print(f"Process {process_id} passed the barrier")

def run():
    barrier = Barrier(3)

    processes = [Process(target=task, args=(barrier, i)) for i in range(3)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

run()
```

#### Methods

- `wait(timeout=None)`: Wait for the barrier. When all the threads or processes have called this method, they are all released. If a timeout is provided, it will only wait for this time.
- `abort()`: Put the barrier into a broken state.
- `reset()`: Reset the barrier to the default empty state.

#### Properties

- `parties`: The number of processes that need to call wait() before the barrier is passed.
- `n_waiting`: The number of processes currently waiting at the barrier.
- `broken`: A boolean, True if the barrier is in a broken state.

## Worker Pools

### What is a Worker Pool?

A Worker Pool in the `multiprocessing` module is a group of worker processes that execute tasks asynchronously. It's created using the `Pool` class. A pool can be thought of as a way to parallelize the execution of a function across multiple input values, distributing the input data across processes (data parallelism).

### Key Features

- **Parallel Execution**: The primary purpose of a Worker Pool is to run tasks in parallel across multiple processors, thus leveraging multiple cores of the CPU.

- **Task Distribution**: The Pool automatically handles the distribution of tasks to the worker processes. When a task is completed by a worker, the Pool assigns a new task to that worker.

- **Flexibility in Number of Workers**: You can specify the number of worker processes in the pool. If not specified, it defaults to the number of CPUs available on the machine.

- **Asynchronous or Synchronous Execution**: The Pool provides methods for both asynchronous (apply_async) and synchronous (apply, map) task submission.

- **Handling Results and Exceptions**: The Pool has mechanisms to collect results from the worker processes and to handle exceptions.

### Example

In this example, we'll use a pool to process a list of URLs to simulate downloading content from each URL in parallel. This example is hypothetical, focusing on the structure rather than actual network operations.

```python
from multiprocessing import Pool
import time
import random

# Dummy function to simulate processing a URL
def process_url(url):
    print(f"Processing {url}...")
    time.sleep(2)  # Simulate time taken to process the URL
    return f"Content of {url}"

def run():
    # List of dummy URLs
    urls = [f"http://example.com/page{i}" for i in range(10)]
    
    # Create a Pool with 5 workers
    with Pool(5) as p:
        # Map the function 'process_url' to the URLs
        results = p.map(process_url, urls)
    
    # Print the results
    for result in results:
        print(result)

run()
```

Example Explanation:

1. **Creation of the Worker Pool**: 
   - When you create a Pool with 5 workers (with Pool(5) as p:), you are initializing a pool of 5 worker processes. These processes are ready to run tasks in parallel.

2. **Calling map Function**: 
   - The line results = p.map(process_url, urls) is crucial. The map function is a synchronous operation. It will distribute the task of processing each URL (process_url function) across the worker processes in the pool.

3. **Task Execution**:

   - Each worker in the pool will pick up a task (in this case, a URL to process) from the list of URLs. Since you have 5 workers and 10 URLs, each worker will initially pick one URL and start processing it.
   - The process_url function simulates a 2-second processing time for each URL (time.sleep(2)).

4. **Synchronous Processing**:

   - The map function will block (i.e., wait) until all the URLs are processed. This means the main thread, which is executing the run function, will wait at the map line until all URLs are processed by the worker processes.
   - Even though the processing is happening in parallel across multiple processes, the map function collects all the results before moving on to the next line of code.

5. **Completion and Result Collection**:

   - Once all the URLs have been processed by the worker processes, the map function returns a list of results. This list (results) will contain the return values of process_url for each URL in the same order as the URLs were provided.
   - The for loop at the end (for result in results:) then iterates over these results and prints them.

6. **Timing**:

   - Since there are 5 workers and 10 tasks, and each task takes 2 seconds, the total time to process all URLs will be around 4 seconds (2 batches of 5 URLs each, processed in parallel).
   - However, this is an approximation and actual time may slightly vary depending on the system's resource allocation and scheduling.


### Common Methods & Properties

#### Methods:

- `apply(func, args=(), kwds={})`: 
  - Equivalent to func(*args, **kwds).
  - This is a synchronous operation; the pool will block until the function is completed.
- `apply_async(func, args=(), kwds={}, callback=None, error_callback=None)`:
  - Asynchronous version of apply().
  - Returns a result object and does not block the calling thread. Callbacks can be executed when the function completes.
- `map(func, iterable, chunksize=None)`:
  - A parallel equivalent of the built-in map() function. It blocks until the result is ready.
  - Distributes the workload across the pool's worker processes.
- `map_async(func, iterable, chunksize=None, callback=None, error_callback=None)`:
  - Asynchronous version of map().
  - Returns a result object immediately and executes callbacks when all operations are complete.
- `close()`:
  - Prevents any more tasks from being submitted to the pool.
  - Once called, you cannot submit new tasks to this pool.
- `terminate()`:
  - Stops all worker processes immediately without completing outstanding work.
  - It should be used with caution as it does not allow processes to clean up properly.
- `join()`:
  - Wait for all the worker processes to exit.
  - Must be called after close() or terminate() to ensure that all processes have completed.

#### Properties:

- `_processes`:
  - The number of worker processes in the pool.
  - Useful for understanding the parallelism level of the pool.
- `_state`:
  - Indicates the current state of the pool (e.g., running, closed).
  - Useful for checking the pool's status programmatically.
- `_taskqueue`:
  - A queue of tasks that are pending to be executed by the pool.
  - Provides insight into the tasks that are waiting to be processed.
- `_result_handler`:
  - Handles the processing of the results of the tasks executed by the pool.
  - Internally used for managing how results are fetched and callbacks are invoked.

## Contexts and start methods

### Contexts

A context in the `multiprocessing` module refers to the environment in which the processes are created. The context defines how exactly the process will be created and how it will communicate with the parent process. Different platforms (like Windows, macOS, and Linux) might have different default contexts.

The context can be explicitly specified, which is particularly useful when you need behavior that is different from the default on your operating system. For instance, you can create a context that mimics the behavior of POSIX fork on a Windows system.

### Start Methods

The start method is the part of the context that actually initiates the process. There are typically three start methods available in Python:

1. **fork:**

- The default on Unix-like systems.
- The child process is created as a copy of the parent process.
- Fast start-up but can be problematic with multi-threaded programs.
- Not available on Windows.

2. **spawn:**

- The default on Windows and an option on Unix-like systems.
- The child process is started from scratch, running only the Python interpreter with the relevant code.
- Safer and more compatible with different types of Python objects, but has a slower start-up time because it initializes a new Python interpreter.

3. **forkserver (where available):**

- When a program using multiprocessing starts and selects the forkserver start method, a server process is started.
- New processes are created by asking this server process to fork a new process.
- This can be safer than using fork directly, as the fork server process is single-threaded and therefore less likely to be in a problematic state when the fork happens.

### Example

Here's a basic example to demonstrate how you can set a start method in Python:

```python
import multiprocessing as mp

def worker():
    # Code for each worker process
    pass

def run():
    # Set the start method (e.g., 'fork', 'spawn', or 'forkserver')
    mp.set_start_method('spawn')

    # Create and start a process
    p = mp.Process(target=worker)
    p.start()
    p.join()

run()
```

## Logging with multiprocessing

todo