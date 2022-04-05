Context managers & Stop writing classes
=================================

Goals for this lecture:
- Introduction to resource management
- How to handle resources
- How context managers can help
- Quick tips on when not to use classes and why


Resources
==================

Resources in this context are things like open files, network connections, database connection, and other things which go through the following process:

1. Acquire the resource
2. Use the resource
3. Release the resource

An example of this is files, which you open (acquire), read/write (use) and close (release).

If you do not relinquish the resource, you will at some point not be allowed to aquire more resources. For this reason, it is very important to release resources when they are not in use.

### Example with files
Open alot of files (same file...) and putting them into a list (without closing them)

```python
open_files_list=[]
for i in range(1,100000):
    f=open("test.txt","w+")
    open_files_list.append(f)
```
Resulterer i en feilmelding:
```python
OSError: [Errno 24] Too many open files: 'test.txt'
```

Context managers
================

How to ensure a resource is released when you are done with it.

Let's look at an example with an open file.

```python
f = open("filename")
data = f.read()
f.close()
print(data)
```

Not quite good enough, if the read() fails, the file is never closed.

Now with exception handling:

```python
f = open("filename")
try:
    data = f.read()
finally:
    f.close()
print(data)
```

Very good, we're safe!

Now with context manager:

```python
with open("filename") as f:
    data = f.read()
print(data)
```

This is the same thing, but it's a lot simpler to reason about (especially in larger sections of code).


What is actually going on?

Create context         <->        ```with``` statement

Enter context          <->        ```__enter__()```      <-> before try

Do something           <->        code blocks            <-> inside try

Exit the context       <->        ```__exit__()```       <-> inside finally

```python
class ctx:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename)
        return self.file
    def __exit__(self, e_type, e_value, e_traceback):
        self.file.close()


with ctx("some_file") as f:
    print(f.read())

```

So to create a context manager we have to impplement two methods: ```__enter__()```and ```__exit__(type,value,traceback)```.

```__exit__(type,value,traceback)``` may return True or False. If True then exceptions is silenced. If no exceptions occurs then type/value/traceback is None.


Alternatively (with a decorator)

```python
from contextlib import contextmanager

@contextmanager
def ctx(filename):
    file = open(filename)
    yield file
    file.close()


with ctx("some_file") as f:
    print(f.read())
``` 

What is actually going on?
before ```yield``` -> ```__enter__()```
yield resource     -> return generator (only once)
after ```yield```  -> ```__exit__(type,value,traceback)```

### Contex managers can be usefull in other contexts than only resources.

Creating a start-stop contextmanager with a timer.
```python
from time import process_time
#perf_counter

class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = process_time()
        return self

    def __exit__(self, e_type, e_value, e_traceback):
        self.stop = process_time()
        self.elapsed = self.stop - self.start
        return False
```
Creating a function that calculate fibonacchi numbers (1,1,2,3,5,8,13....)
```python
def fibo(n):
    a=1
    b=1
    for _ in range(n):
        c=a+b
        a=b
        b=c
    return c
```
Using the Timer context manager
```python
with Timer() as t:
    fibo(1000000)
print(t.elapsed)
```

A couple of resources:
- [wikibooks link](https://en.wikibooks.org/wiki/Python_Programming/Context_Managers)
- [PEP 343](https://www.python.org/dev/peps/pep-0343/)
- [contextlib documentation](https://docs.python.org/3/library/contextlib.html)


Stop Writing Classes
=====================

Objects in an OOP setting are (as previously discussed) things that contain data as well as methods to operate on that data. However, this distinction is not always clear.

```python
class WordRepeater:
    def __init__(self, number):
        self.num = number
    
    def repeat(self, words):
        for i in range(self.num):
            print(words)
```

Example of use:
```python
repeat_50 = WordRepeater(50)

repeat_50.repeat("Hello World")
```

Alternative:
```python
def repeat(num, words):
    for i in range(num):
        print(words)
```

Example of use:
```python
# Non-partial
repeat(50, "Hello World")

# With partial
from functools import partial
repeat_50 = partial(repeat, 50)
repeat_50("Hello World")
```

[How about this?](https://docs.python.org/3.8/library/heapq.html)

This video illustrates some ways of thinking that might add complexity rather than help writing better programs.

[Jack Diederich, Stop Writing Classes](https://www.youtube.com/watch?v=o9pEzgHorH0)

