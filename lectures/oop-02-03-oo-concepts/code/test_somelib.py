#!/usr/bin/env python3

import somelib

# need to explicitly import each of the sublibs
import somelib.sublib
import somelib.test1

print(somelib.somevar)
print(somelib.sublib.foo)
print(somelib.test1.foo)
