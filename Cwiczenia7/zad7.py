class Node():
    def __init__(self, val = None):
        self.val = val
        self.next = None

first = Node(3)

def is_el_in_list(el):
    current = first
    if current.val == el:
        return True
    while current.next:
        current = current.next
        if current.val == el:
            return True
    return False

def len_of_set():
    current = first
    length = 1
    while current.next:
        length += 1
        current = current.next
    return length

def add_el_to_list(el):
    if first.next == None:
        first.next = Node(el)
    else:
        prev = None
        current = first
        while current.next:
            prev = current
            current = current.next
        prev.next = Node(el)
        prev.next.next = current

def print_list():
    current = first
    while current:
        print(current.val)
        current = current.next

def del_el_from_list(el):
    global first
    prev = None
    current = first
    is_it_first_el = True
    while current.val != el:
        is_it_first_el = False
        prev = current
        current = current.next
    if is_it_first_el:
        first = current.next
    elif current == None:
        print("brak elementu")
    elif current.next:
        prev.next = current.next
    else:
        prev.next = None


#print(len_of_set())
add_el_to_list(4)
add_el_to_list(5)
add_el_to_list(6)
del_el_from_list(3)
print_list()