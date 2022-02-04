# Exceptions

In this lecture, we will look at **exceptions**, special error objects raised when a normal response is 
impossible. Python are mixing the words **error** and **exception**, but they are dealt with in exactly the same way. Almost everyone have **Exception** as their superclass (4 that dont have it, they have **BaseException** as superclass including **Exception**).

**Cover the following:**
- How to cause an exception to occur
- How to recover when an exception has occured
- How to handle different exception types in different ways
- Cleaning up when an exception has occured
- Creating new types of exception
- Using the exception syntax for flow control
- Context manager


## Triggering an exception
To trigger an exception is not difficult, just look at the examples below. And we all have experience it before and will experience it again in the future.

- program will halt
- Unwinds the call stack until a handler for that exception (or a general handler) is found
- If no handler found: Python prints the call stack and some exception information before halting

```python
>>> print "Hello world"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello world")?
```

```python
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero

```
```python
>>> liste=[1,2,3,4,5]
>>> liste[5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    liste[5]
IndexError: list index out of range
```
**Some exceptions**
- SyntaxError (We programmers have written something wrong)
- NameError (trying to use a variable that doesnt exist) 
- RuntimeError (wrong version of python)
- ZeroDivisionError (Program try to divide with zero)
- IndexError (going outside of the range)
- KeyError (try to use a key that doesnt exist)
- TypeError (trying to mix different datatypes that doesnt fit)

- AttributeError (trying to use an attribute that doesnt exist for that object)
- and many more
[Overview over exceptions in python](https://docs.python.org/3/library/exceptions.html)

## Raising an exception
To raise an exception, python uses the keyword **raise** with an Exception object. Other langues uses throw.

```python
class OddOnly(list):
    #Override append()-method
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("bare heltall kan bli lagt til i listen...")
        if integer%2==0:
            raise ValueError("Bare oddetall kan legges til i listen...")
        #No Exceptions raised, adding integer to the list
        super().append(integer)
```
Trying to append string to the list
```python
>>> oddList=OddOnly()
>>> oddList.append("Test")
Traceback (most recent call last):

  File "t.py", line 1, in <module>
    oddList.append("Test")

  File "OddOnly.py", line 12, in append
    raise TypeError("bare heltall kan bli lagt til i listen...")

TypeError: bare heltall kan bli lagt til i listen...
```
Trying to append a even number to the list
```python
>>> oddList.append(4)
Traceback (most recent call last):

  File "t.py", line 1, in <module>
    oddList.append(4)

  File "OddOnly.py", line 14, in append
    raise ValueError("Bare oddetall kan legges til i listen...")

ValueError: Bare oddetall kan legges til i listen...
```
Trying to append a odd number
```python
>>> oddList.append(3)
>>>
```
Testing our code 
```python 
def testOddOnly():
    oddList=OddOnly()
    print("Starting:")
    oddList.append(7)
    print("Still running")
    oddList.append(4)
    print("Halting, but this will never printed...")
```
Why will the last print() never run?

## Handling exceptions
We have only raised exceptions so far, but we will have to deal with them...
Python using try/except/else/finally to handle them. other languages use try ... catch.
There are three types of except clauses:
- **except:** (Its block is executed when any exception occurs)
- **except ExceptionType:** (Its block is executed only when the specified type of exception occurs)
- **except ExceptionType as ex:** (Its block is executed only when the specified type of exception occurs. Additional information about the problem is assigned to ex)


```python 
try:    
    testOddOnly()
except:
    print("Got an exception, but dont know which one...")
```
Two problems with the code above:
- don't know which exception we have caught
- may have caught many exception, but we dont handle them

Better to check what type/class the exception object is. 

```python
def testOddOnly():
    oddList=OddOnly()
    print("Starting:")
    oddList.append(7)
    print("Still running")
    oddList.append("4e")
    print("Halting, but this will never printed...")

    
try: 
    testOddOnly()
except TypeError:
    print("Got a TypeError, remember that you have to use integers")
except ValueError:
    print("Got a ValueError, remember that only odd numbers is allowed")
```
With the code above we dont have the additional information, so if we want that to then we can write it like this.
```python
try: 
    testOddOnly()
except TypeError as tex:
    print("Got a TypeError, and additional information are:",tex)
except ValueError as vex:
    print("Got a ValueError, and additional information are:", vex)
```
Catching more than one Exception:
```python
try: 
    testOddOnly()
except (TypeError, ValueError) as ex:
    print("Got either a TypeError or ValueError, and additional information are:",ex)
```

**else clauses**
a try statement can also include a single **else** clause that follows the except clauses. The block is executed when no exceptions occur. It is a good place to put code that does not need protection.

```python
try: 
    testOddOnly()
except TypeError:
    print("Got a TypeError, remember that you have to use integers")
except ValueError:
    print("Got a ValueError, remember that only odd numbers is allowed")
else:
    print("No exceptions occured, so this block are executed.")
```

**finally clauses**
A try statement can end with a **finally clause**. This block will be executed regardless if a exception has occoured or not.
It is used to clean up resources. Example files that is left open.

```python
try: 
    testOddOnly()
except TypeError:
    print("Got a TypeError, remember that you have to use integers")
except ValueError:
    print("Got a ValueError, remember that only odd numbers is allowed")
finally:
    print("This block will always run")
```

## Defining own Exceptions
Sometimes you want to define your own exceptions so you can use them in your program. 
```python
#From textbook
class OutOfStock(Exception):
    pass
class InvalidItemType(Exception):
    pass

class Inventory:
    def __init__(self):
        pass
    
    def purchase(self, item_type):
        if item_type=="Widget":
            raise OutOfStock(item_type)
        elif item_type=="Gadget":
            return 42
        else: 
            raise InvalidItemType(item_type)
```
and test the code
```python
inv=Inventory()
try:
    inv.purchase("Gadget")
except OutOfStock as ex:
    print("We dont have ",ex)
except InvalidItemType as ex:
    print("We dont sell ", ex)
else:
    print("Thank you for your purchase")
```
```python
>>> Thank you for your purchase
```





