from bubblesort import bubbleSort
from insertionsort import insertionSort
from quicksort import quickSort
from supersort import supersort
import time
import copy

def time_algorithm(fn):
    def wrapper(*argv, **argc):
        start = time.time()
        fn(*argv)
        print(fn.__name__, round(time.time()-start, 5), "seconds to complete.")
    return wrapper

if __name__ == "__main__":
    bubbleSort = time_algorithm(bubbleSort)
    insertionSort = time_algorithm(insertionSort)
    quickSort = time_algorithm(quickSort)
    supersort = time_algorithm(supersort)

    with open("sowpods_shuffled.txt") as f:
        words = []
        for word in f:
            words.append(word[:-1])
    words = words[:90]

    bubbleSort(copy.deepcopy(words))
    insertionSort(copy.deepcopy(words))
    quickSort(copy.deepcopy(words), 0, len(words)-1)
    supersort(copy.deepcopy(words))

