def bubbleSort(words):
    n = len(words)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]

if __name__ == "__main__":
    a = ["Hei", "På", "Deg"]
    bubbleSort(a)
    print(a)