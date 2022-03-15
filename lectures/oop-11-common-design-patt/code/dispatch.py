
# Don't do this!
def bad_func(arg, verbose=False):
    if type(arg) == int:
        if verbose:
            print("Here's an int:", end=" ")
        print(arg)
    elif type(arg) == list:
        if verbose:
            print("Here's a list:", end=" ")
        print(arg)
    else:
        if verbose:
            print("Here's something else:", end=" ")
        print(arg)

# Do this!
from functools import singledispatch

@singledispatch
def fun(arg):
    print("Here's something unidentified:", arg)

@fun.register(int)
def _(arg):
    print("This is a number:", arg)

@fun.register(list)
def _(arg):
    print("Here's a list, let's iterate!")
    for elem in arg:
        print(elem)

if __name__ == "__main__":
    fun("Hei")
    fun(123)
    fun([1, 2, 3, 4, 5])