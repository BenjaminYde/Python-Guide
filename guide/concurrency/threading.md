# threading Module

## Introduction

Threading in Python allows for the execution of multiple threads (smaller units of a process) concurrently. It's particularly useful for I/O-bound applications. The threading module in Python provides a way to create and manage threads.

## Basics of Threading

A thread is a separate flow of execution. Unlike multiprocessing, threads in Python share the same memory space but execute independently.

### Advantages:

- **Concurrent Execution**: Threads can perform tasks without waiting for others to complete.

- **Resource Sharing**: Threads share the same memory space, making data sharing easier.

- **Responsive Applications**: In GUI applications, threading prevents the UI from becoming unresponsive.

### Disadvantages:

- **GIL (Global Interpreter Lock)**: In CPython, the GIL allows only one thread to execute at a time, which can limit performance.

- **Thread Safety and Synchronization**: When multiple threads access shared data, there is a potential for conflicts. Synchronization techniques, such as using Locks, Semaphores, Events, or Conditions, are crucial to prevent data corruption and ensure thread safety.

## Methods of the Thread Class

The `Thread` class in the threading module has several methods that are essential for thread management:

### start()

Initiates the thread’s activity. It must be called once per thread object, and it arranges for the object’s run() method to be invoked in a separate thread of control.

```python
my_thread = threading.Thread(target=my_function)
my_thread.start()
```

### run()

Represents the thread’s activity. By default, it calls the target function passed to the constructor with the corresponding arguments. You can override this method in a subclass.

```python
class MyThread(threading.Thread):
    def run(self):
        print("Custom thread running")
```

### join()

Waits for the thread to terminate. The optional `timeout` argument specifies a time-out for the operation.

```python
my_thread.join(timeout=None)
```

### is_alive()

Returns whether the thread is alive. A thread is alive from the moment the start() method is called until its run() method terminates.

```python
if my_thread.is_alive():
    print("Thread is still running")
```

## Creating a Thread

To create a thread in Python, you use the Thread class from the threading module. 

Example:

```python
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

# Creating a thread
thread = threading.Thread(target=print_numbers)

# Starting the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Thread finished execution.")
```

## Thread Synchronization

The `Lock` class in Python's `threading` module is a synchronization primitive that is used to ensure that only one thread can enter a particular section of code at a time. This is crucial in scenarios where multiple threads need to access or modify a shared resource. Without proper synchronization, concurrent accesses and modifications can lead to inconsistent or corrupted data, a problem known as a race condition.

A lock is the simplest synchronization primitive used to ensure that only one thread can access a particular section of code or resource at a time. It's a mutual exclusion (mutex) mechanism.

### What Does Lock Avoid?

- **Race Conditions**: When multiple threads access or modify shared data simultaneously, the final state of the data can depend on the order of accesses, leading to unpredictable and erroneous results. Locks prevent race conditions by ensuring that only one thread can access the shared resource at a time.

- **Data Corruption**: Inconsistent or simultaneous changes to shared data by multiple threads can result in data corruption. Locks help maintain data integrity by serializing access to the data.

- **Consistency Issues**: In multi-step operations where each step depends on the previous one, locks ensure that the operations are carried out atomically without interruption, maintaining consistency.

## How Does the Lock Class Work?

- **Acquire and Release**: A Lock can be in a "locked" or "unlocked" state. When a thread wants to access a shared resource, it must first "acquire" the lock. If the lock is already acquired by another thread, the requesting thread will block until the lock is released. After finishing its operation on the shared resource, the thread must "release" the lock, allowing other threads to acquire it.

- **Context Manager**: Python's Lock can be used as a context manager with the with statement, which automatically acquires and releases the lock, ensuring that it is always released, even if an exception occurs. This is a more Pythonic and safer way to handle locks.

Example:

```python
import threading

# Shared resource
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    with lock:
        counter += 1

threads = []
for i in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
```

It is also possible to call the `acquire()` and `release()` methods manually instead of using the `with` statement.

Example:

```python
# Shared resource
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    lock.acquire()  # Acquiring the lock
    try:
        counter += 1
    finally:
        lock.release()  # Releasing the lock
```

## Daemon Threads

Daemon threads are background threads that are killed when all non-daemon threads exit. They're useful for background tasks that don't need to run independently of the main program.

Example:

```python
import threading
import time

def background_task():
    while True:
        print("Heartbeat...")
        time.sleep(2)

daemon_thread = threading.Thread(target=background_task)
daemon_thread.setDaemon(True)
daemon_thread.start()

# Main thread will run for 10 seconds
time.sleep(10)
```

### Setting Daemon Status

In Python, threads are **non-daemon by default**. This means that when you create a new thread using the `threading.Thread` class, it is automatically set as a non-daemon thread unless explicitly specified otherwise.

