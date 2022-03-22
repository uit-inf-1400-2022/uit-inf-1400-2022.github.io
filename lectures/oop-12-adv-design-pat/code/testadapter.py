from linkedlistadapter import LLAdapter

if __name__ == "__main__":
    print("Running tests...", "\n")

    # Test construction
    print("== TEST CONSTRUCTION ==")
    print("Constructing list with 5 strings")
    a = LLAdapter("hei", "på", "deg", "din", "gamle")
    print(a)
    print()

    # Test append
    print("== TEST APPEND ==")
    print("Appending \"skrei\" to the list")
    a.append("skrei")
    print(a)
    print()

    # Test getitem
    print("== TEST GETITEM ==")
    print("Getting item at index 0")
    print(a[0])
    print()

    # Test remove
    print("== TEST REMOVE ==")
    print("Removing item \"gamle\" from list")
    a.remove("gamle")
    print(a)
    print()

    # Test setitem
    print("== TEST SETITEM ==")
    print("Setting element at idx 0 to \"ha det bra\"")
    a[0] = "ha det bra"
    print(a)
    print()

    print("...all tests passed!")
