#!/usr/bin/env python3
#
# John Markus Bjørndalen, 2012-01-09
# Minor updates 2021-01-25
#

"""
Example code demonstrating some of the inheritance mechanisms in Python.

There are two types of attributes:

a) attributes (and methods) defined at class level show up in the __dict__
   dictionary of the class.

b) attributes defined at object level (assigned in any of the methods,
   including __init__ etc, and from external code) show up in the
   object's __dict__ attribute.

The __dict__ attribute is one of the special attributes that are automatically
initialized by python.

When Python tries to resolve someobject.someattribute, it will search
as follows (slightly simplified):

1. search the object's __dict__ for the attribute. If found there, use that one.
2. If not found, search the __dict__ of the class.
3. If not found, search the __dict__ of the parent classes
   of the class. This is done by searching recursively through
   the __bases__ attribute of each class (see __mro__ of the class for more information if
   you use multiple inheritance).

We call this process attribute lookup or attribute search.


A side effect of the way Python implements inheritance and attribute
lookup is that attributes defined in Parent.__init__ will only be
inherited to the child if Child.__init__ calls Parent.__init__ (see
example code below). This means that it is important to follow the
convention of calling the parent's __init__ method from child classes
since there is no other automatic mechanism for ensuring this
inheritance. The easy way to do this is to use super().__init__().


Extra / advanced topic:
-----------------------

The above behaviour can be modified using Metaobject Programming, but
that is outside the scope of this course.

For a more detailed discussion:

http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html

There is also some information in the Python reference (look for
method lookup and attribute lookup):

http://docs.python.org/reference/datamodel.html
"""


def dprint(d, dname, prefix=""):
    """Helper function to pretty-print dictionaries.
    Also check the pprint module for pretty printing."""
    print(f"{prefix}{dname} = {{")
    for k in sorted(d.keys()):
        print(f"{prefix}  {str(k):12s} : {str(d[k]):10s}")
    print(f"{prefix}}}")


# *************************************************************************
#
# Part 1: Demonstrating where attributes are located in classes and objects.
#
# *************************************************************************
#
# Run the program below and study the source code and the output.
#
# Try to use the 3-step method shown in the docstring above to find out
# where methods and attributes are found.
#
#

class A:
    cvar1 = 400
    cvar1b = 200

    def __init__(self):
        self.ovar1 = 10


class B(A):
    cvar2 = 200

    def __init__(self):
        A.__init__(self)
        self.ovar2 = 20


a = A()
b = B()


print("Dumping the __dict__ dictionaries of the classes and objects.")
dprint(A.__dict__, "A.__dict__")
dprint(B.__dict__, "B.__dict__")
dprint(a.__dict__, "a.__dict__")
dprint(b.__dict__, "b.__dict__")

print("b.__class__ can be used to find the class of the b object: ")
print("    ", b.__class__)

print("B.__bases__ is a tuple with the parent class(es) of B")
print("    ", B.__bases__)

print()
print("Setting b.cvar2 = 900. This 'hides' the class level cvar2 attribute.")
b.cvar2 = 900
dprint(b.__dict__, "b.__dict__")

print()
print("Setting b.newvar = 950. This introduces a new attribute from outside.")
b.newvar = 900
dprint(b.__dict__, "b.__dict__")


# ***************************************************
#
# Part 2: attribute name collisions and name mangling
#
# ***************************************************
#
#
#
# Attributes that start with __ are "mangled".
#
# Python automatically renames attributes starting with __ to include the class
# name. This process is called mangling and reduces the chance of name collisions
# for attributes.
#
# The example below shows an example of a child class defining attributes with
# identical names to the parent class. This should not cause any problems since
# the names are mangled, and methods defined in C will use the _C__cvar attribute,
# and methods in D will use the _D__cvar attribute.
#
# Mangling is only done from inside methods defined in classes.
# If you try to make a d.__foo below (ex: d.__foo = 42 from outside the classes),
# it will be assigned as d.__foo with no mangling.
#
# Other languages may not have this type of mechanism, which can cause problems
# that can be difficult to manage in large class hieararchies. A term related to
# this is "deep inheritance".
#
# Study the program output to see the effect.
#

class C:
    __cvar = 10
    _oink = 2      # single underscore does not trigger mangling.

    def __init__(self):
        self.__ovar = 20


class D(C):
    __cvar = 15

    def __init__(self):
        C.__init__(self)
        self.__ovar = 25


c = C()
d = D()

dprint(C.__dict__, "C.__dict__")
dprint(D.__dict__, "D.__dict__")
dprint(c.__dict__, "c.__dict__")
dprint(d.__dict__, "d.__dict__")

print("Setting c.__cvar = 42")
c.__cvar = 42
dprint(c.__dict__, "c.__dict__")
