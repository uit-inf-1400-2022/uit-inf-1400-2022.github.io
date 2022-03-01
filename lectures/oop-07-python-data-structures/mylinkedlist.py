
class MyLinkedList:

    class Node:

        def __init__(self, data):
            self.next = None
            self.data = data

    def __init__(self):
        self.first = None
        self.last = None

    def append(self, data):
        if self.first == None:
            self.first = self.Node(data)
            self.last = self.first
        else:
            self.last.next = self.Node(data)
            self.last = self.last.next

    def __getitem__(self, n):
        curr = self.first
        for _ in range(n):
            curr = curr.next
            if curr == None:
                raise IndexError("Index past length of MyLinkedList")
        return curr.data

    def __setitem__(self, n, data):
        curr = self.first
        for _ in range(n):
            curr = curr.next
            if curr == None:
                raise IndexError("Index past length of MyLinkedList")
        curr.data = data
    
    def __str__(self):
        s = "<"
        curr = self.first
        while curr != None:
            s += curr.data + ", "
            curr = curr.next
        return s[:-2] + ">"




if __name__ == "__main__":
    ll = MyLinkedList()
    ll.append("Hei")
    ll.append("hallo")
    ll.append("joho")

    print(ll)

    ll[1] = "jajaja"

    print(ll)


