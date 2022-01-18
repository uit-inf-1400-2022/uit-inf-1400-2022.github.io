Lecture notes - OOP - chapter 2-3
=========================================

Chapter 2:

* Python Modules
* Python docstrings

Chapter 3

* Basic inheritance
* extending built-ins
* overriding and super
* multiple inheritance
* diamond problem
* method resolution order
* polymorphism

Python Modules
--------------

Simplest version: a Python file is a module that can be imported and used by other Python files.

Creating a module:

```python
#simplemod.py
somevar = 42
def somefunc(v):
    print(v)
```

Using a module:

```python
# Using simplemod.py as a module
import simplemod

print('Value of simplemod var is', simplemod.somevar)
simplemod.somefunc(9000)
```

Python Modules
---------------

Main uses:
* organize code
* provide libraries

Entire packages/libraries can be imported as modules. Requires `__init__.py` in the package directory.

```
somelib/
    __init__.py     <-- contains variable 'somevar'
    blarb.py
    sublib/
        __init__.py  <-- contains variable 'foo'
        other.py
```

Can be used:

```python
import somelib
import somelib.sublib

print(somelib.somevar)
print(somelib.sublib.foo)
```

Python has several libraries included (as modules):
[https://docs.python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html)

Also third party packages (such as PyGame). One resource is
[https://pypi.python.org/pypi](https://pypi.python.org/pypi)

Python docstrings
-----------------

Document your code. Code is "write once read many" (not quite but almost)

Most people reading the code will not know (or have forgotten) what, why, and how. That includes yourself in the future.

What does this code do?
[http://www.ioccc.org/2013/birken/birken.c](http://www.ioccc.org/2013/birken/birken.c)

Solution:
[http://www.ioccc.org/2013/birken/hint.html](http://www.ioccc.org/2013/birken/hint.html). See [http://www.ioccc.org/2013/birken/hint.html](http://www.ioccc.org/2013/birken/) if you want to build and play with it yourself. 

From [IOCCC](http://www.ioccc.org/)

This type of documentation is useful

```python
def foo(bar):
    # This function does nothing
    pass
```

However, you need to read the source to view this documentation.

### Java: javadoc based on specially formatted comments

[http://www.oracle.com/technetwork/articles/java/index-137868.html](http://www.oracle.com/technetwork/articles/java/index-137868.html)

[https://skmedix.github.io/ForgeJavaDocs/javadoc/forge/1.11.2-13.20.0.2228/](https://skmedix.github.io/ForgeJavaDocs/javadoc/forge/1.11.2-13.20.0.2228/)

### Python: make the comments available as a property of functions, objects, and module: a docstring.

```python
#!/usr/bin/env python
"""This is a file/module docstring. It has to be a string and be
the first object in the file."""

def foo(bar):
    """This is a function docstring. It must be the first object
    in the function."""
    pass
```

### Taking things one step further. 

Showing example code and output in the docstring helps the programmer understand how to use the library.
It can also be used for automated testing.

[https://docs.python.org/3/library/doctest.html](https://docs.python.org/3/library/doctest.html)

Basic inheritance
------------------

Sub-class/Child class: derives from (or extends) parent.

```python
class Parent():
    def somemethod(self):
        print("oink")

class Child(Parent):
    def othermethod(self):
        """ extends parent with a new method """
```

Classes provide type identity which gives a contract about interface.
Children will have the same interface, but can choose to extend it.

Extending built-ins
-------------------

Build in types can also be extended (code from the OOP book)

```python
class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)
```

Overriding and super
--------------------

Overriding the behavior/method of a parent. The interface is the same, but what the method does is changed.

```python
class Contact:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)
    def foo(self):
        print('Foo')

class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def foo(self):
        print('Bazooka')
```

The above code has one bug: Friend adds a phone attribute, but fails
to add the friend to all_contacts. It also contains duplicate code,
which can cause further bugs at a later stage.

A solution: super()

``` python
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init(name, email)
        self.phone = phone
    def foo(self):
        print('Bazooka')
```





Multiple inheritance
--------------------

Multiple Inheritance: a class specifies several classes that it inherits from.

```python
class A():
    def athing(self):
        pass
class B():
    def bthing(self):
        pass
class M(A, B):
    def mthing(self):
        pass

m = M()
```

Now `M` inherits from both `A` and `B`. We can call

```python
m.athing()
m.bthing()
m.mthing()
```


### Mix-ins

Mix-ins: classes that are not intended to be used on their own. Extends or modifies other classes.

Example use in standard library:
[https://docs.python.org/3/library/socketserver.html](https://docs.python.org/3/library/socketserver.html)

Specify mix-ins first to override method(s) in the normal base/parent class. Example from Python documentation: 

``` python
class ThreadingUDPServer(ThreadingMixIn, UDPServer):
    pass
```


### Multiple inheritance can be complicated.

Some languages (like Java) do not allow multiple inheritance, restricting programmers to avoid potential complexity issues.

Java provides _Interfaces_ to let a class inherit the interface of multiple types. A Java class can inherit from one class and several interfaces. The child class must implement each of the methods in the interfaces as there is no code to inherit.

Diamond problem
----------------

```python
class A:
    def foo(self):
        print("This is A")
    def baz(self):
        print("baz A")

class B(A):
    def foo(self):
        print("This is B")
        super().foo()
    def bar(self):
        print("bar B")

class C(A):
    def foo(self):
        print("This is C")
        super().foo()
    def bar(self):
        print("bar C")
    def baz(self):
        print("baz C")

class D(B,C):
    def foo(self):
        print("This is D")
        super().foo()

b = B()
c = C()
d = D()

# in which order are the methods called?
print("Calling b.foo()")
b.foo()
print("Calling c.foo()")
c.foo()
print("Calling d.foo()")
d.foo()
print("Calling d.bar()")
d.bar()
print("Calling d.baz()")
d.baz()
```

![Diamond problem](figs/diamond_problem.png)

Method resolution order
-----------------------

The defined search order through the objects and classes.

Think of this as a searching problem: Python searches objects and classes to find the first matching attribute or method. It starts by looking at the object, then the classes. 

Can be modified by modifying the `__mro__` attribute (this is beyond the scope of this lecture).

`super()` finds the _next_ class in the search list, not necessarily the parent of the current object/class. 

The method and attribute lookup order for the D object is the d object, then the classes in the following order: D, B, C, A

If you are curious and want to dive deeper there are a few starting points here: 
* [Python 3 documentation, look for MRO](https://docs.python.org/3/reference/datamodel.html)
* [Description of the MRO algorithm](https://www.python.org/download/releases/2.3/mro/)

Polymorphism
------------

One basic definition: when the type of the object determines the behavior when calling a method or interface.

```python
class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

someaudiofile.play()
```

We have seen this with the initial PyGame examples.

Note that there are multiple types of polymorphism. We will get back to this later in the course. The above is typically called "Subtype Polymorphism". 


Python duck typing goes beyond this by only caring about the interface and not the type.

```python
print(3 + 5)
print(3.1415926 + 5.8)
print('Hello ' + 'there')

class Tomato:
    def __init__(self, desc="Tomato"):
        self.desc = desc
    def __repr__(self):
        return self.desc
    def __add__(self, other):
        print("Smashing {} and {}".format(self.desc, other))
        return Tomato("Ketchup")

t1 = Tomato()
t2 = Tomato('Tomato B')
print(t1 + t2) # What does this print?
```


Lecture review and questions
==========

Don't worry if you don't have a firm grasp of the following yet. We will re-visit or use many of them throughout in the course, and you will get a better understanding when you try to use them in programs. 

### Terms
Can you give a short explanation and example of the following? 

- Class
- Object
- Attribute
- Method
- Inherit / inheritance
- Parent vs. Child
- Extending vs. overriding (in classes)
- Multiple inheritance. 
- Method resolution order
- Polymorphism

### Exercise 1

- create a class `A` with a method `foo()`.
- create a class `B` which
  - inherits from `A`
  - extends `A` with a method `bar()`
  - overrides `A`'s `foo()`
- create objects from `A` and `B`. 

Let the methods print out some unique text and call methods on the objects created from the two classes. 
Use it to explore how inheritance works. 

### Exercise 2

Write a Python program that demonstrates the terms defined above. It doesn't have to do anything useful and you can look at the code from the lectures, but try to write your own code. 

