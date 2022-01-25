Summary and examples
====================

Lecture 2021-01-26
@ John Markus Bjørndalen

Today's lecture topics
----------------------
- Looking through some of the topics covered by now through example code. 
- Example code 
  - Simple vector class
  - Simple point class
- Object vs. class
  - class attributes (read vs. assign) 
  - searching for attributes (through examples) 
    - public static void main in Java vs. main() in C. 
  - adding methods to objects at runtime. 




Vector class
----------

Simple vector class to illustrate vectors. 

Don't use this one in your games. Vector2 from PyGame is faster and more complete. 

This also illustrates the following relationships: 
- has-a (contains something / composition) 
- is-a (inheritance)


Point class
---------------

Chapter 2 in OOP 

Local copy is in [code/point.py](code/point.py). 


Class attributes / variables and attribute search
-----------------------------

Chapter 3 in OOP introces the following example. 

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
        super().__init(name, email)
        self.phone = phone
    def foo(self):
        print('Bazooka')
```

This example code illustrates how Python finds an attribute in an object. 
* [classattribs.py](code/classattribs.py)

A more complete example that prints out the attributes of objects and classes. This illustrates the discussion we had about attribute search and method resolution order (MRO) in the previous lecture: 

* [inherit-mechanism.py](code/inherit-mechanism.py)


Review questions
================

- what is a class attribute?  where is it stored? 
- what is the search order for attributes in Python? 
- what is the difference between has-a vs. is-a relationships in object oriented programming? 

