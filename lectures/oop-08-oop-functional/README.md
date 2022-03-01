Python Object-oriented Shortcuts
======================

Chapter 7 in the OOP book with some examples from "Writing Idiomatic Python" (see readings) and the Python documentation.

In Python: many of the other styles of programming are implemented using object-oriented programming below the surface. You can provide the same API in your classes to use the same methods and mechanisms on them.

Python built-in functions
-------------------------

https://docs.python.org/3/library/functions.html

### Len

```python
>>> len([1,2,3,4])
4
```

`len()` asks the object directly using the `__len__()` method of the object.


### Reversed

First tries to call `__reversed__()` on the class of the object. If that fails (non-existing method), it tries to manually reverse the sequence using `__len__()` and `__getitem__()`. Returns an iterator.

```
>>> l = [1,2,3]
>>> l.__reversed__()
<list_reverseiterator object at 0x7fe4cc5a36d8>
>>> reversed(l)
<list_reverseiterator object at 0x7fe4ca939898>
>>> list(reversed(l))
[3, 2, 1]
>>> for v in reversed(l):
...    print(v)
...
3
2
1
```


### Enumerate

__Use enumerate!__

Don't do
```python
i = 0
for item in sequence:
    print(i, item)
    i += 1
````

It's too easy to forget incrementing `i` (I even forgot when writing this example because my mind was on the enumerate version), and it's very easy to mess it up with more complex statements.


```python
for i, item in enumerate(sequence):
    print(i, item)
````

Enumerate is a much simpler alternative supported by Python's tuple/sequence unpacking and multiple return values.




###  Zip

```python
>>> list(zip([1,2,3],[6,7,8]))
[(1, 6), (2, 7), (3, 8)
# you can "unzip" by zipping again:
>>> list(zip(*zip([1,2,3],[6,7,8])))
[(1, 2, 3), (6, 7, 8)]
```

Built-in function, but there are several useful functions in the `itertools` module:

https://docs.python.org/3/library/itertools.html

The itertools functions take one or more input sequences and produce output sequences or objects/iterators. Useful for some functional programming techniques.

###  Variable length and default arguments

Arguments to functions/methods do not need to be fully defined.
Variable length arguments are denoted by * and are accessed as a list
Arbitrary keyword arguments are denoted by ** and are accessed as a dict
Default values are specified by argument=default

```python
def print_arguments(*args, final_message=False):
    for arg in args:
        print(arg)
    if final_message:
        print("That's all!")

print_arguments(1, "hello", print_arguments)
print_arguments(1, "hello", print_arguments, final_message=True)

```

### Functions as objects

Functions are objects!

Functions can have attributes, and be passed around like any other object.

```python
def my_func():
    print("my_func was called!")

def your_func():
    print("This one is much worse")

def no_func():
    print("Never called")

def our_func(*functions):
    for func in functions:
        try:
            func.called += 1
        except AttributeError:
            func.called = 1
        func()

our_func(my_func, your_func, my_func)
print(my_func.called)
print(no_func.called)

```

### A quick note on decorators

We can write decorators to wrap a function in some code
```python
def log_calls(func):
    def wrapper():
        print("Function {} called".format(func.__name__))
        func()
    return wrapper

@log_calls
def called_func():
    print("Hello")

called_func()

```

This replaces called_func() with wrapper(), leading to some (perhaps unexpected)
results when using functions as objects.

```python
def count_calls(func):
    def wrapper():
        try:
            wrapper.called += 1
        except AttributeError:
            wrapper.called = 1
        func()
    return wrapper

@count_calls
def my_func():
    print("my_func was called!")

@count_calls
def your_func():
    print("This one is much worse")

@count_calls
def no_func():
    print("Never called")

def our_func(*functions):
    for func in functions:
        func()

our_func(my_func, your_func, my_func)
print(my_func.called)
print(no_func.called)

```

### Objects as functions

Functions are objects with a __call__ method, but this method can be implemented on our existing classes.

```python
class Test:
    def __init__(self):
        self.num = 1

    def __call__(self):
        print(self.num)

# Call the object after instantiating
Test()()

# Equivalent to
a = Test()
a()
```

