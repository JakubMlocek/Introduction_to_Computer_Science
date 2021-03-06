class Node():
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.first = None

    def add_item(self,val):
        tmp = Node(val,self.first)
        self.first = tmp

    def print_list(self):
        tmp = self.first
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next

    def reverse(self):
        current = self.first
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        self.first = prev


LL = LinkedList()
LL.add_item(1)
LL.add_item(2)
LL.add_item(3)
LL.add_item(4)
LL.add_item(5)
LL.print_list()
LL.reverse()
LL.print_list()


