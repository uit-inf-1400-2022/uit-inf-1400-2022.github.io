Ch 10 -- Python Design Patterns I
=================================

Classical reference to design patterns is the "Gang of Four" book by Gamma, Helm, Johnson and Vlissides (reference to the book in the Wikipedia article : [http://en.wikipedia.org/wiki/Design_Patterns](http://en.wikipedia.org/wiki/Design_Patterns))

Part of the motivation behind patterns is to identify software/code design patterns that people often use and describe and name them such that they can be easily re-used by other programmers without having to re-invent solutions for known problems. Understanding patterns can also make it easier to understand code that others have written. 

The original patterns book (focused on C++) describes many patterns that are not relevant for Python or similar high-level languages. Enforcing such patterns in dynamic languages can lead to needlessly convoluted programs. 

Many takes on this. A couple:
- [http://www.aleax.it/Python/5ep.html](http://www.aleax.it/Python/5ep.html)
- [http://norvig.com/design-patterns/design-patterns.pdf](http://norvig.com/design-patterns/design-patterns.pdf)

The focus here is not to dive into these, just to make you aware of them. The relevant patterns for your exam will be the ones in the main book. 

One view on patterns is that the existence of a pattern _may_ be an indication of a weakness in a programming language.

The decorator pattern below is an example where, in Python, a pattern has been added as a built-in mechanism that serves to both simplify the work for the programmer and to document that you are using the pattern. 


Decorator pattern
-----------------

A decorator "wraps" a modifier around another object. If you decorate a function, you force others to call the function through a wrapper.

### Some backgrounds for how it works

Before we start to show the decorators, we should look into functions as objects. This is one of the main mechanisms behind decorators. 

``` python
def foo():
    print("This is 'foo'")

def bar():
    print("This is 'bar'")


def caller(fn):
    print("Calling", fn)
    fn()

print("Calling the foo an bar functions initially")
foo()
bar()

# A Function is just another object. The name that we see inside the module/python file is just a variable that
# points to that function object. We can therefore use functions as parameters to other functions. 
print("\nTrying to the caller function with 'foo'")
caller(foo)


# Since 'foo' and 'bar' are variables, we can play tricks with them
# Swapping foo and bar
bar,foo = foo,bar
print("\nAfter swapping. Now calling foo(), then bar()")
foo()
bar()
print("Using the caller function with 'foo' again.")
caller(foo)
# Notice that 'caller' still thinks it's calling the 'bar' function. The reason for this is that a function object
# has an attribute __name__ that is assigned when the function is created. When we swapped references to the functions in
# the 'foo' and 'bar' variables, we didn't change the __name__ attribute of the functions. 
print("Checking the name of the foo function: ", foo.__name__)
```

We normally call the type of functions Python has *first class functions*; they can be treated just like another object (passed to
functions, returned by functions etc).


### Back to decorators

One (slightly modified) example from the book. Functions are objects, and function names are variables that point to the functions. This means that we can re-assign the variable using wrapper functions: 

```python
import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}s".format(func.__name__, time.time() - now))
        return return_value
    return wrapper

def test1(a,b,c):
    print("\ttest1 called")
def test2(a,b):
    print("\ttest2 called")
def test3(a,b):
    print("\ttest3 called")
    time.sleep(1) 

@log_calls
def test4(a,b):
    print("\ttest4 called")
    time.sleep(1) 

test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1,2,3)
test2(4,b=5)
test3(6,7)

test4(1,2)
```

Running the program:
```

Calling test1 with (1, 2, 3) and {}
	test1 called
Executed test1 in 0.00011110305786132812s
Calling test2 with (4,) and {'b': 5}
	test2 called
Executed test2 in 6.628036499023438e-05s
Calling test3 with (6, 7) and {}
	test3 called
Executed test3 in 1.0031397342681885s
Calling test4 with (1, 2) and {}
	test4 called
Executed test4 in 1.0051391124725342s
```

Every time `log_calls` is called, it creates a new `wrapper` that keeps a reference to the passed `func`. The wrapper function is returned by log_calls, so we basically assign this to test1 (etc), wrapping around the original function.

`test4` is wrapped in the same way as `test1-test3`, but it uses the "decorator" syntax in Python to do so. Usign this syntax documents that we are actually using a decorator to modify or wrap the function.


### Decorator classes

Decorators can also be created using callable classes instead of functions. See for example:  [http://python-3-patterns-idioms-test.readthedocs.org/en/latest/PythonDecorators.html](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/PythonDecorators.html)  (the example below is from that site). 

```
# PythonDecorators/entry_exit_class.py
class entry_exit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")
```

### Some decorator examples from functools 

You can find many decorators in the standard Python library, and many programs will use them. One example is the `lru_cache` (least recently used cache) from the functools module: 
[https://docs.python.org/3/library/functools.html](https://docs.python.org/3/library/functools.html)

```python
from functools import lru_cache

@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

>>> for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
...     pep = get_pep(n)
...     print(n, len(pep))

>>> get_pep.cache_info()
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
```

```
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
```

The functools module also has a decorator that can be used to implement single-dispatch generic functions, similar to method overloading in many other languages: 

```python
from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)
   
@fun.register(list)
def _(arg, verbose=False):
    if verbose:
       print("Enumerate this:")
    for i, elem in enumerate(arg):
       print(i, elem)

>>> fun(42)
42
>>> fun(42, verbose=True)
Strength in numbers, eh? 42
>>> fun([2,3,4], verbose=True)
Enumerate this:
0 2
1 3
2 4
```


Observer pattern
-----------------

A single core object being monitored by a (dynamic) set of observer objects.

Slightly modified example (attach has been moved inside the observer object as this reduces the risk of attaching to the wrong object):

```python
class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory
        self.inventory.attach(self)
    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)

>>> i = Inventory()
>>> c = ConsoleObserver(i)
>>> i.product = "Widget" 
Widget
0
>>> i.quantity = 5
Widget
5
>>> c2 = ConsoleObserver(i)
>>> i.product="Gadget"
Gadget
5
Gadget
5
>>>
```

Real-life example, can we spot the pattern here?:
[https://github.com/tornadoweb/tornado/blob/master/demos/websocket/chatdemo.py](https://github.com/tornadoweb/tornado/blob/master/demos/websocket/chatdemo.py)


Strategy pattern
----------------

Implements different solutions to a single problem. The solutions can be selected or changed at run-time based needs in the program.

Example 1: different sorting algorithms that optimize for memory use, speed, or particular properties in the list (nearly-sorted sequence etc).

Many languages, such as Java, have to implement this using classes that inherit a common interface and implement a particular method.

```python
class sorter1(SorterStrategy):
    ...
    def sort(self, sequence):
        ...
class sorter2(SorterStrategy):
    ...
    def sort(self, sequence):
        ...
class sorter3(SorterStrategy):
    ...
    def sort(self, sequence):
        ...
```

You can, of course, do this in Python as well, but languages with first-class functions (functions are objects) allow you to implement the strategy pattern using functions without having to add extra class scaffolding:

```python
def sorter1(sequence):
    ...
def sorter2(sequence):
    ...
def sorter3(sequence):
    ...
```

State pattern
-------------

Similar mechanisms to Strategy pattern, but the problem is different:
the goal is to represent state transition systems. Think state
machines where a change of state in the system changes the behaviour
of the system.

The code in [code/state_example.py](code/state_example.py) is a
simplified state example.


Singleton pattern
-----------------

One of the "anti-patterns". You're probably doing something wrong if you use it in Python, but some other languages still need it.

Idea: allow exactly one instance of a certain object to exist.

Ways of creating a singleton:

1. Make a constructor private and make a static / class method to retrieve a reference to the single object.
2. Make a class method for the singleton object. Any other instanced object forwards method calls to that single object. 
3. Override `__new__` (in Python) or similar method to return reference to the singleton object

Example from the book on method 3: 
```python 
class OneOnly:
   _singleton = None
   def __new__(cls, *args, **kwargs):
      if not cls._singleton:
         cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
   return cls._singleton
```

Alternatives:

1. Use a global variable (a singleton _is_ a global variable)
2. Use a module variable (put the global variable in the right context)



Template pattern
----------------

Intended to support the DRY (Don't Repeat Yourself) principle. 

Somewhat similar to a strategy pattern, but similar code is shared using a base class. 

General idea:
- implement basic structure and shared code in the base class
- implement/override specific steps in child classes

A modified example from the book is included [here](code/template_example.py).

NB: remember this example when you get to get database course ;-)



