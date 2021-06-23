class Node():
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.first = None

    def add_element(self, val):
        pointer = self.first
        while pointer != None:
            pointer = pointer.next
        tmp = self.first
        self.first = Node(val,tmp)

    def del_element(self,val):
        if self.first == None:
            return
        elif self.first.val == val:
            self.first = self.first.next
        else:
            prev = self.first
            current = self.first.next
            while current:
                if current.val == val:
                    if current.next:
                        prev.next = current.next
                    else:
                        prev.next = None
                prev = current
                current = current.next

    def is_el_in_list(self, val):
        pointer = self.first
        while pointer:
            if pointer.val == val:
                return True
            pointer = pointer.next
        return False

    def print_list(self):
        tmp = self.first
        while tmp != None:
            print(tmp.val, end = ' ')
            tmp = tmp.next
        print()

    def add_or_del(self,val):
        if self.is_el_in_list(val):
            self.del_element(val)
        else:
            self.add_element(val)

LL = LinkedList()
LL.add_element(3)
LL.add_element(4)
LL.add_element(1)
LL.add_element(9)
LL.is_el_in_list(4)
LL.print_list()
#LL.del_element(4)
LL.add_or_del(4)
LL.print_list()
LL.add_or_del(4)
LL.print_list()