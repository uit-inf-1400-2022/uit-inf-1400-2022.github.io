Lecture notes - OOP 1 - Introduction to Python
=========================================

Topics:
* Python interpreter
* Source code files
* Example object: lists
* str, tuple, int, long, float
* Type conversion
* Functions
* Expressions
* Python modules


This is a summary of some of the examples and points from the introduction lecture. The introduction uses many of the examples from the Python tutorial (link below). 

Some resources: 
* [Python 3 tutorial](https://docs.python.org/3/tutorial/)
* [Moving to Python from other languages](https://wiki.python.org/moin/MovingToPythonFromOtherLanguages)
* [Python 3 documentation](https://docs.python.org/3/)


Python interpreter
-------------------

Python has an interactive interpreter. This means that you can start Python and write code directly without compiling a program.

```
$ python3
Python 3.4.3+ (default, Oct 14 2015, 16:03:50) 
[GCC 5.2.1 20151010] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello world")
Hello world
```

You can even use it as a calculator:
```python
>>> 4 + 5
9
```

An expression will be interpreted and evaluated by Python directly. This is different from C, where you need to write the code in a file, compile the program and then run the compiled program. 

The return value from any expression you write will be printed on the next line. 

Interactive Python can be useful for testing code and exploring. For larger programs and things you intend to re-use, it's more common to use normal source files:

helloworld.py:
```python
print("Hello world")
```

You can execute this by giving the Python interpreter the filename:

```
$ python3 helloworld.py
Hello world
```

Note that you don't need a `main()` function in Python. 

A more common way is to include a "magic" line at the top that specifies which interpreter to use for running the program on Unix systems (Linux, OS X etc). The first two characters of a file will be examined (#!) and the rest of that line specifies the interpreter to use. 

helloworld.py:
```python
#!/usr/bin/env python3 

print("Hello world")
```

If you use this trick and make the file executable (`chmod +x helloworld.py` on Unix systems), it's possible to start the Python file like any other program: 

```
$./helloworld.py
Hello world
```


Idle - a simple editor and Python execution environment
-----------------------------------

Comes with Python. 

* Has an interactive window where you can type and execute python expressions
* Has an editor for editing Python files (with syntax highlighting)
* You can run code directly from the editor (using F5)
* Sufficient for this course unless you want more advanced features. 

Other editors and IDEs:
* Emacs
* vi/vim
* Sublime
* Kate
* Microsoft Developer Studio
* PyCharm
* PyDev for Eclipse
* And so on: [https://wiki.python.org/moin/PythonEditors](https://wiki.python.org/moin/PythonEditors)


Note: try to avoid saving files with tab characters. It sometimes causes problems with other editors and source tools that use a different tab width than what your editor happened to be set up with. The de facto standard is multiples of 8, which is interpreted differently by different editors. Some editors use the tab key to to indent code according to the language syntax, and confusingly _also_ use the tab key to add the tab character. [More on the history of tab](https://en.wikipedia.org/wiki/Tab_key). 

Many people also use [Jupyter Notebooks](http://jupyter.org/)



Further topics/examples
------------------------
See the Python tutorial (link above) for examples:
- lists: insert, append, slices, access, pop, sorted, reversed, index
- lists as objects (and using methods on objects)
- accessors and mutators
- tuple, str (other sequences),
- str split, str index
- defining a class. 
- objects
- modules
- modules documentation and overview (see library in the Python documentation)
- help and dir
- exceptions (simple overview - we will discuss them more later)


