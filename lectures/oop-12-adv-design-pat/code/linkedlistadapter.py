from mylinkedlist import LinkedList

class LLAdapter:

    def __init__(self, *args):
        self.lst = LinkedList(*args)

    def append(self, elem):
        self.lst.insert(elem)

    def remove(self, elem):
        self.lst.delete(elem)

    def __getitem__(self, idx):
        return self.lst.getElemAtIdx(idx)

    def __setitem__(self, idx, item):
        self.lst.setElemAtIdx(idx, item)

    def __str__(self):
        return self.lst.__str__()

