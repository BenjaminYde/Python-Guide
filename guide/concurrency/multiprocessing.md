# multiprocessing Module

## Basics of Multiprocessing

The `multiprocessing` module in Python allows for the execution of multiple processes concurrently. It's particularly useful for CPU-bound applications, leveraging multiple CPU cores for parallel processing. Unlike threading, multiprocessing in Python involves running separate memory spaces.

### Use Cases

- **Data Processing**: Multiprocessing is ideal for scenarios where you have to process large datasets or perform complex mathematical calculations that can be parallelized.

- **Concurrent Execution**: Running multiple operations that are independent of each other and can be executed simultaneously, such as batch processing tasks.

## What is a Process?

A **process** is an independent instance of a Python interpreter. The multiprocessing module provides an API similar to the threading module but uses processes instead of threads. This bypasses the Global Interpreter Lock (GIL) and allows full parallelism.

### Advantages:

- **True Parallelism**: Each process runs in its own Python interpreter and memory space, enabling parallel CPU computation.

- **Bypassing the GIL**: Avoids the limitations of the GIL in CPython, which only allows one thread to execute Python bytecode at a time.

- **Improved Stability**: A crash in one process does not affect other processes.

### Disadvantages:

- **Higher Overhead**: Processes are heavier than threads and consume more system resources.

- **Inter-process Communication**: Communication between processes is more complex and requires serialization (e.g., using queues or pipes).

## Creating a Process

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

## Terminating Processes

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

Example:

```python
from multiprocessing import Process, Pipe

def worker(conn):
    conn.send("Hello from the child process!")
    conn.close()

def run():
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # Prints the message from the child process
    p.join()

run()
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
## Process Pool

The Process `Pool` object is used to manage a pool of worker processes. It provides methods to execute calls asynchronously.

- **Parallel Execution**: Distributes input data across processes (data parallelism).

- **Pool of Workers**: Manages a fixed number of workers to execute function calls asynchronously.

Example:

```python
from multiprocessing import Pool

def square(n):
    return n * n

def run():
    with Pool(4) as p:  # Pool of 4 processes
        results = p.map(square, range(10))
    print(results)

run()
```

Example Explained:

The example shows using a pool of 4 processes to execute the `square` function in parallel. The `map` method applies the `square` function to each item in the range, distributing the work across the processes in the pool.

## Daemon Processes

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

## Shared Memory Objects

In multiprocessing, shared memory objects allow processes to share data. This is essential for communication and state sharing between processes.

### Value and Array

- These are the simplest ways to share data between processes.
- Value is used for a single simple data type, while Array is used for multiple values of a standard type.
- Both are synchronized and can be used safely by multiple processes.

Example:

```python
from multiprocessing import Process, Value, Array

def update_shared_value(shared_value, shared_array):
    shared_value.value += 1
    for i in range(len(shared_array)):
        shared_array[i] += 1

def run():
    shared_value = Value('i', 0)  # Integer shared between processes
    shared_array = Array('i', range(5))  # Array shared between processes

    processes = [Process(target=update_shared_value, args=(shared_value, shared_array)) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(shared_value.value)
    print(shared_array[:])

run()
```

### Manager

- Used for creating shared objects of more complex data types like lists, dictionaries, etc.
- Slower than Value and Array but more flexible.

Example:

```python
from multiprocessing import Process, Manager

def append_to_shared_list(shared_list, data):
    shared_list.append(data)

def run():
    with Manager() as manager:
        shared_list = manager.list()
        processes = [Process(target=append_to_shared_list, args=(shared_list, i)) for i in range(5)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()

        print(list(shared_list))

run()
```

## Logging with multiprocessing

todo