The iterator pattern
---------------------

This lecture will cover:

* Design patterns in general
* The iterator pattern
* Comprehensions
* Generators

Iterators
----------

An iterator is a class with a `__next__` method.

`__next__` returns the next element, and raises a StopIteration exception when the elements are exhausted.

For a class to be iterable, it must have an `__iter__` method, which returns an iterator over the items in the class.

```python
class ExampleIterator:
    def __init__(self):
        self.items = range(1,1000)
        self.current_place = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.items[self.current_place]
        except IndexError:
            raise StopIteration
        finally:
            self.current_place += 1


for item in ExampleIterator():
    print(item)
```


Comprehensions
---------------

Creating sequences, sets and dicts with shorter notations.


### List comprehensions

A common pattern:
```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Alternatively, using list comprehensions:
```python
squares = [x**2 for x in range(10)]
```

In this sense the expression creates a new list object by inspecting the sequence object at the right side of the `for/in` expression.


The for statement makes use of the `__iter__` method on the following object (in this case what is returned by `range`) that returns an iterator object.


Illustrating some of the mechanisms:
```python
>>> r = range(10)       # range returns a range object
>>> type(r)
<class 'range'>
>>> it = r.__iter__()   # for asks for the iterater of the object. We can get it by calling __iter__()
>>> it
<range_iterator object at 0x7f1b2f7dda20>
>>> next(it)            # getting the next iteration/element from the sequence
0
>>> it.__next__()       # built-in function next() calls __next__() on the iterator object
1
>>>
....
>>> next(it)            # final element
9
>>> next(it)            # End of sequence/iterator - triggers a StopIteration exception
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```



List comprehensions can be used to filter sequences by using an 'if' statement

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
```

Or, you can use nested sequences:

```python
>>> [(x,y) for x in [1,2,3] for y in [5,6,7]]
[(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
```

A slightly more advanced version:
```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

which is equivalent to:

```python
>>>
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

Another way to format the list comprehension statement that may be clearer to see if you're not used to them:
```python
comb = [(x, y) for x in [1,2,3]
                   for y in [3,1,4]
        if x != y]
```


### Dictionary comprehension

Basically the same `for/if` statements and rules as in list comprehensions, but with curly brackets and a colon to separate key from value:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

### Set comprehension

Sets can be created using almost the same syntax as dictionary comprehensions, but without the colon. One method for remembering: a set is basically the same as the set of keys for a dictionary.

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```


### Generator expression


List comprehensions create a new list that the for loop iterates over. This can a) use a lot of extra memory and b) generate items in the list that we don't need in case of for loops that, for instance, search for items.


Generator expressions are nearly identical, but can be more efficient as they don't generate a full list. Instead, they create a generator object that only generates each item when the for loop requests them.

It is basically 'lazy evaluation' : don't produce a new value until you actually need it.

```python
>>> g = [x for x in [1,2,3]]
>>> g
[1, 2, 3]
>>> g = (x for x in [1,2,3])
>>> g
<generator object <genexpr> at 0x7febd2d9b438>
>>> g.__next__
>>> next(g)
1
>>> next(g)
2
>>> next(g)
3
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

In general, you should use a generator expression instead of a list expression unless you actually need a list.


Generators
------------

Generator expressions: short hand for creating generators (a more general concept). Generator expressions is where generators and list comprehensions meet.


Example from https://wiki.python.org/moin/Generators:


Creating a long list of values and then iterating over that list can be expensive - especially if we don't know how many items we need:
```python
# Build and return a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
```

An alternative is creating an iterator that creates new items when requested. This is better memory-wise, but the code is more complex:
```python
# Using the generator pattern (an iterable)
class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(firstn(1000000))
```

A generator allows us to create an iterator that "yields" new values every time somebody requests it from the iterator:
```python
# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
```

The keyword `yield` in the function transforms this into a generator function.

The important modification here is that calling `firstn(n)` doesn't return a yielded value, it returns an iterator object that wraps around the code inside the function.
- The first time somebody calls `next()` on the iterator object, the code inside executes and yields the first value before it temporarily halts.
- When somebody calls `next()` on the iterator again, the code continues from the last yield point and runs until the next yield statement is called.
- When the function returns or reaches the end, a `StopIteration` exception is thrown to termate the loop using the generator

```python
>>> g = firstn(3)
>>> g
<generator object firstn at 0x7fddd70bdc18>
>>> next(g)
0
>>> next(g)
1
>>> next(g)
2
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

A slightly modified example from the book uses a generator to filter statements in a logfile:
```python
import sys

inname, outname = sys.argv[1:3]

def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')

with open(inname) as infile:
    with open(outname, "w") as outfile:
        for l in warnings_filter(infile):
            outfile.write(l)
```


### Generators, co-routines and asynchronous io

A new library in Python 3.4 uses generators for asynchronous I/O and computations:
https://docs.python.org/3/library/asyncio.html

Coroutines and asynchronous I/O are not covered in this course, but it could be useful to have a peek as they can make your life easier when you start building programs that try to do many things concurrently.




