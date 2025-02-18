I'll help you save the Markdown file. Since you want to convert the Python file to Markdown while keeping the original Python file, I'll create a new file with the same name but a .md extension.

```markdown:7-Multithreading/interview_questions.md
# Python Concurrency Interview Questions and Answers

## 1. What is the difference between Process and Thread?

### Process:
- Independent execution unit with its own memory space
- Has more overhead due to separate memory allocation
- Better for CPU-bound tasks
- Not affected by GIL (Global Interpreter Lock)
- Harder to share data between processes

### Thread:
- Lightweight execution unit that shares memory space with parent process
- Less overhead than processes
- Better for I/O-bound tasks
- Affected by GIL in CPython
- Easy to share data between threads but needs synchronization

## 2. What is GIL (Global Interpreter Lock)?
- A mutex that protects access to Python objects
- Prevents multiple native threads from executing Python bytecode simultaneously
- Only one thread can execute Python code at a time
- Released during I/O operations
- Main reason why Python threads are not suitable for CPU-bound tasks

## 3. What are different ways to create threads in Python?

### a) Using Thread class directly:
```python
thread = Thread(target=function, args=(arg1, arg2))
```

### b) Extending Thread class:
```python
class MyThread(Thread):
    def run(self):
        # code here
```

### c) Using ThreadPoolExecutor:
```python
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(function, arg1, arg2)
```

## 4. What is the difference between start() and run() methods in Thread?
- `start()`: Creates new thread and calls run() method
- `run()`: Executes the target function in the current thread
- Always use start() to create new thread

## 5. What is asyncio?
- Python's built-in library for writing concurrent code using coroutines
- Uses event loop and async/await syntax
- Single-threaded, non-blocking I/O operations
- Best for I/O-bound tasks

Example:
```python
async def main():
    await asyncio.sleep(1)
    print("Hello")
```

## 6. What are common threading issues?
- Race conditions: When multiple threads access shared data simultaneously
- Deadlocks: When threads wait for each other indefinitely
- Thread starvation: When a thread never gets resources
- Solution: Use proper synchronization (Lock, RLock, Semaphore)

## 7. What is the difference between Lock and RLock?
- Lock: Can be acquired only once
- RLock (Reentrant Lock): Can be acquired multiple times by same thread

## 8. What is a ThreadPool?
- Pool of worker threads for executing tasks
- Manages a fixed number of threads
- Reuses threads instead of creating new ones

Example using concurrent.futures:
```python
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(function, iterable)
```

## 9. When to use Threads vs Processes vs Asyncio?
- Threads: I/O-bound tasks (file operations, network calls)
- Processes: CPU-bound tasks (heavy computations)
- Asyncio: I/O-bound tasks with many concurrent operations

## 10. What is thread synchronization?
- Coordinating access to shared resources
- Tools:
  * Lock: Basic mutual exclusion
  * RLock: Reentrant lock
  * Semaphore: Controls access to limited resources
  * Event: Signals between threads
  * Condition: Complex synchronization scenarios

Example of using Lock:
```python
from threading import Lock

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()
    
    def increment(self):
        with self.lock:
            self.count += 1
```

## 11. What is a daemon thread?
- Background thread that exits when main program exits
- Used for tasks that don't need to complete
- Created using: `thread.daemon = True`

## 12. What is multiprocessing Pool?
- Creates pool of worker processes
- Distributes tasks across multiple CPU cores

Example:
```python
from multiprocessing import Pool
with Pool(processes=4) as pool:
    results = pool.map(function, iterable)
```

## 13. What is the difference between map() and apply() in multiprocessing?
- `map()`: Parallel execution for multiple inputs
- `apply()`: Single task execution in separate process

## 14. What are context managers in threading?
- `with` statement for automatic resource management
- Examples: Lock, RLock, Semaphore
- Ensures proper release of resources

## 15. How to share data between processes?
- Using multiprocessing.Value or Array
- Using Queue or Pipe
- Using Manager objects
- Using shared memory

## 16. Common Multithreading Scenarios and Solutions

### Scenario 1: Producer-Consumer Problem
**Question:** How would you implement a thread-safe producer-consumer pattern where one thread produces data and another consumes it?

**Solution:**
```python
from queue import Queue
from threading import Thread
import time

