from bubblesort import bubbleSort
from insertionsort import insertionSort
from quicksort import quickSort

class supersort:

    def __init__(self, lst):
        self.lst = lst
        self.bubblesort = bubbleSort
        self.insertionsort = insertionSort
        self.quicksort = quickSort
        self.__call__()

    def __call__(self):
        if len(self.lst) < 20:
            print("supersort chose to bubblesort this list")
            self.bubblesort(self.lst)
        elif len(self.lst) < 100:
            print("supersort chose to insertionsort this list")
            self.insertionsort(self.lst)
        else:
            print("supersort chose to quicksort this list")
            self.quicksort(self.lst, 0, len(self.lst)-1)
