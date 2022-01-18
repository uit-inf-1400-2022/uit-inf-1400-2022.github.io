#!/usr/bin/env python3


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


class D(B, C):
    def foo(self):
        print("This is D")
        super().foo()


b = B()
c = C()
d = D()

print("Calling b.foo():")
b.foo()
print("Calling c.foo():")
c.foo()
print("Calling d.foo():")
d.foo()
print("Calling d.bar():")
d.bar()
print("Calling d.baz():")
d.baz()
