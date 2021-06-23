class Node():
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, first = None):
        self.first = first

    def first_returner(self):
        return self.first

    def add_to_list(self, val):
        if self.first == None:
            self.first = Node(val)
        else:
            prev = None
            pointer = self.first
            while pointer:
                prev = pointer
                pointer = pointer.next
            prev.next = Node(val)

    def print_list(self):
        cur = self.first
        while cur:
            print(cur.val, end = ' ')
            cur = cur.next
        print()

    def reverse_list(self):
        prev = None
        current = self.first
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        self.first = prev

    def increase_by_1(self):
        self.reverse_list()
        current = self.first
        prev = None
        current.val += 1
        over9 = False
        while current:
            if over9:
                current.val += 1
            if current.val == 10:
                current.val = 0
                over9 = True
            prev = current
            current = current.next
        if over9:
            prev.next = Node(1)
        self.reverse_list()

LL = LinkedList()
LL.add_to_list(9)
LL.add_to_list(9)
LL.add_to_list(9)
LL.add_to_list(9)
LL.add_to_list(9)
LL.print_list()
LL.increase_by_1()
LL.print_list()