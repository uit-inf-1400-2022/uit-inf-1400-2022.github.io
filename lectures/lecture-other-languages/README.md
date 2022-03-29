OOP in other languages
=======================

- OOP in other languages (Java, C++, ...)
- Classless object oriented languages


We will only scratch the surface of these other languages as the main
focus is on how some of the design choices influence use patterns in
the languages as well as further design choices.


Java
----

Java is a statically typed, object oriented language that compiles
down to Java bytecode. The bytecode targets a Java virtual machine
that is intended to be portable across platforms so that you can take
a single compiled program and run it on many different platforms.

That almost works. People quickly ran into portability issues, but
Java programs can often be moved directly between desktop operating
systems (at least).

The byte code that has to be interpreted by a virtual machine makes
Java, in principle, much slower than languages that are compiled
directly to machine code. Much of that overhead is removed by Just In
Time (JIT) compiling the byte code, which means that the byte code is
compiled down to machine code at run time.

Many saw Java, when it was introduced, as an attempt to resolve some
of the complexity problems with C++.

Syntax wise, it has a lot of similarity with C# and C++. The three
languages also share many concepts, but also differ in many ways due
to trying to solve different problems.

### Hello world and concepts you stumble across while trying to get your first Java program to run

In Java, everything is defined within a class. There are no modules
similar to Python modules (the closest is a combination of packages
and large classes), no global variables and no functions that can
exist outside a class.

Therefore, hello world in Java becomes

```java
public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hello, World");
    }
}
```

To start your program, you need an entry point. The defined way of
starting a Java program is to specify a "main" class (when you run
`java HelloWorld`, the runtime looks for the HelloWorld class). The
Java runtime system then looks for a `main` method inside the class.

That main method has to be a static method (in other words: a class
method) so that you can invoke it without having an instance of the
specified class. Java doesn't create a default object of the main
class - that would require there to be a default constructor for the
class with an interface that the runtime could use.

Both the class and the main methods must be public so that the runtime
system can access them.

`System` is a globally defined class that works more or less as a name
space (a module equivalent in Java would be a class with class level
attributes). Standard out is an object (`out`) that has a `println`
method. In that way, the line with the print expression demonstrates
both class attributes and attribute references.


The program can be compiled and executed as follows. 
We specify the class that Java should load and inspect to find the `main` method:
```
> javac HelloWorld.java
> java HelloWorld
Hello, World
```

If you need objects, you need to instantiate them in the main method:

```java
public class HelloWorld {

    public static void main(String[] args) {
        HelloWorld helloWorld = new HelloWorld();
        System.out.println("Hello, World");
    }
}
```

### R.I.P. Multiple inheritance.

Multiple inheritance can cause many issues if you don't use it
properly or carefully enough.

Java only supports single inheritance. This, however, is too
restrictive and causes issues with objects that have to support
multiple interfaces.

As an alternative solution, Java has a separate "inheritance"
mechanism: Interfaces.

By implementing an interface, you specify which methods you implement
and that those methods should work in the context of that interface. A
sortable interface that specifies a "sort" method means that you will
actually try to sort the contents of your object if somebody calls it.

You do _not_ inherit the implementation of the method (it doesn't
exist in the first place), only the method signature and type
identity.

Example from http://www.tutorialspoint.com/java/java_interfaces.htm :

```java
/* File name : Animal.java */
interface Animal {

   public void eat();
   public void travel();
}
```
```java
/* File name : MammalInt.java */
public class MammalInt implements Animal{

   public void eat(){
      System.out.println("Mammal eats");
   }

   public void travel(){
      System.out.println("Mammal travels");
   }

   public int noOfLegs(){
      return 0;
   }

   public static void main(String args[]){
      MammalInt m = new MammalInt();
      m.eat();
      m.travel();
   }
}
```

### Primitive types vs. objects

Primitive types in Java (int etc) are not objects. There are, however
object types that can represent the same values:

```java
public class Test
{
    public static void main(String[] args) {
        int val = 42;
        Integer foo = 42;
        System.out.println("type of foo " + foo.getClass().getName());  // type of foo java.lang.Integer
        System.out.println("type of val " + val.getClass().getName());  // fails when trying to compile (error: int cannot be dereferenced)
    }
}
```

In that sense, you can say that Java has two type systems that are not
directly compatible. The primitive types, however, can be more
efficient in some cases.

### Methods vs. functions

Methods are defined on classes. There are no functions. If you need an
anonymous function for something, you need to create an anonymous
class that has a method.

