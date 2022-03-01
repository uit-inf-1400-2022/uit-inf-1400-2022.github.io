
def gjør_beregning(a, b):
    s = a + b
    d = a - b
    p = a * b
    k = a / b
    return s, d, p, k

x, y, _, _ = gjør_beregning(10, 5)

print("Summen er", x)
print("Diff er", y)
