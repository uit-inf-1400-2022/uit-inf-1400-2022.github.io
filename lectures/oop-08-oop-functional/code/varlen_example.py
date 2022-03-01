
# Example of variable length parameters and name of module

def doSomething(word, *args, end=""):
    for elem in args:
        print(word, elem, end)

def whatIsMyName():
    print(__name__)


if __name__ == "__main__":
    whatIsMyName()

