
# Using a function as an object

def sayHello():
    print("Hello!")
    sayHello.cnt += 1


if __name__ == "__main__":
    sayHello.cnt = 0
    
    for _ in range(10):
        sayHello()

    print(sayHello.cnt)
