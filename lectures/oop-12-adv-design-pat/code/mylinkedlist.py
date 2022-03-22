
class LinkedList:

    def __init__(self, *args):
        self.first = None
        self.last = None
        self.iter = None
        if args:
            for arg in args:
                self.insert(arg)

    def insert(self, elem):
        if self.first == None:
            self.first = LinkedList.Node(elem)
            self.last = self.first
        else:
            self.last.next = LinkedList.Node(elem)
            self.last = self.last.next

    def delete(self, elem):
        if self.first.data == elem:
            self.first = self.first.next
            return
        i = self.first
        while i.next != None:
            if i.next.data == elem:
                i.next = i.next.next
                return
            i = i.next
        if i == self.last and i.data != elem:
            raise ValueError("No such element in linkedlist")

    def getElemAtIdx(self, idx):
        i = 0
        current = self.first
        while i < idx:
            if current.next == None:
                raise IndexError("Index out of range")
            current = current.next
            i += 1
        return current.data
    
    def setElemAtIdx(self, idx, data):
        i = 0
        current = self.first
        while i < idx:
            if current.next == None:
                raise IndexError("Index out of range")
            current = current.next
            i += 1
        current.data = data

    def __iter__(self):
        self.iter = self.first
        return self
    
    def __next__(self):
        if self.iter == None:
            raise StopIteration
        ret = self.iter.data
        self.iter = self.iter.next
        return ret

    def __str__(self):
        s = "["
        for elem in self:
            if elem != self.last.data:
                s += str(elem) + "  ->  "
            else:
                s += str(elem)
        s += "]"
        return s
    
    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
