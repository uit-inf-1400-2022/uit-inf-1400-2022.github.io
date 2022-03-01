
# Simple example of zipping lists when used in for loop

l = ["Arne", "Berit", "Caroline", "Dina", "Elling"]
p = [1, 2, 3, 4, 5]

for plass, person in zip(p, l):
    print(plass, person)

