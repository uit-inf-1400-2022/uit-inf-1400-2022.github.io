
# An example of the __len__ and __reversed__ methods

class Vector:

    def __init__(self, values):
        self.values = values
        self.dims = len(values)

    def __len__(self):
        return self.dims

    def __reversed__(self):
        rev = []
        for i in range(self.dims-1, -1, -1):
            rev.append(self.values[i])
        return Vector(rev)

    def __str__(self):
        output = "Vector: "
        for i in range(self.dims):
            output += str(self.values[i]) + " "
        return output



if __name__ == "__main__":
    v = Vector((1, 2, 3, 4))

    print(v)
    print(len(v))
    print(reversed(v))

    

    