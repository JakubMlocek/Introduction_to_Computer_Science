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

    def del_not_uniqe_elements(self,second):
        deleted = 0
        prev2 = None
        cur2 = second
        while cur2:
            el = cur2.val
            prev1 = None
            cur1 = self.first
            while cur1:
                if cur1.val == el:
                    if not(prev1 or prev2):
                        if prev2 == None:
                            second = second.next
                        if prev1 == None:
                            self.first = self.first.next
                    else:
                        prev1.next = cur1.next
                        prev2.next = cur2.next
                    deleted += 1
                if cur1.val > el:
                    break
                cur1 = cur1.next
            cur2 = cur2.next
        return deleted

LL1 = LinkedList()
LL2 = LinkedList()

LL1.add_to_list(3)
LL1.add_to_list(4)
LL1.add_to_list(5)
LL1.add_to_list(6)
LL1.add_to_list(7)
LL1.add_to_list(12)
LL1.add_to_list(14)
LL1.print_list()

LL2.add_to_list(9)
LL2.add_to_list(3)
LL2.add_to_list(6)
LL2.add_to_list(1)
LL2.add_to_list(17)
LL2.add_to_list(14)
LL2.add_to_list(7)
LL2.print_list()

print(LL1.del_not_uniqe_elements(LL2.first_returner()))
