class Node():
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.first = None

    def add_element(self, val):
        prev = None
        pointer = self.first
        while pointer != None:
            prev = pointers
            pointer = pointer.next
        prev.next = Node(val)

    def del_if_prev_higher(self):
        if self.first == None or self.first.next == None:
            return
        else:
            prev = self.first
            current = self.first.next
            while current:
                if current.val % prev.val == 0:
                    if current.next:
                        else:
                        prev.next = None
                    prev = current
                    current = current.next
                    prev.next = current.next

    def print_list(self):
        tmp = self.first
        while tmp != None:
            print(tmp.val, end = ' ')
            tmp = tmp.next
        print()


LL = LinkedList()
LL.add_element(15)
LL.add_element(5)
LL.add_element(9)
LL.add_element(3)
LL.print_list()
LL.del_if_prev_higher()
LL.print_list()
