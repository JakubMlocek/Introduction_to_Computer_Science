from random import randint

class Node():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.first = None

    def add_to_list(self, val):
        tmp = Node(val,self.first)
        self.first = tmp

    def print_list(self):
        current = self.first
        while current:
            print(current.val, end = ' ')
            current = current.next
        print()

    def podziel_na_listy(self):
        LL = []
        for i in range(10):
            LL.append(LinkedList())

        pointer = self.first
        while pointer:
            LL[pointer.val % 10].add_to_list(pointer.val)
            pointer = pointer.next
        return LL

wsadowa = LinkedList()
for i in range(40):
    tmp = randint(1,100)
    wsadowa.add_to_list(tmp)
wsadowa.print_list()

for list in wsadowa.podziel_na_listy():
    list.print_list()
