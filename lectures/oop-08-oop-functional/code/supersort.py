
# This class chooses an algorithm for you, based on number of elements

class SuperSort:

    def __init__(self):
        pass

    def bubblesort(self):
        print("Bubblesort was used")

    def insertionsort(self):
        print("Insertionsort was used")

    def quicksort(self):
        print("Quicksort was used")

    def __call__(self, elem_count):
        if elem_count < 10:
            self.bubblesort()
        elif elem_count < 100:
            self.insertionsort()
        else:
            self.quicksort()


if __name__ == "__main__":
    ss = SuperSort()
    ss(10000)