This combined with static type checking means that, for instance,
event based and functional programming need to use Interfaces or
parent classes that define methods (so that receivers of a "function"
can call those methods) and with classes for each specific case.

A filter pipeline could, for instance, be something like this in
Python. We're demonstrating multiple options for implementing filter
stages:

```python
def highFilter(maxval):
    def func(val):
        return min(val, maxval)
    return func

class LowFilter:
    def __init__(self, minval):
        self.minval = minval
    def __call__(self, val):
        return max(val, self.minval)

pipe = [
    highFilter(301),
    LowFilter(100),
    lambda x: x % 2,
    ]

# apply every filter in the pipe one by one
v = 400
for f in pipe:
    v = f(v)

print(v)  # prints 1, which is rubbish, but you get the idea
```

Java requires that methods are defined in classes, so we need to
define a class per stage type. This example shows that you can also
create an instance of an anonymous class if you don't need to re-use
it elsewhere:

```java
interface Filter {
    int doFilter(int val);
};

class HighFilter implements Filter{
    int maxval;
    HighFilter(int maxvalue) {
        maxval = maxvalue;
    }
    public int doFilter(int value) {
        return Math.min(value, maxval);
    }
};

class LowFilter implements Filter{
    int minval;
    LowFilter(int minvalue) {
        minval = minvalue;
    }
    public int doFilter(int value) {
        return Math.max(value, minval);
    }
};


public class FilterPipe {
    public static void main(String[] args) {
        Filter[] pipe = {
            new HighFilter(301),
            new LowFilter(100),

            // anonymous class
            new Filter() {
                public int doFilter(int value) {
                    return value % 2;
                }
            }
        };
        int val = 400;
        for (int i = 0; i < pipe.length; i++) {
            val = pipe[i].doFilter(val);
        }
        System.out.println("Res is " + val); // Res is 300
    }
}
```

Callbacks often implement a specific interface rather than inheriting
from a callback class.

