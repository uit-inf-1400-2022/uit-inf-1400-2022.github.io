# Testing Object-Oriented Programs (OOP 13)

Today's plan

- Why test
- Types of testing
- Levels of testing
- Test-driven development
- Unit testing

## Why test
- Difficult to catch all analytically through code review
- Alternative is to implicitly let users do the testing
- Changing code may break other parts of the system that used to work

Note: testing will not catch all errors. It will only show you that the ones you specifically tested for didn't occur in testing. 
Likewise, proving mathematically that a program is error free doesn't mean that we know that it will run without bugs. 
Proofs usually focus on specific properties in a program, so you could, for instance, say that a design is deadlock-free 
but fail to detect problems in the run-time that causes your program to crash.

Manual testing is labour-intensive. A small modification one place may break the system in several other places. 
Testing all potentially influenced places manually is impractical, therefore we normally use automated testing.

## Types of testing

### Ad-hoc
Toy around with the software until it breaks. What we typically do for our assignments!
### Manual
Perform a procedure on the software to see if something breaks. ("When I click on the screen, a Hoik spawns...")
### Automated
Run a script to see if something breaks. ("Run script tests.sh, see that the ouput is 'PASSED'")
### Continous
Can not commit code unless automated tests pass. (Try to commit your code, if you are able to commit, the tests pass!)
## Levels of testing
Testing can be performed at multiple levels. These levels are used to verify that the system behaves as expected for different "users". 
Note that errors propagate upwards (e.g. if a unit test fails, it may be expected that the system tests will fail).

### System testing
Testing the complete system/application as a whole, working as a black box. This is used to verify that the system as a whole behaves as the user expects.

This type of testing is performed by giving the system as a whole a known input, and checking the output against the expected output from this input.

### Integration testing
Testing parts of the system as a standalone component, working as a black box. This is used to verify that parts of the system behave as the rest of the system expects.

This is performed by giving a part of the system a known input (by simulating the other part(s) of the system that normally provide this input), and comparing the output of this part of the system to the expected output from this part of the system given the input.

### Unit testing
Testing the code. This is used for development, to verify that the code behaves as the developer expects.

This is the part of testing we focus on in this course.

## Test-driven development
Main mantra: write tests first. Then you can write the code that should pass the tests.

A few points:

- writing tests after writing the main code often results in forgetting to put the test in
- writing tests afterwards may lead to tests that test the implemented code, you want to focus on the specification of what the code should do instead
- writing the test first may expose that the planned interface is too complicated, and the interface can be changed before implementing it

## Unit testing
Unit testing focuses on testing small units. It's much easier to isolate and find bugs if you can, for instance, test every function or method in your program before you test the combination of many.

Example built-in library for unit testing in Python: [unittest](https://docs.python.org/3/library/unittest.html)

The TestCase class has a number of built-in methods for comparing values and results of functions. This can be useful when setting up a set of tests. You add your own test methods by adding methods that start with `test` and that take no arguments except `self`.

```python
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
    
```
Running the unit test:
```python
> python3 unittest1.py -v
test_isupper (__main__.TestStringMethods) ... ok
test_split (__main__.TestStringMethods) ... ok
test_upper (__main__.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

```

### Excerise
Make a class Customer, that have 4 attributes: name, active, level and points. Default values for active are False, points are 0 and all Customer starts at level 1.
When the customer have more than 300 points the customer are at level 2 and level 3 above 500 points. 

Use cases:
- Create a new customer with a name, and default values as described over for the other attributes
- Activate a customer
- Add points to customer
- Change level based on points (Above 300 points = level 2, above 500 = level 3)

What do do:
- Write Customer class. 
- Write a unittest class to test the Customer class.


## Unit testing with pytest 
The unittest library design is based on the JUnit testing framework for Java and results in a lot of boilerplate code. An alternative is pytest:

[http://pytest.org/latest/](http://pytest.org/latest/)

https://wiki.python.org/moin/PyTest

Documentation: http://pytest.org/latest/contents.html#toc

Examples: http://pytest.org/latest/example/index.html

Any properly named module/function can be a test. With properly it means:
modules or sub packages with names beginning with ```test_``` and in this modules any functions start with ```test```.

So ```pytest``` starts in current folder and searches after modules properly named and inside of the modules it search for functions properly named.(and also after a folder named ```tests```).

It doesn't even need to import any library:

Command ```pip -U install pytest``` for install on windows, should be pretty same for macOS and Linux.

```python
#!/usr/bin/env python3

def test_int_float():
    assert 1 == 1.0
```

```python
> pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.10.4, pytest-7.1.1, pluggy-1.0.0 -- \Python310\python.exe
cachedir: .pytest_cache
rootdir: \inf1400\kode\tests
collected 1 item

test_testing.py::test_int_float PASSED                                                                           [100%]

================================================== 1 passed in 0.01s ==================================================
```

You can also use classes:

```python
def test_int_float():
    assert 1 == 1.0

def poink():
    print("foo")
    assert 2 == 3

class TestFoo():
    def test_int_float(self):
        assert 1 == 1.0
    def test_int_str(self):
        pass
        #assert 1 == "1"
 ```
 
 ```python
 pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.10.4, pytest-7.1.1, pluggy-1.0.0 -- \Python310\python.exe
cachedir: .pytest_cache
rootdir: \inf1400\kode\tests
collected 3 items

test_testing.py::test_int_float PASSED                                                                           [ 33%]
test_testing.py::TestFoo::test_int_float PASSED                                                                  [ 66%]
test_testing.py::TestFoo::test_int_str PASSED                                                                    [100%]

================================================== 3 passed in 0.02s ==================================================
```

### Excerise 
Given the code below, which compute factorial (0!=1, 1!=1, 2!=2, 3!=6 and so on)

```python
def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
```

- Create a test using pytest for this function.

- Bonus if time: Create a test using unittest for the function.





