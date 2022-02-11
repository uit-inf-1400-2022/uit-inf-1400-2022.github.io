# When to Use Object-Oriented Programming
In this lecture, we will look at when to use OO programming.

**Covers the following:**
- What is an object -> data and behavior
- What are getters and setters
- Private versus Public
- Wrapping data behaviors using properties

## What is an object -> data and behavior

One view:
- objects have both data and behaviour
- only data -> collections (lists, tuples, sets, dicionaries etc.)
- only behaviour -> functions

![tekst](http://4.bp.blogspot.com/-ZVMs-2__6pg/UES3ykgiAlI/AAAAAAAADsw/aQEHMFFQ3nI/s1600/Cppw1.3.png)

Figur hentet fra: http://4.bp.blogspot.com/-ZVMs-2__6pg/UES3ykgiAlI/AAAAAAAADsw/aQEHMFFQ3nI/s1600/Cppw1.3.png

Use built-in data structures unless (or until) there is an obvious need to define a class. There is no reason to add an extra level of complexity if it doesn't help organize our code.

**Example using functions**
```python
import math

square = [(1,1),(1,2),(2,2),(2,1)]

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def perimeter(polygon):
    thePerimeter=0
    #adding the first polygon in the end of the points list
    points = polygon + [polygon[0]]
    for i in range (len(polygon)):
        thePerimeter+=distance(points[i], points[i+1])
    return thePerimeter
```
```python
>>> perimeter(square)
4.0
```
**Same example using classes**
```python
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,p2):
        return math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2)
    
class Polygon:
    def __init__(self):
        self.vertices = []
    def add_point(self,point):
        self.vertices.append((point))
    def perimeter(self):
        thePerimeter = 0
        #adding the first point at the end of the list (start and end is the same point)
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            thePerimeter += points[i].distance(points[i+1])
        return thePerimeter
```
```python
>>> square=Polygon()
>>> square.add_point(Point(1,1))
>>> square.add_point(Point(1,2))
>>> square.add_point(Point(2,2))
>>> square.add_point(Point(2,1))    
>>> square.perimeter()
4.0
```
Hmm more lines, more work.... But it is easier to understand what a Point are than p1,p2. Easier for other people (and you) to resuse your code later. Don't have to rewrite same code again.

## setter and getters
Many languages encourage the use of getters and setters (some says always, may be used for them in the future).

**All public**
```python 
class Color:
    def __init__(self,rgb_value,name):
        self.rgb_value = rgb_value
        self.name = name
        
    #getters and setters
    def getRgb_value(self):
        return self.rgb_value
    def setRgb_value(self,newRgb_value):
        self.rgb_value = newRgb_value
        
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
```
We can access attributes/properties directly, dont have to go trough methods.
```python
>>> c = Color(0xff0000,"red")
>>> c.rgb_value
16711680
>>> c.getRgb_value()
16711680
>>> c.rgb_value=0x00ff00
>>> c.rgb_value
65280
```
The value of rgb no longer reflects the name of the color (green is not red...)

**Semi private**
In python we can add an underscore before an attribute/method, to signal the our intentions are that it is private (but it is still public).

```python
class Color:
    def __init__(self,rgb_value,name):
        self._rgb_value = rgb_value
        self._name = name
        
    #getters and setters
    def get_rgb_value(self):
        return self._rgb_value
    def set_rgb_value(self,newRgb_value):
        self._rgb_value = newRgb_value
        
    def get_name(self):
        return self._name
    def set_name(self,newName):
        self._name = newName
```
We can still access attributes/properties directly, but we are ignoring the intention from the programmer that has created the code.

```python
>>> c = Color(0xff0000,"red")
>>> c._rgb_value
16711680
>>> c._rgb_value=0x0000ff
>>> c._rgb_value
255
```
**With properties**
We want to work with the properties like we had direct access to them, but still in a "safe" way.
```python
class Color:
    def __init__(self,rgb_value,name):
        self._rgb_value = rgb_value
        self._name = name
        
    #getters and setters
    def _get_rgb_value(self):
        return self._rgb_value
    def _set_rgb_value(self,newRgb_value):
        #0xffffff biggest number which are 16777215 
        if newRgb_value>16777215 or newRgb_value<0:
            raise ValueError("Not an valid rgb number!")
        self._rgb_value = newRgb_value
        
    def _get_name(self):
        return self._name
    def _set_name(self,newName):
        if not newName:
            raise ValueError("No name..")
        self._name = newName
        
    rgb_value = property(_get_rgb_value,_set_rgb_value)
    name = property(_get_name,_set_name)
```
```python
>>> c = Color(0xff0000,"red")
>>> c.rgb_value=0xffffff
>>> c.rgb_value
16777215
>>> c._rgb_value
16777215
>>> c.rgb_value=0xffffff1
Traceback (most recent call last):

  File , line 1, in <module>
    c.rgb_value=0xffffff1

  File "colors.py", line 19, in _set_rgb_value
    raise ValueError("Not an valid rgb number!")

ValueError: Not an valid rgb number!
```
Here we can see that we are using the methods to have controll on what data that can be added to the properties. THe property constructor can accept two additional arguments, a delete function and a docstring. If we do not supply this argument, the docstring will instead be copied from the docstring for the first argument (the getter method).


**properties using decorators**
A little sneak peak at decorators (more later in the course).

Python has a simpler way of defining properties using decorators. Decorators are defined using @-syntax.

```python
class Color:
    def __init__(self,rgb_value,name):
        self._rgb_value = rgb_value
        self._name = name
    
    @property
    def rgb_value(self):
        "This is the rgb_value property"
        return self._rgb_value
    
    @rgb_value.setter
    def rgb_value(self,newRgb_value):
        if newRgb_value>16777215 or newRgb_value<0:
            raise ValueError("Not an valid rgb number!")
        self._rgb_value = newRgb_value
    
    @property
    def name(self):
        return self._name
        
    
    @name.setter
    def name(self,newName):
        if not newName:
            raise ValueError("No name..")
        self._name = newName
```
```python 
>>> c = Color(0xff0000,"red")
>>> c.rgb_value=0xffffff
>>> c.rgb_value
16777215
>>> c._rgb_value
16777215
>>> c.rgb_value=0xffffff1
Traceback (most recent call last):

  File , line 1, in <module>
    c.rgb_value=0xffffff1

  File "colors-with.dec.py", line 19, in _set_rgb_value
    raise ValueError("Not an valid rgb number!")

ValueError: Not an valid rgb number!
```

**When to use properties**
- Methods and functions should represent action
- Data should be represented as attributes
- When you need to add attribute control (like filtering) or other internal representation, use properties.

## Managing objects
- using other objects in a class (composite design)
- Dont make a method that does everything, rather split it up on helper methods and use them in a "master" method (allows us to inherit from a base class and overide some of the helper methods). 
- Dont make one class that does everything, split up and use inheritance.
- Ask the question: "Will my code be easier to read and extend if I transform this into a class?"

Some questions that can be asked:
- Do you really need a class?
- Does the class add clarity?
- What are the implications of introducing a class? Will it be easier or harder to solve the problem now/in the future?
- What are the alternatives?


### Exercise
Code below there is a simple account class.
```python
class Account:
    def __init__(self, balance=0):
        self._balance=balance
        
    
    #getter and setter
    def get_balance(self):
        return self._balance
    
    def _set_balance(self,newBalance):
        self._balance=newBalance
        
    #special methods
    def withdraw(self,amount):
        if self._balance<amount:
            raise Exception("You dont have that kind of money!")
        else:
            self._balance-=amount
            
    def deposit(self, amount):
        self._balance+=amount
```
1. Explain the code to the person next to you        
2. Try to make changes, use *property*
3. What other classes to you feel should be here (think simple), if this is an account in a bank.
