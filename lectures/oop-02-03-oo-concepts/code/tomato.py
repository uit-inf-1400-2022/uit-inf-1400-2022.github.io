#!/usr/bin/env python3


class Tomato:
    def __init__(self, desc="Tomato"):
        self.desc = desc

    def __repr__(self):
        return self.desc

    def __add__(self, other):
        print("Smashing {} and {}".format(self.desc, other))
        return Tomato("Ketchup")


t1 = Tomato()
t2 = Tomato('Tomato B')
print(t1 + t2)
