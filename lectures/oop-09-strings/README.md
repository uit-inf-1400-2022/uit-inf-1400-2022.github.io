Strings and Serialization
-------------------------

Here be dragons!

Basic string operations
-----------------------

```python
a = "This is a string"
b = 'Also this'
c = '''and
this'''
d = "not" " to" " mention" " this" " monstrosity"
e = a + b
```

Note that strings in many languages (most?) are immutable (can not be changed).

Formatting strings
-------------------

> There should be one-- and preferably only one --obvious way to do it. - The Zen of Python

```python
a = "formatting"

print(f"{a} text is hard")
print("{} text is hard".format(a))
print("%s text is hard" % a)
```

Character sets
---------------

When reading or writing data, character sets matter. Different bytes mean different things in different character sets.

```
>>> "æøå".encode("ascii", "replace")
b'???'
>>> "æøå".encode("latin-1", "replace")
b'\xe6\xf8\xe5'
>>> "æøå".encode("UTF-8", "replace")
b'\xc3\xa6\xc3\xb8\xc3\xa5'
```

Regular expressions
-------------------

> Some people, when confronted with a problem, think
> “I know, I'll use regular expressions.”   Now they have two problems.
> - Jamie Zawinski


Parsing non-structured data is difficult, regular expressions (regex) is a tool for doing just that.

```python
import re
pattern = "o.[a-z]"
string = "A book of old words"

re.findall(pattern, string)
```

How to check if an URL is valid?

```
#([a-z]([a-z]|\d|\+|-|\.)*):(\/\/(((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?((\[(|(v[\da-f]{1,}\.(([a-z]|\d|-|\.|_|~)|[!\$&'\(\)\*\+,;=]|:)+))\])|((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|(([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=])*)(:\d*)?)(\/(([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*|(\/((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)|((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)|((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)){0})(\?((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\xE000-\xF8FF]|\/|\?)*)?(\#((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?#iS
```

There's a tradeoff between the complexities of parsing strings and readable and maintainable code.


Serializing objects
-------------------

When storing objects for later use, or sending objects somewhere, the objects need to be in a format that is understandable. This is serialization.

In python this is supported by (among others) the pickle module.

```python
import pickle

class SomeData:
    def __init__(self, numbers, other_numbers):
        self.other_numbers = other_numbers
        self.numbers = numbers

a = SomeData(list(range(10)), list(range(1000)))

with open("data.dat", "wb") as f:
    pickle.dump(a, f)
```

Beware loading user-supplied data with pickle, as it allows arbitrary code execution.
Instead, use something like JSON (JavaScript Object Notation), which only encodes data.

