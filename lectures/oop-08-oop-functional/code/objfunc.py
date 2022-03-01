
# Simple example of a callable class with counter
class SumMachine:

    def __init__(self):
        self.cnt = 0

    def __call__(self, x, y):
        self.cnt += 1
        return x + y



if __name__ == "__main__":

    sm = SumMachine()
    sm(1, 4)
    sm(2, 4)
    sm(5, 1)
    sm(1, 4)

    print(sm.cnt)





