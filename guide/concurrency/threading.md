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
