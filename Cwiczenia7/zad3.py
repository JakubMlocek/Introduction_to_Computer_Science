class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
        self.first = None

    def retfirst(self):
        return self.first

    def add_sorted(self, val):
        if self.first == None:
            self.first = Node(val)
        elif self.first.val == None:
            self.first.val = val
        else:
            if val < self.first.val:
                tmp = Node(val, self.first)
                self.first = tmp
                return
            else:
                current = self.first
                prev = None
                while current:
                    if current.val > val:
                        prev.next = Node(val, current)
                        return
                    prev = current
                    current = current.next
                prev.next = Node(val)

    def print_list(self):
        tmp = self.first
        while tmp:
            print(tmp.val, end=' ')
            tmp = tmp.next
        print()


def sorted_scal_it(first, second):
    if first == None:
        return second
    if second == None:
        return first

    wsk1, wsk2 = first, second
    after = None
    if wsk1.val < wsk2.val:
        after = wsk1
        if wsk1.next:
            wsk1 = wsk1.next
    else:
        after = wsk2
        if wsk2.next:
            wsk2 = wsk2.next
    begin_of_after = after
    while wsk1.next or wsk2.next:
        if wsk1.val < wsk2.val:
            after.next = wsk1
            if wsk1.next:
                wsk1 = wsk1.next
        else:
            after.next = wsk2
            if wsk2.next:
                wsk2 = wsk2.next
        after = after.next
    return begin_of_after

def sorted_scal_rek(first, second):
    if first == None:
        return second
    if second == None:
        return first
    if first.val < second.val:
        result = first
        result.next=sorted_scal_rek(first.next,second)
    else:
        result = second
        result.next=sorted_scal_rek(first, second.next)
    return result

def print_list(first):
    tmp = first
    while tmp:
       print(tmp.val, end=' ')
       tmp = tmp.next
    print()


LL1 = LinkedList()
LL2 = LinkedList()
LL1.add_sorted(5)
LL2.add_sorted(3)
LL1.add_sorted(13)
LL2.add_sorted(8)
LL1.add_sorted(89)
LL2.add_sorted(8)
LL1.add_sorted(1)
LL2.add_sorted(43)
LL1.add_sorted(9)
LL2.add_sorted(9)
print_list(sorted_scal_rek(LL1.retfirst(),LL2.retfirst()))
