
# A simple example of enumeration

if __name__ == "__main__":

    l = ["Arne", "Berit", "Caroline", "Dina", "Elling"]

    # Do not do this:
    i = 0
    for person in l:
        print(i+1, person)
        i = i + 1

    print()

    # Do this instead!
    for i, person in enumerate(l):
        print(i+1, person)




    

    