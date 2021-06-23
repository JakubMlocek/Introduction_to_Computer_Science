class Node():
    def __init__(self, val = None):
        self.val = val
        self.next = None


def add(first, val):
    if first == None:
        return Node(val)
    elif first.val == None:
        first.val = val
        return first
    else:
        prev = None
        current = first
        while current != None:
            prev = current
            current = current.next
        prev.next = Node(val)
        return first

def remove_every_second(first):
    if first == None or first.val == None:
        return

    while first != None and first.next != None:
        first.next = first.next.next
        first = first.next

def prt(first):
    while first != None:
        print(first.val)
        first = first.next

p = Node(2)
add(p,3)
add(p,5)
add(p,8)
remove_every_second(p)
prt(p)