Dig deeper: Java 8 introduced lambda expressions (see 
[here](http://www.oracle.com/webfolder/technetwork/tutorials/obe/java/Lambda-QuickStart/index.html)) 
that simplify the anonymous classes by providing a shorthand syntax.

### Static type checking and Generics

Examples from http://en.wikipedia.org/wiki/Generics_in_Java

One of the early problems in Java was that people often needed generic
container classes that could hold values of different types. A way of
solving this was to (ab)use casting: pretend it's an "Object" type
when adding it to a container and then cast it back to the right type
when you retrieve it from the container and use it. If you cast the
retrieved value to the wrong type and try to use it, you end up with
errors:

```java
List v = new ArrayList();
v.add("test");
Integer i = (Integer)v.get(0); // Run time error
```

This resulted in run time type errors, something that statically typed
languages are supposed to protect against. One of the major selling
points (catch type errors at compile time) had a loop hole.

C++ already had a solution for this through the template system.

In Java, they solved this by introducing Generics, which uses a
similar idea to templates. Using generics, we can write an
implementation that uses "wildcard" types for variables and
arguments. When you create instances of the new generic type, you
specify the actual type for the wildcard, and a specific
implementation for that type will be generated (or re-used if already
existing).

```java
List<String> v = new ArrayList<>();
v.add("test");
Integer i = v.get(0); // (type error)  compile-time error
```

Example implementation of a generic type:

```java
public class Entry<KeyType, ValueType> {

    private final KeyType key;
    private final ValueType value;

    public Entry(KeyType key, ValueType value) {
        this.key = key;
        this.value = value;
    }

    public KeyType getKey() {
        return key;
    }

    public ValueType getValue() {
        return value;
    }

    public String toString() {
        return "(" + key + ", " + value + ")";
    }
}
```

```java
Entry<String, String> grade = new Entry<String, String>("Mike", "A");
Entry<String, Integer> mark = new Entry<String, Integer>("Mike", 100);
System.out.println("grade: " + grade);
System.out.println("mark: " + mark);

Entry<Integer, Boolean> prime = new Entry<Integer, Boolean>(13, true);
if (prime.getValue())
   System.out.println(prime.getKey() + " is prime.");
else
   System.out.println(prime.getKey() + " is not prime.");
```
```
grade: (Mike, A)
mark: (Mike, 100)
13 is prime.
```

type checking vs. object casting vs. generics.  c++ templates.


### Encapsulation and protection

See this page for more information:
https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html

In Python, we rely on conventions and the name-rewriting mechanims
(mangling) for attributes and methods that start with with double
underscores to protect internal state and methods in objects from
external users.

Java provides a stricter form of access control: classes, attributes
and methods are tagged as public (available from the outside), private
(only available within the class) or protected (restricted but
subclass can also access).

A table from the above link shows access to members permitted by each
of the tags/modifiers:

| modifier    | Class | Package | Subclass | World |
|-------------|-------|---------|----------|-------|
| public      | y     | y       | y        | y     |
| protected   | y     | y       | y        | n     |
| no modifier | y     | y       | n        | n     |
| private     | y     | n       | n        | n     |


As we discussed in an earlier lecture, this type of protection can be
circumvented if a user really wants to. It's fairly simple in C++:

```c++
#define private public
#include <somelib>
```

Java uses a well-defined virtual machine and instruction set, so one
way of getting around it could be to rewrite the byte code in the
.class files.

### Polymorphism

Inheritance provides one type of polymorphism similar to what we have
experienced in Python. This goes both for inherited methods that are
redefined in subclasses or methods that need to be implemented based
on method signatures specified in interfaces. This is often called
"single dispatch" polymorphism: the type of the object you invoke the
method on determines which implementation you call. 
Also see "Subtyping". 

### Additional overriding / dispatching

Java also provides an additional level of dispatch based on argument
types (though this is not quite the same as multiple dispatch).

```java
class Dispatch {
    public void foo(int val) {
        System.out.println("Got an integer: " + val);
    }
    public void foo(String val) {
        System.out.println("Got a string: " + val);
    }

    public static void main(String[] args) {
        Dispatch d = new Dispatch();

        d.foo("Hello");
        d.foo(42);
    }
}
```

Running this program resuls in:


```
> javac Dispatch.java
> java Dispatch
Got a string: Hello
Got an integer: 42
```

Also see "Ad Hoc" polymorphism. 


OOP without classes - JavaScript
-----------------------------------

JavaScript is an object-oriented language, and you can easily create
objects with methods there.

For more info see also "The Principles of Object-Oriented JavaScript",
Nicholas C. Zakas, 2014, ISBN 978-1-59327-540-2. It's a recommended
read if you want to understand how JavaScript supports Object-Oriented
programming (and several pitfalls that we don't cover here).

Some central oo concepts (keywords):
- Encapsulation
- Aggregation
- Inheritance
- Polymorphism


JavaScript has two basic types:
- primitive types
- reference types (basically references to objects/locations in memory)

Primitive types can be identified using `typeof`:

```javascript
// From page 4 in the book:
console.log(typeof "Nicholas"); // "string"
console.log(typeof 10);         // "number"
console.log(typeof 5.1);        // "number"
console.log(typeof true);       // "boolean"
console.log(typeof undefined);  // "undefined"
```

### Creating simple objects

A basic object can be created as follows (using a "Literal" syntax):

```javascript
var obj1 = {
    name : "Hello",
    age  : 42
};
```

Or, using a syntax closer to python's dicts:
```javascript
var obj2 = {
    "name" : "Hello Again",
    "age"  : 400
};
```

Objects in JavaScript are similar to dicts or hash tables in other
languages.  Be a bit careful though, the language is loaded with
bullets aimed at your toes, and the objects may not behave exactly
as you expect from dicts.

You can also create objects by creating an `Object` instance and 
setting properties afterwards:

```javascript
var obj3 = new Object();
obj3.name = "Hello";
obj3["age"] = 9000;
```



Attributes / properties in objects can be referenced using dot and
bracket notation. Using `jjs` (Nashorn, see below).

```javascript
print("Dot syntax   :", obj1.name, obj2.name);
print('"Dict" syntax:', obj1['name'], obj2["name"]);
```

Produces:
```
Dot syntax   : Hello Hello Again
"Dict" syntax: Hello Hello Again
```

Javascript with Java VM:
- Rhino was used for JavaScript scripting in Java up to Java 1.7 (as `rhino`).
- Nashorn is used from 1.8 (as `jjs`):
- GraalVM is suggested from Java 11 (Nashorn was deprecated from Java 11)

If you have Node.js, you can get a command line prompt using "js". 

### Methods

Objects can also contain methods:

```javascript
var fly1 = {
    name : "Some plane",
    fly  : function() {
        print("Flap, flap");
    }
};

print("fly1 name", fly1.name);
fly1.fly();
```

Produces
```
fly1 name Some plane
Flap, flap
```

JavaScript functions are, like Python functions, first class objects
that can be passed around like other objects and values. This is how
the method is created above.


### Creating objects using constructors

A typical method for creating objects in JS is to use a constructor function:

```javascript
function FlappyPlane() {
    // empty yet
}

var fplane = new FlappyPlane();

print(fplane);
print(fplane instanceof FlappyPlane);
print(fplane.constructor);
```

The `FlappyPlane` function is now a constructor for flappy planes. The
`new` operator creates a new instance of a given object type and keeps
a reference back to the constructor function through the `constructor`
property (similar to the `__class__` attribute in Python, except it's
pointing to a constructor function). This can be used to give objects
a type identity.

A constructor doesn't return the new object, instead it modifies an
object created by `new` that is available through the `this` variable
(similar to C++ etc).

```javascript
function FlappyPlane() {
    this.flap = function() {
        print("Flap flap");
    }
}
var fplane = new FlappyPlane();
fplane.flap();
```

Any attribute that is assigned to the `this` variable is visible when
accessing the object from the outside. The scoping rules of JavaScript
creates additional options that we can use to introduce protected or
internal variables and functions:

```javascript
function FlappyPlane(planeid) {
    this.planeid = planeid;
    var test = planeid;
    this.flap = function() {
        print("Flap flap " + this.planeid);
        print("    ouch  " + planeid);
        print("    ouch2 " + test);
    }
}
var fplane = new FlappyPlane(42);
fplane.flap();
var f = fplane.flap;
f();
```

This produces the following output:
```
Flap flap 42
    ouch  42
    ouch2 42
Flap flap undefined
    ouch  42
    ouch2 42
```

Can you see why?

For more information about this bit, check out:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures


### Prototypes

We can also check if a property exists on an object:
```javascript
print("fplane has a flap property: ", fplane.hasOwnProperty("flap"));  // true
print("fplane has a name property: ", fplane.hasOwnProperty("name"));  // false
```

`hasOwnProperty` is a method that exists through _prototypes_. It's
available trough the prototype of `Object`, and therefore initialized
before `FlappyPlane` gets to initialize the object.

The analogy of prototypes and objects for property lookup is similar
to object and class in Python: first the object is searched for a
property, if it's not found, the prototype is searched.

Putting methods on properties can be more efficient than defining them
for each object:

```javascript
function FlappyPlane() {
    // empty again
}

FlappyPlane.prototype.flap = function() {
    print("Flap flap");
}
```

### Inheritance through prototype chaining / prototype inheritance

The chain: the prototype is also an object. That object inherits a
prototype as well, creating a prototype chain.

Some methods for supporting inheritance (examples taken from the book):


#### Method 1: direct object inheritance.

These two methods for creating objects that are equivalent (code 
from the object oriented js programming book).
```javascript
// page 70
var book = {
    title: "The Principles of Object-Oriented JavaScript"
};
// is the same as
var book = Object.create(Object.prototype, {
    title: {
        configurable: true,
        enumerable: true,
        value: "The Principles of Object-Oriented JavaScript",
        writable: true
    }
});
```

Which means that we can create a new object and specify the prototype
directly to inherit from another _object_:
```javascript
var person1 = {
   name: "Nicholas",
   sayName: function() {
      console.log(this.name);
   }
};
var person2 = Object.create(person1, {
    name: {
       configurable: true,
       enumerable: true,
       value: "Greg",
       writable: true
    }
});
person1.sayName(); // outputs "Nicholas"
person2.sayName(); // outputs "Greg"
```

#### Method 2: constructor inheritance


```javascript
function Rectangle(length, width) {
   this.length = length;
   this.width = width;
}
Rectangle.prototype.getArea = function() {
   return this.length * this.width;
};
Rectangle.prototype.toString = function() {
   return "[Rectangle " + this.length + "x" + this.width + "]";
};

// inherits from Rectangle
function Square(size) {
   this.length = size;
   this.width = size;
}
Square.prototype = new Rectangle();
Square.prototype.constructor = Square;
Square.prototype.toString = function() {
   return "[Square " + this.length + "x" + this.width + "]";
};

var rect = new Rectangle(5, 10);
var square = new Square(6);

console.log(rect.getArea());     //50
console.log(square.getArea());   //36
console.log(rect.toString());    // "[Rectangle 5x10]"
console.log(square.toString());  // "[Square 6x6]"

console.log(rect instanceof Rectangle);    //true
console.log(rect instanceof Object);       // true
console.log(square instanceof Square);     // true
console.log(square instanceof Rectangle);  // true
console.log(square instanceof Object);     // true
```

More methods are described in the book.

## TODO

- [classes in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
