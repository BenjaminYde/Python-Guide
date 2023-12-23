# concurrent Module

## Introduction

The `concurrent` module in Python, specifically` concurrent.futures`, provides a high-level interface for asynchronously executing callables. It simplifies the use of threads and processes, making it easier to parallelize code.

### Advantages:

- **Simplified Interface**: Offers a clean and easy-to-use API for managing threads and processes.

- **Future Objects**: Represents the result of asynchronous execution, which can be queried for status without blocking.

- **Executor Classes:** Abstracts the thread and process creation, managing pools of threads or processes.

### Disadvantages:

- **Overhead**: Can introduce overhead, especially when used for numerous short-lived tasks.

- **Limited Control**: Provides less fine-grained control over thread or process management compared to using threading or multiprocessing directly.

## ThreadPoolExecutor and ProcessPoolExecutor

`ThreadPoolExecutor` and `ProcessPoolExecutor` are two of the main executor classes provided by the `concurrent.futures` module in Python. They abstract the complexities of thread and process management, making it easier to execute tasks concurrently. Let's delve deeper into each of them:

### ThreadPoolExecutor

`ThreadPoolExecutor` is used for creating a pool of threads to execute calls asynchronously. It is most suitable for tasks that are I/O-bound or where the overhead of process creation is too high.

Key Characteristics:

- **Thread-based Parallelism**: Utilizes threads, which are lighter weight than processes and share the same memory space.

- **Best for I/O-bound Tasks**: Ideal for tasks that spend a lot of time waiting for I/O operations (like network or file I/O).

- **GIL Limitations**: In CPython, the Global Interpreter Lock (GIL) can be a limiting factor for CPU-bound tasks, as it only allows one thread to execute Python bytecode at a time.

Example:

```python
from concurrent.futures import ThreadPoolExecutor

def fetch_url(url):
    # Code to fetch data from URL
    return data

def run():
    urls = ["http://example.com", "http://another.com"]

    with ThreadPoolExecutor(max_workers=10) as executor:
        responses = executor.map(fetch_url, urls)
        for response in responses:
            # Process response

run()
```

In this example, `fetch_url` is executed concurrently for different URLs using a pool of 10 threads.

### ProcessPoolExecutor

`ProcessPoolExecutor` is used for executing calls in separate processes. It is most suitable for CPU-bound tasks that benefit from multiple CPU cores and require parallel computation.

Key Characteristics:

- **Process-based Parallelism**: Utilizes separate processes, each with its own Python interpreter and memory space.

- **Best for CPU-bound Tasks**: Ideal for tasks that require heavy computation and can be parallelized.

- **Overcomes GIL Limitations**: Each process has its own Python interpreter, thus bypassing the GIL and allowing parallel execution of Python bytecode.

Example:

```python
from concurrent.futures import ProcessPoolExecutor

def compute(data):
    # Code for CPU-intensive computation
    return result

def run():
    data_list = ["data1", "data2", "data3"]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(compute, data_set)
        for result in results:
            # Process result

run()
```

In this example, the `compute` function, which is CPU-intensive, is executed in parallel across different data sets using a pool of 4 processes.

### Common Methods

`submit(fn, *args, kwargs)`

- **Purpose**: The submit method is used to schedule a single callable to be executed in a separate thread or process. It returns a Future object which represents the execution of the callable.

- **Usage**: submit is ideal when you have a single function that you want to run asynchronously, and you're interested in the result of that specific call.

- **Flexibility**: It allows more control over individual tasks. You can submit different functions or the same function with different arguments, and you can manage each Future object individually.

- **Syntax**: future = executor.submit(function, arg1, arg2)
  
Example:

```python
from concurrent.futures import ThreadPoolExecutor

def load_data(file):
    # Code to load data from the file
    return file_data

def run():
  with ThreadPoolExecutor(max_workers=4) as executor:
      future1 = executor.submit(load_data, 'file1.txt')
      future2 = executor.submit(load_data, 'file2.txt')
      data1 = future1.result()
      data2 = future2.result()

run()
```

`map(func, iterables, timeout=None, chunksize=1)`

- **Purpose**: The map method is similar to the built-in Python map function. It applies a function to every item of an iterable (like a list) and returns an iterator that yields the results.

- **Usage**: map is useful when you have a sequence of tasks that all involve calling the same function with different arguments.

- **Convenience**: It abstracts away the creation and management of Future objects. You don't have to call result on each Future as map returns the results directly.

- **Blocking**: map blocks until the results are ready, returning results in the order that the original calls were made, which means even if a later task finishes before earlier ones, it will wait.

Example:

```python
from concurrent.futures import ThreadPoolExecutor

def process_data(data):
    # Code to process data
    return processed_data

def run():
    data_list = ["data1", "data2", "data3"]

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(process_data, data_list)
        for result in results:
            # Process the result
            pass

run()
```

`shutdown(wait=True)`

- Signals the executor that it should free up any resources that it is using when the currently pending futures are done executing.
- If wait is True, this method will not return until all the pending futures are executed and the resources are freed.
- Example: executor.shutdown()

### Key Differences Between submit() and map()

**Return Type**:

- `submit` returns a Future object for each task.
- `map` returns an iterator that yields results directly.

**Handling Different Tasks**:

- `submit` can handle different functions and arguments.
- `map` is for applying the same function to different elements of an iterable.

**Result Ordering**:

- `submit` gets you the results as soon as each task completes (by calling result on each Future).
- `map` maintains the order of the input iterable, even if tasks complete out of order.

