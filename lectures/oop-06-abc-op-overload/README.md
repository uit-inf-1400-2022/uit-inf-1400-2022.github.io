# Abstract Base Classes and Operator Overloading

In this lecture we will look at:
- What is a abstract base class
- Why use abstract base class
- Creating our own abstract base classes
- Operator overloading
- Extending built-ins


## Abstract Base Class
An abstract base class (ABC) is a class that cannot be used to create objects. The purpose of such classes is to define interfaces. 
This interface is a kind of a promise that derived class will provide the methods and properties that the abstract base class have specified. 
Can only create instances of a derived class if the class reimplement all the abstract methods and abstract properties they have inherited. We cannot create an instance of an abstract class.

**What does define a class to be abstract?**
- It must have a metaclass of abc.ABCMeta or from one of its subclasses. abc.ABC is a helper class that has abc.ABCMeta as its metaclass.
- It must have a least one of: abstract method (@abc.abstractmethod) or abstract property (@property @abc.abstractmethod) or both.

abc.ABC is a helper class that can be used by deriving, avoiding the confusing metaclass usage, to create an abstract class. Decorators @abc.abstractmethod and @abc.abstractproperty to create abstract method or abstract property. In UML diagrams abstract classes/method/property is marked with italic/slanted font.


![abc](https://user-images.githubusercontent.com/97092780/153901267-13eb9ab0-4c88-4940-9573-219ed647b149.png)



```python
import abc
class AbstractClass(abc.ABC):
    @abc.abstractmethod
    def a_method(self):
        pass
        
class ConcreteClass_1(AbstractClass):
    def a_method(self):
        print("I am very concrete, not abstract!")

class ConcreteClass_2(AbstractClass):
    def a_method(self):
        print("I am also concrete...")
```
```python 
>>> a=AbstractClass()
TypeError: Can't instantiate abstract class abstractClass with abstract method a_method
```
No suprise here, since we cannot create an instance of a abstract class.
```python 
>> c1=ConcreteClass_1()
>> c1.a_method()
"I am very concrete, not abstract!"
>> c2=ConcreteClass_2()
>> c2.a_method()
"I am also concrete..."
```
We have implemented the abstract parts of the abstract class, so we can make instances of the concrete classes.
```python
class AbstractClass(abc.ABC):   
    @abc.abstractmethod
    def a_method(self):
        pass
class StillAbstract(abstractClass):
    def move(self):
        print("I want to move, but i cant since i am so abstract!")
```
```python 
>>> s=StillAbstract()
TypeError: Can't instantiate abstract class stillAbstract with abstract method a_method
```
Since we havent implemented the abstracts parts of the parentclass (which are abstract), we cannot make instances of that class.

Example with abstract property
```python
class AbstractColor(abc.ABC):
    def __init__(self,rgb_value,name):
        self._rgb_value = rgb_value
        self._name = name
    
    @property
    @abc.abstractmethod
    def rgb_value(self):
        "This is the rgb_value property"
        pass
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,newName):
        if not newName:
            raise ValueError("No name..")
        self._name = newName
        
class ConcreteColor(AbstractColor):   
    @property
    def rgb_value(self):
        return self._rgb_value
    
    @rgb_value.setter
    def rgb_value(self,newRgb_value):
        if newRgb_value>16777215 or newRgb_value<0:
            raise ValueError("Not an valid rgb number!")
        self.__rgb_value = newRgb_value
```
```python
>>> c=ConcreteColor(0xeeffee,"Strange color")
>>> c.rgb_value
15663086
>>> c.name
'Strange color'
```
### Excerices
1. Create an abstract class **Employee** that has two attributes: first name and last name. It should have one abstract method **get_salary()**
2. Create two classes: **FulltimeEmployee** and **HourlyEmployee** that implements the abstract method from parent class **Employee**. For FulltimeEmployee the salary is an attribute for that class, while HourlyEmployee has two attributes, hours_worked and rate.
3. Create a fourth class, **Payroll** that contains a list with all the employees. It should have two methods, one for adding new employees and one for printing out all the employees with name and salary.
4. Add some employees (both types of employees) and print them out to screen. (try to extend the magic build_in method __str__)


## Operator overloading
In python we have "magic methods", that start with __ and end with __. 
```python 
__add__(a,b), __mul__(a,b),__lt__(a,b), __contains__(a,b) etc. 
```
With use of this magic methods we can overload an operator. When we overload an operator we extend the meaning beyond predefined meaning. When + is used, the magic method __add__ is automatically invoked. If we try to + on two different datatypes it will throw a error, because it wont know how to handle it. But we can overload the operator so it can handle it.
```python
#Example of adding a string to a int.
class powerInt(int):
    def __add__(self,aNumberString):
        return self.real+int(aNumberString)
```
```python
>>> p=powerInt(2)
>>> p+"13"
15
```
```python
__add__(a,b) +
__sub__(a,b) -
__mul__(a, b) *
__truediv__(a, b) /
__floordiv__(a, b) //
__mod__(a, b) %
__pow__(a, b) **
```
[Link to python documentation about operators](https://docs.python.org/3/library/operator.html)

We want to add two colors with + operator and we want to check if two colors are equal. Then we can implement ``` __add__(self,other) and __eg__(self,other) method ```, so we can do oneColor+secondColor or oneColor==secondColor.
```python
class Color:
    def __init__(self,rgb_value,name):
        self.__rgb_value = rgb_value
        self.__name = name
        
    #getters and setters
    def _get_rgb_value(self):
        return self.__rgb_value
    def _set_rgb_value(self,newRgb_value):
        #0xffffff biggest number which are 16777215 
        if newRgb_value>16777215 or newRgb_value<0:
            raise ValueError("Not an valid rgb number!")
        self.__rgb_value = newRgb_value
        
    def _get_name(self):
        return self.__name
    def _set_name(self,newName):
        if not newName:
            raise ValueError("No name..")
        self.__name = newName
        
    rgb_value = property(_get_rgb_value,_set_rgb_value)
    name = property(_get_name,_set_name)
    
    def __add__(self,other):
        return self.rgb_value+other.rgb_value
    
    def __eq__(self, other):
        if self.rgb_value==other.rgb_value:
            return True
        else:
            return False
```
```python 
>>> c1=c1=Color(0x04fe0f,"Very")
>>> c2=Color(0x04fe0f," Strange")
>>> c1+c2
654366
>>> c1==c2
True
```


### Excerise
1. Extend **PowerInt** so it can handle -,*,<,>,/ when right operand is a string. 
2. Extend **PowerInt** so it can handle another datatype than string as the right operand.
