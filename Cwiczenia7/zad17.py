def ile1bin(dec):
    ile1 = 0
    while dec:
        if dec % 2 == 1:
            ile1 += 1
        dec //= 2
    return ile1


class Node():
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self. next = next
        self.prev = prev

class LikedList():
    def __init__(self,first = None):
        self.first = first

    def add_to_list(self,val):
        if self.first == None:
            self.first = Node(val)
        else:
            tmp = self.first
            self.first = Node(val)
            tmp.prev = self.first
            self.first.next = tmp


    def print_list(self):
        cur = self.first
        while cur:
            print(cur.val, end = ' ')
            cur = cur.next
        print()

    def del_from_list_if_nbin(self):
        if ile1bin(self.first.val) % 2 != 0:
            self.first = self.first.next
        prev = None
        current = self.first
        while current != None:
            if ile1bin(current.val) % 2 != 0:
                prev.next = current.next
                current.next.prev = prev
            prev = current
            current = current.next

LL = LikedList()
LL.add_to_list(3)
LL.add_to_list(4)
LL.add_to_list(5)
LL.add_to_list(6)
LL.add_to_list(7)
LL.print_list()
LL.del_from_list_if_nbin()
LL.print_list()



