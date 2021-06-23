class Node:
    def __init__(self, v, n=None):
        self.value = v
        self.next = n

def in_set(first, v):
    pointer = first
    while pointer != None:
        if pointer.value == v:
            return True
        pointer = pointer.next
    return False


def add(first, v):
    pointer = first
    while pointer != None:
        if pointer.value == v:
            return first
        pointer = pointer.next
    tmp = first
    first = Node(v)
    first.next = tmp
    return first

def del_el_from_set(first, el):
    if in_set(first, el):
        prev = None
        current = first
        is_it_first_el = True
        while current.val != el:
            is_it_first_el = False
            prev = current
            current = current.next
        if is_it_first_el:
            tmp = first
            first = current.next
            del tmp
            return first
        elif current.next:
            prev.next = current.next
            return first
        else:
            prev.next = None
            return first

def print_set(p):
    while p != None:
        print(p.value, end=' ')
        p = p.next
        print()

first = None
first = add(first, 1)
first = add(first, 3)
print_set(first)
print(in_set(first, 3))
print(in_set(first, 2))
