
def les_fil(filnavn):
    f = open(filnavn, "r")
    f.readline()
    temps = []
    for line in f:
        words = line.split(";")
        temps.append(words)
    return temps

t = les_fil("temp.csv")
mnd = []
temp = []

for data in t:
    mnd.append(data[0])
    temp.append(data[1:])
    print(mnd[0])

for x, y in zip(mnd, temp):
    print(x, y)

    