To set a thread as a daemon, you need to explicitly set its daemon property to True either by passing daemon=True as an argument to the Thread constructor or by setting the daemon attribute before starting the thread. For example:

```python
my_thread = threading.Thread(target=my_function, daemon=True)
# or
my_thread = threading.Thread(target=my_function)
my_thread.daemon(True)
```

### Program Termination

When you forcibly stop your Python program, such as by pressing Ctrl+C (which sends an interrupt signal), both daemon and non-daemon threads are affected, but in slightly different ways:

- **For Non-Daemon Threads**: These threads will attempt to complete their current operation and can be interrupted by the stop signal (like an interrupt signal). However, if they are in the middle of a blocking operation or if they don't check for such signals, they might not stop immediately. The Python interpreter will attempt to terminate these threads gracefully, but this may not always be effective if the threads are not designed to handle interruptions.

- **For Daemon Threads**: Daemon threads are abruptly terminated when the main program exits, regardless of their state. If you forcibly stop the program, these threads will also be terminated immediately. They do not get a chance to complete their current operations or perform any cleanup.

Example:

```python
import threading
import time

def non_daemon_task():
    try:
        time.sleep(6)
        print(f"Non-Daemon: {i}")
    except KeyboardInterrupt:
        print("Non-Daemon Thread: Caught KeyboardInterrupt")

def daemon_task():
    time.sleep(6)
    print(f"Daemon: {i}")

# Creating non-daemon thread
non_daemon_thread = threading.Thread(target=non_daemon_task)
non_daemon_thread.start()

# Creating daemon thread
daemon_thread = threading.Thread(target=daemon_task)
daemon_thread.daemon = True
daemon_thread.start()

try:
    time.sleep(3)  # Main program sleeps for 3 seconds
except KeyboardInterrupt:
    print("Main Program: Caught KeyboardInterrupt")

# Wait for the non-daemon thread to complete
non_daemon_thread.join()

print("Main Program: Exiting")
```

## Thread args

The `args` parameter in the `Thread` constructor is used to pass a tuple of arguments to the target function. It's important to note that `args` should always be a tuple. Even if there is only one argument, it should be formatted as a tuple by including a comma, like (`arg`,).

### Single Argument

Suppose you have a function process_data(data) that processes some data. If you want to run this function in a separate thread and pass the data to it, you would do it like this:

```python
import threading

def process_data(data: str):
    # Function logic here
    print(f"Processing {data}")

# Data to be processed
my_data = "example_data"

# Creating a thread and passing arguments to the function
thread = threading.Thread(target=process_data, args=(my_data,))
thread.start()
thread.join()
```

### Multiple Arguments

f your target function requires multiple arguments, you can include them all in the `args` tuple:

```python
def process_multiple_data(data1, data2, data3):
    # Function logic here
    print(f"Processing {data1}, {data2}, {data3}")

# Creating a thread with multiple arguments
thread = threading.Thread(target=process_multiple_data, args=("data1", "data2", "data3"))
thread.start()
thread.join()
```

## Semaphores

### Definition

A semaphore is a more flexible synchronization primitive than a Lock, as it allows a resource to be accessed by a specific number of threads at a time. It is ideal for scenarios where a resource can handle limited concurrent accesses.

### Behavior

A semaphore is initialized with a counter that represents the number of threads that can access the resource simultaneously.
When a thread acquires the semaphore (semaphore.acquire()), the counter is decremented. When the counter reaches zero, subsequent threads attempting to acquire the semaphore will block until one of the threads releases the semaphore (semaphore.release()), incrementing the counter again.

### Use Case

Semaphores are used in situations where a resource can support a limited number of concurrent accesses, but more than one. For instance, managing access to a pool of database connections or limiting the number of threads performing a particular I/O operation.

Example:

```python
import threading
import time

# Initialize a semaphore allowing 3 concurrent accesses
semaphore = threading.Semaphore(3)

def access_resource(i):
    print(f"Thread {i} is waiting to access the resource")
    with semaphore:
        print(f"Resource accessed by Thread {i}")
        time.sleep(1) # Simulate resource usage
    print(f"Thread {i} is releasing the resource")

threads = [
    threading.Thread(target=access_resource, args=(i,)) 
    for i in range(5)
]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
```

## Events

### Definition

An Event is used for signaling between threads, allowing one or more threads to wait for a signal from another thread before proceeding. It is a simple yet powerful mechanism for thread synchronization.

### Behavior

- An Event object maintains an internal flag which can be set to `True` (using `event.set()`) or False (using `event.clear()`).

- Threads wait for the Event to be set using `event.wait()`. If the Event's internal flag is `True`, `wait()` returns immediately, otherwise, it blocks until the flag is set to `True`.

- When the Event is set, all threads waiting on it are awakened. Once awakened, they typically check some condition and then proceed with their execution.