def producer(queue):
    for i in range(5):
        print(f"Producing item {i}")
        queue.put(i)
        time.sleep(1)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming item {item}")
        queue.task_done()

# Usage
queue = Queue()
prod = Thread(target=producer, args=(queue,))
cons = Thread(target=consumer, args=(queue,))

prod.start()
cons.start()

prod.join()
queue.put(None)  # Signal to stop consumer
cons.join()
```

### Scenario 2: Web Scraper
**Question:** How would you design a concurrent web scraper that respects rate limiting?

**Solution:**
```python
import threading
import time
from queue import Queue
import requests

class RateLimitedScraper:
    def __init__(self, rate_limit=1):
        self.rate_limit = rate_limit  # requests per second
        self.lock = threading.Lock()
        self.last_request = time.time()
        
    def fetch_url(self, url):
        with self.lock:
            # Ensure rate limiting
            now = time.time()
            if now - self.last_request < self.rate_limit:
                time.sleep(self.rate_limit - (now - self.last_request))
            self.last_request = time.time()
            
            return requests.get(url)

# Usage
urls = ["http://example1.com", "http://example2.com"]
scraper = RateLimitedScraper()
threads = [Thread(target=scraper.fetch_url, args=(url,)) for url in urls]
```

### Scenario 3: Parallel File Processing
**Question:** How would you implement a solution to process multiple files concurrently while writing results to a shared output file?

**Solution:**
```python
from concurrent.futures import ThreadPoolExecutor
import threading

class FileProcessor:
    def __init__(self):
        self.write_lock = threading.Lock()
        
    def process_file(self, filename, output_file):
        # Process individual file
        result = self._process_single_file(filename)
        
        # Write to shared output with lock
        with self.write_lock:
            with open(output_file, 'a') as f:
                f.write(f"{filename}: {result}\n")
    
    def process_multiple_files(self, filenames, output_file):
        with ThreadPoolExecutor(max_workers=3) as executor:
            for filename in filenames:
                executor.submit(self.process_file, filename, output_file)
```

### Scenario 4: Cache with Time-based Expiration
**Question:** How would you implement a thread-safe cache with automatic expiration of entries?

**Solution:**
```python
from threading import Lock
import time
from collections import defaultdict

class ThreadSafeCache:
    def __init__(self, expiration_time=60):
        self.cache = {}
        self.timestamps = {}
        self.lock = Lock()
        self.expiration_time = expiration_time
    
    def get(self, key):
        with self.lock:
            if key in self.cache:
                if time.time() - self.timestamps[key] > self.expiration_time:
                    del self.cache[key]
                    del self.timestamps[key]
                    return None
                return self.cache[key]
            return None
    
    def set(self, key, value):
        with self.lock:
            self.cache[key] = value
            self.timestamps[key] = time.time()
```

### Scenario 5: Periodic Task Executor
**Question:** How would you implement a system that executes different tasks at different intervals?

**Solution:**
```python
import threading
import time

class PeriodicExecutor:
    def __init__(self):
        self.tasks = {}
        self.running = True
    
    def add_task(self, interval, task, *args, **kwargs):
        def run_task():
            while self.running:
                task(*args, **kwargs)
                time.sleep(interval)
        
        thread = threading.Thread(target=run_task)
        thread.daemon = True
        thread.start()
        self.tasks[task.__name__] = thread
    
    def stop(self):
        self.running = False

# Usage
def task1():
    print("Task 1 executed")

def task2():
    print("Task 2 executed")

executor = PeriodicExecutor()
executor.add_task(5, task1)  # Execute every 5 seconds
executor.add_task(10, task2)  # Execute every 10 seconds
```

These scenarios cover common real-world situations where multithreading is useful. They demonstrate:
- Thread synchronization
- Resource sharing
- Rate limiting
- Concurrent I/O operations
- Thread-safe data structures
- Periodic task execution

Each scenario includes both the problem description and a practical solution that can be adapted for similar situations.

---
*Note: These scenarios are common in technical interviews and real-world applications.*
```

I've created a new Markdown file with:
1. Proper Markdown formatting
2. Code blocks specifically marked as Python
3. Better visual hierarchy with headers
4. Consistent formatting throughout
5. Preserved all the original content but in a more readable format

The file has been saved as `interview_questions.md` in the same directory as the original Python file.
