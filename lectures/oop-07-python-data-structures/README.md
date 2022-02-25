Python Data Structures
======================

Chapter 6 in the OOP book with some examples from "Writing Idiomatic Python" (see readings). 

- More on how to use object-oriented programming. 
- Classes and objects: when you need to specify both data and behaviour. 
- If you only need to store data, you may just as well use existing classes. 


Tuples and named tuples
-------------------------

Tuples: *immutable*. We can't change immutable objects such as tuples. To make changes, we need to create a new tuple.

Used for aggregating data (mainly read-only). 

```python
sometuple = ("hello", 4, 92)
sometuple2 = "This", "is", "also", "possible"
```

### Unpacking

```python
def somefun():
    return (400, 300)


a, b = somefun()

c, d = 10, 20
c, d = (10, 20)
```

Need to provide as many variables as there are values in the tuple: 


Idiomatic Python: use underscore for values that you want to discard. 

```python
bad:    (x, y, tmp1, tmp2) = somefun() 
good:   (x, y, _, _) = somefun()
```

### Extended iterable unpacking

"Extended iterable unpacking" is also allowed (see [https://www.python.org/dev/peps/pep-3132/](https://www.python.org/dev/peps/pep-3132/) for more information):


```python
>>> a, *b, c = range(5)
>>> a
0
>>> c
4
>>> b
[1, 2, 3]
```

Useful for cases where you, for instance, need to unpack into first and rest pairs:

```python
first, rest = seq[0], seq[1:]
```
can now be written as

```python
first, *rest = seq
```


### Slicing

Slicing also works for tuples. Slicing is a concept used with multiple sequence types: 

```python
>>> t = (10,20,30,40)
>>> t[1:3]
(20, 30)
>>> s = "hallo"
>>> s[2:4]
'll'
>>> s[-2:]
'lo'
```

Negative indexes are counted from the right hand side/end. 

Sharing a concept such as this across sequence types allows programmers to re-use patterns for multiple types. 


You can also provide "stride" as a third parameter: 
```python
>>> (1,2,3,4,5,6)[::2]
(1, 3, 5)
```

### Dig deeper: how to implement slicing

The slicing syntax in Python uses a the standard sequence access and assignment object interfaces with a small twist. 

Reading values from sequences or storing values uses the `__getitem__` and `__setitem__` methods on an object. 

``` python
a[32]        # calls a.__getitem__(32)
a[32] = 42   # calls a.__setitem__(32, 42)
```

If we use slicing, the index (32 above) is replaced with a 'slice' object and we still use the same methods. 

``` python
a[:32]        # calls a.__getitem__(slice(None,32,None))
a[:32] = 42   # calls a.__setitem__(slice(None,32,None), 42)
```

Here is an example you can start with if you want to play with this by adding slice support to your own classes: 

``` python
# The [:] syntax sends a slice object to __getitem__ or __setitem__. 
# Slices have start, step and stop attributes. 

class Tst:
    def __getitem__(self, *rest):
        print("Getitem with args", *rest)
        for v in rest:
            print('- ', v, type(v))
            if isinstance(v, slice):
                print(f"   slice start {v.start} stop {v.stop} step {v.step}")

    def __setitem__(self, *rest):
        print("Setitem with args", *rest)
        for v in rest:
            print('- ', v, type(v))
            if isinstance(v, slice):
                print(f"   slice start {v.start} stop {v.stop} step {v.step}")

tst = Tst()

tst[2]
tst[:1]
tst[1:]
tst[1:2:3]

tst[:1] = 'foo'
```




### Named tuples

Did we use the right indexes? 
```python
print("Foo {} bar {}".format(t[1], t[5]))
```

Named tuples provide "Immutable objects without behaviours".  Now we can use attribute names as an alternative to indexes. 

```python
from collections import namedtuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("GOOG", 613.30, high=625.86, low=610.50)

>>> stock.high
625.86
>>> stock[0]
'GOOG'
```


Dataclasses
------------

A simpler variant of classes where the main idea is to store values without defining methods. Dataclasses are _mutable_. 

NB: the dataclasess library is included in Python 3.7. Older versions need to install them (see https://github.com/ericvsmith/dataclasses for a backport which can be installed with pip). 

Two methods for creating dataclasses. The first is similar to named tuples 

``` python
from dataclasses import make_dataclass

Stock = make_dataclass("Stock", ["symbol", "current", "high", "low"])
stock = Stock("FB", 177.46, high=178.67, low=175.79)
>>> stock
Stock(symbol='FB', current=177.46, high=178.67, low=175.79)
>>> stock.current
177.46
>>> stock.current=178.25
>>> stock
Stock(symbol='FB', current=178.25, high=178.67, low=175.79)
>>> stock.unexpected_attribute = 'allowed'
>>> stock.unexpected_attribute
'allowed'
```

Advantages compared to standard classes: 
* More compact definition (`make_dataclass`)
* Useful string definition per default
* Equality comparison exists


Alternative decorator based method of defining dataclasses (example uses Python 3.6+ type information): 

``` python
from dataclasses import dataclass
@dataclass
class StockDecorated:
    name: str
    current: float
    high: float
    low: float

# alternative with defaults
@dataclass
class StockDefaults:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

>>> StockDefaults('FB')
StockDefaults(name='FB', current=0.0, high=0.0, low=0.0)
>>> StockDefaults('FB', 177.46, 178.67, 175.79)
StockDefaults(name='FB', current=177.46, high=178.67, low=175.79)

```

Comparisons for sorting can also be added using a parameter to the decorator (`@dataclass(order=True)). See book or documentation for more details. 


Dictionaries
-------------

Key-value storage. Useful for mapping objects to other objects (not only names or integers to objects). 

Similar concept found in other languages / standard libraries. 

```python 
stocks = {"GOOG": (613.30, 625.86, 610.50),
          "MSFT": (30.25, 30.70, 30.19)}
>>> stocks["GOOG"]
(613.3, 625.86, 610.5)
>>> stocks["RIM"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'RIM'

# can also use the "get" method to access values without throwing KeyError for missing keys. 
>>> print(stocks.get("RIM"))
None
>>> stocks.get("RIM", "NOT FOUND")
'NOT FOUND'

# setdefault sets a value if key doesn't already exist. returns the same as get(k,d)
>>> stocks.setdefault("GOOG", "INVALID")
(613.3, 625.86, 610.5)
>>> stocks.setdefault("RIM", (67.38, 68.48, 67.28))
(67.38, 68.48, 67.28)
>>> stocks["RIM"]
(67.38, 68.48, 67.28)



# "Harmful": 
log_severity = None
if 'severity' in configuration:
   log_severity = configuration['severity']
else:
   log_severity = 'Info'

# Idiomatic
log_severity = configuration.get('severity', 'Info')
```

Keys need to be hashable. Tuples can be used, lists can't as they're not hashable. 

No limits to type of objects that can be values in the dictionary. 

You _can_ use objects from classes (an object has a unique identity, making it hashable): 

```python 
>>> class F: pass
... 
>>> f = F()
>>> f.var = 1
>>> d[f] = 900
>>> d
{'P': 'f', <__main__.F object at 0x7febd4c7c4a8>: 900}
>>> f.var2 = 33
>>> d
{'P': 'f', <__main__.F object at 0x7febd4c7c4a8>: 900}
```



### defaultdict 

A common pattern is as follows (other variations typically use lists instead of integers):

```python
def letter_frequency(sentence):
   frequencies = {}
   for letter in sentence:
      if letter in frequencies:
         frequencies[letter] += 1
      else: 
         frequencies[letter] = 1
   return frequencies
```

Or using setdefault(): 

```python
def letter_frequency(sentence):
   frequencies = {}
   for letter in sentence:
      frequency = frequencies.setdefault(letter, 0)
      frequencies[letter] += 1
   return frequencies
```

A defaultdict is a dictionary that lest you specify a default constructor for keys that don't exist in the dictionary. "int" with no parameters returns 0:


```python
from collections import defaultdict
def letter_frequency(sentence):
   frequencies = defaultdict(int)
   for letter in sentence:
       frequencies[letter] += 1
   return frequencies
```

This class removes a common source of bugs: testing for and handling non-existing keys in a dictionary. 


### Dict as a replacement for switch...case

Python doesn't have a switch statement, but in many cases it's more flexible to replace it with a dictionary: 


```python
def apply_operation(left_operand, right_operand, operator):
   if operator == '+':
      return left_operand + right_operand
   elif operator == '-':
      return left_operand - right_operand
   elif operator == '*':
      return left_operand * right_operand
   elif operator == '/':
      return left_operand / right_operand
```

As functions are first class objects, it's easy to use functions as values in a dictionary. A lookup finds the right function, which can then be called with the provided arguments. 

```python
def apply_operation(left_operand, right_operand, operator):
   import operator as op
   operator_mapper = {'+': op.add, '-': op.sub,
                      '*': op.mul, '/': op.truediv}
   return operator_mapper[operator](left_operand, right_operand)
```

The `operator_mapper` dictionary can even be extended and modified at runtime to create extensible or adaptable code. 



Lists
-----

Don't be fooled by the name. Python lists are not as inefficient as linked lists for indexing. They're more like a combination of lists and arrays in other languages. 


### Sorting

```python
>>> l = ["hello", "HELP", "Helo"]
>>> l.sort()
>>> l
['HELP', 'Helo', 'hello']
>>> l.sort(key=str.lower)
>>> l
['hello', 'Helo', 'HELP']
>>> sorted([5,6,2,13])
[2, 5, 6, 13]
```


Sets
-----

```python
artists = set()
for song, artist in song_library:
   artists.add(artist)
```

Sets can also be created using curly braces (you can view them as dicts without values): 
```python
{'Sarah Brightman', "Guns N' Roses", 'Vixy and Tony', 'Opeth'}
```

Basic operations: 

- Union: `A | B`  - elements in either or both of A and B 
- Intersection: `A & B` - elements in _both_ A and B
- Difference: `A - B` - elements in A but not B. 
- Symmetric Difference: `A ^ B` - set of elements in either A or B but not in both (similar to XOR)


```python
>>> A = {1,2,3,4} 
>>> B = {3,4,5,6}
>>> A | B 
{1, 2, 3, 4, 5, 6}
>>> A & B
{3, 4}
>>> A - B 
{1, 2}
>>> B - A
{5, 6}
>>> A ^ B
{1, 2, 5, 6}
```

```python 
# Harmful
def get_both_popular_and_active_users():
   # Assume the following two functions each return a
   # list of user names
   most_popular_users = get_list_of_most_popular_users()
   most_active_users = get_list_of_most_active_users()
   popular_and_active_users = []
      for user in most_active_users:
         if user in most_popular_users:
            popular_and_active_users.append(user)

# Idiomatic
def get_both_popular_and_active_users():
   # Assume the following two functions each return a
   # list of user names
   return(set(get_list_of_most_active_users()) & 
          set(get_list_of_most_popular_users()))
```


Extending built-ins
-------------------

Two options for extending built-in containers: 

- composition : create a new object that holds the original as an attribute
- inheritance : add or adapt the behaviour of an existing class by subclassing

Choosing, some rules of thumb: 

- If you need to remove behaviour/methods or restrict too many methods, it may be better to use composition
- Extending or altering slightly: may be better to use inheritance
- If type identity is important: inheritance


Python uses objects and methods to implement much of the functionality. Duck typing lets us implement compatible classes without interitance. That is not the case in many other languages (like C++ and Java) where inheritance (either by class or interface) is necessary to provide compatible interfaces.

The type systems in languages can influence which patterns you use when you design your programs. We will look at patterns later. 



