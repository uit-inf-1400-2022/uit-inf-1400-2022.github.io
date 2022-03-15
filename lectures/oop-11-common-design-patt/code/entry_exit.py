
class entry_exit:

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exiting...")

@entry_exit
def say_hello():
    print("Hello")

@entry_exit
def say_hi():
    print("Hi!")

if __name__ == "__main__":
    say_hello()
    say_hi()
