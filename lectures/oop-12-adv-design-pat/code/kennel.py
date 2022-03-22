import random as rnd
import os
import psutil
from dog1 import Dog1
from dog2 import Dog2

if __name__ == "__main__":
    dogs = []
    for _ in range(40000):
        dogs.append(Dog2(rnd.choice(["golden", "labrador"]),
                        rnd.choice(["male", "female"]),
                        rnd.randint(50, 100)))

    print(psutil.Process(os.getpid()).memory_info().rss /
            1024**2, "MBs of memory used by this program")
    print("Finished loading dogs")
