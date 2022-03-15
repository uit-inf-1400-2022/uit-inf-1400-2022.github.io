
def insertionSort(words):
    for i in range(1, len(words)):
        key = words[i]
        j = i-1
        while j >= 0 and key < words[j]:
            words[j+1] = words[j]
            j -= 1
        words[j+1] = key

if __name__ == "__main__":
    a = ["Hei", "På", "Deg"]
    insertionSort(a)
    print(a)