### Use Case

Events are ideal for one-time signaling and are often used in scenarios where threads are performing tasks that must be paused until a specific condition or state change occurs elsewhere in the program.

Example:

```python
import threading
import time

event = threading.Event()

def wait_for_event():
    print("Thread waiting for event")
    event.wait()
    print("Event has been signaled, continuing execution")

def signal_event():
    print("Thread signaling the event in 3 sec...")
    time.sleep(3)
    event.set()

def run():
    print("Main Thread: Start")

    waiter_thread = threading.Thread(target=wait_for_event)
    signaler_thread = threading.Thread(target=signal_event)

    waiter_thread.start()
    signaler_thread.start()

    waiter_thread.join()
    signaler_thread.join()

    print("Main Thread: Finished")
    
run()
```

## Conditions

### Definition

A Condition is a more complex synchronization tool that allows threads to wait for certain conditions to become true. Unlike Events, Conditions are associated with some state change in the application and are typically used with a shared resource.

### Behavior

- A Condition object encapsulates a Lock and adds the ability for threads to wait for a particular condition or state change. It allows threads to safely check and modify shared state.

- Threads call `condition.wait()` to suspend their execution until another thread calls `condition.notify()` or `condition.notify_all()`.

- When `notify()` is called, one of the waiting threads is awakened; `notify_all()` wakes up all waiting threads. However, before they resume execution, they must re-acquire the Condition's underlying Lock.

- The Condition object must be locked using `with condition`: before calling `wait()`, `notify()`, or `notify_all()`.

### Use Case

Conditions are used in more complex scenarios where the state of the shared resource changes over time and threads need to wait for specific states. They are common in producer-consumer problems, where the producers and consumers share a common resource (like a queue) and must wait for specific conditions (like queue being non-empty or non-full).

Example:

```python
import threading

condition = threading.Condition()
item_available = False

def consumer():
    with condition:
        if not item_available:
            print("Consumer waiting for item")
            condition.wait()
        print("Consumer consumed the item")

def producer():
    global item_available
    with condition:
        print("Producer produced an item")
        item_available = True
        condition.notify()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

consumer_thread.start()
producer_thread.start()

producer_thread.join()
consumer_thread.join()
```

#### Explanation

1. **Initial Check**: When the consumer() function is called, it first acquires the condition lock (because of the with condition: statement).

2. **Waiting for the Condition**:
    - The `if not item_available`: check is used to determine if the item is available for consumption.
    - If `item_available` is `False` (meaning the item is not available), the consumer calls condition.wait(). This does two things:
      - Releases the lock temporarily. This allows other threads (like the producer) to acquire the lock and change the state (i.e., produce an item).
      - Blocks (waits) until `condition.notify()` or `condition.notify_all()` is called by another thread (the producer in this case).
  
3. **Resuming After Notification**:
   - Once the producer calls `condition.notify()`, the consumer is awakened (unblocked) and re-acquires the lock.
   - After re-acquiring the lock, it proceeds to the next line and completes its execution.

## Thread Local Storage (TLS)

Thread Local Storage (TLS) in Python is a way to create data that is local to a specific thread. This concept is particularly useful in scenarios where you want to avoid conflicts between threads accessing shared data. By using thread-local storage, each thread gets its own separate copy of a data variable, ensuring that one thread does not interfere with another.

### Purpose

TLS is used to store data that is unique and isolated to each thread. It's a form of global storage that is accessed globally but isolated per thread.

### Implementation

In Python, TLS is implemented using the `threading.local()` class. When you create an instance of `threading.local()`, each thread will have its own independent instance of that object.

### Usage

- You can set attributes on the `threading.local()` instance as you would with any other object. Each thread will see a different value for these attributes.
- It’s a convenient way to hold per-thread state without needing to pass objects explicitly from function to function within a thread.

Example:

```python
import threading

# Create a thread-local data object
mydata = threading.local()

def thread_function():
    # Each thread will have its own 'mydata.value'
    mydata.value = 0
    for _ in range(100):
        mydata.value += 1
    print(f"Thread {threading.current_thread().name} value: {mydata.value}")

# Create and start several threads
threads = [threading.Thread(target=thread_function) for _ in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
```

In this example, each thread increments its own `mydata.value` independently. Despite `mydata` being a global object, its `value` attribute is specific to each thread.

### Benefits and Use Cases

- **Isolation**: TLS is useful when you need to maintain data that is specific to a thread, such as user session information in a web application server.

- **Safety**: It helps avoid the pitfalls of shared data in multithreaded applications, as each thread has its own copy of data, eliminating the need for locks or other synchronization primitives for that data.

- **Convenience**: It can make it easier to design thread-safe applications since you don't have to pass objects around to keep track of thread-specific data.