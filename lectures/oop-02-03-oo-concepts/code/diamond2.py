#!/usr/bin/env python3


class A:
    def __init__(self, name):
        print("A-init-start", name)
        self.name = name
        print("A-init-done", name)

    def foo(self):
        print("This is A")

    def baz(self):
        print("baz A")


class B(A):
    def __init__(self, name):
        print("B-init-start", name)
        super().__init__(name)
        print("B-init-done", name)

    def foo(self):
        print("This is B")
        super().foo()

    def bar(self):
        print("bar B")


class C(A):
    def __init__(self, name):
        print("C-init-start", name)
        super().__init__(name)
        print("C-init-done", name)

    def foo(self):
        print("This is C")
        super().foo()

    def bar(self):
        print("bar C")

    def baz(self):
        print("baz C")


class D(B, C):
    def __init__(self, name):
        print("D-init-start", name)
        super().__init__(name)
        print("D-init-done", name)
        # super().__init__(name)

    def foo(self):
        print("This is D")
        super().foo()


b = B('b')
c = C('c')
d = D('d')

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