**Blocking Behavior**:

- `submit` is non-blocking. You can continue doing other things while the task is running and check the result later.
- `map` is blocking. It waits for all the results to be ready, although you can start processing earlier results as they become available in the iterator.

### Choosing Between ThreadPoolExecutor and ProcessPoolExecutor

The choice between using `ThreadPoolExecutor` and `ProcessPoolExecutor` depends on the nature of the tasks:

#### Use ThreadPoolExecutor when:

- Tasks are I/O-bound.
- Overhead of creating new processes is too high.
- Tasks require shared memory and are lightweight in terms of CPU usage.

#### Use ProcessPoolExecutor when:

- Tasks are CPU-bound and can be parallelized.
- You want to utilize multiple CPU cores.
- Tasks are independent and do not need to share memory.

## Future Objects

### What Are Future Objects?

Future objects encapsulate the execution of asynchronous operations and provide a means to access their results once they are complete. Understanding the workings and functionalities of Future objects is essential when dealing with concurrent programming in Python.

A Future object is created when a task is scheduled for execution with an Executor (like `ThreadPoolExecutor` or `ProcessPoolExecutor`). It represents an eventual result of an asynchronous operation and acts as a proxy for a result that is initially unknown, usually because the computation of its value is not yet complete.

### Properties and Methods

### Properties:

- **State**: A Future object can be in one of the following states:
  - **Pending**: The task is waiting to be executed.
  - **Running**: The task is being executed.
  - **Done**: The task was cancelled or finished executing.

### Methods:

- `cancel()`: Attempts to cancel the task. Returns True if the task was successfully cancelled. A task can only be cancelled if it has not yet started running.

- `cancelled()`: Returns True if the future was cancelled.

- `running()`: Returns True if the future is currently being executed and cannot be cancelled.

- `done()`: Returns True if the task was cancelled or finished executing.

- `result(timeout=None)`: Returns the result of the call when it completes. If the call hasn’t completed in timeout seconds, a concurrent.futures.TimeoutError will be raised. If the future is cancelled before completing, concurrent.futures.CancelledError will be raised.

- `exception(timeout=None)`: Returns the exception raised by the call. If the call hasn’t completed in timeout seconds, a concurrent.futures.TimeoutError will be raised.

- `add_done_callback(fn)`: Attaches a callable fn to the future, which will be called with the future as its only argument when the future is cancelled or finishes running.

## Executing Functions

### as_completed

The `as_completed` function is used to iterate over the `Future` instances as they complete their execution. It takes an iterable of futures and returns an iterator that yields futures as they finish, regardless of the order in which they were originally submitted.

- **Order of Completion**: Yields futures in the order they complete, not in the order they were submitted.

- **Non-blocking**: It doesn’t block the thread from which it’s called; instead, it allows you to handle futures as they finish.

- **Useful for Progress Updates**: Ideal for scenarios where you want to provide real-time feedback or process results as soon as they are available.

Example:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def task(n):
    # Some task
    return n * 2

def run():
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        for future in as_completed(futures):
            result = future.result()
            print(f"Task returned: {result}")

run()
```

### wait

The `wait` function is used to wait for the completion of Future instances and can be used to block until specific conditions are met. It allows more control over how you wait for futures to complete.

- **Blocking**: Blocks execution until the given futures are done or until an optional timeout occurs.

- **Flexible Waiting Conditions**: You can specify conditions like `FIRST_COMPLETED`, `FIRST_EXCEPTION`, or `ALL_COMPLETED` to control the behavior of wait.

- **Returns Two Sets of Futures**: Returns two sets — one containing the futures that satisfied the specified condition, and another containing the ones that did not.

Example:

```python
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

def task(n):
    # Some task
    return n * 2

def run():
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        done, not_done = wait(futures, return_when=FIRST_COMPLETED)
        
        for future in done:
            result = future.result()
            print(f"Task returned: {result}")

run()
```

## Usage

### Example: Concurrently Downloading Website Content

Suppose we have a function `download_url(url)` that takes a URL and returns its content. We'll simulate the download with a sleep and return a message.
When you submit a task (a callable) to an Executor, a Future object is returned:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def download_url(url: str) -> str:
    print(f"Starting download of {url}")
    time.sleep(random.randint(1,4))  # Simulate time taken to download
    return f"Content of {url}"


def run():
    urls = ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks and get Future objects
        futures_to_url = {executor.submit(download_url, url): url for url in urls}

        # Process results as they become available
        for future in as_completed(futures_to_url):
            url = futures_to_url[future]
            try:
                data = future.result()
                print(f"Download completed for {url}: {data}")
            except Exception as exc:
                print(f"Error for {url}: {exc}")

run()
```

#### Explanation

1. **Function Setup**: `download_url(url)` is a function that simulates downloading content from a URL.

2. **URLs List**: urls is a list of URLs that we want to download.

3. **ThreadPoolExecutor**: We use `ThreadPoolExecutor` with `max_workers=3`, allowing up to three download tasks to run concurrently.

4. **Submitting Tasks**: Each call to `executor.submit(download_url, url)` submits a task to the executor and returns a Future object. We store these in a dictionary, `futures_to_url`, mapping Future objects to their corresponding URLs.

5. **Processing Results**: `as_completed(futures_to_url)` is an iterator that yields Future objects as they complete. We iterate over these completed Future objects:

   - `future.result()` retrieves the result of the task. If the task raised an exception, `future.result()` will re-raise the exception.

   - We print the result of each download or handle exceptions if any occurred.