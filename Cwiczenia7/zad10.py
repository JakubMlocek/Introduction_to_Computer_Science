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

class Workingboth():
    def add_2_numbers(pierwsza,druga):
        pierwsza.reverse_list()
        druga.reverse_list()
        a = pierwsza.first
        b = druga.first
        FinalSum = None
        over9 = 0
        while a is not None and b is not None:
            sum = a.val + b.val + over9
            newnode = Node(sum % 10)
            newnode.next = FinalSum
            FinalSum = newnode
            over9 = sum // 10
            a,b = a.next, b.next
        if b is not None:
            sum = b.val + over9 + over9
            newnode = Node(suma % 10)
            newnode.next = FinalSum
            FinalSum = newnode
            over9 = sum // 10
            b = b.next

        if a is not None:
            sum = a.val + over9
            newnode = Node(suma % 10)
            newnode.next = FinalSum
            FinalSum = newnode
            over9 = sum // 10
            a = a.next

        if over9 > 0:
            newnode = Node(over9)
            newnode.next = FinalSum
            FinalSum = newnode
        return FinalSum

    def print_sum(pointer):
        cur = pointer
        while cur:
            print(cur.val, end = ' ')
            cur = cur.next
        print()


LL1 = LinkedList()
LL1.add_to_list(1)
LL1.add_to_list(2)
LL1.add_to_list(3)
LL1.add_to_list(4)
LL1.add_to_list(5)
LL1.print_list()

LL2 = LinkedList()
LL2.add_to_list(2)
LL2.add_to_list(2)
LL2.add_to_list(9)
LL2.add_to_list(2)
LL2.add_to_list(2)
LL2.print_list()

LL3 = Workingboth.add_2_numbers(LL1,LL2)
Workingboth.print_sum(LL3)